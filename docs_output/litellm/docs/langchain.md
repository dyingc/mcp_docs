# Using ChatLiteLLM() - Langchain | liteLLM

On this page

## Pre-Requisites​
    
    
    !pip install litellm langchain  
    

## Quick Start​

  * OpenAI
  * Anthropic
  * Replicate
  * Cohere

    
    
    import os  
    from langchain_community.chat_models import ChatLiteLLM  
    from langchain_core.prompts import (  
        ChatPromptTemplate,  
        SystemMessagePromptTemplate,  
        AIMessagePromptTemplate,  
        HumanMessagePromptTemplate,  
    )  
    from langchain_core.messages import AIMessage, HumanMessage, SystemMessage  
      
    os.environ['OPENAI_API_KEY'] = ""  
    chat = ChatLiteLLM(model="gpt-3.5-turbo")  
    messages = [  
        HumanMessage(  
            content="what model are you"  
        )  
    ]  
    chat.invoke(messages)  
    
    
    
    import os  
    from langchain_community.chat_models import ChatLiteLLM  
    from langchain_core.prompts import (  
        ChatPromptTemplate,  
        SystemMessagePromptTemplate,  
        AIMessagePromptTemplate,  
        HumanMessagePromptTemplate,  
    )  
    from langchain_core.messages import AIMessage, HumanMessage, SystemMessage  
      
    os.environ['ANTHROPIC_API_KEY'] = ""  
    chat = ChatLiteLLM(model="claude-2", temperature=0.3)  
    messages = [  
        HumanMessage(  
            content="what model are you"  
        )  
    ]  
    chat.invoke(messages)  
    
    
    
    import os  
    from langchain_community.chat_models import ChatLiteLLM  
    from langchain_core.prompts.chat import (  
        ChatPromptTemplate,  
        SystemMessagePromptTemplate,  
        AIMessagePromptTemplate,  
        HumanMessagePromptTemplate,  
    )  
    from langchain_core.messages import AIMessage, HumanMessage, SystemMessage  
      
    os.environ['REPLICATE_API_TOKEN'] = ""  
    chat = ChatLiteLLM(model="replicate/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1")  
    messages = [  
        HumanMessage(  
            content="what model are you?"  
        )  
    ]  
    chat.invoke(messages)  
    
    
    
    import os  
    from langchain_community.chat_models import ChatLiteLLM  
    from langchain_core.prompts import (  
        ChatPromptTemplate,  
        SystemMessagePromptTemplate,  
        AIMessagePromptTemplate,  
        HumanMessagePromptTemplate,  
    )  
    from langchain_core.messages import AIMessage, HumanMessage, SystemMessage  
      
    os.environ['COHERE_API_KEY'] = ""  
    chat = ChatLiteLLM(model="command-nightly")  
    messages = [  
        HumanMessage(  
            content="what model are you?"  
        )  
    ]  
    chat.invoke(messages)  
    

## Use Langchain ChatLiteLLM with MLflow​

MLflow provides open-source observability solution for ChatLiteLLM.

To enable the integration, simply call `mlflow.litellm.autolog()` before in your code. No other setup is necessary.
    
    
    import mlflow  
      
    mlflow.litellm.autolog()  
    

Once the auto-tracing is enabled, you can invoke `ChatLiteLLM` and see recorded traces in MLflow.
    
    
    import os  
    from langchain.chat_models import ChatLiteLLM  
      
    os.environ['OPENAI_API_KEY']="sk-..."  
      
    chat = ChatLiteLLM(model="gpt-4o-mini")  
    chat.invoke("Hi!")  
    

## Use Langchain ChatLiteLLM with Lunary​
    
    
    import os  
    from langchain.chat_models import ChatLiteLLM  
    from langchain.schema import HumanMessage  
    import litellm  
      
    os.environ["LUNARY_PUBLIC_KEY"] = "" # from https://app.lunary.ai/settings  
    os.environ['OPENAI_API_KEY']="sk-..."  
      
    litellm.success_callback = ["lunary"]   
    litellm.failure_callback = ["lunary"]   
      
    chat = ChatLiteLLM(  
      model="gpt-4o"  
      messages = [  
        HumanMessage(  
            content="what model are you"  
        )  
    ]  
    chat(messages)  
    

Get more details [here](/docs/observability/lunary_integration)

## Use LangChain ChatLiteLLM + Langfuse​

Checkout this section [here](/docs/observability/langfuse_integration#use-langchain-chatlitellm--langfuse) for more details on how to integrate Langfuse with ChatLiteLLM.

  * Pre-Requisites
  * Quick Start
  * Use Langchain ChatLiteLLM with MLflow
  * Use Langchain ChatLiteLLM with Lunary
  * Use LangChain ChatLiteLLM + Langfuse