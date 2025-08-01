# Custom Prompt Management | liteLLM

On this page

Connect LiteLLM to your prompt management system with custom hooks.

## Overview​

## How it works​

## Quick Start​

### 1\. Create Your Custom Prompt Manager​

Create a class that inherits from `CustomPromptManagement` to handle prompt retrieval and formatting:

**Example Implementation**

Create a new file called `custom_prompt.py` and add this code. The key method here is `get_chat_completion_prompt` you can implement custom logic to retrieve and format prompts based on the `prompt_id` and `prompt_variables`.
    
    
    from typing import List, Tuple, Optional  
    from litellm.integrations.custom_prompt_management import CustomPromptManagement  
    from litellm.types.llms.openai import AllMessageValues  
    from litellm.types.utils import StandardCallbackDynamicParams  
      
    class MyCustomPromptManagement(CustomPromptManagement):  
        def get_chat_completion_prompt(  
            self,  
            model: str,  
            messages: List[AllMessageValues],  
            non_default_params: dict,  
            prompt_id: str,  
            prompt_variables: Optional[dict],  
            dynamic_callback_params: StandardCallbackDynamicParams,  
        ) -> Tuple[str, List[AllMessageValues], dict]:  
            """  
            Retrieve and format prompts based on prompt_id.  
              
            Returns:  
                - model: The model to use  
                - messages: The formatted messages  
                - non_default_params: Optional parameters like temperature  
            """  
            # Example matching the diagram: Add system message for prompt_id "1234"  
            if prompt_id == "1234":  
                # Prepend system message while preserving existing messages  
                new_messages = [  
                    {"role": "system", "content": "Be a good Bot!"},  
                ] + messages  
                return model, new_messages, non_default_params  
              
            # Default: Return original messages if no prompt_id match  
            return model, messages, non_default_params  
      
    prompt_management = MyCustomPromptManagement()  
    

### 2\. Configure Your Prompt Manager in LiteLLM `config.yaml`​
    
    
    model_list:  
      - model_name: gpt-4  
        litellm_params:  
          model: openai/gpt-4  
          api_key: os.environ/OPENAI_API_KEY  
      
    litellm_settings:  
      callbacks: custom_prompt.prompt_management  # sets litellm.callbacks = [prompt_management]  
    

### 3\. Start LiteLLM Gateway​

  * Docker Run
  * litellm pip

Mount your `custom_logger.py` on the LiteLLM Docker container.
    
    
    docker run -d \  
      -p 4000:4000 \  
      -e OPENAI_API_KEY=$OPENAI_API_KEY \  
      --name my-app \  
      -v $(pwd)/my_config.yaml:/app/config.yaml \  
      -v $(pwd)/custom_logger.py:/app/custom_logger.py \  
      my-app:latest \  
      --config /app/config.yaml \  
      --port 4000 \  
      --detailed_debug \  
    
    
    
    litellm --config config.yaml --detailed_debug  
    

### 4\. Test Your Custom Prompt Manager​

When you pass `prompt_id="1234"`, the custom prompt manager will add a system message "Be a good Bot!" to your conversation:

  * OpenAI Python v1.0.0+
  * Langchain
  * Curl

    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        api_key="sk-1234",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    response = client.chat.completions.create(  
        model="gemini-1.5-pro",  
        messages=[{"role": "user", "content": "hi"}],  
        prompt_id="1234"  
    )  
      
    print(response.choices[0].message.content)  
    
    
    
    from langchain.chat_models import ChatOpenAI  
    from langchain.schema import HumanMessage  
      
    chat = ChatOpenAI(  
        model="gpt-4",  
        openai_api_key="sk-1234",  
        openai_api_base="http://0.0.0.0:4000",  
        extra_body={  
            "prompt_id": "1234"  
        }  
    )  
      
    messages = []  
    response = chat(messages)  
      
    print(response.content)  
    
    
    
    curl -X POST http://0.0.0.0:4000/v1/chat/completions \  
    -H "Content-Type: application/json" \  
    -H "Authorization: Bearer sk-1234" \  
    -d '{  
        "model": "gemini-1.5-pro",  
        "messages": [{"role": "user", "content": "hi"}],  
        "prompt_id": "1234"  
    }'  
    

The request will be transformed from:
    
    
    {  
        "model": "gemini-1.5-pro",  
        "messages": [{"role": "user", "content": "hi"}],  
        "prompt_id": "1234"  
    }  
    

To:
    
    
    {  
        "model": "gemini-1.5-pro",  
        "messages": [  
            {"role": "system", "content": "Be a good Bot!"},  
            {"role": "user", "content": "hi"}  
        ]  
    }  
    

  * Overview
  * How it works
  * Quick Start
    * 1\. Create Your Custom Prompt Manager
    * 2\. Configure Your Prompt Manager in LiteLLM `config.yaml`
    * 3\. Start LiteLLM Gateway
    * 4\. Test Your Custom Prompt Manager