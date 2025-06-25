# Create Pass Through Endpoints | liteLLM

On this page

Route requests from your LiteLLM proxy to any external API. Perfect for custom models, image generation APIs, or any service you want to proxy through LiteLLM.

**Key Benefits:**

  * Onboard third-party endpoints like Bria API and Mistral OCR
  * Set custom pricing per request
  * Proxy Admins don't need to give developers api keys to upstream llm providers like Bria, Mistral OCR, etc.
  * Maintain centralized authentication, spend tracking, budgeting

## Quick Start with UI (Recommended)​

The easiest way to create pass through endpoints is through the LiteLLM UI. In this example, we'll onboard the [Bria API](https://docs.bria.ai/image-generation/endpoints/text-to-image-base) and set a cost per request.

### Step 1: Create Route Mappings​

To create a pass through endpoint:

  1. Navigate to the LiteLLM Proxy UI
  2. Go to the `Models + Endpoints` tab
  3. Click on `Pass Through Endpoints`
  4. Click "Add Pass Through Endpoint"
  5. Enter the following details:

**Required Fields:**

  * `Path Prefix`: The route clients will use when calling LiteLLM Proxy (e.g., `/bria`, `/mistral-ocr`)
  * `Target URL`: The URL where requests will be forwarded

**Route Mapping Example:**

The above configuration creates these route mappings:

LiteLLM Proxy Route| Target URL  
---|---  
`/bria`| `https://engine.prod.bria-api.com`  
`/bria/v1/text-to-image/base/model`| `https://engine.prod.bria-api.com/v1/text-to-image/base/model`  
`/bria/v1/enhance_image`| `https://engine.prod.bria-api.com/v1/enhance_image`  
`/bria/<any-sub-path>`| `https://engine.prod.bria-api.com/<any-sub-path>`  
  
info

All routes are prefixed with your LiteLLM proxy base URL: `https://<litellm-proxy-base-url>`

### Step 2: Configure Headers and Pricing​

Configure the required authentication and pricing:

**Authentication Setup:**

  * The Bria API requires an `api_token` header
  * Enter your Bria API key as the value for the `api_token` header

**Pricing Configuration:**

  * Set a cost per request (e.g., $12.00 in this example)
  * This enables cost tracking and billing for your users

### Step 3: Save Your Endpoint​

Once you've completed the configuration:

  1. Review your settings
  2. Click "Add Pass Through Endpoint"
  3. Your endpoint will be created and immediately available

### Step 4: Test Your Endpoint​

Verify your setup by making a test request to the Bria API through your LiteLLM Proxy:
    
    
    curl -i -X POST \  
      'http://localhost:4000/bria/v1/text-to-image/base/2.3' \  
      -H 'Content-Type: application/json' \  
      -H 'Authorization: Bearer <your-litellm-api-key>' \  
      -d '{  
        "prompt": "a book",  
        "num_results": 2,  
        "sync": true  
      }'  
    

**Expected Response:** If everything is configured correctly, you should receive a response from the Bria API containing the generated image data.

* * *

## Config.yaml Setup​

You can also create pass through endpoints using the `config.yaml` file. Here's how to add a `/v1/rerank` route that forwards to Cohere's API:

### Example Configuration​
    
    
    general_settings:  
      master_key: sk-1234  
      pass_through_endpoints:  
        - path: "/v1/rerank"                                  # Route on LiteLLM Proxy  
          target: "https://api.cohere.com/v1/rerank"          # Target endpoint  
          headers:                                            # Headers to forward  
            Authorization: "bearer os.environ/COHERE_API_KEY"  
            content-type: application/json  
            accept: application/json  
          forward_headers: true                               # Forward all incoming headers  
    

### Start and Test​

  1. **Start the proxy:**
         
         litellm --config config.yaml --detailed_debug  
         

  2. **Make a test request:**
         
         curl --request POST \  
           --url http://localhost:4000/v1/rerank \  
           --header 'accept: application/json' \  
           --header 'content-type: application/json' \  
           --data '{  
             "model": "rerank-english-v3.0",  
             "query": "What is the capital of the United States?",  
             "top_n": 3,  
             "documents": ["Carson City is the capital city of the American state of Nevada."]  
           }'  
         

### Expected Response​
    
    
    {  
      "id": "37103a5b-8cfb-48d3-87c7-da288bedd429",  
      "results": [  
        {  
          "index": 2,  
          "relevance_score": 0.999071  
        }  
      ],  
      "meta": {  
        "api_version": {"version": "1"},  
        "billed_units": {"search_units": 1}  
      }  
    }  
    

* * *

## ✨ Enterprise Features​

### Authentication & Rate Limiting​

Enable LiteLLM authentication and rate limiting on pass through endpoints:
    
    
    general_settings:  
      master_key: sk-1234  
      pass_through_endpoints:  
        - path: "/v1/rerank"  
          target: "https://api.cohere.com/v1/rerank"  
          auth: true                                          # Enable LiteLLM auth  
          headers:  
            Authorization: "bearer os.environ/COHERE_API_KEY"  
            content-type: application/json  
    

