# Google AI Studio SDK | liteLLM

On this page

Pass-through endpoints for Google AI Studio - call provider-specific endpoint, in native format (no translation).

Feature| Supported| Notes  
---|---|---  
Cost Tracking| ✅| supports all models on `/generateContent` endpoint  
Logging| ✅| works across all integrations  
End-user Tracking| ❌| [Tell us if you need this](https://github.com/BerriAI/litellm/issues/new)  
Streaming| ✅|   
  
Just replace `https://generativelanguage.googleapis.com` with `LITELLM_PROXY_BASE_URL/gemini`

#### **Example Usage**​

  * curl
  * Google AI Node.js SDK

    
    
    curl 'http://0.0.0.0:4000/gemini/v1beta/models/gemini-1.5-flash:countTokens?key=sk-anything' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "contents": [{  
            "parts":[{  
              "text": "The quick brown fox jumps over the lazy dog."  
              }]  
            }]  
    }'  
    
    
    
    const { GoogleGenerativeAI } = require("@google/generative-ai");  
      
    const modelParams = {  
        model: 'gemini-pro',  
    };  
        
    const requestOptions = {  
        baseUrl: 'http://localhost:4000/gemini', // http://<proxy-base-url>/gemini  
    };  
        
    const genAI = new GoogleGenerativeAI("sk-1234"); // litellm proxy API key  
    const model = genAI.getGenerativeModel(modelParams, requestOptions);  
      
    async function main() {  
        try {  
            const result = await model.generateContent("Explain how AI works");  
            console.log(result.response.text());  
        } catch (error) {  
            console.error('Error:', error);  
        }  
    }  
      
    // For streaming responses  
    async function main_streaming() {  
        try {  
            const streamingResult = await model.generateContentStream("Explain how AI works");  
            for await (const chunk of streamingResult.stream) {  
                console.log('Stream chunk:', JSON.stringify(chunk));  
            }  
            const aggregatedResponse = await streamingResult.response;  
            console.log('Aggregated response:', JSON.stringify(aggregatedResponse));  
        } catch (error) {  
            console.error('Error:', error);  
        }  
    }  
      
    main();  
    // main_streaming();  
    

Supports **ALL** Google AI Studio Endpoints (including streaming).

[**See All Google AI Studio Endpoints**](https://ai.google.dev/api)

## Quick Start​

Let's call the Gemini [`/countTokens` endpoint](https://ai.google.dev/api/tokens#method:-models.counttokens)

  1. Add Gemini API Key to your environment

    
    
    export GEMINI_API_KEY=""  
    

  2. Start LiteLLM Proxy

    
    
    litellm  
      
    # RUNNING on http://0.0.0.0:4000  
    

  3. Test it!

Let's call the Google AI Studio token counting endpoint
    
    
    http://0.0.0.0:4000/gemini/v1beta/models/gemini-1.5-flash:countTokens?key=anything' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "contents": [{  
            "parts":[{  
              "text": "The quick brown fox jumps over the lazy dog."  
              }]  
            }]  
    }'  
    

## Examples​

Anything after `http://0.0.0.0:4000/gemini` is treated as a provider-specific route, and handled accordingly.

Key Changes:

**Original Endpoint**| **Replace With**  
---|---  
`https://generativelanguage.googleapis.com`| `http://0.0.0.0:4000/gemini` (LITELLM_PROXY_BASE_URL="<http://0.0.0.0:4000>")  
`key=$GOOGLE_API_KEY`| `key=anything` (use `key=LITELLM_VIRTUAL_KEY` if Virtual Keys are setup on proxy)  
  
### **Example 1: Counting tokens**​

#### LiteLLM Proxy Call​
    
    
    curl http://0.0.0.0:4000/gemini/v1beta/models/gemini-1.5-flash:countTokens?key=anything \  
        -H 'Content-Type: application/json' \  
        -X POST \  
        -d '{  
          "contents": [{  
            "parts":[{  
              "text": "The quick brown fox jumps over the lazy dog."  
              }],  
            }],  
          }'  
    

#### Direct Google AI Studio Call​
    
    
    curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:countTokens?key=$GOOGLE_API_KEY \  
        -H 'Content-Type: application/json' \  
        -X POST \  
        -d '{  
          "contents": [{  
            "parts":[{  
              "text": "The quick brown fox jumps over the lazy dog."  
              }],  
            }],  
          }'  
    

