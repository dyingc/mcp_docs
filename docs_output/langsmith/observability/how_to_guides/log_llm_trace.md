# Log custom LLM traces | 🦜️🛠️ LangSmith

On this page

note

Nothing will break if you don't log LLM traces in the correct format - data will still be logged. However, the data will not be processed or rendered in a way that is specific to LLMs.

LangSmith provides special rendering and processing for LLM traces, including token counting (assuming token counts are not available from the model provider) and token-based cost calculation. In order to make the most of this feature, you must log your LLM traces in a specific format.

note

The examples below uses the `traceable` decorator/wrapper to log the model run (which is the recommended approach for Python and JS/TS). However, the same idea applies if you are using the [RunTree](/observability/how_to_guides/annotate_code#use-the-runtree-api) or [API](https://api.smith.langchain.com/redoc) directly.

## Chat-style models​

### Using LangChain OSS or LangSmith wrappers​

If you are using OpenAI or Anthropic models, we suggest using the [`wrap_openai`](/observability/how_to_guides/annotate_code#wrap-the-openai-client) or [`wrap_anthropic`](https://docs.smith.langchain.com/reference/python/wrappers/langsmith.wrappers._anthropic.wrap_anthropic) which will automatically log traces in the format LangSmith expects.

You can also use any of the [LangChain OSS chat models](https://python.langchain.com/docs/integrations/chat/#all-chat-models) as a drop in for directly accessing the API of any of the providers, and this will also log LLM traces in the format LangSmith expects.

### Implementing your own custom chat-model​

You may also trace your model calls using [`traceable`](/observability/how_to_guides/annotate_code) or other broader tracing techniques. To properly mark the traced function as an LLM run in this case, at bare minimum you must pass `run_type` as `"llm"` like this:

  * Python
  * TypeScript

    
    
    from langsmith import traceable  
      
    @traceable(run_type="llm")  
    def chat_model(messages: list):  
      ...  
    
    
    
    import { traceable } from "langsmith/traceable";  
      
    const chatModel = traceable(  
    async (messages) => {  
      // Call the model here  
    },  
    { run_type: "llm" }  
    );  
    

To make your custom LLM traces appear well-formatted in the LangSmith UI, your trace inputs and outputs must conform to a format LangSmith recognizes:

  * A list of messages in [OpenAI](https://platform.openai.com/docs/api-reference/messages) or [Anthropic](https://docs.anthropic.com/en/api/messages) format, represented as Python dictionaries or TypeScript objects.
    * Each message must contain the key `role` and `content`.
    * Messages with the `"assistant"` role may optionally contain `tool_calls`. These `tool_calls` may be in [OpenAI](https://platform.openai.com/docs/guides/function-calling?api-mode=chat) format or [LangChain's format](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCall.html#langchain_core.messages.tool.ToolCall).
  * An dict/object containing `"messages"` key with a list of messages in the above format.
    * LangSmith may use additional parameters in this input dict that match OpenAI's [chat completion endpoint](https://platform.openai.com/docs/guides/text?api-mode=chat) for rendering in the trace view, such as a list of available `tools` for the model to call.

Here are some examples:

  * List of messages
  * Messages dict

    
    
    # Format 1: List of messages  
    inputs = [  
        {"role": "system", "content": "You are a helpful assistant."},  
        {"role": "user", "content": "What's the weather like?"},  
        {  
            "role": "assistant",   
            "content": "I need to check the weather for you.",  
            "tool_calls": [  
                {  
                    "id": "call_123",  
                    "type": "function",  
                    "function": {  
                        "name": "get_weather",  
                        "arguments": '{"location": "current"}'  
                    }  
                }  
            ]  
        }  
    ]  
      
    @traceable(run_type="llm")  
    def chat_model(messages: list):  
        ...  
      
    chat_model(inputs)  
    
    
    
    # Format 2: Object with messages key  
    inputs = {  
        "messages": [  
            {"role": "system", "content": "You are a helpful assistant."},  
            {"role": "user", "content": "What's the weather like?"}  
        ],  
        "tools": [  
            {  
                "type": "function",  
                "function": {  
                    "name": "get_weather",  
                    "description": "Get current weather",  
                    "parameters": {  
                        "type": "object",  
                        "properties": {  
                            "location": {"type": "string"}  
                        }  
                    }  
                }  
            }  
        ],  
        "temperature": 0.7  
    }  
      
    @traceable(run_type="llm")  
    def chat_model(messages: dict):  
        ...  
      
    chat_model(inputs)  
    

The output is accepted in any of the following formats:

  * A dictionary/object that contains the key `choices` with a value that is a list of dictionaries/objects. Each dictionary/object must contain the key `message`, which maps to a message object with the keys `role` and `content`.
  * A dictionary/object that contains the key `message` with a value that is a message object with the keys `role` and `content`.
  * A tuple/array of two elements, where the first element is the role and the second element is the content.
  * A dictionary/object that contains the key `role` and `content`.

Here are some examples:

  * Choices format
  * Message format
  * Tuple format
  * Direct format

    
    
    from langsmith import traceable  
      
    @traceable(run_type="llm")  
    def chat_model_choices(messages):  
        # Your model logic here  
        return {  
            "choices": [  
                {  
                    "message": {  
                        "role": "assistant",  
                        "content": "Sure, what time would you like to book the table for?"  
                    }  
                }  
            ]  
        }  
      
    # Usage  
    inputs = [  
        {"role": "system", "content": "You are a helpful assistant."},  
        {"role": "user", "content": "I'd like to book a table for two."}  
    ]  
    chat_model_choices(inputs)  
    
    
    
    from langsmith import traceable  
      
    @traceable(run_type="llm")  
    def chat_model_message(messages):  
        # Your model logic here  
        return {  
            "message": {  
                "role": "assistant",  
                "content": "Sure, what time would you like to book the table for?"  
            }  
        }  
      
    # Usage  
    inputs = [  
        {"role": "system", "content": "You are a helpful assistant."},  
        {"role": "user", "content": "I'd like to book a table for two."}  
    ]  
    chat_model_message(inputs)  
    
    
    
    from langsmith import traceable  
      
    @traceable(run_type="llm")  
    def chat_model_tuple(messages):  
        # Your model logic here  
        return ["assistant", "Sure, what time would you like to book the table for?"]  
      
    # Usage  
    inputs = [  
        {"role": "system", "content": "You are a helpful assistant."},  
        {"role": "user", "content": "I'd like to book a table for two."}  
    ]  
    chat_model_tuple(inputs)  
    
    
    
    from langsmith import traceable  
      
    @traceable(run_type="llm")  
    def chat_model_direct(messages):  
        # Your model logic here  
        return {  
            "role": "assistant",  
            "content": "Sure, what time would you like to book the table for?"  
        }  
      
    # Usage  
    inputs = [  
        {"role": "system", "content": "You are a helpful assistant."},  
        {"role": "user", "content": "I'd like to book a table for two."}  
    ]  
    chat_model_direct(inputs)  
    

You can also provide the following `metadata` fields to help LangSmith identify the model - which if recognized, LangSmith will use to automatically calculate costs. To learn more about how to use the `metadata` fields, see [this guide](/observability/how_to_guides/add_metadata_tags).

  * `ls_provider`: The provider of the model, eg "openai", "anthropic", etc.
  * `ls_model_name`: The name of the model, eg "gpt-4o-mini", "claude-3-opus-20240307", etc.

  * Python
  * TypeScript

    
    
    from langsmith import traceable  
      
    inputs = [  
      {"role": "system", "content": "You are a helpful assistant."},  
      {"role": "user", "content": "I'd like to book a table for two."},  
    ]  
      
    output = {  
      "choices": [  
          {  
              "message": {  
                  "role": "assistant",  
                  "content": "Sure, what time would you like to book the table for?"  
              }  
          }  
      ]  
    }  
      
    # Can also use one of:  
    # output = {  
    #     "message": {  
    #         "role": "assistant",  
    #         "content": "Sure, what time would you like to book the table for?"  
    #     }  
    # }  
    #  
    # output = {  
    #     "role": "assistant",  
    #     "content": "Sure, what time would you like to book the table for?"  
    # }  
    #  
    # output = ["assistant", "Sure, what time would you like to book the table for?"]  
      
    @traceable(  
      run_type="llm",  
      metadata={"ls_provider": "my_provider", "ls_model_name": "my_model"}  
    )  
    def chat_model(messages: list):  
      return output  
      
    chat_model(inputs)  
    
    
    
    import { traceable } from "langsmith/traceable";  
      
    const messages = [  
    { role: "system", content: "You are a helpful assistant." },  
    { role: "user", content: "I'd like to book a table for two." }  
    ];  
      
    const output = {  
    choices: [  
      {  
        message: {  
          role: "assistant",  
          content: "Sure, what time would you like to book the table for?"  
        }  
      }  
    ]  
    };  
      
    // Can also use one of:  
    // const output = {  
    //   message: {  
    //     role: "assistant",  
    //     content: "Sure, what time would you like to book the table for?"  
    //   }  
    // };  
    //  
    // const output = {  
    //   role: "assistant",  
    //   content: "Sure, what time would you like to book the table for?"  
    // };  
    //  
    // const output = ["assistant", "Sure, what time would you like to book the table for?"];  
      
    const chatModel = traceable(  
    async ({ messages }: { messages: { role: string; content: string }[] }) => {  
      return output;  
    },  
    { run_type: "llm", name: "chat_model", metadata: { ls_provider: "my_provider", ls_model_name: "my_model" } }  
    );  
      
    await chatModel({ messages });  
    

The above code will log the following trace:

![](/assets/images/chat_model-e77d56df5dcd75403b5f6d4f76d23f5b.png)

If you implement a custom streaming chat_model, you can "reduce" the outputs into the same format as the non-streaming version. This is currently only supported in Python.
    
    
    def _reduce_chunks(chunks: list):  
        all_text = "".join([chunk["choices"][0]["message"]["content"] for chunk in chunks])  
        return {"choices": [{"message": {"content": all_text, "role": "assistant"}}]}  
      
    @traceable(  
        run_type="llm",  
        reduce_fn=_reduce_chunks,  
        metadata={"ls_provider": "my_provider", "ls_model_name": "my_model"}  
    )  
    def my_streaming_chat_model(messages: list):  
        for chunk in ["Hello, " + messages[1]["content"]]:  
            yield {  
                "choices": [  
                    {  
                        "message": {  
                            "content": chunk,  
                            "role": "assistant",  
                        }  
                    }  
                ]  
            }  
      
    list(  
        my_streaming_chat_model(  
            [  
                {"role": "system", "content": "You are a helpful assistant. Please greet the user."},  
                {"role": "user", "content": "polly the parrot"},  
            ],  
        )  
    )  
    

tip

If `ls_model_name` is not present in `extra.metadata`, other fields might be used from the `extra.metadata` for estimating token counts. The following fields are used in the order of precedence:

  1. `metadata.ls_model_name`
  2. `inputs.model`
  3. `inputs.model_name`

## Provide token and cost information​

By default, LangSmith uses [tiktoken](https://github.com/openai/tiktoken) to count tokens, utilizing a best guess at the model's tokenizer based on the `ls_model_name` provided. It also calculates costs automatically by using the [model pricing table](https://smith.langchain.com/settings/workspaces/models). To learn how LangSmith calculates token-based costs, see [this guide](/observability/how_to_guides/calculate_token_based_costs).

However, many models already include exact token counts as part of the response. If you have this information, you can override the default token calculation in LangSmith in one of two ways:

  1. Extract usage within your traced function and set a `usage_metadata` field on the run's metadata.
  2. Return a `usage_metadata` field in your traced function outputs.

In both cases, the usage metadata you send should contain a subset of the following LangSmith-recognized fields:

Setting usage metadata

You cannot set any fields other than the ones listed below. You do not need to include all fields.
    
    
    class UsageMetadata(TypedDict, total=False):  
        input_tokens: int  
        """The number of tokens used for the prompt."""  
        output_tokens: int  
        """The number of tokens generated as output."""  
        total_tokens: int  
        """The total number of tokens used."""  
        input_token_details: dict[str, float]  
        """The details of the input tokens."""  
        output_token_details: dict[str, float]  
        """The details of the output tokens."""  
        input_cost: float  
        """The cost of the input tokens."""  
        output_cost: float  
        """The cost of the output tokens."""  
        total_cost: float  
        """The total cost of the tokens."""  
        input_cost_details: dict[str, float]  
        """The cost details of the input tokens."""  
        output_cost_details: dict[str, float]  
        """The cost details of the output tokens."""  
    

Note that the usage data can also include cost information, in case you do not want to rely on LangSmith's token-based cost formula. This is useful for models with pricing that is not linear by token type.

### Setting run metadata​

You can [modify the current run's metadata](/observability/how_to_guides/add_metadata_tags) with usage information within your traced function. The advantage of this approach is that you do not need to change your traced function's runtime outputs. Here's an example:

Dependencies

Requires `langsmith>=0.3.43` (Python) and `langsmith>=0.3.30` (JS/TS).

  * Python
  * TypeScript

    
    
    from langsmith import traceable, get_current_run_tree  
      
    inputs = [  
      {"role": "system", "content": "You are a helpful assistant."},  
      {"role": "user", "content": "I'd like to book a table for two."},  
    ]  
      
    @traceable(  
      run_type="llm",  
      metadata={"ls_provider": "my_provider", "ls_model_name": "my_model"}  
    )  
    def chat_model(messages: list):  
      llm_output = {  
          "choices": [  
              {  
                  "message": {  
                      "role": "assistant",  
                      "content": "Sure, what time would you like to book the table for?"  
                  }  
              }  
          ],  
          "usage_metadata": {  
              "input_tokens": 27,  
              "output_tokens": 13,  
              "total_tokens": 40,  
              "input_token_details": {"cache_read": 10},  
              # If you wanted to specify costs:  
              # "input_cost": 1.1e-6,  
              # "input_cost_details": {"cache_read": 2.3e-7},  
              # "output_cost": 5.0e-6,  
          },  
      }  
      run = get_current_run_tree()  
      run.set(usage_metadata=llm_output["usage_metadata"])  
      return llm_output["choices"][0]["message"]  
      
    chat_model(inputs)  
    
    
    
    import { traceable, getCurrentRunTree } from "langsmith/traceable";  
      
    const messages = [  
    { role: "system", content: "You are a helpful assistant." },  
    { role: "user", content: "I'd like to book a table for two." },  
    ];  
      
    const chatModel = traceable(  
    async ({  
      messages,  
    }: {  
      messages: { role: string; content: string }[];  
      model: string;  
    }) => {  
      const llmOutput = {  
        choices: [  
          {  
            message: {  
              role: "assistant",  
              content: "Sure, what time would you like to book the table for?",  
            },  
          },  
        ],  
        usage_metadata: {  
          input_tokens: 27,  
          output_tokens: 13,  
          total_tokens: 40,  
        },  
      };  
      const runTree = getCurrentRunTree();  
      runTree.metadata.usage_metadata = llmOutput.usage_metadata;  
      return llmOutput.choices[0].message;  
    },  
    { run_type: "llm", name: "chat_model", metadata: { ls_provider: "my_provider", ls_model_name: "my_model" } }  
    );  
      
    await chatModel({ messages });  
    

### Setting run outputs​

You can add a `usage_metadata` key to the function's response to set manual token counts and costs.

  * Python
  * TypeScript

    
    
    from langsmith import traceable  
      
    inputs = [  
      {"role": "system", "content": "You are a helpful assistant."},  
      {"role": "user", "content": "I'd like to book a table for two."},  
    ]  
      
    output = {  
      "choices": [  
          {  
              "message": {  
                  "role": "assistant",  
                  "content": "Sure, what time would you like to book the table for?"  
              }  
          }  
      ],  
      "usage_metadata": {  
          "input_tokens": 27,  
          "output_tokens": 13,  
          "total_tokens": 40,  
          "input_token_details": {"cache_read": 10},  
          # If you wanted to specify costs:  
          # "input_cost": 1.1e-6,  
          # "input_cost_details": {"cache_read": 2.3e-7},  
          # "output_cost": 5.0e-6,  
      },  
    }  
      
    @traceable(  
      run_type="llm",  
      metadata={"ls_provider": "my_provider", "ls_model_name": "my_model"}  
    )  
    def chat_model(messages: list):  
      return output  
      
    chat_model(inputs)  
    
    
    
    import { traceable } from "langsmith/traceable";  
      
    const messages = [  
    { role: "system", content: "You are a helpful assistant." },  
    { role: "user", content: "I'd like to book a table for two." },  
    ];  
      
    const output = {  
    choices: [  
      {  
        message: {  
          role: "assistant",  
          content: "Sure, what time would you like to book the table for?",  
        },  
      },  
    ],  
    usage_metadata: {  
      input_tokens: 27,  
      output_tokens: 13,  
      total_tokens: 40,  
    },  
    };  
      
    const chatModel = traceable(  
    async ({  
      messages,  
    }: {  
      messages: { role: string; content: string }[];  
      model: string;  
    }) => {  
      return output;  
    },  
    { run_type: "llm", name: "chat_model", metadata: { ls_provider: "my_provider", ls_model_name: "my_model" } }  
    );  
      
    await chatModel({ messages });  
    

## Instruct-style models​

For instruct-style models (string in, string out), your inputs must contain a key `prompt` with a string value. Other inputs are also permitted. The output must return an object that, when serialized, contains the key `choices` with a list of dictionaries/objects. Each must contain the key `text` with a string value. The same rules for `metadata` and `usage_metadata` apply as for chat-style models.

  * Python
  * TypeScript

    
    
    @traceable(  
      run_type="llm",  
      metadata={"ls_provider": "my_provider", "ls_model_name": "my_model"}  
    )  
    def hello_llm(prompt: str):  
      return {  
          "choices": [  
              {"text": "Hello, " + prompt}  
          ],  
          "usage_metadata": {  
              "input_tokens": 4,  
              "output_tokens": 5,  
              "total_tokens": 9,  
          },  
      }  
      
    hello_llm("polly the parrot\n")  
    
    
    
    import { traceable } from "langsmith/traceable";  
      
    const helloLLM = traceable(  
    ({ prompt }: { prompt: string }) => {  
      return {  
        choices: [  
          { text: "Hello, " + prompt }  
        ],  
          usage_metadata: {  
              input_tokens: 4,  
              output_tokens: 5,  
              total_tokens: 9,  
          },  
      };  
    },  
    { run_type: "llm", name: "hello_llm", metadata: { ls_provider: "my_provider", ls_model_name: "my_model" } }  
    );  
      
    await helloLLM({ prompt: "polly the parrot\n" });  
    

The above code will log the following trace:

![](/assets/images/hello_llm-d68121a499264f9769e79a303c02611f.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Chat-style models
    * Using LangChain OSS or LangSmith wrappers
    * Implementing your own custom chat-model
  * Provide token and cost information
    * Setting run metadata
    * Setting run outputs
  * Instruct-style models

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)