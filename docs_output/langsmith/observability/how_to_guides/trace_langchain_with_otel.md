# Trace LangChain with OpenTelemetry | 🦜️🛠️ LangSmith

On this page

The LangSmith Python SDK supports OpenTelemetry integration out of the box, letting you trace LangChain and LangGraph apps and export data to LangSmith, to any OTLP-compatible backend, or to both at the same time.

This guide covers three core topics:

  * Sending Traces to LangSmith through OTel

  * Exporting to OTel-Compatible Providers – Send traces to third-party platforms via the OpenTelemetry Collector.

  * Distributed Tracing – Propagate context across services for end-to-end visibility.

info

Since langsmith ≥ 0.4.1, setting LANGSMITH_OTEL_ENABLED=true will by default send traces to both LangSmith and your OTEL endpoint (if you have global trace provider initiazlied). No extra code is needed for fan-out.

## Sending Traces to LangSmith through OTel​

### 1\. Installation​

info

Requires Python SDK version `langsmith>=0.3.18`.

Install the LangSmith package with OpenTelemetry support:
    
    
    pip install "langsmith[otel]"  
    pip install langchain  
    

### 2\. Enable the OpenTelemetry integration​

In your LangChain/LangGraph App, enable the OpenTelemetry integration by setting the `LANGSMITH_OTEL_ENABLED` environment variable:
    
    
    LANGSMITH_OTEL_ENABLED=true  
    LANGSMITH_TRACING=true  
    LANGSMITH_ENDPOINT=https://api.smith.langchain.com  
    LANGSMITH_API_KEY=<your_langsmith_api_key>  
    

### 3\. Create a LangChain application with tracing​

Here's a simple example showing how to use the OpenTelemetry integration with LangChain:
    
    
    import os  
    from langchain_openai import ChatOpenAI  
    from langchain_core.prompts import ChatPromptTemplate  
      
      
    # Create a chain  
    prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")  
    model = ChatOpenAI()  
    chain = prompt | model  
      
    # Run the chain  
    result = chain.invoke({"topic": "programming"})  
    print(result.content)  
    

### 4\. View the traces in LangSmith​

Once your application runs, you'll see the traces in your LangSmith dashboard [like this one](https://smith.langchain.com/public/a762af6c-b67d-4f22-90a0-728df16baeba/r).

## Sending Traces to Alternate Providers​

While LangSmith is the default destination for OpenTelemetry traces, you can also configure OpenTelemetry to send traces to other observability platforms.

### Using Environment Variables or Global Configuration​

By default, the LangSmith OpenTelemetry exporter will send data to the LangSmith API OTEL endpoint (and to OTEL endpoint as well, if you configured global TracerProvider), but this can be customized by setting standard OTEL environment variables:
    
    
    OTEL_EXPORTER_OTLP_ENDPOINT: Override the endpoint URL  
    OTEL_EXPORTER_OTLP_HEADERS: Add custom headers (LangSmith API keys and Project are added automatically)  
    OTEL_SERVICE_NAME: Set a custom service name (defaults to "langsmith")  
    

LangSmith uses the HTTP trace exporter by default. If you'd like to use your own tracing provider, you can either:

  1. Set the OTEL environment variables as shown above, or
  2. Set a global trace provider before initializing LangChain components, which LangSmith will detect and use instead of creating its own.

### Configuring Alternate OTLP Endpoints​

To send traces to a different provider, configure the OTLP exporter with your provider's endpoint:
    
    
    import os  
    from opentelemetry import trace  
    from opentelemetry.sdk.trace import TracerProvider  
    from opentelemetry.sdk.trace.export import BatchSpanProcessor  
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter  
    from langchain_openai import ChatOpenAI  
    from langchain_core.prompts import ChatPromptTemplate  
      
    # Set environment variables for LangChain  
    os.environ["LANGSMITH_OTEL_ENABLED"] = "true"  
    os.environ["LANGSMITH_TRACING"] = "true"  
      
    # Configure the OTLP exporter for your custom endpoint  
    provider = TracerProvider()  
    otlp_exporter = OTLPSpanExporter(  
        # Change to your provider's endpoint  
        endpoint="https://otel.your-provider.com/v1/traces",  
        # Add any required headers for authentication  
        headers={"api-key": "your-api-key"}  
    )  
    processor = BatchSpanProcessor(otlp_exporter)  
    provider.add_span_processor(processor)  
    trace.set_tracer_provider(provider)  
      
    # Create and run a LangChain application  
    prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")  
    model = ChatOpenAI()  
    chain = prompt | model  
      
    result = chain.invoke({"topic": "programming"})  
    print(result.content)  
    

info

To disable the hybrid behavior after 0.4.1 and send traces only to your OTEL endpoint and exclude sending to LangSmith, add an additional env var:

LANGSMITH_OTEL_ONLY = "true"

### Using OpenTelemetry Collector for Fan-out​

