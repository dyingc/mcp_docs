# Meta Llama | liteLLM

On this page

Property| Details  
---|---  
Description| Meta's Llama API provides access to Meta's family of large language models.  
Provider Route on LiteLLM| `meta_llama/`  
Supported Endpoints| `/chat/completions`, `/completions`, `/responses`  
API Reference| [Llama API Reference ↗](https://llama.developer.meta.com?utm_source=partner-litellm&utm_medium=website)  
  
## Required Variables​

Environment Variables
    
    
    os.environ["LLAMA_API_KEY"] = ""  # your Meta Llama API key  
    

## Supported Models​

info

All models listed here <https://llama.developer.meta.com/docs/models/> are supported. We actively maintain the list of models, token window, etc. [here](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json).

Model ID| Input context length| Output context length| Input Modalities| Output Modalities  
---|---|---|---|---  
`Llama-4-Scout-17B-16E-Instruct-FP8`| 128k| 4028| Text, Image| Text  
`Llama-4-Maverick-17B-128E-Instruct-FP8`| 128k| 4028| Text, Image| Text  
`Llama-3.3-70B-Instruct`| 128k| 4028| Text| Text  
`Llama-3.3-8B-Instruct`| 128k| 4028| Text| Text  
  
## Usage - LiteLLM Python SDK​

### Non-streaming​

Meta Llama Non-streaming Completion
    
    
    import os  
    import litellm  
    from litellm import completion  
      
    os.environ["LLAMA_API_KEY"] = ""  # your Meta Llama API key  
      
    messages = [{"content": "Hello, how are you?", "role": "user"}]  
      
    # Meta Llama call  
    response = completion(model="meta_llama/Llama-4-Maverick-17B-128E-Instruct-FP8", messages=messages)  
    

### Streaming​

Meta Llama Streaming Completion
    
    
    import os  
    import litellm  
    from litellm import completion  
      
    os.environ["LLAMA_API_KEY"] = ""  # your Meta Llama API key  
      
    messages = [{"content": "Hello, how are you?", "role": "user"}]  
      
    # Meta Llama call with streaming  
    response = completion(  
        model="meta_llama/Llama-4-Maverick-17B-128E-Instruct-FP8",  
        messages=messages,  
        stream=True  
    )  
      
    for chunk in response:  
        print(chunk)  
    

### Function Calling​

Meta Llama Function Calling
    
    
    import os  
    import litellm  
    from litellm import completion  
      
    os.environ["LLAMA_API_KEY"] = ""  # your Meta Llama API key  
      
    messages = [{"content": "What's the weather like in San Francisco?", "role": "user"}]  
      
    # Define the function  
    tools = [  
        {  
            "type": "function",  
            "function": {  
                "name": "get_weather",  
                "description": "Get the current weather in a given location",  
                "parameters": {  
                    "type": "object",  
                    "properties": {  
                        "location": {  
                            "type": "string",  
                            "description": "The city and state, e.g. San Francisco, CA"  
                        },  
                        "unit": {  
                            "type": "string",  
                            "enum": ["celsius", "fahrenheit"]  
                        }  
                    },  
                    "required": ["location"]  
                }  
            }  
        }  
    ]  
      
    # Meta Llama call with function calling  
    response = completion(  
        model="meta_llama/Llama-4-Maverick-17B-128E-Instruct-FP8",  
        messages=messages,  
        tools=tools,  
        tool_choice="auto"  
    )  
      
    print(response.choices[0].message.tool_calls)  
    

### Tool Use​

Meta Llama Tool Use
    
    
    import os  
    import litellm  
    from litellm import completion  
      
    os.environ["LLAMA_API_KEY"] = ""  # your Meta Llama API key  
      
    messages = [{"content": "Create a chart showing the population growth of New York City from 2010 to 2020", "role": "user"}]  
      
    # Define the tools  
    tools = [  
        {  
            "type": "function",  
            "function": {  
                "name": "create_chart",  
                "description": "Create a chart with the provided data",  
                "parameters": {  
                    "type": "object",  
                    "properties": {  
                        "chart_type": {  
                            "type": "string",  
                            "enum": ["bar", "line", "pie", "scatter"],  
                            "description": "The type of chart to create"  
                        },  
                        "title": {  
                            "type": "string",  
                            "description": "The title of the chart"  
                        },  
                        "data": {  
                            "type": "object",  
                            "description": "The data to plot in the chart"  
                        }  
                    },  
                    "required": ["chart_type", "title", "data"]  
                }  
            }  
        }  
    ]  
      
    # Meta Llama call with tool use  
    response = completion(  
        model="meta_llama/Llama-4-Maverick-17B-128E-Instruct-FP8",  
        messages=messages,  
        tools=tools,  
        tool_choice="auto"  
    )  
      
    print(response.choices[0].message.content)  
    

## Usage - LiteLLM Proxy​

Add the following to your LiteLLM Proxy configuration file:

config.yaml
    
    
    model_list:  
      - model_name: meta_llama/Llama-3.3-70B-Instruct  
        litellm_params:  
          model: meta_llama/Llama-3.3-70B-Instruct  
          api_key: os.environ/LLAMA_API_KEY  
      
      - model_name: meta_llama/Llama-3.3-8B-Instruct  
        litellm_params:  
          model: meta_llama/Llama-3.3-8B-Instruct  
          api_key: os.environ/LLAMA_API_KEY  
    

Start your LiteLLM Proxy server:

Start LiteLLM Proxy
    
    
    litellm --config config.yaml  
      
    # RUNNING on http://0.0.0.0:4000  
    

  * OpenAI SDK
  * LiteLLM SDK
  * cURL

Meta Llama via Proxy - Non-streaming
    
    
    from openai import OpenAI  
      
    # Initialize client with your proxy URL  
    client = OpenAI(  
        base_url="http://localhost:4000",  # Your proxy URL  
        api_key="your-proxy-api-key"       # Your proxy API key  
    )  
      
    # Non-streaming response  
    response = client.chat.completions.create(  
        model="meta_llama/Llama-4-Maverick-17B-128E-Instruct-FP8",  
        messages=[{"role": "user", "content": "Write a short poem about AI."}]  
    )  
      
    print(response.choices[0].message.content)  
    

Meta Llama via Proxy - Streaming
    
    
    from openai import OpenAI  
      
    # Initialize client with your proxy URL  
    client = OpenAI(  
        base_url="http://localhost:4000",  # Your proxy URL  
        api_key="your-proxy-api-key"       # Your proxy API key  
    )  
      
    # Streaming response  
    response = client.chat.completions.create(  
        model="meta_llama/Llama-4-Maverick-17B-128E-Instruct-FP8",  
        messages=[{"role": "user", "content": "Write a short poem about AI."}],  
        stream=True  
    )  
      
    for chunk in response:  
        if chunk.choices[0].delta.content is not None:  
            print(chunk.choices[0].delta.content, end="")  
    

Meta Llama via Proxy - LiteLLM SDK
    
    
    import litellm  
      
    # Configure LiteLLM to use your proxy  
    response = litellm.completion(  
        model="litellm_proxy/meta_llama/Llama-3.3-70B-Instruct",  
        messages=[{"role": "user", "content": "Write a short poem about AI."}],  
        api_base="http://localhost:4000",  
        api_key="your-proxy-api-key"  
    )  
      
    print(response.choices[0].message.content)  
    

Meta Llama via Proxy - LiteLLM SDK Streaming
    
    
    import litellm  
      
    # Configure LiteLLM to use your proxy with streaming  
    response = litellm.completion(  
        model="litellm_proxy/meta_llama/Llama-3.3-70B-Instruct",  
        messages=[{"role": "user", "content": "Write a short poem about AI."}],  
        api_base="http://localhost:4000",  
        api_key="your-proxy-api-key",  
        stream=True  
    )  
      
    for chunk in response:  
        if hasattr(chunk.choices[0], 'delta') and chunk.choices[0].delta.content is not None:  
            print(chunk.choices[0].delta.content, end="")  
    

Meta Llama via Proxy - cURL
    
    
    curl http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer your-proxy-api-key" \  
      -d '{  
        "model": "meta_llama/Llama-3.3-70B-Instruct",  
        "messages": [{"role": "user", "content": "Write a short poem about AI."}]  
      }'  
    

Meta Llama via Proxy - cURL Streaming
    
    
    curl http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer your-proxy-api-key" \  
      -d '{  
        "model": "meta_llama/Llama-3.3-70B-Instruct",  
        "messages": [{"role": "user", "content": "Write a short poem about AI."}],  
        "stream": true  
      }'  
    

For more detailed information on using the LiteLLM Proxy, see the [LiteLLM Proxy documentation](/docs/providers/litellm_proxy).

  * Required Variables
  * Supported Models
  * Usage - LiteLLM Python SDK
    * Non-streaming
    * Streaming
    * Function Calling
    * Tool Use
  * Usage - LiteLLM Proxy