### **Example 2: Generate content**​

#### LiteLLM Proxy Call​
    
    
    curl "http://0.0.0.0:4000/gemini/v1beta/models/gemini-1.5-flash:generateContent?key=anything" \  
        -H 'Content-Type: application/json' \  
        -X POST \  
        -d '{  
          "contents": [{  
            "parts":[{"text": "Write a story about a magic backpack."}]  
            }]  
           }' 2> /dev/null  
    

#### Direct Google AI Studio Call​
    
    
    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$GOOGLE_API_KEY" \  
        -H 'Content-Type: application/json' \  
        -X POST \  
        -d '{  
          "contents": [{  
            "parts":[{"text": "Write a story about a magic backpack."}]  
            }]  
           }' 2> /dev/null  
    

### **Example 3: Caching**​
    
    
    curl -X POST "http://0.0.0.0:4000/gemini/v1beta/models/gemini-1.5-flash-001:generateContent?key=anything" \  
    -H 'Content-Type: application/json' \  
    -d '{  
          "contents": [  
            {  
              "parts":[{  
                "text": "Please summarize this transcript"  
              }],  
              "role": "user"  
            },  
          ],  
          "cachedContent": "'$CACHE_NAME'"  
        }'  
    

#### Direct Google AI Studio Call​
    
    
    curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-001:generateContent?key=$GOOGLE_API_KEY" \  
    -H 'Content-Type: application/json' \  
    -d '{  
          "contents": [  
            {  
              "parts":[{  
                "text": "Please summarize this transcript"  
              }],  
              "role": "user"  
            },  
          ],  
          "cachedContent": "'$CACHE_NAME'"  
        }'  
    

## Advanced​

Pre-requisites

  * [Setup proxy with DB](/docs/proxy/virtual_keys#setup)

Use this, to avoid giving developers the raw Google AI Studio key, but still letting them use Google AI Studio endpoints.

### Use with Virtual Keys​

  1. Setup environment

    
    
    export DATABASE_URL=""  
    export LITELLM_MASTER_KEY=""  
    export GEMINI_API_KEY=""  
    
    
    
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

    
    
    http://0.0.0.0:4000/gemini/v1beta/models/gemini-1.5-flash:countTokens?key=sk-1234ewknldferwedojwojw' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "contents": [{  
            "parts":[{  
              "text": "The quick brown fox jumps over the lazy dog."  
              }]  
            }]  
    }'  
    

### Send `tags` in request headers​

Use this if you want `tags` to be tracked in the LiteLLM DB and on logging callbacks.

Pass tags in request headers as a comma separated list. In the example below the following tags will be tracked
    
    
    tags: ["gemini-js-sdk", "pass-through-endpoint"]  
    

  * curl
  * Google AI Node.js SDK

    
    
    curl 'http://0.0.0.0:4000/gemini/v1beta/models/gemini-1.5-flash:generateContent?key=sk-anything' \  
    -H 'Content-Type: application/json' \  
    -H 'tags: gemini-js-sdk,pass-through-endpoint' \  
    -d '{  
        "contents": [{  
            "parts":[{  
              "text": "The quick brown fox jumps over the lazy dog."  
              }]  
            }]  
    }'  
    
    
    
    const { GoogleGenerativeAI } = require("@google/generative-ai");  
      
    const modelParams = {  
        model: 'gemini-pro',  
    };  
        
    const requestOptions = {  
        baseUrl: 'http://localhost:4000/gemini', // http://<proxy-base-url>/gemini  
        customHeaders: {  
            "tags": "gemini-js-sdk,pass-through-endpoint"  
        }  
    };  
        
    const genAI = new GoogleGenerativeAI("sk-1234");  
    const model = genAI.getGenerativeModel(modelParams, requestOptions);  
      
    async function main() {  
        try {  
            const result = await model.generateContent("Explain how AI works");  
            console.log(result.response.text());  
        } catch (error) {  
            console.error('Error:', error);  
        }  
    }  
      
    main();  
    

  * Quick Start
  * Examples
    * **Example 1: Counting tokens**
    * **Example 2: Generate content**
    * **Example 3: Caching**
  * Advanced
    * Use with Virtual Keys
    * Send `tags` in request headers