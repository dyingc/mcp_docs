# Cerebras | liteLLM

On this page

<https://inference-docs.cerebras.ai/api-reference/chat-completions>

tip

**We support ALL Cerebras models, just set`model=cerebras/<any-model-on-cerebras>` as a prefix when sending litellm requests**

## API Key​
    
    
    # env variable  
    os.environ['CEREBRAS_API_KEY']  
    

## Sample Usage​
    
    
    from litellm import completion  
    import os  
      
    os.environ['CEREBRAS_API_KEY'] = ""  
    response = completion(  
        model="cerebras/llama3-70b-instruct",  
        messages=[  
            {  
                "role": "user",  
                "content": "What's the weather like in Boston today in Fahrenheit? (Write in JSON)",  
            }  
        ],  
        max_tokens=10,  
              
        # The prompt should include JSON if 'json_object' is selected; otherwise, you will get error code 400.  
        response_format={ "type": "json_object" },  
        seed=123,  
        stop=["\n\n"],  
        temperature=0.2,  
        top_p=0.9,  
        tool_choice="auto",  
        tools=[],  
        user="user",  
    )  
    print(response)  
    

## Sample Usage - Streaming​
    
    
    from litellm import completion  
    import os  
      
    os.environ['CEREBRAS_API_KEY'] = ""  
    response = completion(  
        model="cerebras/llama3-70b-instruct",  
        messages=[  
            {  
                "role": "user",  
                "content": "What's the weather like in Boston today in Fahrenheit? (Write in JSON)",  
            }  
        ],  
        stream=True,  
        max_tokens=10,  
      
        # The prompt should include JSON if 'json_object' is selected; otherwise, you will get error code 400.  
        response_format={ "type": "json_object" },   
        seed=123,  
        stop=["\n\n"],  
        temperature=0.2,  
        top_p=0.9,  
        tool_choice="auto",  
        tools=[],  
        user="user",  
    )  
      
    for chunk in response:  
        print(chunk)  
    

## Usage with LiteLLM Proxy Server​

Here's how to call a Cerebras model with the LiteLLM Proxy Server

  1. Modify the config.yaml

    
    
    model_list:  
      - model_name: my-model  
        litellm_params:  
          model: cerebras/<your-model-name>  # add cerebras/ prefix to route as Cerebras provider  
          api_key: api-key                 # api key to send your model  
    

  2. Start the proxy

    
    
    $ litellm --config /path/to/config.yaml  
    

  3. Send Request to LiteLLM Proxy Server

  * OpenAI Python v1.0.0+
  * curl

    
    
    import openai  
    client = openai.OpenAI(  
        api_key="sk-1234",             # pass litellm proxy key, if you're using virtual keys  
        base_url="http://0.0.0.0:4000" # litellm-proxy-base url  
    )  
      
    response = client.chat.completions.create(  
        model="my-model",  
        messages = [  
            {  
                "role": "user",  
                "content": "what llm are you"  
            }  
        ],  
    )  
      
    print(response)  
    
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
        --header 'Authorization: Bearer sk-1234' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "my-model",  
        "messages": [  
            {  
            "role": "user",  
            "content": "what llm are you"  
            }  
        ],  
    }'  
    

  * API Key
  * Sample Usage
  * Sample Usage - Streaming
  * Usage with LiteLLM Proxy Server