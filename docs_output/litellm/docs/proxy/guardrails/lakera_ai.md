# Lakera AI | liteLLM

On this page

## Quick Start​

### 1\. Define Guardrails on your LiteLLM config.yaml​

Define your guardrails under the `guardrails` section

litellm config.yaml
    
    
    model_list:  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: openai/gpt-3.5-turbo  
          api_key: os.environ/OPENAI_API_KEY  
      
    guardrails:  
      - guardrail_name: "lakera-guard"  
        litellm_params:  
          guardrail: lakera_v2  # supported values: "aporia", "bedrock", "lakera"  
          mode: "during_call"  
          api_key: os.environ/LAKERA_API_KEY  
          api_base: os.environ/LAKERA_API_BASE  
      - guardrail_name: "lakera-pre-guard"  
        litellm_params:  
          guardrail: lakera_v2  # supported values: "aporia", "bedrock", "lakera"  
          mode: "pre_call"  
          api_key: os.environ/LAKERA_API_KEY  
          api_base: os.environ/LAKERA_API_BASE  
        
    

#### Supported values for `mode`​

  * `pre_call` Run **before** LLM call, on **input**
  * `post_call` Run **after** LLM call, on **input & output**
  * `during_call` Run **during** LLM call, on **input** Same as `pre_call` but runs in parallel as LLM call. Response not returned until guardrail check completes

### 2\. Start LiteLLM Gateway​
    
    
    litellm --config config.yaml --detailed_debug  
    

### 3\. Test request​

**[Langchain, OpenAI SDK Usage Examples](/docs/proxy/proxy/user_keys#request-format)**

  * Unsuccessful call
  * Successful Call 

Expect this to fail since since `ishaan@berri.ai` in the request is PII

Curl Request
    
    
    curl -i http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-npnwjPQciVRok5yNZgKmFQ" \  
      -d '{  
        "model": "gpt-3.5-turbo",  
        "messages": [  
          {"role": "user", "content": "hi my email is ishaan@berri.ai"}  
        ],  
        "guardrails": ["lakera-guard"]  
      }'  
    

Expected response on failure
    
    
    {  
     "error": {  
       "message": {  
         "error": "Violated content safety policy",  
         "lakera_ai_response": {  
           "model": "lakera-guard-1",  
           "results": [  
             {  
               "categories": {  
                 "prompt_injection": true,  
                 "jailbreak": false  
               },  
               "category_scores": {  
                 "prompt_injection": 0.999,  
                 "jailbreak": 0.0  
               },  
               "flagged": true,  
               "payload": {}  
             }  
           ],  
           "dev_info": {  
             "git_revision": "cb163444",  
             "git_timestamp": "2024-08-19T16:00:28+02:00",  
             "version": "1.3.53"  
           }  
         }  
       },  
       "type": "None",  
       "param": "None",  
       "code": "400"  
     }  
    }  
      
    

Curl Request
    
    
    curl -i http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-npnwjPQciVRok5yNZgKmFQ" \  
      -d '{  
        "model": "gpt-3.5-turbo",  
        "messages": [  
          {"role": "user", "content": "hi what is the weather"}  
        ],  
        "guardrails": ["lakera-guard"]  
      }'  
    

  * Quick Start
    * 1\. Define Guardrails on your LiteLLM config.yaml
    * 2\. Start LiteLLM Gateway
    * 3\. Test request