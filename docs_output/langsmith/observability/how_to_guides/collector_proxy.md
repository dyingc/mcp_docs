# [Beta] LangSmith Collector-Proxy | 🦜️🛠️ LangSmith

On this page

Note

The LangSmith Collector-Proxy feature is currently in Beta and subject to change. [View the source code on GitHub](https://github.com/langchain-ai/langsmith-collector-proxy).

The LangSmith Collector-Proxy is a middleware service designed to efficiently aggregate, compress, and bulk-upload OTEL tracing data from your applications to LangSmith. It's optimized for large-scale, parallel environments generating high volumes of spans.

## When to Use the Collector-Proxy​

The Collector-Proxy is particularly valuable when:

  * You're running multiple instances of your application in parallel and need to efficiently aggregate traces
  * You want more efficient tracing than direct OTEL API calls to LangSmith (the collector optimizes batching and compression)
  * You're using a language that doesn't have a native LangSmith SDK

## Key Features​

  * **Efficient Data Transfer** Batches multiple spans into fewer, larger uploads.
  * **Compression** Uses zstd to minimize payload size.
  * **OTLP Support** Accepts OTLP JSON and Protobuf over HTTP POST.
  * **Semantic Translation** Maps GenAI/OpenInference conventions to the LangSmith Run model.
  * **Flexible Batching** Flush by span count or time interval.

## Configuration​

Configure via environment variables:

Variable| Description| Default  
---|---|---  
`HTTP_PORT`| Port to run the proxy server| `4318`  
`LANGSMITH_ENDPOINT`| LangSmith backend URL| `https://api.smith.langchain.com`  
`LANGSMITH_API_KEY`| API key for LangSmith| **Required** (env var or header)  
`LANGSMITH_PROJECT`| Default tracing project| Default project if not specified  
`BATCH_SIZE`| Spans per upload batch| `100`  
`FLUSH_INTERVAL_MS`| Flush interval in milliseconds| `1000`  
`MAX_BUFFER_BYTES`| Max uncompressed buffer size| `10485760` (10 MB)  
`MAX_BODY_BYTES`| Max incoming request body size| `209715200` (200 MB)  
`MAX_RETRIES`| Retry attempts for failed uploads| `3`  
`RETRY_BACKOFF_MS`| Initial backoff in milliseconds| `100`  
  
### Project Configuration​

The Collector-Proxy supports LangSmith project configuration with the following priority:

  1. If a project is specified in the request headers (`Langsmith-Project`), that project will be used
  2. If no project is specified in headers, it will use the project set in the `LANGSMITH_PROJECT` environment variable
  3. If neither is set, it will trace to the `default` project.

### Authentication​

The API key can be provided either:

  * As an environment variable (`LANGSMITH_API_KEY`)
  * In the request headers (`X-API-Key`)

## Deployment (Docker)​

You can deploy the Collector-Proxy with Docker:

  1. **Build the image**
         
         docker build \  
           -t langsmith-collector-proxy:beta .  
         

  2. **Run the container**

    
    
    docker run -d \  
      -p 4318:4318 \  
      -e LANGSMITH_API_KEY=<your_api_key> \  
      -e LANGSMITH_PROJECT=<your_project> \  
      langsmith-collector-proxy:beta  
    

## Usage​

Point any OTLP-compatible client or the OpenTelemetry Collector exporter at:
    
    
    export OTEL_EXPORTER_OTLP_ENDPOINT=http://<host>:4318/v1/traces  
    export OTEL_EXPORTER_OTLP_HEADERS="X-API-Key=<your_api_key>,Langsmith-Project=<your_project>"  
    

Send a test trace:
    
    
    curl -X POST http://localhost:4318/v1/traces \  
      -H "Content-Type: application/json" \  
      --data '{  
        "resourceSpans": [  
          {  
            "resource": {  
              "attributes": [  
                {  
                  "key": "service.name",  
                  "value": { "stringValue": "test-service" }  
                }  
              ]  
            },  
            "scopeSpans": [  
              {  
                "scope": {  
                  "name": "example/instrumentation",  
                  "version": "1.0.0"  
                },  
                "spans": [  
                  {  
                    "traceId": "T6nh/mMkIONaoHewS9UWIw==",  
                    "spanId": "0tEqJwCpvU0=",  
                    "name": "parent-span",  
                    "kind": "SPAN_KIND_INTERNAL",  
                    "startTimeUnixNano": 1747675155185223936,  
                    "endTimeUnixNano":   1747675156185223936,  
                    "attributes": [  
                      {  
                        "key": "gen_ai.prompt",  
                        "value": {  
                          "stringValue": "{\"text\":\"Hello, world!\"}"  
                        }  
                      },  
                      {  
                        "key": "gen_ai.usage.input_tokens",  
                        "value": {  
                          "intValue": "5"  
                        }  
                      },  
                      {  
                        "key": "gen_ai.completion",  
                        "value": {  
                          "stringValue": "{\"text\":\"Hi there!\"}"  
                        }  
                      },  
                      {  
                        "key": "gen_ai.usage.output_tokens",  
                        "value": {  
                          "intValue": "3"  
                        }  
                      }  
                    ],  
                    "droppedAttributesCount": 0,  
                    "events": [],  
                    "links": [],  
                    "status": {}  
                  }  
                ]  
              }  
            ]  
          }  
        ]  
      }'  
    

## Health & Scaling​

  * **Liveness** : `GET /live` → 200
  * **Readiness** : `GET /ready` → 200

## Horizontal Scaling​

To ensure full traces are batched correctly, route spans with the same trace ID to the same instance (e.g., via consistent hashing).

## Fork & Extend​

Fork the [Collector-Proxy repo on GitHub](https://github.com/langchain-ai/langsmith-collector-proxy) and implement your own converter:

  * Create a custom `GenAiConverter` or modify the existing one in `internal/translator/otel_converter.go`
  * Register the custom converter in `internal/translator/translator.go`

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * When to Use the Collector-Proxy
  * Key Features
  * Configuration
    * Project Configuration
    * Authentication
  * Deployment (Docker)
  * Usage
  * Health & Scaling
  * Horizontal Scaling
  * Fork & Extend

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)