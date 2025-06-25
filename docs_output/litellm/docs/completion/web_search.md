# Using Web Search | liteLLM

On this page

Use web search with litellm

Feature| Details  
---|---  
Supported Endpoints| \- `/chat/completions`   
\- `/responses`  
Supported Providers| `openai`, `xai`, `vertex_ai`, `gemini`, `perplexity`  
LiteLLM Cost Tracking| ✅ Supported  
LiteLLM Version| `v1.71.0+`  
  
## `/chat/completions` (litellm.completion)​

### Quick Start​

  * SDK
  * PROXY

    
    
    from litellm import completion  
      
    response = completion(  
        model="openai/gpt-4o-search-preview",  
        messages=[  
            {  
                "role": "user",  
                "content": "What was a positive news story from today?",  
            }  
        ],  
        web_search_options={  
            "search_context_size": "medium"  # Options: "low", "medium", "high"  
        }  
    )  
    

  1. Setup config.yaml

    
    
    model_list:  
      # OpenAI  
      - model_name: gpt-4o-search-preview  
        litellm_params:  
          model: openai/gpt-4o-search-preview  
          api_key: os.environ/OPENAI_API_KEY  
        
      # xAI  
      - model_name: grok-3  
        litellm_params:  
          model: xai/grok-3  
          api_key: os.environ/XAI_API_KEY  
        
      # VertexAI  
      - model_name: gemini-2-flash  
        litellm_params:  
          model: gemini-2.0-flash  
          vertex_project: your-project-id  
          vertex_location: us-central1  
        
      # Google AI Studio  
      - model_name: gemini-2-flash-studio  
        litellm_params:  
          model: gemini/gemini-2.0-flash  
          api_key: os.environ/GOOGLE_API_KEY  
    

  2. Start the proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
    from openai import OpenAI  
      
    # Point to your proxy server  
    client = OpenAI(  
        api_key="sk-1234",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    response = client.chat.completions.create(  
        model="grok-3",  # or any other web search enabled model  
        messages=[  
            {  
                "role": "user",  
                "content": "What was a positive news story from today?"  
            }  
        ]  
    )  
    

### Search context size​

  * SDK
  * PROXY

**OpenAI (using web_search_options)**
    
    
     from litellm import completion  
      
    # Customize search context size  
    response = completion(  
        model="openai/gpt-4o-search-preview",  
        messages=[  
            {  
                "role": "user",  
                "content": "What was a positive news story from today?",  
            }  
        ],  
        web_search_options={  
            "search_context_size": "low"  # Options: "low", "medium" (default), "high"  
        }  
    )  
    

**xAI (using web_search_options)**
    
    
     from litellm import completion  
      
    # Customize search context size for xAI  
    response = completion(  
        model="xai/grok-3",  
        messages=[  
            {  
                "role": "user",  
                "content": "What was a positive news story from today?",  
            }  
        ],  
        web_search_options={  
            "search_context_size": "high"  # Options: "low", "medium" (default), "high"  
        }  
    )  
    

**VertexAI/Gemini (using web_search_options)**
    
    
     from litellm import completion  
      
    # Customize search context size for Gemini  
    response = completion(  
        model="gemini-2.0-flash",  
        messages=[  
            {  
                "role": "user",  
                "content": "What was a positive news story from today?",  
            }  
        ],  
        web_search_options={  
            "search_context_size": "low"  # Options: "low", "medium" (default), "high"  
        }  
    )  
    
    
    
    from openai import OpenAI  
      
    # Point to your proxy server  
    client = OpenAI(  
        api_key="sk-1234",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    # Customize search context size  
    response = client.chat.completions.create(  
        model="grok-3",  # works with any web search enabled model  
        messages=[  
            {  
                "role": "user",  
                "content": "What was a positive news story from today?"  
            }  
        ],  
        web_search_options={  
            "search_context_size": "low"  # Options: "low", "medium" (default), "high"  
        }  
    )  
    

## `/responses` (litellm.responses)​

### Quick Start​

  * SDK
  * PROXY

    
    
    from litellm import responses  
      
    response = responses(  
        model="openai/gpt-4o",  
        input=[  
            {  
                "role": "user",  
                "content": "What was a positive news story from today?"  
            }  
        ],  
        tools=[{  
            "type": "web_search_preview"  # enables web search with default medium context size  
        }]  
    )  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: gpt-4o  
        litellm_params:  
          model: openai/gpt-4o  
          api_key: os.environ/OPENAI_API_KEY  
    

  2. Start the proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
    from openai import OpenAI  
      
    # Point to your proxy server  
    client = OpenAI(  
        api_key="sk-1234",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    response = client.responses.create(  
        model="gpt-4o",  
        tools=[{  
            "type": "web_search_preview"  
        }],  
        input="What was a positive news story from today?",  
    )  
      
    print(response.output_text)  
    

### Search context size​

  * SDK
  * PROXY

    
    
    from litellm import responses  
      
    # Customize search context size  
    response = responses(  
        model="openai/gpt-4o",  
        input=[  
            {  
                "role": "user",  
                "content": "What was a positive news story from today?"  
            }  
        ],  
        tools=[{  
            "type": "web_search_preview",  
            "search_context_size": "low"  # Options: "low", "medium" (default), "high"  
        }]  
    )  
    
    
    
    from openai import OpenAI  
      
    # Point to your proxy server  
    client = OpenAI(  
        api_key="sk-1234",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    # Customize search context size  
    response = client.responses.create(  
        model="gpt-4o",  
        tools=[{  
            "type": "web_search_preview",  
            "search_context_size": "low"  # Options: "low", "medium" (default), "high"  
        }],  
        input="What was a positive news story from today?",  
    )  
      
    print(response.output_text)  
    

## Configuring Web Search in config.yaml​

You can set default web search options directly in your proxy config file:

  * Default Web Search
  * Custom Search Context

    
    
    model_list:  
      # Enable web search by default for all requests to this model  
      - model_name: grok-3  
        litellm_params:  
          model: xai/grok-3  
          api_key: os.environ/XAI_API_KEY  
          web_search_options: {}  # Enables web search with default settings  
    
    
    
    model_list:  
      # Set custom web search context size  
      - model_name: grok-3  
        litellm_params:  
          model: xai/grok-3  
          api_key: os.environ/XAI_API_KEY  
          web_search_options:  
            search_context_size: "high"  # Options: "low", "medium", "high"  
        
      # Different context size for different models  
      - model_name: gpt-4o-search-preview  
        litellm_params:  
          model: openai/gpt-4o-search-preview  
          api_key: os.environ/OPENAI_API_KEY  
          web_search_options:  
            search_context_size: "low"  
        
      # Gemini with medium context (default)  
      - model_name: gemini-2-flash  
        litellm_params:  
          model: gemini-2.0-flash  
          vertex_project: your-project-id  
          vertex_location: us-central1  
          web_search_options:  
            search_context_size: "medium"  
    

**Note:** When `web_search_options` is set in the config, it applies to all requests to that model. Users can still override these settings by passing `web_search_options` in their API requests.

## Checking if a model supports web search​

  * SDK
  * PROXY

Use `litellm.supports_web_search(model="model_name")` -> returns `True` if model can perform web searches
    
    
    # Check OpenAI models  
    assert litellm.supports_web_search(model="openai/gpt-4o-search-preview") == True  
      
    # Check xAI models  
    assert litellm.supports_web_search(model="xai/grok-3") == True  
      
    # Check VertexAI models  
    assert litellm.supports_web_search(model="gemini-2.0-flash") == True  
      
    # Check Google AI Studio models  
    assert litellm.supports_web_search(model="gemini/gemini-2.0-flash") == True  
    

  1. Define models in config.yaml

    
    
    model_list:  
      # OpenAI  
      - model_name: gpt-4o-search-preview  
        litellm_params:  
          model: openai/gpt-4o-search-preview  
          api_key: os.environ/OPENAI_API_KEY  
        model_info:  
          supports_web_search: True  
        
      # xAI  
      - model_name: grok-3  
        litellm_params:  
          model: xai/grok-3  
          api_key: os.environ/XAI_API_KEY  
        model_info:  
          supports_web_search: True  
        
      # VertexAI  
      - model_name: gemini-2-flash  
        litellm_params:  
          model: gemini-2.0-flash  
          vertex_project: your-project-id  
          vertex_location: us-central1  
        model_info:  
          supports_web_search: True  
        
      # Google AI Studio  
      - model_name: gemini-2-flash-studio  
        litellm_params:  
          model: gemini/gemini-2.0-flash  
          api_key: os.environ/GOOGLE_API_KEY  
        model_info:  
          supports_web_search: True  
    

  2. Run proxy server

    
    
    litellm --config config.yaml  
    

  3. Call `/model_group/info` to check if a model supports web search

    
    
    curl -X 'GET' \  
      'http://localhost:4000/model_group/info' \  
      -H 'accept: application/json' \  
      -H 'x-api-key: sk-1234'  
    

Expected Response
    
    
    {  
      "data": [  
        {  
          "model_group": "gpt-4o-search-preview",  
          "providers": ["openai"],  
          "max_tokens": 128000,  
          "supports_web_search": true  
        },  
        {  
          "model_group": "grok-3",  
          "providers": ["xai"],  
          "max_tokens": 131072,  
          "supports_web_search": true  
        },  
        {  
          "model_group": "gemini-2-flash",  
          "providers": ["vertex_ai"],  
          "max_tokens": 8192,  
          "supports_web_search": true  
        }  
      ]  
    }  
    

  * `/chat/completions` (litellm.completion)
    * Quick Start
    * Search context size
  * `/responses` (litellm.responses)
    * Quick Start
    * Search context size
  * Configuring Web Search in config.yaml
  * Checking if a model supports web search