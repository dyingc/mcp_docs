# Langchain, OpenAI SDK, LlamaIndex, Instructor, Curl examples | liteLLM

On this page

LiteLLM Proxy is **OpenAI-Compatible** , and supports:

  * /chat/completions
  * /embeddings
  * /completions
  * /image/generations
  * /moderations
  * /audio/transcriptions
  * /audio/speech
  * [Assistants API endpoints](https://docs.litellm.ai/docs/assistants)
  * [Batches API endpoints](https://docs.litellm.ai/docs/batches)
  * [Fine-Tuning API endpoints](https://docs.litellm.ai/docs/fine_tuning)

LiteLLM Proxy is **Azure OpenAI-compatible** :

  * /chat/completions
  * /completions
  * /embeddings

LiteLLM Proxy is **Anthropic-compatible** :

  * /messages

LiteLLM Proxy is **Vertex AI compatible** :

  * [Supports ALL Vertex Endpoints](/docs/vertex_ai)

This doc covers:

  * /chat/completion
  * /embedding

These are **selected examples**. LiteLLM Proxy is **OpenAI-Compatible** , it works with any project that calls OpenAI. Just change the `base_url`, `api_key` and `model`.

To pass provider-specific args, [go here](https://docs.litellm.ai/docs/completion/provider_specific_params#proxy-usage)

To drop unsupported params (E.g. frequency_penalty for bedrock with librechat), [go here](https://docs.litellm.ai/docs/completion/drop_params#openai-proxy-usage)

info

**Input, Output, Exceptions are mapped to the OpenAI format for all supported models**

How to send requests to the proxy, pass metadata, allow users to pass in their OpenAI API key

## `/chat/completions`​

### Request Format​

  * OpenAI Python v1.0.0+
  * AzureOpenAI Python
  * LlamaIndex
  * Curl Request
  * Langchain
  * Langchain JS
  * OpenAI JS
  * Anthropic Python SDK
  * Mistral Python SDK
  * Instructor

Set `extra_body={"metadata": { }}` to `metadata` you want to pass
    
    
    import openai  
    client = openai.OpenAI(  
        api_key="anything",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    # request sent to model set on litellm proxy, `litellm --model`  
    response = client.chat.completions.create(  
        model="gpt-3.5-turbo",  
        messages = [  
            {  
                "role": "user",  
                "content": "this is a test request, write a short poem"  
            }  
        ],  
        extra_body={ # pass in any provider-specific param, if not supported by openai, https://docs.litellm.ai/docs/completion/input#provider-specific-params  
            "metadata": { # 👈 use for logging additional params (e.g. to langfuse)  
                "generation_name": "ishaan-generation-openai-client",  
                "generation_id": "openai-client-gen-id22",  
                "trace_id": "openai-client-trace-id22",  
                "trace_user_id": "openai-client-user-id2"  
            }  
        }  
    )  
      
    print(response)  
    

Set `extra_body={"metadata": { }}` to `metadata` you want to pass
    
    
    import openai  
    client = openai.AzureOpenAI(  
        api_key="anything",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    # request sent to model set on litellm proxy, `litellm --model`  
    response = client.chat.completions.create(  
        model="gpt-3.5-turbo",  
        messages = [  
            {  
                "role": "user",  
                "content": "this is a test request, write a short poem"  
            }  
        ],  
        extra_body={ # pass in any provider-specific param, if not supported by openai, https://docs.litellm.ai/docs/completion/input#provider-specific-params  
            "metadata": { # 👈 use for logging additional params (e.g. to langfuse)  
                "generation_name": "ishaan-generation-openai-client",  
                "generation_id": "openai-client-gen-id22",  
                "trace_id": "openai-client-trace-id22",  
                "trace_user_id": "openai-client-user-id2"  
            }  
        }  
    )  
      
    print(response)  
    
    
    
    import os, dotenv  
      
    from llama_index.llms import AzureOpenAI  
    from llama_index.embeddings import AzureOpenAIEmbedding  
    from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext  
      
    llm = AzureOpenAI(  
        engine="azure-gpt-3.5",               # model_name on litellm proxy  
        temperature=0.0,  
        azure_endpoint="http://0.0.0.0:4000", # litellm proxy endpoint  
        api_key="sk-1234",                    # litellm proxy API Key  
        api_version="2023-07-01-preview",  
    )  
      
    embed_model = AzureOpenAIEmbedding(  
        deployment_name="azure-embedding-model",  
        azure_endpoint="http://0.0.0.0:4000",  
        api_key="sk-1234",  
        api_version="2023-07-01-preview",  
    )  
      
      
    documents = SimpleDirectoryReader("llama_index_data").load_data()  
    service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)  
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)  
      
    query_engine = index.as_query_engine()  
    response = query_engine.query("What did the author do growing up?")  
    print(response)  
      
    

Pass `metadata` as part of the request body
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "gpt-3.5-turbo",  
        "messages": [  
            {  
            "role": "user",  
            "content": "what llm are you"  
            }  
        ],  
        "metadata": {  
            "generation_name": "ishaan-test-generation",  
            "generation_id": "gen-id22",  
            "trace_id": "trace-id22",  
            "trace_user_id": "user-id2"  
        }  
    }'  
    
    
    
    from langchain.chat_models import ChatOpenAI  
    from langchain.prompts.chat import (  
        ChatPromptTemplate,  
        HumanMessagePromptTemplate,  
        SystemMessagePromptTemplate,  
    )  
    from langchain.schema import HumanMessage, SystemMessage  
    import os   
      
    os.environ["OPENAI_API_KEY"] = "anything"  
      
    chat = ChatOpenAI(  
        openai_api_base="http://0.0.0.0:4000",  
        model = "gpt-3.5-turbo",  
        temperature=0.1,  
        extra_body={  
            "metadata": {  
                "generation_name": "ishaan-generation-langchain-client",  
                "generation_id": "langchain-client-gen-id22",  
                "trace_id": "langchain-client-trace-id22",  
                "trace_user_id": "langchain-client-user-id2"  
            }  
        }  
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
    
    
    
    import { ChatOpenAI } from "@langchain/openai";  
      
      
    const model = new ChatOpenAI({  
      modelName: "gpt-4",  
      openAIApiKey: "sk-1234",  
      modelKwargs: {"metadata": "hello world"} // 👈 PASS Additional params here  
    }, {  
      basePath: "http://0.0.0.0:4000",  
    });  
      
    const message = await model.invoke("Hi there!");  
      
    console.log(message);  
      
    
    
    
    const { OpenAI } = require('openai');  
      
    const openai = new OpenAI({  
      apiKey: "sk-1234", // This is the default and can be omitted  
      baseURL: "http://0.0.0.0:4000"  
    });  
      
    async function main() {  
      const chatCompletion = await openai.chat.completions.create({  
        messages: [{ role: 'user', content: 'Say this is a test' }],  
        model: 'gpt-3.5-turbo',  
      }, {"metadata": {  
                "generation_name": "ishaan-generation-openaijs-client",  
                "generation_id": "openaijs-client-gen-id22",  
                "trace_id": "openaijs-client-trace-id22",  
                "trace_user_id": "openaijs-client-user-id2"  
            }});  
    }  
      
    main();  
      
    
    
    
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
    
    
    
    import os  
    from mistralai.client import MistralClient  
    from mistralai.models.chat_completion import ChatMessage  
      
      
    client = MistralClient(api_key="sk-1234", endpoint="http://0.0.0.0:4000")  
    chat_response = client.chat(  
        model="mistral-small-latest",  
        messages=[  
            {"role": "user", "content": "this is a test request, write a short poem"}  
        ],  
    )  
    print(chat_response.choices[0].message.content)  
    
    
    
    from openai import OpenAI  
    import instructor  
    from pydantic import BaseModel  
      
    my_proxy_api_key = "" # e.g. sk-1234 - LITELLM KEY  
    my_proxy_base_url = "" # e.g. http://0.0.0.0:4000 - LITELLM PROXY BASE URL  
      
    # This enables response_model keyword  
    # from client.chat.completions.create  
    ## WORKS ACROSS OPENAI/ANTHROPIC/VERTEXAI/ETC. - all LITELLM SUPPORTED MODELS!  
    client = instructor.from_openai(OpenAI(api_key=my_proxy_api_key, base_url=my_proxy_base_url))  
      
    class UserDetail(BaseModel):  
        name: str  
        age: int  
      
    user = client.chat.completions.create(  
        model="gemini-pro-flash",  
        response_model=UserDetail,  
        messages=[  
            {"role": "user", "content": "Extract Jason is 25 years old"},  
        ]  
    )  
      
    assert isinstance(user, UserDetail)  
    assert user.name == "Jason"  
    assert user.age == 25  
    

### Response Format​
    
    
    {  
      "id": "chatcmpl-8c5qbGTILZa1S4CK3b31yj5N40hFN",  
      "choices": [  
        {  
          "finish_reason": "stop",  
          "index": 0,  
          "message": {  
            "content": "As an AI language model, I do not have a physical form or personal preferences. However, I am programmed to assist with various topics and provide information on a wide range of subjects. Is there something specific you would like assistance with?",  
            "role": "assistant"  
          }  
        }  
      ],  
      "created": 1704089632,  
      "model": "gpt-35-turbo",  
      "object": "chat.completion",  
      "system_fingerprint": null,  
      "usage": {  
        "completion_tokens": 47,  
        "prompt_tokens": 12,  
        "total_tokens": 59  
      },  
      "_response_ms": 1753.426  
    }  
      
    

### **Streaming**​

  * curl
  * SDK

    
    
    curl http://0.0.0.0:4000/v1/chat/completions \  
    -H "Content-Type: application/json" \  
    -H "Authorization: Bearer $OPTIONAL_YOUR_PROXY_KEY" \  
    -d '{  
      "model": "gpt-4-turbo",  
      "messages": [  
        {  
          "role": "user",  
          "content": "this is a test request, write a short poem"  
        }  
      ],  
      "stream": true  
    }'  
    
    
    
    from openai import OpenAI  
    client = OpenAI(  
        api_key="sk-1234", # [OPTIONAL] set if you set one on proxy, else set ""  
        base_url="http://0.0.0.0:4000",  
    )  
      
    messages = [{"role": "user", "content": "this is a test request, write a short poem"}]  
    completion = client.chat.completions.create(  
      model="gpt-4o",  
      messages=messages,  
      stream=True  
    )  
      
    print(completion)  
      
    

### Function Calling​

Here's some examples of doing function calling with the proxy.

You can use the proxy for function calling with **any** openai-compatible project.

  * curl
  * SDK

    
    
    curl http://0.0.0.0:4000/v1/chat/completions \  
    -H "Content-Type: application/json" \  
    -H "Authorization: Bearer $OPTIONAL_YOUR_PROXY_KEY" \  
    -d '{  
      "model": "gpt-4-turbo",  
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
    
    
    
    from openai import OpenAI  
    client = OpenAI(  
        api_key="sk-1234", # [OPTIONAL] set if you set one on proxy, else set ""  
        base_url="http://0.0.0.0:4000",  
    )  
      
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
        }  
      }  
    ]  
    messages = [{"role": "user", "content": "What's the weather like in Boston today?"}]  
    completion = client.chat.completions.create(  
      model="gpt-4o", # use 'model_name' from config.yaml  
      messages=messages,  
      tools=tools,  
      tool_choice="auto"  
    )  
      
    print(completion)  
      
    

## `/embeddings`​

### Request Format​

Input, Output and Exceptions are mapped to the OpenAI format for all supported models

  * OpenAI Python v1.0.0+
  * Curl Request
  * Langchain Embeddings

    
    
    import openai  
    from openai import OpenAI  
      
    # set base_url to your proxy server  
    # set api_key to send to proxy server  
    client = OpenAI(api_key="<proxy-api-key>", base_url="http://0.0.0.0:4000")  
      
    response = client.embeddings.create(  
        input=["hello from litellm"],  
        model="text-embedding-ada-002"  
    )  
      
    print(response)  
      
    
    
    
    curl --location 'http://0.0.0.0:4000/embeddings' \  
      --header 'Content-Type: application/json' \  
      --data ' {  
      "model": "text-embedding-ada-002",  
      "input": ["write a litellm poem"]  
      }'  
    
    
    
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
    

