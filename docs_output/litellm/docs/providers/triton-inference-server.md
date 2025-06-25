# Triton Inference Server | liteLLM

On this page

LiteLLM supports Embedding Models on Triton Inference Servers

Property| Details  
---|---  
Description| NVIDIA Triton Inference Server  
Provider Route on LiteLLM| `triton/`  
Supported Operations| `/chat/completion`, `/completion`, `/embedding`  
Supported Triton endpoints| `/infer`, `/generate`, `/embeddings`  
Link to Provider Doc| [Triton Inference Server ↗](https://developer.nvidia.com/triton-inference-server)  
  
## Triton `/generate` \- Chat Completion​

  * SDK
  * PROXY

Use the `triton/` prefix to route to triton server
    
    
    from litellm import completion  
    response = completion(  
        model="triton/llama-3-8b-instruct",  
        messages=[{"role": "user", "content": "who are u?"}],  
        max_tokens=10,  
        api_base="http://localhost:8000/generate",  
    )  
    

  1. Add models to your config.yaml

    
    
    model_list:  
      - model_name: my-triton-model  
        litellm_params:  
          model: triton/<your-triton-model>"  
          api_base: https://your-triton-api-base/triton/generate  
    

  2. Start the proxy

    
    
    $ litellm --config /path/to/config.yaml --detailed_debug  
    

  3. Send Request to LiteLLM Proxy Server

  * OpenAI Python v1.0.0+
  * curl

    
    
    import openai  
    from openai import OpenAI  
      
    # set base_url to your proxy server  
    # set api_key to send to proxy server  
    client = OpenAI(api_key="<proxy-api-key>", base_url="http://0.0.0.0:4000")  
      
    response = client.chat.completions.create(  
        model="my-triton-model",  
        messages=[{"role": "user", "content": "who are u?"}],  
        max_tokens=10,  
    )  
      
    print(response)  
      
    

`--header` is optional, only required if you're using litellm proxy with Virtual Keys
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
    --header 'Content-Type: application/json' \  
    --header 'Authorization: Bearer sk-1234' \  
    --data ' {  
    "model": "my-triton-model",  
    "messages": [{"role": "user", "content": "who are u?"}]  
    }'  
      
    

## Triton `/infer` \- Chat Completion​

  * SDK
  * PROXY

Use the `triton/` prefix to route to triton server
    
    
    from litellm import completion  
      
      
    response = completion(  
        model="triton/llama-3-8b-instruct",  
        messages=[{"role": "user", "content": "who are u?"}],  
        max_tokens=10,  
        api_base="http://localhost:8000/infer",  
    )  
    

  1. Add models to your config.yaml

    
    
    model_list:  
      - model_name: my-triton-model  
        litellm_params:  
          model: triton/<your-triton-model>"  
          api_base: https://your-triton-api-base/triton/infer  
    

  2. Start the proxy

    
    
    $ litellm --config /path/to/config.yaml --detailed_debug  
    

  3. Send Request to LiteLLM Proxy Server

  * OpenAI Python v1.0.0+
  * curl

    
    
    import openai  
    from openai import OpenAI  
      
    # set base_url to your proxy server  
    # set api_key to send to proxy server  
    client = OpenAI(api_key="<proxy-api-key>", base_url="http://0.0.0.0:4000")  
      
    response = client.chat.completions.create(  
        model="my-triton-model",  
        messages=[{"role": "user", "content": "who are u?"}],  
        max_tokens=10,  
    )  
      
    print(response)  
      
    

`--header` is optional, only required if you're using litellm proxy with Virtual Keys
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
    --header 'Content-Type: application/json' \  
    --header 'Authorization: Bearer sk-1234' \  
    --data ' {  
    "model": "my-triton-model",  
    "messages": [{"role": "user", "content": "who are u?"}]  
    }'  
      
    

## Triton `/embeddings` \- Embedding​

  * SDK
  * PROXY

Use the `triton/` prefix to route to triton server
    
    
    from litellm import embedding  
    import os  
      
    response = await litellm.aembedding(  
        model="triton/<your-triton-model>",                                                         
        api_base="https://your-triton-api-base/triton/embeddings", # /embeddings endpoint you want litellm to call on your server  
        input=["good morning from litellm"],  
    )  
    

  1. Add models to your config.yaml

    
    
    model_list:  
      - model_name: my-triton-model  
        litellm_params:  
          model: triton/<your-triton-model>"  
          api_base: https://your-triton-api-base/triton/embeddings  
    

  2. Start the proxy

    
    
    $ litellm --config /path/to/config.yaml --detailed_debug  
    

  3. Send Request to LiteLLM Proxy Server

  * OpenAI Python v1.0.0+
  * curl

    
    
    import openai  
    from openai import OpenAI  
      
    # set base_url to your proxy server  
    # set api_key to send to proxy server  
    client = OpenAI(api_key="<proxy-api-key>", base_url="http://0.0.0.0:4000")  
      
    response = client.embeddings.create(  
        input=["hello from litellm"],  
        model="my-triton-model"  
    )  
      
    print(response)  
      
    

`--header` is optional, only required if you're using litellm proxy with Virtual Keys
    
    
    curl --location 'http://0.0.0.0:4000/embeddings' \  
    --header 'Content-Type: application/json' \  
    --header 'Authorization: Bearer sk-1234' \  
    --data ' {  
    "model": "my-triton-model",  
    "input": ["write a litellm poem"]  
    }'  
      
    

  * Triton `/generate` \- Chat Completion
  * Triton `/infer` \- Chat Completion
  * Triton `/embeddings` \- Embedding