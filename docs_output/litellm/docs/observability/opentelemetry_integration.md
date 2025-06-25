# OpenTelemetry - Tracing LLMs with any observability tool | liteLLM

On this page

OpenTelemetry is a CNCF standard for observability. It connects to any observability tool, such as Jaeger, Zipkin, Datadog, New Relic, Traceloop and others.

## Getting Started​

Install the OpenTelemetry SDK:
    
    
    pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp  
    

Set the environment variables (different providers may require different variables):

  * Log to Traceloop Cloud
  * Log to OTEL HTTP Collector
  * Log to OTEL GRPC Collector
  * Log to Laminar

    
    
    OTEL_EXPORTER="otlp_http"  
    OTEL_ENDPOINT="https://api.traceloop.com"  
    OTEL_HEADERS="Authorization=Bearer%20<your-api-key>"  
    
    
    
    OTEL_EXPORTER_OTLP_ENDPOINT="http://0.0.0.0:4318"  
    OTEL_EXPORTER_OTLP_PROTOCOL=http/json  
    OTEL_EXPORTER_OTLP_HEADERS="api-key=key,other-config-value=value"  
    
    
    
    OTEL_EXPORTER_OTLP_ENDPOINT="http://0.0.0.0:4318"  
    OTEL_EXPORTER_OTLP_PROTOCOL=grpc  
    OTEL_EXPORTER_OTLP_HEADERS="api-key=key,other-config-value=value"  
    
    
    
    OTEL_EXPORTER="otlp_grpc"  
    OTEL_ENDPOINT="https://api.lmnr.ai:8443"  
    OTEL_HEADERS="authorization=Bearer <project-api-key>"  
    

Use just 1 line of code, to instantly log your LLM responses **across all providers** with OpenTelemetry:
    
    
    litellm.callbacks = ["otel"]  
    

## Redacting Messages, Response Content from OpenTelemetry Logging​

### Redact Messages and Responses from all OpenTelemetry Logging​

Set `litellm.turn_off_message_logging=True` This will prevent the messages and responses from being logged to OpenTelemetry, but request metadata will still be logged.

### Redact Messages and Responses from specific OpenTelemetry Logging​

In the metadata typically passed for text completion or embedding calls you can set specific keys to mask the messages and responses for this call.

Setting `mask_input` to `True` will mask the input from being logged for this call

Setting `mask_output` to `True` will make the output from being logged for this call.

Be aware that if you are continuing an existing trace, and you set `update_trace_keys` to include either `input` or `output` and you set the corresponding `mask_input` or `mask_output`, then that trace will have its existing input and/or output replaced with a redacted message.

## Support​

For any question or issue with the integration you can reach out to the OpenLLMetry maintainers on [Slack](https://traceloop.com/slack) or via [email](mailto:dev@traceloop.com).

## Troubleshooting​

### Trace LiteLLM Proxy user/key/org/team information on failed requests​

LiteLLM emits the user_api_key_metadata

  * key hash
  * key_alias
  * org_id
  * user_id
  * team_id

for successful + failed requests

click under `litellm_request` in the trace

  * Getting Started
  * Redacting Messages, Response Content from OpenTelemetry Logging
    * Redact Messages and Responses from all OpenTelemetry Logging
    * Redact Messages and Responses from specific OpenTelemetry Logging
  * Support
  * Troubleshooting
    * Trace LiteLLM Proxy user/key/org/team information on failed requests