# Observability how-to guides | 🦜️🛠️ LangSmith

On this page

Step-by-step guides that cover key tasks and operations for adding observability to your LLM applications with LangSmith.

## Tracing configuration​

Set up LangSmith tracing to get visibility into your production applications.

### Basic configuration​

  * [Set your tracing project](/observability/how_to_guides/log_traces_to_project)
  * [Trace any Python or JS Code](/observability/how_to_guides/annotate_code)
  * [Trace using the LangSmith REST API](/observability/how_to_guides/trace_with_api)
  * [Trace without environment variables](/observability/how_to_guides/trace_without_env_vars)

### Integrations​

  * [LangChain OSS libraries](/observability/how_to_guides/trace_with_langchain)
  * [LangGraph](/observability/how_to_guides/trace_with_langgraph)
  * [OpenAI](/observability/how_to_guides/annotate_code#wrap-the-openai-client)
  * [Anthropic (Python only)](/observability/how_to_guides/annotate_code#wrap-the-anthropic-client-python-only)
  * [Instructor](/observability/how_to_guides/trace_with_instructor)
  * [Vercel AI SDK (JS only)](/observability/how_to_guides/trace_with_vercel_ai_sdk)
  * [OpenTelemetry](/observability/how_to_guides/trace_with_opentelemetry)
  * [OpenAI Agent SDK (Python only)](/observability/how_to_guides/trace_with_openai_agents_sdk)

### Advanced configuration​

  * [Configure threads](/observability/how_to_guides/threads)
  * [Set a sampling rate for traces](/observability/how_to_guides/sample_traces)
  * [Add metadata and tags to traces](/observability/how_to_guides/add_metadata_tags)
  * [Implement distributed tracing](/observability/how_to_guides/distributed_tracing)
  * [Trace LangChain with OpenTelemetry (Python only)](/observability/how_to_guides/trace_langchain_with_otel)
  * [Access the current span within a traced function](/observability/how_to_guides/access_current_span)
  * [Log custom LLM traces](/observability/how_to_guides/log_llm_trace)
  * [Log LLM token counts](/observability/how_to_guides/log_llm_trace#provide-token-and-cost-information)
  * [Calculate token-based costs for traces](/observability/how_to_guides/calculate_token_based_costs)
  * [Log multimodal traces](/observability/how_to_guides/log_multimodal_traces)
  * [Log retriever traces](/observability/how_to_guides/log_retriever_trace)
  * [Prevent logging of sensitive data in traces](/observability/how_to_guides/mask_inputs_outputs)
  * [Trace generator functions](/observability/how_to_guides/trace_generator_functions)
  * [Trace JS functions in serverless environments](/observability/how_to_guides/serverless_environments)
  * [Troubleshoot trace testing](/observability/how_to_guides/nest_traces)
  * [Upload files with traces](/observability/how_to_guides/upload_files_with_traces)
  * [Print out logs from the LangSmith SDK (Python Only)](/observability/how_to_guides/output_detailed_logs)
  * [Troubleshooting: Missing or Misrouted Traces](/observability/how_to_guides/toubleshooting_variable_caching)
  * [Using the LangSmith Collector Proxy](/observability/how_to_guides/collector_proxy)

## Tracing projects UI & API​

View and interact with your traces to debug your applications.

  * [Filter traces in a project](/observability/how_to_guides/filter_traces_in_application)
  * [Save a filter for your project](/observability/how_to_guides/filter_traces_in_application#saved-filters)
  * [Query / Export traces using the SDK (low volume)](/observability/how_to_guides/export_traces)
  * [Bulk exporting traces (high volume)](/observability/how_to_guides/data_export)
  * [Share or unshare a trace publicly](/observability/how_to_guides/share_trace)
  * [Compare traces](/observability/how_to_guides/compare_traces)
  * [View threads](/observability/how_to_guides/threads#view-threads)

## Monitoring​

Continuously monitor your production systems applications using dashboards, and set up alerts to get notified when metrics drop.

  * [Monitor projects with dashboards](/observability/how_to_guides/dashboards)
  * [Set up alerts for your project](/observability/how_to_guides/alerts)

## Automations​

Leverage LangSmith's powerful monitoring, automation, and online evaluation features to make sense of your production data.

  * [Set up automation rules](/observability/how_to_guides/rules)
  * [Set up webhook notifications for rules](/observability/how_to_guides/webhooks)
  * [Perform online evaluations](/observability/how_to_guides/online_evaluations)

## Human feedback​

  * [Log user feedback using the SDK](/evaluation/how_to_guides/attach_user_feedback)
  * [Set up a new feedback criteria](/evaluation/how_to_guides/set_up_feedback_criteria)
  * [Annotate traces inline in the UI](/evaluation/how_to_guides/annotate_traces_inline)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Tracing configuration
    * Basic configuration
    * Integrations
    * Advanced configuration
  * Tracing projects UI & API
  * Monitoring
  * Automations
  * Human feedback

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)