### Response Format​
    
    
    {  
      "object": "list",  
      "data": [  
        {  
          "object": "embedding",  
          "embedding": [  
            0.0023064255,  
            -0.009327292,  
            ....   
            -0.0028842222,  
          ],  
          "index": 0  
        }  
      ],  
      "model": "text-embedding-ada-002",  
      "usage": {  
        "prompt_tokens": 8,  
        "total_tokens": 8  
      }  
    }  
      
    

## `/moderations`​

### Request Format​

Input, Output and Exceptions are mapped to the OpenAI format for all supported models

  * OpenAI Python v1.0.0+
  * Curl Request

    
    
    import openai  
    from openai import OpenAI  
      
    # set base_url to your proxy server  
    # set api_key to send to proxy server  
    client = OpenAI(api_key="<proxy-api-key>", base_url="http://0.0.0.0:4000")  
      
    response = client.moderations.create(  
        input="hello from litellm",  
        model="text-moderation-stable"  
    )  
      
    print(response)  
      
    
    
    
    curl --location 'http://0.0.0.0:4000/moderations' \  
        --header 'Content-Type: application/json' \  
        --header 'Authorization: Bearer sk-1234' \  
        --data '{"input": "Sample text goes here", "model": "text-moderation-stable"}'  
    

### Response Format​
    
    
    {  
      "id": "modr-8sFEN22QCziALOfWTa77TodNLgHwA",  
      "model": "text-moderation-007",  
      "results": [  
        {  
          "categories": {  
            "harassment": false,  
            "harassment/threatening": false,  
            "hate": false,  
            "hate/threatening": false,  
            "self-harm": false,  
            "self-harm/instructions": false,  
            "self-harm/intent": false,  
            "sexual": false,  
            "sexual/minors": false,  
            "violence": false,  
            "violence/graphic": false  
          },  
          "category_scores": {  
            "harassment": 0.000019947197870351374,  
            "harassment/threatening": 5.5971017900446896e-6,  
            "hate": 0.000028560316422954202,  
            "hate/threatening": 2.2631787999216613e-8,  
            "self-harm": 2.9121162015144364e-7,  
            "self-harm/instructions": 9.314219084899378e-8,  
            "self-harm/intent": 8.093739012338119e-8,  
            "sexual": 0.00004414955765241757,  
            "sexual/minors": 0.0000156943697220413,  
            "violence": 0.00022354527027346194,  
            "violence/graphic": 8.804164281173144e-6  
          },  
          "flagged": false  
        }  
      ]  
    }  
    

