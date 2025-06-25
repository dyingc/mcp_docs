# Deepseek | liteLLM

On this page

<https://deepseek.com/>

**We support ALL Deepseek models, just set`deepseek/` as a prefix when sending completion requests**

## API Key​
    
    
    # env variable  
    os.environ['DEEPSEEK_API_KEY']  
    

## Sample Usage​
    
    
    from litellm import completion  
    import os  
      
    os.environ['DEEPSEEK_API_KEY'] = ""  
    response = completion(  
        model="deepseek/deepseek-chat",   
        messages=[  
           {"role": "user", "content": "hello from litellm"}  
       ],  
    )  
    print(response)  
    

## Sample Usage - Streaming​
    
    
    from litellm import completion  
    import os  
      
    os.environ['DEEPSEEK_API_KEY'] = ""  
    response = completion(  
        model="deepseek/deepseek-chat",   
        messages=[  
           {"role": "user", "content": "hello from litellm"}  
       ],  
        stream=True  
    )  
      
    for chunk in response:  
        print(chunk)  
    

## Supported Models - ALL Deepseek Models Supported!​

We support ALL Deepseek models, just set `deepseek/` as a prefix when sending completion requests

Model Name| Function Call  
---|---  
deepseek-chat| `completion(model="deepseek/deepseek-chat", messages)`  
deepseek-coder| `completion(model="deepseek/deepseek-coder", messages)`  
  
## Reasoning Models​

Model Name| Function Call  
---|---  
deepseek-reasoner| `completion(model="deepseek/deepseek-reasoner", messages)`  
  
  * SDK
  * PROXY

    
    
    from litellm import completion  
    import os  
      
    os.environ['DEEPSEEK_API_KEY'] = ""  
    resp = completion(  
        model="deepseek/deepseek-reasoner",  
        messages=[{"role": "user", "content": "Tell me a joke."}],  
    )  
      
    print(  
        resp.choices[0].message.reasoning_content  
    )  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: deepseek-reasoner  
        litellm_params:  
            model: deepseek/deepseek-reasoner  
            api_key: os.environ/DEEPSEEK_API_KEY  
    

  2. Run proxy

    
    
    python litellm/proxy/main.py  
    

  3. Test it!

    
    
    curl -L -X POST 'http://0.0.0.0:4000/v1/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
        "model": "deepseek-reasoner",  
        "messages": [  
          {  
            "role": "user",  
            "content": [  
              {  
                "type": "text",  
                "text": "Hi, how are you ?"  
              }  
            ]  
          }  
        ]  
    }'  
    

  * API Key
  * Sample Usage
  * Sample Usage - Streaming
  * Supported Models - ALL Deepseek Models Supported!
  * Reasoning Models