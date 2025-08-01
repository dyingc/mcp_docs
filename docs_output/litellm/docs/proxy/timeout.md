# Timeouts | liteLLM

On this page

The timeout set in router is for the entire length of the call, and is passed down to the completion() call level as well.

### Global Timeouts​

  * SDK
  * PROXY

    
    
    from litellm import Router   
      
    model_list = [{...}]  
      
    router = Router(model_list=model_list,   
                    timeout=30) # raise timeout error if call takes > 30s   
      
    print(response)  
    
    
    
    router_settings:  
        timeout: 30 # sets a 30s timeout for the entire call  
    

**Start Proxy**
    
    
     $ litellm --config /path/to/config.yaml  
    

### Custom Timeouts, Stream Timeouts - Per Model​

For each model you can set `timeout` & `stream_timeout` under `litellm_params`

  * SDK
  * PROXY

    
    
    from litellm import Router   
    import asyncio  
      
    model_list = [{  
        "model_name": "gpt-3.5-turbo",  
        "litellm_params": {  
            "model": "azure/chatgpt-v-2",  
            "api_key": os.getenv("AZURE_API_KEY"),  
            "api_version": os.getenv("AZURE_API_VERSION"),  
            "api_base": os.getenv("AZURE_API_BASE"),  
            "timeout": 300 # sets a 5 minute timeout  
            "stream_timeout": 30 # sets a 30s timeout for streaming calls  
        }  
    }]  
      
    # init router  
    router = Router(model_list=model_list, routing_strategy="least-busy")  
    async def router_acompletion():  
        response = await router.acompletion(  
            model="gpt-3.5-turbo",   
            messages=[{"role": "user", "content": "Hey, how's it going?"}]  
        )  
        print(response)  
        return response  
      
    asyncio.run(router_acompletion())  
    
    
    
    model_list:  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: azure/gpt-turbo-small-eu  
          api_base: https://my-endpoint-europe-berri-992.openai.azure.com/  
          api_key: <your-key>  
          timeout: 0.1                      # timeout in (seconds)  
          stream_timeout: 0.01              # timeout for stream requests (seconds)  
          max_retries: 5  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: azure/gpt-turbo-small-ca  
          api_base: https://my-endpoint-canada-berri992.openai.azure.com/  
          api_key:   
          timeout: 0.1                      # timeout in (seconds)  
          stream_timeout: 0.01              # timeout for stream requests (seconds)  
          max_retries: 5  
      
    

**Start Proxy**
    
    
     $ litellm --config /path/to/config.yaml  
    

### Setting Dynamic Timeouts - Per Request​

LiteLLM supports setting a `timeout` per request

**Example Usage**

  * SDK
  * PROXY

    
    
    from litellm import Router   
      
    model_list = [{...}]  
    router = Router(model_list=model_list)  
      
    response = router.completion(  
        model="gpt-3.5-turbo",   
        messages=[{"role": "user", "content": "what color is red"}],  
        timeout=1  
    )  
    

  * Curl Request
  * OpenAI v1.0.0+

    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
         --header 'Content-Type: application/json' \  
         --data-raw '{  
            "model": "gpt-3.5-turbo",  
            "messages": [  
                {"role": "user", "content": "what color is red"}  
            ],  
            "logit_bias": {12481: 100},  
            "timeout": 1  
         }'  
    
    
    
    import openai  
      
      
    client = openai.OpenAI(  
        api_key="anything",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    response = client.chat.completions.create(  
        model="gpt-3.5-turbo",  
        messages=[  
            {"role": "user", "content": "what color is red"}  
        ],  
        logit_bias={12481: 100},  
        extra_body={"timeout": 1} # 👈 KEY CHANGE  
    )  
      
    print(response)  
    

## Testing timeout handling​

To test if your retry/fallback logic can handle timeouts, you can set `mock_timeout=True` for testing.

This is currently only supported on `/chat/completions` and `/completions` endpoints. Please [let us know](https://github.com/BerriAI/litellm/issues) if you need this for other endpoints.
    
    
    curl -L -X POST 'http://0.0.0.0:4000/v1/chat/completions' \  
        -H 'Content-Type: application/json' \  
        -H 'Authorization: Bearer sk-1234' \  
        --data-raw '{  
            "model": "gemini/gemini-1.5-flash",  
            "messages": [  
            {"role": "user", "content": "hi my email is ishaan@berri.ai"}  
            ],  
            "mock_timeout": true # 👈 KEY CHANGE  
        }'  
    

  * Global Timeouts
  * Custom Timeouts, Stream Timeouts - Per Model
  * Setting Dynamic Timeouts - Per Request
  * Testing timeout handling