# Perplexity AI (pplx-api) | liteLLM

On this page

<https://www.perplexity.ai>

## API Key​
    
    
    # env variable  
    os.environ['PERPLEXITYAI_API_KEY']  
    

## Sample Usage​
    
    
    from litellm import completion  
    import os  
      
    os.environ['PERPLEXITYAI_API_KEY'] = ""  
    response = completion(  
        model="perplexity/sonar-pro",   
        messages=messages  
    )  
    print(response)  
    

## Sample Usage - Streaming​
    
    
    from litellm import completion  
    import os  
      
    os.environ['PERPLEXITYAI_API_KEY'] = ""  
    response = completion(  
        model="perplexity/sonar-pro",   
        messages=messages,  
        stream=True  
    )  
      
    for chunk in response:  
        print(chunk)  
    

## Reasoning Effort​

Requires v1.72.6+

info

See full guide on Reasoning with LiteLLM [here](/docs/reasoning_content)

You can set the reasoning effort by setting the `reasoning_effort` parameter.

  * SDK
  * Proxy

    
    
    from litellm import completion  
    import os  
      
    os.environ['PERPLEXITYAI_API_KEY'] = ""  
    response = completion(  
        model="perplexity/sonar-reasoning",   
        messages=messages,  
        reasoning_effort="high"  
    )  
    print(response)  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: perplexity-sonar-reasoning-model  
        litellm_params:  
            model: perplexity/sonar-reasoning  
            api_key: os.environ/PERPLEXITYAI_API_KEY  
    

  2. Start proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

Replace `anything` with your LiteLLM Proxy Virtual Key, if [setup](/docs/proxy/virtual_keys).
    
    
    curl http://0.0.0.0:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer anything" \  
      -d '{  
        "model": "perplexity-sonar-reasoning-model",  
        "messages": [{"role": "user", "content": "Who won the World Cup in 2022?"}],  
        "reasoning_effort": "high"  
      }'  
    

## Supported Models​

All models listed here <https://docs.perplexity.ai/docs/model-cards> are supported. Just do `model=perplexity/<model-name>`.

Model Name| Function Call  
---|---  
sonar-deep-research| `completion(model="perplexity/sonar-deep-research", messages)`  
sonar-reasoning-pro| `completion(model="perplexity/sonar-reasoning-pro", messages)`  
sonar-reasoning| `completion(model="perplexity/sonar-reasoning", messages)`  
sonar-pro| `completion(model="perplexity/sonar-pro", messages)`  
sonar| `completion(model="perplexity/sonar", messages)`  
r1-1776| `completion(model="perplexity/r1-1776", messages)`  
  
info

For more information about passing provider-specific parameters, [go here](/docs/completion/provider_specific_params)

  * API Key
  * Sample Usage
  * Sample Usage - Streaming
  * Reasoning Effort
  * Supported Models