For more advanced scenarios, you can use the OpenTelemetry Collector to fan out your telemetry data to multiple destinations. This is a more scalable approach than configuring multiple exporters in your application code.

  1. **Install the OpenTelemetry Collector** : Follow the [official installation instructions](https://opentelemetry.io/docs/collector/getting-started/) for your environment.

  2. **Configure the Collector** : Create a configuration file (e.g., `otel-collector-config.yaml`) that exports to multiple destinations:

    
    
    receivers:  
      otlp:  
        protocols:  
          grpc:  
            endpoint: 0.0.0.0:4317  
          http:  
            endpoint: 0.0.0.0:4318  
      
    processors:  
      batch:  
      
    exporters:  
      otlphttp/langsmith:  
        endpoint: https://api.smith.langchain.com/otel/v1/traces  
        headers:  
          x-api-key: ${env:LANGSMITH_API_KEY}  
          Langsmith-Project: my_project  
      
      otlphttp/other_provider:  
        endpoint: https://otel.your-provider.com/v1/traces  
        headers:  
          api-key: ${env:OTHER_PROVIDER_API_KEY}  
      
    service:  
      pipelines:  
        traces:  
          receivers: [otlp]  
          processors: [batch]  
          exporters: [otlphttp/langsmith, otlphttp/other_provider]  
    

  3. **Configure your application to send to the collector** :

    
    
    import os  
    from opentelemetry import trace  
    from opentelemetry.sdk.trace import TracerProvider  
    from opentelemetry.sdk.trace.export import BatchSpanProcessor  
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter  
    from langchain_openai import ChatOpenAI  
    from langchain_core.prompts import ChatPromptTemplate  
      
    # Point to your local OpenTelemetry Collector  
    otlp_exporter = OTLPSpanExporter(  
        endpoint="http://localhost:4318/v1/traces"  
    )  
      
    provider = TracerProvider()  
    processor = BatchSpanProcessor(otlp_exporter)  
    provider.add_span_processor(processor)  
    trace.set_tracer_provider(provider)  
      
    # Set environment variables for LangChain  
    os.environ["LANGSMITH_OTEL_ENABLED"] = "true"  
    os.environ["LANGSMITH_TRACING"] = "true"  
      
    # Create and run a LangChain application  
    prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")  
    model = ChatOpenAI()  
    chain = prompt | model  
      
    result = chain.invoke({"topic": "programming"})  
    print(result.content)  
    

This approach offers several advantages:

  * Centralized configuration for all your telemetry destinations
  * Reduced overhead in your application code
  * Better scalability and resilience
  * Ability to add or remove destinations without changing application code

## Distributed Tracing with LangChain and OpenTelemetry​

Distributed tracing is essential when your LLM application spans multiple services or processes. OpenTelemetry's context propagation capabilities ensure that traces remain connected across service boundaries.

### Context Propagation in Distributed Tracing​

In distributed systems, context propagation passes trace metadata between services so that related spans are linked to the same trace:

  * **Trace ID** : A unique identifier for the entire trace
  * **Span ID** : A unique identifier for the current span
  * **Sampling Decision** : Indicates whether this trace should be sampled

### Setting up Distributed Tracing with LangChain​

To enable distributed tracing across multiple services:
    
    
    import os  
    from opentelemetry import trace  
    from opentelemetry.propagate import inject, extract  
    from opentelemetry.sdk.trace import TracerProvider  
    from opentelemetry.sdk.trace.export import BatchSpanProcessor  
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter  
    import requests  
    from langchain_openai import ChatOpenAI  
    from langchain_core.prompts import ChatPromptTemplate  
      
    # Set up OpenTelemetry trace provider  
    provider = TracerProvider()  
    otlp_exporter = OTLPSpanExporter(  
        endpoint="https://api.smith.langchain.com/otel/v1/traces",  
        headers={"x-api-key": os.getenv("LANGSMITH_API_KEY"), "Langsmith-Project": "my_project"}  
    )  
    processor = BatchSpanProcessor(otlp_exporter)  
    provider.add_span_processor(processor)  
    trace.set_tracer_provider(provider)  
    tracer = trace.get_tracer(__name__)  
      
    # Service A: Create a span and propagate context to Service B  
    def service_a():  
        with tracer.start_as_current_span("service_a_operation") as span:  
            # Create a chain  
            prompt = ChatPromptTemplate.from_template("Summarize: {text}")  
            model = ChatOpenAI()  
            chain = prompt | model  
      
            # Run the chain  
            result = chain.invoke({"text": "OpenTelemetry is an observability framework"})  
      
            # Propagate context to Service B  
            headers = {}  
            inject(headers)  # Inject trace context into headers  
      
            # Call Service B with the trace context  
            response = requests.post(  
                "http://service-b.example.com/process",  
                headers=headers,  
                json={"summary": result.content}  
            )  
            return response.json()  
      
    # Service B: Extract the context and continue the trace  
    from flask import Flask, request, jsonify  
      
    app = Flask(__name__)  
      
    @app.route("/process", methods=["POST"])  
    def service_b_endpoint():  
        # Extract the trace context from the request headers  
        context = extract(request.headers)  
      
        with tracer.start_as_current_span("service_b_operation", context=context) as span:  
            data = request.json  
            summary = data.get("summary", "")  
      
            # Process the summary with another LLM chain  
            prompt = ChatPromptTemplate.from_template("Analyze the sentiment of: {text}")  
            model = ChatOpenAI()  
            chain = prompt | model  
      
            result = chain.invoke({"text": summary})  
      
            return jsonify({"analysis": result.content})  
      
    if __name__ == "__main__":  
        app.run(port=5000)  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Sending Traces to LangSmith through OTel
    * 1\. Installation
    * 2\. Enable the OpenTelemetry integration
    * 3\. Create a LangChain application with tracing
    * 4\. View the traces in LangSmith
  * Sending Traces to Alternate Providers
    * Using Environment Variables or Global Configuration
    * Configuring Alternate OTLP Endpoints
    * Using OpenTelemetry Collector for Fan-out
  * Distributed Tracing with LangChain and OpenTelemetry
    * Context Propagation in Distributed Tracing
    * Setting up Distributed Tracing with LangChain

  *[/]: Positional-only parameter separator (PEP 570)