**Test with LiteLLM key:**
    
    
    curl --request POST \  
      --url http://localhost:4000/v1/rerank \  
      --header 'Authorization: Bearer sk-1234' \  
      --header 'content-type: application/json' \  
      --data '{"model": "rerank-english-v3.0", "query": "test"}'  
    

* * *

## Configuration Reference​

### Complete Specification​
    
    
    general_settings:  
      pass_through_endpoints:  
        - path: string                    # Route on LiteLLM Proxy Server  
          target: string                  # Target URL for forwarding  
          auth: boolean                   # Enable LiteLLM authentication (Enterprise)  
          forward_headers: boolean        # Forward all incoming headers  
          headers:                        # Custom headers to add  
            Authorization: string         # Auth header for target API  
            content-type: string         # Request content type  
            accept: string               # Expected response format  
            LANGFUSE_PUBLIC_KEY: string  # For Langfuse endpoints  
            LANGFUSE_SECRET_KEY: string  # For Langfuse endpoints  
            <custom-header>: string      # Any custom header  
    

### Header Options​

  * **Authorization** : Authentication for the target API
  * **content-type** : Request body format specification
  * **accept** : Expected response format
  * **LANGFUSE_PUBLIC_KEY/SECRET_KEY** : For Langfuse integration
  * **Custom headers** : Any additional key-value pairs

* * *

## Advanced: Custom Adapters​

For complex integrations (like Anthropic/Bedrock clients), you can create custom adapters that translate between different API schemas.

### 1\. Create an Adapter​
    
    
    from litellm import adapter_completion  
    from litellm.integrations.custom_logger import CustomLogger  
    from litellm.types.llms.anthropic import AnthropicMessagesRequest, AnthropicResponse  
      
    class AnthropicAdapter(CustomLogger):  
        def translate_completion_input_params(self, kwargs):  
            """Translate Anthropic format to OpenAI format"""  
            request_body = AnthropicMessagesRequest(**kwargs)  
            return litellm.AnthropicConfig().translate_anthropic_to_openai(  
                anthropic_message_request=request_body  
            )  
      
        def translate_completion_output_params(self, response):  
            """Translate OpenAI response back to Anthropic format"""  
            return litellm.AnthropicConfig().translate_openai_response_to_anthropic(  
                response=response  
            )  
      
    anthropic_adapter = AnthropicAdapter()  
    

### 2\. Configure the Endpoint​
    
    
    model_list:  
      - model_name: my-claude-endpoint  
        litellm_params:  
          model: gpt-3.5-turbo  
          api_key: os.environ/OPENAI_API_KEY  
      
    general_settings:  
      master_key: sk-1234  
      pass_through_endpoints:  
        - path: "/v1/messages"  
          target: custom_callbacks.anthropic_adapter  
          headers:  
            litellm_user_api_key: "x-api-key"  
    

### 3\. Test Custom Endpoint​
    
    
    curl --location 'http://0.0.0.0:4000/v1/messages' \  
      -H 'x-api-key: sk-1234' \  
      -H 'anthropic-version: 2023-06-01' \  
      -H 'content-type: application/json' \  
      -d '{  
        "model": "my-claude-endpoint",  
        "max_tokens": 1024,  
        "messages": [{"role": "user", "content": "Hello, world"}]  
      }'  
    

* * *

## Troubleshooting​

### Common Issues​

**Authentication Errors:**

  * Verify API keys are correctly set in headers
  * Ensure the target API accepts the provided authentication method

**Routing Issues:**

  * Confirm the path prefix matches your request URL
  * Verify the target URL is accessible
  * Check for trailing slashes in configuration

**Response Errors:**

  * Enable detailed debugging with `--detailed_debug`
  * Check LiteLLM proxy logs for error details
  * Verify the target API's expected request format

### Getting Help​

[Schedule Demo 👋](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version)

[Community Discord 💭](https://discord.gg/wuPM9dRgDw)

Our numbers 📞 +1 (770) 8783-106 / ‭+1 (412) 618-6238‬

Our emails ✉️ [ishaan@berri.ai](mailto:ishaan@berri.ai) / [krrish@berri.ai](mailto:krrish@berri.ai)

  * Quick Start with UI (Recommended)
    * Step 1: Create Route Mappings
    * Step 2: Configure Headers and Pricing
    * Step 3: Save Your Endpoint
    * Step 4: Test Your Endpoint
  * Config.yaml Setup
    * Example Configuration
    * Start and Test
    * Expected Response
  * ✨ Enterprise Features
    * Authentication & Rate Limiting
  * Configuration Reference
    * Complete Specification
    * Header Options
  * Advanced: Custom Adapters
    * 1\. Create an Adapter
    * 2\. Configure the Endpoint
    * 3\. Test Custom Endpoint
  * Troubleshooting
    * Common Issues
    * Getting Help