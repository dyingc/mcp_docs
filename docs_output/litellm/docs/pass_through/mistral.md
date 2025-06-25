# Mistral | liteLLM

On this page

Pass-through endpoints for Mistral - call provider-specific endpoint, in native format (no translation).

Feature| Supported| Notes  
---|---|---  
Cost Tracking| ❌| Not supported  
Logging| ✅| works across all integrations  
End-user Tracking| ❌| [Tell us if you need this](https://github.com/BerriAI/litellm/issues/new)  
Streaming| ✅|   
  
Just replace `https://api.mistral.ai/v1` with `LITELLM_PROXY_BASE_URL/mistral` 🚀

#### **Example Usage**​
    
    
    curl -L -X POST 'http://0.0.0.0:4000/mistral/v1/ocr' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
        "model": "mistral-ocr-latest",  
        "document": {  
            "type": "image_url",  
            "image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png"  
        }  
      
    }'  
    

Supports **ALL** Mistral Endpoints (including streaming).

## Quick Start​

Let's call the Mistral [`/chat/completions` endpoint](https://docs.mistral.ai/api/#tag/chat/operation/chat_completion_v1_chat_completions_post)

  1. Add MISTRAL_API_KEY to your environment

    
    
    export MISTRAL_API_KEY="sk-1234"  
    

  2. Start LiteLLM Proxy

    
    
    litellm  
      
    # RUNNING on http://0.0.0.0:4000  
    

  3. Test it!

Let's call the Mistral `/ocr` endpoint
    
    
    curl -L -X POST 'http://0.0.0.0:4000/mistral/v1/ocr' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
        "model": "mistral-ocr-latest",  
        "document": {  
            "type": "image_url",  
            "image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png"  
        }  
      
    }'  
    

## Examples​

Anything after `http://0.0.0.0:4000/mistral` is treated as a provider-specific route, and handled accordingly.

Key Changes:

**Original Endpoint**| **Replace With**  
---|---  
`https://api.mistral.ai/v1`| `http://0.0.0.0:4000/mistral` (LITELLM_PROXY_BASE_URL="<http://0.0.0.0:4000>")  
`bearer $MISTRAL_API_KEY`| `bearer anything` (use `bearer LITELLM_VIRTUAL_KEY` if Virtual Keys are setup on proxy)  
  
### **Example 1: OCR endpoint**​

#### LiteLLM Proxy Call​
    
    
    curl -L -X POST 'http://0.0.0.0:4000/mistral/v1/ocr' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer $LITELLM_API_KEY' \  
    -d '{  
        "model": "mistral-ocr-latest",  
        "document": {  
            "type": "image_url",  
            "image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png"  
        }  
    }'  
    

#### Direct Mistral API Call​
    
    
    curl https://api.mistral.ai/v1/ocr \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer ${MISTRAL_API_KEY}" \  
      -d '{  
        "model": "mistral-ocr-latest",  
        "document": {  
            "type": "document_url",  
            "document_url": "https://arxiv.org/pdf/2201.04234"  
        },  
        "include_image_base64": true  
      }'  
    

### **Example 2: Chat API**​

#### LiteLLM Proxy Call​
    
    
    curl -L -X POST 'http://0.0.0.0:4000/mistral/v1/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer $LITELLM_VIRTUAL_KEY' \  
    -d '{  
        "messages": [  
            {  
                "role": "user",  
                "content": "I am going to Paris, what should I see?"  
            }  
        ],  
        "max_tokens": 2048,  
        "temperature": 0.8,  
        "top_p": 0.1,  
        "model": "mistral-large-latest",  
    }'  
    

#### Direct Mistral API Call​
    
    
    curl -L -X POST 'https://api.mistral.ai/v1/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "messages": [  
            {  
                "role": "user",  
                "content": "I am going to Paris, what should I see?"  
            }  
        ],  
        "max_tokens": 2048,  
        "temperature": 0.8,  
        "top_p": 0.1,  
        "model": "mistral-large-latest",  
    }'  
    

## Advanced - Use with Virtual Keys​

Pre-requisites

  * [Setup proxy with DB](/docs/proxy/virtual_keys#setup)

Use this, to avoid giving developers the raw Mistral API key, but still letting them use Mistral endpoints.

### Usage​

  1. Setup environment

    
    
    export DATABASE_URL=""  
    export LITELLM_MASTER_KEY=""  
    export MISTRAL_API_BASE=""  
    
    
    
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

    
    
    curl -L -X POST 'http://0.0.0.0:4000/mistral/v1/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234ewknldferwedojwojw' \  
      --data '{  
        "messages": [  
            {  
                "role": "user",  
                "content": "I am going to Paris, what should I see?"  
            }  
        ],  
        "max_tokens": 2048,  
        "temperature": 0.8,  
        "top_p": 0.1,  
        "model": "qwen2.5-7b-instruct",  
    }'  
    

  * Quick Start
  * Examples
    * **Example 1: OCR endpoint**
    * **Example 2: Chat API**
  * Advanced - Use with Virtual Keys
    * Usage