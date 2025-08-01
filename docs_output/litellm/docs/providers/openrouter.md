# OpenRouter | liteLLM

On this page

LiteLLM supports all the text / chat / vision models from [OpenRouter](https://openrouter.ai/docs)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BerriAI/litellm/blob/main/cookbook/LiteLLM_OpenRouter.ipynb)

## Usage​
    
    
    import os  
    from litellm import completion  
    os.environ["OPENROUTER_API_KEY"] = ""  
    os.environ["OPENROUTER_API_BASE"] = "" # [OPTIONAL] defaults to https://openrouter.ai/api/v1  
      
      
    os.environ["OR_SITE_URL"] = "" # [OPTIONAL]  
    os.environ["OR_APP_NAME"] = "" # [OPTIONAL]  
      
    response = completion(  
                model="openrouter/google/palm-2-chat-bison",  
                messages=messages,  
            )  
    

## OpenRouter Completion Models​

🚨 LiteLLM supports ALL OpenRouter models, send `model=openrouter/<your-openrouter-model>` to send it to open router. See all openrouter models [here](https://openrouter.ai/models)

Model Name| Function Call  
---|---  
openrouter/openai/gpt-3.5-turbo| `completion('openrouter/openai/gpt-3.5-turbo', messages)`  
openrouter/openai/gpt-3.5-turbo-16k| `completion('openrouter/openai/gpt-3.5-turbo-16k', messages)`  
openrouter/openai/gpt-4| `completion('openrouter/openai/gpt-4', messages)`  
openrouter/openai/gpt-4-32k| `completion('openrouter/openai/gpt-4-32k', messages)`  
openrouter/anthropic/claude-2| `completion('openrouter/anthropic/claude-2', messages)`  
openrouter/anthropic/claude-instant-v1| `completion('openrouter/anthropic/claude-instant-v1', messages)`  
openrouter/google/palm-2-chat-bison| `completion('openrouter/google/palm-2-chat-bison', messages)`  
openrouter/google/palm-2-codechat-bison| `completion('openrouter/google/palm-2-codechat-bison', messages)`  
openrouter/meta-llama/llama-2-13b-chat| `completion('openrouter/meta-llama/llama-2-13b-chat', messages)`  
openrouter/meta-llama/llama-2-70b-chat| `completion('openrouter/meta-llama/llama-2-70b-chat', messages)`  
  
## Passing OpenRouter Params - transforms, models, route​

Pass `transforms`, `models`, `route`as arguments to `litellm.completion()`
    
    
    import os  
    from litellm import completion  
    os.environ["OPENROUTER_API_KEY"] = ""  
      
    response = completion(  
                model="openrouter/google/palm-2-chat-bison",  
                messages=messages,  
                transforms = [""],  
                route= ""  
            )  
    

  * Usage
  * OpenRouter Completion Models
  * Passing OpenRouter Params - transforms, models, route