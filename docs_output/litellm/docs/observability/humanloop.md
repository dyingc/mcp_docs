# Humanloop | liteLLM

On this page

[Humanloop](https://humanloop.com/docs/v5/getting-started/overview) enables product teams to build robust AI features with LLMs, using best-in-class tooling for Evaluation, Prompt Management, and Observability.

## Getting Started​

Use Humanloop to manage prompts across all LiteLLM Providers.

  * SDK
  * PROXY

    
    
    import os   
    import litellm  
      
    os.environ["HUMANLOOP_API_KEY"] = "" # [OPTIONAL] set here or in `.completion`  
      
    litellm.set_verbose = True # see raw request to provider  
      
    resp = litellm.completion(  
        model="humanloop/gpt-3.5-turbo",  
        prompt_id="test-chat-prompt",  
        prompt_variables={"user_message": "this is used"}, # [OPTIONAL]  
        messages=[{"role": "user", "content": "<IGNORED>"}],  
        # humanloop_api_key="..." ## alternative to setting env var  
    )  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: humanloop/gpt-3.5-turbo  
          prompt_id: "<humanloop_prompt_id>"  
          api_key: os.environ/OPENAI_API_KEY  
    

  2. Start the proxy

    
    
    litellm --config config.yaml --detailed_debug  
    

  3. Test it!

  * CURL
  * OpenAI Python SDK

    
    
    curl -L -X POST 'http://0.0.0.0:4000/v1/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
        "model": "gpt-3.5-turbo",  
        "messages": [  
            {  
                "role": "user",  
                "content": "THIS WILL BE IGNORED"  
            }  
        ],  
        "prompt_variables": {  
            "key": "this is used"  
        }  
    }'  
    
    
    
    import openai  
    client = openai.OpenAI(  
        api_key="anything",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    # request sent to model set on litellm proxy, `litellm --model`  
    response = client.chat.completions.create(  
        model="gpt-3.5-turbo",  
        messages = [  
            {  
                "role": "user",  
                "content": "this is a test request, write a short poem"  
            }  
        ],  
        extra_body={  
            "prompt_variables": { # [OPTIONAL]  
                "key": "this is used"  
            }  
        }  
    )  
      
    print(response)  
    

**Expected Logs:**
    
    
    POST Request Sent from LiteLLM:  
    curl -X POST \  
    https://api.openai.com/v1/ \  
    -d '{'model': 'gpt-3.5-turbo', 'messages': <YOUR HUMANLOOP PROMPT TEMPLATE>}'  
    

## How to set model​

## How to set model​

### Set the model on LiteLLM​

You can do `humanloop/<litellm_model_name>`

  * SDK
  * PROXY

    
    
    litellm.completion(  
        model="humanloop/gpt-3.5-turbo", # or `humanloop/anthropic/claude-3-5-sonnet`  
        ...  
    )  
    
    
    
    model_list:  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: humanloop/gpt-3.5-turbo # OR humanloop/anthropic/claude-3-5-sonnet  
          prompt_id: <humanloop_prompt_id>  
          api_key: os.environ/OPENAI_API_KEY  
    

### Set the model on Humanloop​

LiteLLM will call humanloop's `https://api.humanloop.com/v5/prompts/<your-prompt-id>` endpoint, to get the prompt template.

This also returns the template model set on Humanloop.
    
    
    {  
      "template": [  
        {  
          ... # your prompt template  
        }  
      ],  
      "model": "gpt-3.5-turbo" # your template model  
    }  
    

  * Getting Started
  * How to set model
  * How to set model
    * Set the model on LiteLLM
    * Set the model on Humanloop