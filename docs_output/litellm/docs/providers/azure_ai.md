# Azure AI Studio | liteLLM

On this page

LiteLLM supports all models on Azure AI Studio

## Usage​

  * SDK
  * PROXY

### ENV VAR​
    
    
    import os   
    os.environ["AZURE_AI_API_KEY"] = ""  
    os.environ["AZURE_AI_API_BASE"] = ""  
    

### Example Call​
    
    
    from litellm import completion  
    import os  
    ## set ENV variables  
    os.environ["AZURE_AI_API_KEY"] = "azure ai key"  
    os.environ["AZURE_AI_API_BASE"] = "azure ai base url" # e.g.: https://Mistral-large-dfgfj-serverless.eastus2.inference.ai.azure.com/  
      
    # predibase llama-3 call  
    response = completion(  
        model="azure_ai/command-r-plus",   
        messages = [{ "content": "Hello, how are you?","role": "user"}]  
    )  
    

  1. Add models to your config.yaml

    
    
    model_list:  
      - model_name: command-r-plus  
        litellm_params:  
          model: azure_ai/command-r-plus  
          api_key: os.environ/AZURE_AI_API_KEY  
          api_base: os.environ/AZURE_AI_API_BASE  
    

  2. Start the proxy

    
    
    $ litellm --config /path/to/config.yaml --debug  
    

  3. Send Request to LiteLLM Proxy Server

  * OpenAI Python v1.0.0+
  * curl

    
    
    import openai  
    client = openai.OpenAI(  
        api_key="sk-1234",             # pass litellm proxy key, if you're using virtual keys  
        base_url="http://0.0.0.0:4000" # litellm-proxy-base url  
    )  
      
    response = client.chat.completions.create(  
        model="command-r-plus",  
        messages = [  
          {  
              "role": "system",  
              "content": "Be a good human!"  
          },  
          {  
              "role": "user",  
              "content": "What do you know about earth?"  
          }  
      ]  
    )  
      
    print(response)  
    
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
        --header 'Authorization: Bearer sk-1234' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "command-r-plus",  
        "messages": [  
          {  
              "role": "system",  
              "content": "Be a good human!"  
          },  
          {  
              "role": "user",  
              "content": "What do you know about earth?"  
          }  
          ],  
    }'  
    

## Passing additional params - max_tokens, temperature​

See all litellm.completion supported params [here](/docs/completion/input#translated-openai-params)
    
    
    # !pip install litellm  
    from litellm import completion  
    import os  
    ## set ENV variables  
    os.environ["AZURE_AI_API_KEY"] = "azure ai api key"  
    os.environ["AZURE_AI_API_BASE"] = "azure ai api base"  
      
    # command r plus call  
    response = completion(  
        model="azure_ai/command-r-plus",   
        messages = [{ "content": "Hello, how are you?","role": "user"}],  
        max_tokens=20,  
        temperature=0.5  
    )  
    

**proxy**
    
    
      model_list:  
        - model_name: command-r-plus  
          litellm_params:  
            model: azure_ai/command-r-plus  
            api_key: os.environ/AZURE_AI_API_KEY  
            api_base: os.environ/AZURE_AI_API_BASE  
            max_tokens: 20  
            temperature: 0.5  
    

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
        model="mistral",  
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
        "model": "mistral",  
        "messages": [  
            {  
            "role": "user",  
            "content": "what llm are you"  
            }  
        ],  
    }'  
    

