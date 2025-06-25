# Bedrock (boto3) SDK | liteLLM

On this page

Pass-through endpoints for Bedrock - call provider-specific endpoint, in native format (no translation).

Feature| Supported| Notes  
---|---|---  
Cost Tracking| ❌| [Tell us if you need this](https://github.com/BerriAI/litellm/issues/new)  
Logging| ✅| works across all integrations  
End-user Tracking| ❌| [Tell us if you need this](https://github.com/BerriAI/litellm/issues/new)  
Streaming| ✅|   
  
Just replace `https://bedrock-runtime.{aws_region_name}.amazonaws.com` with `LITELLM_PROXY_BASE_URL/bedrock` 🚀

#### **Example Usage**​
    
    
    curl -X POST 'http://0.0.0.0:4000/bedrock/model/cohere.command-r-v1:0/converse' \  
    -H 'Authorization: Bearer anything' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "messages": [  
             {"role": "user",  
            "content": [{"text": "Hello"}]  
        }  
        ]  
    }'  
    

Supports **ALL** Bedrock Endpoints (including streaming).

[**See All Bedrock Endpoints**](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html)

## Quick Start​

Let's call the Bedrock [`/converse` endpoint](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html)

  1. Add AWS Keyss to your environment

    
    
    export AWS_ACCESS_KEY_ID=""  # Access key  
    export AWS_SECRET_ACCESS_KEY="" # Secret access key  
    export AWS_REGION_NAME="" # us-east-1, us-east-2, us-west-1, us-west-2  
    

  2. Start LiteLLM Proxy

    
    
    litellm  
      
    # RUNNING on http://0.0.0.0:4000  
    

  3. Test it!

Let's call the Bedrock converse endpoint
    
    
    curl -X POST 'http://0.0.0.0:4000/bedrock/model/cohere.command-r-v1:0/converse' \  
    -H 'Authorization: Bearer anything' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "messages": [  
             {"role": "user",  
            "content": [{"text": "Hello"}]  
        }  
        ]  
    }'  
    

## Examples​

Anything after `http://0.0.0.0:4000/bedrock` is treated as a provider-specific route, and handled accordingly.

Key Changes:

**Original Endpoint**| **Replace With**  
---|---  
`https://bedrock-runtime.{aws_region_name}.amazonaws.com`| `http://0.0.0.0:4000/bedrock` (LITELLM_PROXY_BASE_URL="<http://0.0.0.0:4000>")  
`AWS4-HMAC-SHA256..`| `Bearer anything` (use `Bearer LITELLM_VIRTUAL_KEY` if Virtual Keys are setup on proxy)  
  
### **Example 1: Converse API**​

#### LiteLLM Proxy Call​
    
    
    curl -X POST 'http://0.0.0.0:4000/bedrock/model/cohere.command-r-v1:0/converse' \  
    -H 'Authorization: Bearer sk-anything' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "messages": [  
             {"role": "user",  
            "content": [{"text": "Hello"}]  
        }  
        ]  
    }'  
    

#### Direct Bedrock API Call​
    
    
    curl -X POST 'https://bedrock-runtime.us-west-2.amazonaws.com/model/cohere.command-r-v1:0/converse' \  
    -H 'Authorization: AWS4-HMAC-SHA256..' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "messages": [  
             {"role": "user",  
            "content": [{"text": "Hello"}]  
        }  
        ]  
    }'  
    

### **Example 2: Apply Guardrail**​

#### LiteLLM Proxy Call​
    
    
    curl "http://0.0.0.0:4000/bedrock/guardrail/guardrailIdentifier/version/guardrailVersion/apply" \  
        -H 'Authorization: Bearer sk-anything' \  
        -H 'Content-Type: application/json' \  
        -X POST \  
        -d '{  
          "contents": [{"text": {"text": "Hello world"}}],  
          "source": "INPUT"  
           }'  
    

#### Direct Bedrock API Call​
    
    
    curl "https://bedrock-runtime.us-west-2.amazonaws.com/guardrail/guardrailIdentifier/version/guardrailVersion/apply" \  
        -H 'Authorization: AWS4-HMAC-SHA256..' \  
        -H 'Content-Type: application/json' \  
        -X POST \  
        -d '{  
          "contents": [{"text": {"text": "Hello world"}}],  
          "source": "INPUT"  
           }'  
    

