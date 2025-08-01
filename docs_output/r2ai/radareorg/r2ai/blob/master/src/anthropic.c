# anthropic.c

#include "r2ai.h"

static const char *modelname(const char *model_name) {
	return model_name ? model_name : "claude-3-7-sonnet-20250219";
}

R_IPI R2AI_ChatResponse *r2ai_anthropic(RCore *core, R2AIArgs args) {
	const char *model = args.model;
	char **error = args.error;
	const R2AI_Tools *tools = args.tools;
	R2AI_Messages *messages_input = args.messages;

	if (error) {
		*error = NULL;
	}

	// Setup HTTP headers
	char *auth_header = r_str_newf ("x-api-key: %s", args.api_key);
	char *anthropic_version = "anthropic-version: 2023-06-01";
	const char *headers[] = {
		"Content-Type: application/json",
		auth_header,
		anthropic_version,
		NULL
	};

	const char *anthropic_url = "https://api.anthropic.com/v1/messages";

	// Get system message if available
	const char *system_message = NULL;

	// First check if it's provided in args.system_prompt
	if (R_STR_ISNOTEMPTY (args.system_prompt)) {
		system_message = args.system_prompt;
	} else {
		// If no system_prompt in args, check config as fallback
		system_message = r_config_get (core->config, "r2ai.system");
	}

	// Create messages JSON
	char *messages_json = NULL;

	if (messages_input && messages_input->n_messages > 0) {
		// Convert directly to JSON without filtering
		messages_json = r2ai_msgs_to_anthropic_json (messages_input);
		if (!messages_json) {
			if (error) {
				*error = strdup ("Failed to convert messages to JSON");
			}
			free (auth_header);
			return NULL;
		}
	} else {
		if (error) {
			*error = strdup ("No input or messages provided");
		}
		free (auth_header);
		return NULL;
	}

	// Convert tools to Anthropic format if available
	char *anthropic_tools_json = NULL;
	if (tools && tools->n_tools > 0) {
		anthropic_tools_json = r2ai_tools_to_anthropic_json (tools);
	}

	// Create the request JSON
	PJ *pj = pj_new ();
	pj_o (pj);
	pj_ks (pj, "model", modelname (model));
	pj_kn (pj, "max_tokens", 4096);
	if (args.thinking_tokens >= 1024) {
		pj_ko (pj, "thinking");
		pj_ks (pj, "type", "enabled");
		pj_kn (pj, "budget_tokens", args.thinking_tokens);
		pj_end (pj);
	}
	// Add system message if available
	if (system_message) {
		pj_ks (pj, "system", system_message);
	}

	// Add messages
	pj_k (pj, "messages");
	// messages_json already contains the array itself, so we use raw
	pj_raw (pj, messages_json);

	// Add tools if available
	if (anthropic_tools_json) {
		pj_k (pj, "tools");
		pj_raw (pj, anthropic_tools_json);
		free (anthropic_tools_json);
	}

	pj_end (pj);

	char *data = pj_drain (pj);
	free (messages_json);

	// Save the full JSON for debugging
	r_file_dump ("/tmp/r2ai_anthropic_request.json", (const ut8 *)data, strlen (data), 0);
	R_LOG_DEBUG ("Full request saved to /tmp/r2ai_anthropic_request.json");
	R_LOG_DEBUG ("Anthropic API request data: %s", data);

	// Make the API call
	int code = 0;
	char *res = r2ai_http_post (anthropic_url, headers, data, &code, NULL);
	free (data);
	free (auth_header);

	if (!res || code != 200) {
		R_LOG_ERROR ("Anthropic API error %d", code);
		if (error && res) {
			*error = strdup (res);
		} else if (error) {
			*error = strdup ("Failed to get response from Anthropic API");
		}
		free (res);
		return NULL;
	}

	// Save the response for inspection
	r_file_dump ("/tmp/r2ai_anthropic_response.json", (const ut8 *)res, strlen (res), 0);
	R_LOG_DEBUG ("Anthropic API response saved to /tmp/r2ai_anthropic_response.json");
	R_LOG_DEBUG ("Anthropic API response: %s", res);

	// Parse the response
	R2AI_ChatResponse *result = R_NEW0 (R2AI_ChatResponse);
	if (!result) {
		free (res);
		if (error) {
			*error = strdup ("Failed to allocate memory for response");
		}
		return NULL;
	}

	R2AI_Message *message = NULL;
	R2AI_Usage *usage = NULL;

	char *response_copy = strdup (res);
	if (response_copy) {
		RJson *jres = r_json_parse (response_copy);
		if (jres) {
			// Create a new message structure
			message = R_NEW0 (R2AI_Message);

			const RJson *usage_json = r_json_get (jres, "usage");
			if (usage_json && usage_json->type == R_JSON_OBJECT) {
				usage = R_NEW0 (R2AI_Usage);
				if (usage) {
					const RJson *prompt_tokens = r_json_get (usage_json, "input_tokens");
					const RJson *completion_tokens = r_json_get (usage_json, "output_tokens");
					if (prompt_tokens && prompt_tokens->type == R_JSON_INTEGER) {
						usage->prompt_tokens = prompt_tokens->num.u_value;
					}
					if (completion_tokens && completion_tokens->type == R_JSON_INTEGER) {
						usage->completion_tokens = completion_tokens->num.u_value;
					}
					usage->total_tokens = usage->prompt_tokens + usage->completion_tokens;
				}
			}

			if (message) {
				message->role = strdup ("assistant");

				RStrBuf *content_buf = r_strbuf_new ("");

				// Check for tool calls in Anthropic response
				int has_tool_use = 0;
				int n_tool_calls = 0;

				// Count tool_use blocks to determine array size
				const RJson *content_array = r_json_get (jres, "content");
				if (content_array && content_array->type == R_JSON_ARRAY) {
					// First count the number of tool_use blocks
					const RJson *content_item = content_array->children.first;
					while (content_item) {
						const RJson *type = r_json_get (content_item, "type");
						if (type && type->type == R_JSON_STRING && !strcmp (type->str_value, "tool_use")) {
							has_tool_use = 1;
							n_tool_calls++;
						}
						content_item = content_item->next;
					}
				}

				// Allocate tool_calls array if needed
				if (has_tool_use && n_tool_calls > 0) {
					message->tool_calls = R_NEWS0 (R2AI_ToolCall, n_tool_calls);
					if (!message->tool_calls) {
						if (error) {
							*error = strdup ("Failed to allocate memory for tool calls");
						}
						r_json_free (jres);
						free (response_copy);
						r2ai_message_free (message);
						free (res);
						return NULL;
					}
					message->n_tool_calls = n_tool_calls;
				}

				// Process each content item
				int tool_idx = 0;
				if (content_array && content_array->type == R_JSON_ARRAY) {
					R2AI_ContentBlocks *cb = R_NEW0 (R2AI_ContentBlocks);
					if (!cb) {
						r_json_free (jres);
						free (response_copy);
						r2ai_message_free (message);
						free (res);
						return NULL;
					}
					cb->n_blocks = content_array->children.count;
					cb->blocks = R_NEWS0 (R2AI_ContentBlock, cb->n_blocks);
					if (!cb->blocks) {
						free (cb);
						r_json_free (jres);
						free (response_copy);
						r2ai_message_free (message);
						free (res);
						return NULL;
					}
					int block_idx = 0;
					const RJson *content_item = content_array->children.first;
					while (content_item && block_idx < cb->n_blocks) {
						const RJson *type = r_json_get (content_item, "type");
						if (type && type->type == R_JSON_STRING) {
							R2AI_ContentBlock *block = &cb->blocks[block_idx];
							if (!strcmp (type->str_value, "text")) {
								// Text content
								const RJson *text = r_json_get (content_item, "text");
								if (text && text->type == R_JSON_STRING) {
									r_strbuf_append (content_buf, text->str_value);
									block->type = strdup ("text");
									block->text = strdup (text->str_value);
								}
							} else if (!strcmp (type->str_value, "tool_use") && tool_idx < n_tool_calls) {
								// Tool call - convert from Anthropic format to OpenAI format
								const RJson *name = r_json_get (content_item, "name");
								const RJson *id = r_json_get (content_item, "id");
								const RJson *input = r_json_get (content_item, "input");

								block->type = strdup ("tool_use");
								if (name && name->type == R_JSON_STRING) {
									block->name = strdup (name->str_value);
									R2AI_ToolCall *tc = (R2AI_ToolCall *)&message->tool_calls[tool_idx];
									tc->name = strdup (name->str_value);
								}

								if (id && id->type == R_JSON_STRING) {
									block->id = strdup (id->str_value);
									R2AI_ToolCall *tc = (R2AI_ToolCall *)&message->tool_calls[tool_idx];
									tc->id = strdup (id->str_value);
								}

								if (input && input->type == R_JSON_OBJECT) {
									char *input_str = r_json_to_string (input);
									if (input_str) {
										R_LOG_DEBUG ("Input string: %s", input_str);
										block->input = strdup (input_str);
										R2AI_ToolCall *tc = (R2AI_ToolCall *)&message->tool_calls[tool_idx];
										tc->arguments = strdup (input_str);
										free (input_str);
									}
								}

								tool_idx++;
							} else if (!strcmp (type->str_value, "thinking")) {
								const RJson *data = r_json_get (content_item, "data");
								const RJson *thinking = r_json_get (content_item, "thinking");
								const RJson *signature = r_json_get (content_item, "signature");
								if (data && data->type == R_JSON_STRING) {
									block->data = strdup (data->str_value);
								}
								if (thinking && thinking->type == R_JSON_STRING) {
									block->thinking = strdup (thinking->str_value);
								}
								if (signature && signature->type == R_JSON_STRING) {
									block->signature = strdup (signature->str_value);
								}
								block->type = strdup ("thinking");

								r_strbuf_append (content_buf, "\n\x1b[90m<thinking>\n");
								r_strbuf_append (content_buf, block->thinking);
								r_strbuf_append (content_buf, "\n</thinking>\x1b[0m\n");
							}
							block_idx++;
						}
						content_item = content_item->next;
					}
					message->content_blocks = cb;
				}

				// Store the content
				message->content = r_strbuf_drain (content_buf);

				// If there's no content and no tool calls, clean up
				if (!message->content && !message->n_tool_calls) {
					r2ai_message_free (message);
					message = NULL;
				}
			}
			r_json_free (jres);
		}
		free (response_copy);
	}

	// Assign message and usage to result
	result->message = message;
	result->usage = usage;

	// Free the HTTP response body
	free (res);
	return result;
}

R_IPI char *r2ai_anthropic_stream(RCore *core, R2AIArgs args) {
	// Not implemented yet
	return NULL;
}