## Function Calling​

  * SDK
  * PROXY

    
    
    from litellm import completion  
      
    # set env  
    os.environ["AZURE_AI_API_KEY"] = "your-api-key"  
    os.environ["AZURE_AI_API_BASE"] = "your-api-base"  
      
    tools = [  
        {  
            "type": "function",  
            "function": {  
                "name": "get_current_weather",  
                "description": "Get the current weather in a given location",  
                "parameters": {  
                    "type": "object",  
                    "properties": {  
                        "location": {  
                            "type": "string",  
                            "description": "The city and state, e.g. San Francisco, CA",  
                        },  
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},  
                    },  
                    "required": ["location"],  
                },  
            },  
        }  
    ]  
    messages = [{"role": "user", "content": "What's the weather like in Boston today?"}]  
      
    response = completion(  
        model="azure_ai/mistral-large-latest",  
        messages=messages,  
        tools=tools,  
        tool_choice="auto",  
    )  
    # Add any assertions, here to check response args  
    print(response)  
    assert isinstance(response.choices[0].message.tool_calls[0].function.name, str)  
    assert isinstance(  
        response.choices[0].message.tool_calls[0].function.arguments, str  
    )  
      
    
    
    
    curl http://0.0.0.0:4000/v1/chat/completions \  
    -H "Content-Type: application/json" \  
    -H "Authorization: Bearer $YOUR_API_KEY" \  
    -d '{  
      "model": "mistral",  
      "messages": [  
        {  
          "role": "user",  
          "content": "What'\''s the weather like in Boston today?"  
        }  
      ],  
      "tools": [  
        {  
          "type": "function",  
          "function": {  
            "name": "get_current_weather",  
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
      ],  
      "tool_choice": "auto"  
    }'  
      
    

## Supported Models​

LiteLLM supports **ALL** azure ai models. Here's a few examples:

Model Name| Function Call  
---|---  
Cohere command-r-plus| `completion(model="azure_ai/command-r-plus", messages)`  
Cohere command-r| `completion(model="azure_ai/command-r", messages)`  
mistral-large-latest| `completion(model="azure_ai/mistral-large-latest", messages)`  
AI21-Jamba-Instruct| `completion(model="azure_ai/ai21-jamba-instruct", messages)`  
  
## Rerank Endpoint​

### Usage​

  * LiteLLM SDK Usage
  * LiteLLM Proxy Usage

    
    
    from litellm import rerank  
    import os  
      
    os.environ["AZURE_AI_API_KEY"] = "sk-.."  
    os.environ["AZURE_AI_API_BASE"] = "https://.."  
      
    query = "What is the capital of the United States?"  
    documents = [  
        "Carson City is the capital city of the American state of Nevada.",  
        "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",  
        "Washington, D.C. is the capital of the United States.",  
        "Capital punishment has existed in the United States since before it was a country.",  
    ]  
      
    response = rerank(  
        model="azure_ai/rerank-english-v3.0",  
        query=query,  
        documents=documents,  
        top_n=3,  
    )  
    print(response)  
    

LiteLLM provides an cohere api compatible `/rerank` endpoint for Rerank calls.

**Setup**

Add this to your litellm proxy config.yaml
    
    
    model_list:  
      - model_name: Salesforce/Llama-Rank-V1  
        litellm_params:  
          model: together_ai/Salesforce/Llama-Rank-V1  
          api_key: os.environ/TOGETHERAI_API_KEY  
      - model_name: rerank-english-v3.0  
        litellm_params:  
          model: azure_ai/rerank-english-v3.0  
          api_key: os.environ/AZURE_AI_API_KEY  
          api_base: os.environ/AZURE_AI_API_BASE  
    

Start litellm
    
    
    litellm --config /path/to/config.yaml  
      
    # RUNNING on http://0.0.0.0:4000  
    

Test request
    
    
    curl http://0.0.0.0:4000/rerank \  
      -H "Authorization: Bearer sk-1234" \  
      -H "Content-Type: application/json" \  
      -d '{  
        "model": "rerank-english-v3.0",  
        "query": "What is the capital of the United States?",  
        "documents": [  
            "Carson City is the capital city of the American state of Nevada.",  
            "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",  
            "Washington, D.C. is the capital of the United States.",  
            "Capital punishment has existed in the United States since before it was a country."  
        ],  
        "top_n": 3  
      }'  
    

  * Usage
    * ENV VAR
    * Example Call
  * Passing additional params - max_tokens, temperature
  * Function Calling
  * Supported Models
  * Rerank Endpoint
    * Usage