### **Example 3: Query Knowledge Base**​
    
    
    curl -X POST "http://0.0.0.0:4000/bedrock/knowledgebases/{knowledgeBaseId}/retrieve" \  
    -H 'Authorization: Bearer sk-anything' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "nextToken": "string",  
        "retrievalConfiguration": {   
            "vectorSearchConfiguration": {   
              "filter": { ... },  
              "numberOfResults": number,  
              "overrideSearchType": "string"  
            }  
        },  
        "retrievalQuery": {   
            "text": "string"  
        }  
    }'  
    

#### Direct Bedrock API Call​
    
    
    curl -X POST "https://bedrock-agent-runtime.us-west-2.amazonaws.com/knowledgebases/{knowledgeBaseId}/retrieve" \  
    -H 'Authorization: AWS4-HMAC-SHA256..' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "nextToken": "string",  
        "retrievalConfiguration": {   
            "vectorSearchConfiguration": {   
              "filter": { ... },  
              "numberOfResults": number,  
              "overrideSearchType": "string"  
            }  
        },  
        "retrievalQuery": {   
            "text": "string"  
        }  
    }'  
    

## Advanced - Use with Virtual Keys​

Pre-requisites

  * [Setup proxy with DB](/docs/proxy/virtual_keys#setup)

Use this, to avoid giving developers the raw AWS Keys, but still letting them use AWS Bedrock endpoints.

### Usage​

  1. Setup environment

    
    
    export DATABASE_URL=""  
    export LITELLM_MASTER_KEY=""  
    export AWS_ACCESS_KEY_ID=""  # Access key  
    export AWS_SECRET_ACCESS_KEY="" # Secret access key  
    export AWS_REGION_NAME="" # us-east-1, us-east-2, us-west-1, us-west-2  
    
    
    
    litellm  
      
    # RUNNING on http://0.0.0.0:4000  
    

  2. Generate virtual key

    
    
    curl -X POST 'http://0.0.0.0:4000/key/generate' \  
    -H 'Authorization: Bearer sk-1234' \  
    -H 'Content-Type: application/json' \  
    -d '{}'  
    

Expected Response
    
    
    {  
        ...  
        "key": "sk-1234ewknldferwedojwojw"  
    }  
    

  3. Test it!

    
    
    curl -X POST 'http://0.0.0.0:4000/bedrock/model/cohere.command-r-v1:0/converse' \  
    -H 'Authorization: Bearer sk-1234ewknldferwedojwojw' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "messages": [  
             {"role": "user",  
            "content": [{"text": "Hello"}]  
        }  
        ]  
    }'  
    

## Advanced - Bedrock Agents​

Call Bedrock Agents via LiteLLM proxy
    
    
    import os   
    import boto3   
    from botocore.config import Config  
      
    # # Define your proxy endpoint  
    proxy_endpoint = "http://0.0.0.0:4000/bedrock" # 👈 your proxy base url  
      
    # # Create a Config object with the proxy  
    # Custom headers  
    custom_headers = {  
        'litellm_user_api_key': 'Bearer sk-1234', # 👈 your proxy api key  
    }  
      
      
    os.environ["AWS_ACCESS_KEY_ID"] = "my-fake-key-id"  
    os.environ["AWS_SECRET_ACCESS_KEY"] = "my-fake-access-key"  
      
      
    # Create the client  
    runtime_client = boto3.client(  
        service_name="bedrock-agent-runtime",   
        region_name="us-west-2",   
        endpoint_url=proxy_endpoint  
    )  
      
    # Custom header injection  
    def inject_custom_headers(request, **kwargs):  
        request.headers.update(custom_headers)  
      
    # Attach the event to inject custom headers before the request is sent  
    runtime_client.meta.events.register('before-send.*.*', inject_custom_headers)  
      
      
    response = runtime_client.invoke_agent(  
                agentId="L1RT58GYRW",  
                agentAliasId="MFPSBCXYTW",  
                sessionId="12345",  
                inputText="Who do you know?"  
            )  
      
    completion = ""  
      
    for event in response.get("completion"):  
        chunk = event["chunk"]  
        completion += chunk["bytes"].decode()  
      
    print(completion)  
      
    

  * Quick Start
  * Examples
    * **Example 1: Converse API**
    * **Example 2: Apply Guardrail**
    * **Example 3: Query Knowledge Base**
  * Advanced - Use with Virtual Keys
    * Usage
  * Advanced - Bedrock Agents