## Using with OpenAI compatible projects​

Set `base_url` to the LiteLLM Proxy server

  * OpenAI v1.0.0+
  * LibreChat
  * ContinueDev
  * Aider
  * AutoGen
  * guidance

    
    
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
      
    

#### Start the LiteLLM proxy​
    
    
    litellm --model gpt-3.5-turbo  
      
    #INFO: Proxy running on http://0.0.0.0:4000  
    

#### 1\. Clone the repo​
    
    
    git clone https://github.com/danny-avila/LibreChat.git  
    

#### 2\. Modify Librechat's `docker-compose.yml`​

LiteLLM Proxy is running on port `4000`, set `4000` as the proxy below
    
    
    OPENAI_REVERSE_PROXY=http://host.docker.internal:4000/v1/chat/completions  
    

#### 3\. Save fake OpenAI key in Librechat's `.env`​

Copy Librechat's `.env.example` to `.env` and overwrite the default OPENAI_API_KEY (by default it requires the user to pass a key).
    
    
    OPENAI_API_KEY=sk-1234  
    

#### 4\. Run LibreChat:​
    
    
    docker compose up  
    

Continue-Dev brings ChatGPT to VSCode. See how to [install it here](https://continue.dev/docs/quickstart).

In the [config.py](https://continue.dev/docs/reference/Models/openai) set this as your default model.
    
    
      default=OpenAI(  
          api_key="IGNORED",  
          model="fake-model-name",  
          context_length=2048, # customize if needed for your model  
          api_base="http://localhost:4000" # your proxy server url  
      ),  
    

Credits [@vividfog](https://github.com/ollama/ollama/issues/305#issuecomment-1751848077) for this tutorial.
    
    
    $ pip install aider   
      
    $ aider --openai-api-base http://0.0.0.0:4000 --openai-api-key fake-key  
    
    
    
    pip install pyautogen  
    
    
    
    from autogen import AssistantAgent, UserProxyAgent, oai  
    config_list=[  
        {  
            "model": "my-fake-model",  
            "api_base": "http://localhost:4000",  #litellm compatible endpoint  
            "api_type": "open_ai",  
            "api_key": "NULL", # just a placeholder  
        }  
    ]  
      
    response = oai.Completion.create(config_list=config_list, prompt="Hi")  
    print(response) # works fine  
      
    llm_config={  
        "config_list": config_list,  
    }  
      
    assistant = AssistantAgent("assistant", llm_config=llm_config)  
    user_proxy = UserProxyAgent("user_proxy")  
    user_proxy.initiate_chat(assistant, message="Plot a chart of META and TESLA stock price change YTD.", config_list=config_list)  
    

Credits [@victordibia](https://github.com/microsoft/autogen/issues/45#issuecomment-1749921972) for this tutorial.

A guidance language for controlling large language models. <https://github.com/guidance-ai/guidance>

**NOTE:** Guidance sends additional params like `stop_sequences` which can cause some models to fail if they don't support it.

**Fix** : Start your proxy using the `--drop_params` flag
    
    
    litellm --model ollama/codellama --temperature 0.3 --max_tokens 2048 --drop_params  
    
    
    
    import guidance  
      
    # set api_base to your proxy  
    # set api_key to anything  
    gpt4 = guidance.llms.OpenAI("gpt-4", api_base="http://0.0.0.0:4000", api_key="anything")  
      
    experts = guidance('''  
    {{#system~}}  
    You are a helpful and terse assistant.  
    {{~/system}}  
      
    {{#user~}}  
    I want a response to the following question:  
    {{query}}  
    Name 3 world-class experts (past or present) who would be great at answering this?  
    Don't answer the question yet.  
    {{~/user}}  
      
    {{#assistant~}}  
    {{gen 'expert_names' temperature=0 max_tokens=300}}  
    {{~/assistant}}  
    ''', llm=gpt4)  
      
    result = experts(query='How can I be more productive?')  
    print(result)  
    

## Using with Vertex, Boto3, Anthropic SDK (Native format)​

👉 **[Here's how to use litellm proxy with Vertex, boto3, Anthropic SDK - in the native format](/docs/pass_through/vertex_ai)**

## Advanced​

### (BETA) Batch Completions - pass multiple models​

Use this when you want to send 1 request to N Models

#### Expected Request Format​

Pass model as a string of comma separated value of models. Example `"model"="llama3,gpt-3.5-turbo"`

This same request will be sent to the following model groups on the [litellm proxy config.yaml](https://docs.litellm.ai/docs/proxy/configs)

  * `model_name="llama3"`
  * `model_name="gpt-3.5-turbo"`

  * OpenAI Python SDK
  * Curl

    
    
    import openai  
      
    client = openai.OpenAI(api_key="sk-1234", base_url="http://0.0.0.0:4000")  
      
    response = client.chat.completions.create(  
        model="gpt-3.5-turbo,llama3",  
        messages=[  
            {"role": "user", "content": "this is a test request, write a short poem"}  
        ],  
    )  
      
    print(response)  
    

#### Expected Response Format​

Get a list of responses when `model` is passed as a list
    
    
    [  
        ChatCompletion(  
            id='chatcmpl-9NoYhS2G0fswot0b6QpoQgmRQMaIf',  
            choices=[  
                Choice(  
                    finish_reason='stop',  
                    index=0,  
                    logprobs=None,  
                    message=ChatCompletionMessage(  
                        content='In the depths of my soul, a spark ignites\nA light that shines so pure and bright\nIt dances and leaps, refusing to die\nA flame of hope that reaches the sky\n\nIt warms my heart and fills me with bliss\nA reminder that in darkness, there is light to kiss\nSo I hold onto this fire, this guiding light\nAnd let it lead me through the darkest night.',  
                        role='assistant',  
                        function_call=None,  
                        tool_calls=None  
                    )  
                )  
            ],  
            created=1715462919,  
            model='gpt-3.5-turbo-0125',  
            object='chat.completion',  
            system_fingerprint=None,  
            usage=CompletionUsage(  
                completion_tokens=83,  
                prompt_tokens=17,  
                total_tokens=100  
            )  
        ),  
        ChatCompletion(  
            id='chatcmpl-4ac3e982-da4e-486d-bddb-ed1d5cb9c03c',  
            choices=[  
                Choice(  
                    finish_reason='stop',  
                    index=0,  
                    logprobs=None,  
                    message=ChatCompletionMessage(  
                        content="A test request, and I'm delighted!\nHere's a short poem, just for you:\n\nMoonbeams dance upon the sea,\nA path of light, for you to see.\nThe stars up high, a twinkling show,\nA night of wonder, for all to know.\n\nThe world is quiet, save the night,\nA peaceful hush, a gentle light.\nThe world is full, of beauty rare,\nA treasure trove, beyond compare.\n\nI hope you enjoyed this little test,\nA poem born, of whimsy and jest.\nLet me know, if there's anything else!",  
                        role='assistant',  
                        function_call=None,  
                        tool_calls=None  
                    )  
                )  
            ],  
            created=1715462919,  
            model='groq/llama3-8b-8192',  
            object='chat.completion',  
            system_fingerprint='fp_a2c8d063cb',  
            usage=CompletionUsage(  
                completion_tokens=120,  
                prompt_tokens=20,  
                total_tokens=140  
            )  
        )  
    ]  
    
    
    
    curl --location 'http://localhost:4000/chat/completions' \  
        --header 'Authorization: Bearer sk-1234' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "llama3,gpt-3.5-turbo",  
        "max_tokens": 10,  
        "user": "litellm2",  
        "messages": [  
            {  
            "role": "user",  
            "content": "is litellm getting better"  
            }  
        ]  
    }'  
    

#### Expected Response Format​

Get a list of responses when `model` is passed as a list
    
    
    [  
      {  
        "id": "chatcmpl-3dbd5dd8-7c82-4ca3-bf1f-7c26f497cf2b",  
        "choices": [  
          {  
            "finish_reason": "length",  
            "index": 0,  
            "message": {  
              "content": "The Elder Scrolls IV: Oblivion!\n\nReleased",  
              "role": "assistant"  
            }  
          }  
        ],  
        "created": 1715459876,  
        "model": "groq/llama3-8b-8192",  
        "object": "chat.completion",  
        "system_fingerprint": "fp_179b0f92c9",  
        "usage": {  
          "completion_tokens": 10,  
          "prompt_tokens": 12,  
          "total_tokens": 22  
        }  
      },  
      {  
        "id": "chatcmpl-9NnldUfFLmVquFHSX4yAtjCw8PGei",  
        "choices": [  
          {  
            "finish_reason": "length",  
            "index": 0,  
            "message": {  
              "content": "TES4 could refer to The Elder Scrolls IV:",  
              "role": "assistant"  
            }  
          }  
        ],  
        "created": 1715459877,  
        "model": "gpt-3.5-turbo-0125",  
        "object": "chat.completion",  
        "system_fingerprint": null,  
        "usage": {  
          "completion_tokens": 10,  
          "prompt_tokens": 9,  
          "total_tokens": 19  
        }  
      }  
    ]  
    

  * `/chat/completions`
    * Request Format
    * Response Format
    * **Streaming**
    * Function Calling
  * `/embeddings`
    * Request Format
    * Response Format
  * `/moderations`
    * Request Format
    * Response Format
  * Using with OpenAI compatible projects
  * Using with Vertex, Boto3, Anthropic SDK (Native format)
  * Advanced
    * (BETA) Batch Completions - pass multiple models