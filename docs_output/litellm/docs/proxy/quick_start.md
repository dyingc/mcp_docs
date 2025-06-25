# Quick Start | liteLLM

On this page

Quick start CLI, Config, Docker

LiteLLM Server (LLM Gateway) manages:

  * **Unified Interface** : Calling 100+ LLMs Huggingface/Bedrock/TogetherAI/etc. in the OpenAI `ChatCompletions` & `Completions` format
  * **Cost tracking** : Authentication, Spend Tracking & Budgets [Virtual Keys](https://docs.litellm.ai/docs/proxy/virtual_keys)
  * **Load Balancing** : between Multiple Models \+ Deployments of the same model \- LiteLLM proxy can handle 1.5k+ requests/second during load tests.

    
    
    $ pip install 'litellm[proxy]'  
    

## Quick Start - LiteLLM Proxy CLI​

Run the following command to start the litellm proxy
    
    
    $ litellm --model huggingface/bigcode/starcoder  
      
    #INFO: Proxy running on http://0.0.0.0:4000  
    

info

Run with `--detailed_debug` if you need detailed debug logs
    
    
    $ litellm --model huggingface/bigcode/starcoder --detailed_debug  
    

### Test​

In a new shell, run, this will make an `openai.chat.completions` request. Ensure you're using openai v1.0.0+
    
    
    litellm --test  
    

This will now automatically route any requests for gpt-3.5-turbo to bigcode starcoder, hosted on huggingface inference endpoints.

### Supported LLMs​

All LiteLLM supported LLMs are supported on the Proxy. Seel all [supported llms](https://docs.litellm.ai/docs/providers)

  * AWS Bedrock
  * Azure OpenAI
  * OpenAI
  * Ollama
  * OpenAI Compatible Endpoint
  * Vertex AI [Gemini]
  * Huggingface (TGI) Deployed
  * Huggingface (TGI) Local
  * AWS Sagemaker
  * Anthropic
  * VLLM
  * TogetherAI
  * Replicate
  * Petals
  * Palm
  * AI21
  * Cohere

    
    
    $ export AWS_ACCESS_KEY_ID=  
    $ export AWS_REGION_NAME=  
    $ export AWS_SECRET_ACCESS_KEY=  
    
    
    
    $ litellm --model bedrock/anthropic.claude-v2  
    
    
    
    $ export AZURE_API_KEY=my-api-key  
    $ export AZURE_API_BASE=my-api-base  
    
    
    
    $ litellm --model azure/my-deployment-name  
    
    
    
    $ export OPENAI_API_KEY=my-api-key  
    
    
    
    $ litellm --model gpt-3.5-turbo  
    
    
    
    $ litellm --model ollama/<ollama-model-name>  
    
    
    
    $ export OPENAI_API_KEY=my-api-key  
    
    
    
    $ litellm --model openai/<your model name> --api_base <your-api-base> # e.g. http://0.0.0.0:3000  
    
    
    
    $ export VERTEX_PROJECT="hardy-project"  
    $ export VERTEX_LOCATION="us-west"  
    
    
    
    $ litellm --model vertex_ai/gemini-pro  
    
    
    
    $ export HUGGINGFACE_API_KEY=my-api-key #[OPTIONAL]  
    
    
    
    $ litellm --model huggingface/<your model name> --api_base <your-api-base> # e.g. http://0.0.0.0:3000  
    
    
    
    $ litellm --model huggingface/<your model name> --api_base http://0.0.0.0:8001  
    
    
    
    export AWS_ACCESS_KEY_ID=  
    export AWS_REGION_NAME=  
    export AWS_SECRET_ACCESS_KEY=  
    
    
    
    $ litellm --model sagemaker/jumpstart-dft-meta-textgeneration-llama-2-7b  
    
    
    
    $ export ANTHROPIC_API_KEY=my-api-key  
    
    
    
    $ litellm --model claude-instant-1  
    

Assuming you're running vllm locally
    
    
    $ litellm --model vllm/facebook/opt-125m  
    
    
    
    $ export TOGETHERAI_API_KEY=my-api-key  
    
    
    
    $ litellm --model together_ai/lmsys/vicuna-13b-v1.5-16k  
    
    
    
    $ export REPLICATE_API_KEY=my-api-key  
    
    
    
    $ litellm \  
      --model replicate/meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3  
    
    
    
    $ litellm --model petals/meta-llama/Llama-2-70b-chat-hf  
    
    
    
    $ export PALM_API_KEY=my-palm-key  
    
    
    
    $ litellm --model palm/chat-bison  
    
    
    
    $ export AI21_API_KEY=my-api-key  
    
    
    
    $ litellm --model j2-light  
    
    
    
    $ export COHERE_API_KEY=my-api-key  
    
    
    
    $ litellm --model command-nightly  
    

## Quick Start - LiteLLM Proxy + Config.yaml​

The config allows you to create a model list and set `api_base`, `max_tokens` (all litellm params). See more details about the config [here](https://docs.litellm.ai/docs/proxy/configs)

### Create a Config for LiteLLM Proxy​

Example config
    
    
    model_list:   
      - model_name: gpt-3.5-turbo # user-facing model alias  
        litellm_params: # all params accepted by litellm.completion() - https://docs.litellm.ai/docs/completion/input  
          model: azure/<your-deployment-name>  
          api_base: <your-azure-api-endpoint>  
          api_key: <your-azure-api-key>  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: azure/gpt-turbo-small-ca  
          api_base: https://my-endpoint-canada-berri992.openai.azure.com/  
          api_key: <your-azure-api-key>  
      - model_name: vllm-model  
        litellm_params:  
          model: openai/<your-model-name>  
          api_base: <your-vllm-api-base> # e.g. http://0.0.0.0:3000/v1  
          api_key: <your-vllm-api-key|none>  
    

### Run proxy with config​
    
    
    litellm --config your_config.yaml  
    

## Using LiteLLM Proxy - Curl Request, OpenAI Package, Langchain​

info

LiteLLM is compatible with several SDKs - including OpenAI SDK, Anthropic SDK, Mistral SDK, LLamaIndex, Langchain (Js, Python)

[More examples here](/docs/proxy/user_keys)

  * Curl Request
  * OpenAI v1.0.0+
  * Langchain
  * Langchain Embeddings
  * LiteLLM SDK
  * Anthropic Python SDK

    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
    --header 'Content-Type: application/json' \  
    --data ' {  
          "model": "gpt-3.5-turbo",  
          "messages": [  
            {  
              "role": "user",  
              "content": "what llm are you"  
            }  
          ]  
        }  
    '  
    
    
    
    import openai  
    client = openai.OpenAI(  
        api_key="anything",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    # request sent to model set on litellm proxy, `litellm --model`  
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages = [  
        {  
            "role": "user",  
            "content": "this is a test request, write a short poem"  
        }  
    ])  
      
    print(response)  
      
    
    
    
    from langchain.chat_models import ChatOpenAI  
    from langchain.prompts.chat import (  
        ChatPromptTemplate,  
        HumanMessagePromptTemplate,  
        SystemMessagePromptTemplate,  
    )  
    from langchain.schema import HumanMessage, SystemMessage  
      
    chat = ChatOpenAI(  
        openai_api_base="http://0.0.0.0:4000", # set openai_api_base to the LiteLLM Proxy  
        model = "gpt-3.5-turbo",  
        temperature=0.1  
    )  
      
    messages = [  
        SystemMessage(  
            content="You are a helpful assistant that im using to make a test request to."  
        ),  
        HumanMessage(  
            content="test from litellm. tell me why it's amazing in 1 sentence"  
        ),  
    ]  
    response = chat(messages)  
      
    print(response)  
    
    
    
    from langchain.embeddings import OpenAIEmbeddings  
      
    embeddings = OpenAIEmbeddings(model="sagemaker-embeddings", openai_api_base="http://0.0.0.0:4000", openai_api_key="temp-key")  
      
      
    text = "This is a test document."  
      
    query_result = embeddings.embed_query(text)  
      
    print(f"SAGEMAKER EMBEDDINGS")  
    print(query_result[:5])  
      
    embeddings = OpenAIEmbeddings(model="bedrock-embeddings", openai_api_base="http://0.0.0.0:4000", openai_api_key="temp-key")  
      
    text = "This is a test document."  
      
    query_result = embeddings.embed_query(text)  
      
    print(f"BEDROCK EMBEDDINGS")  
    print(query_result[:5])  
      
    embeddings = OpenAIEmbeddings(model="bedrock-titan-embeddings", openai_api_base="http://0.0.0.0:4000", openai_api_key="temp-key")  
      
    text = "This is a test document."  
      
    query_result = embeddings.embed_query(text)  
      
    print(f"TITAN EMBEDDINGS")  
    print(query_result[:5])  
    

This is **not recommended**. There is duplicate logic as the proxy also uses the sdk, which might lead to unexpected errors.
    
    
    from litellm import completion   
      
    response = completion(  
        model="openai/gpt-3.5-turbo",   
        messages = [  
            {  
                "role": "user",  
                "content": "this is a test request, write a short poem"  
            }  
        ],   
        api_key="anything",   
        base_url="http://0.0.0.0:4000"  
        )  
      
    print(response)  
      
    
    
    
    import os  
      
    from anthropic import Anthropic  
      
    client = Anthropic(  
        base_url="http://localhost:4000", # proxy endpoint  
        api_key="sk-s4xN1IiLTCytwtZFJaYQrA", # litellm proxy virtual key  
    )  
      
    message = client.messages.create(  
        max_tokens=1024,  
        messages=[  
            {  
                "role": "user",  
                "content": "Hello, Claude",  
            }  
        ],  
        model="claude-3-opus-20240229",  
    )  
    print(message.content)  
    

[**More Info**](/docs/proxy/configs)

## 📖 Proxy Endpoints - [Swagger Docs](https://litellm-api.up.railway.app/)​

  * POST `/chat/completions` \- chat completions endpoint to call 100+ LLMs
  * POST `/completions` \- completions endpoint
  * POST `/embeddings` \- embedding endpoint for Azure, OpenAI, Huggingface endpoints
  * GET `/models` \- available models on server
  * POST `/key/generate` \- generate a key to access the proxy

## Debugging Proxy​

Events that occur during normal operation
    
    
    litellm --model gpt-3.5-turbo --debug  
    

Detailed information
    
    
    litellm --model gpt-3.5-turbo --detailed_debug  
    

### Set Debug Level using env variables​

Events that occur during normal operation
    
    
    export LITELLM_LOG=INFO  
    

Detailed information
    
    
    export LITELLM_LOG=DEBUG  
    

No Logs
    
    
    export LITELLM_LOG=None  
    

  * Quick Start - LiteLLM Proxy CLI
    * Test
    * Supported LLMs
  * Quick Start - LiteLLM Proxy + Config.yaml
    * Create a Config for LiteLLM Proxy
    * Run proxy with config
  * Using LiteLLM Proxy - Curl Request, OpenAI Package, Langchain
  * 📖 Proxy Endpoints - Swagger Docs
  * Debugging Proxy
    * Set Debug Level using env variables