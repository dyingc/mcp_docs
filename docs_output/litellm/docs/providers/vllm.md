# VLLM | liteLLM

On this page

LiteLLM supports all models on VLLM.

Property| Details  
---|---  
Description| vLLM is a fast and easy-to-use library for LLM inference and serving. [Docs](https://docs.vllm.ai/en/latest/index.html)  
Provider Route on LiteLLM| `hosted_vllm/` (for OpenAI compatible server), `vllm/` (for vLLM sdk usage)  
Provider Doc| [vLLM ↗](https://docs.vllm.ai/en/latest/index.html)  
Supported Endpoints| `/chat/completions`, `/embeddings`, `/completions`  
  
# Quick Start

## Usage - litellm.completion (calling OpenAI compatible endpoint)​

vLLM Provides an OpenAI compatible endpoints - here's how to call it with LiteLLM

In order to use litellm to call a hosted vllm server add the following to your completion call

  * `model="hosted_vllm/<your-vllm-model-name>"`
  * `api_base = "your-hosted-vllm-server"`

    
    
    import litellm   
      
    response = litellm.completion(  
                model="hosted_vllm/facebook/opt-125m", # pass the vllm model name  
                messages=messages,  
                api_base="https://hosted-vllm-api.co",  
                temperature=0.2,  
                max_tokens=80)  
      
    print(response)  
    

## Usage - LiteLLM Proxy Server (calling OpenAI compatible endpoint)​

Here's how to call an OpenAI-Compatible Endpoint with the LiteLLM Proxy Server

  1. Modify the config.yaml

    
    
    model_list:  
      - model_name: my-model  
        litellm_params:  
          model: hosted_vllm/facebook/opt-125m  # add hosted_vllm/ prefix to route as OpenAI provider  
          api_base: https://hosted-vllm-api.co      # add api base for OpenAI compatible provider  
    

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
    

## Embeddings​

  * SDK
  * PROXY

    
    
    from litellm import embedding     
    import os  
      
    os.environ["HOSTED_VLLM_API_BASE"] = "http://localhost:8000"  
      
      
    embedding = embedding(model="hosted_vllm/facebook/opt-125m", input=["Hello world"])  
      
    print(embedding)  
    

  1. Setup config.yaml

    
    
    model_list:  
        - model_name: my-model  
          litellm_params:  
            model: hosted_vllm/facebook/opt-125m  # add hosted_vllm/ prefix to route as OpenAI provider  
            api_base: https://hosted-vllm-api.co      # add api base for OpenAI compatible provider  
    

  2. Start the proxy

    
    
    $ litellm --config /path/to/config.yaml  
      
    # RUNNING on http://0.0.0.0:4000  
    

  3. Test it!

    
    
    curl -L -X POST 'http://0.0.0.0:4000/embeddings' \  
    -H 'Authorization: Bearer sk-1234' \  
    -H 'Content-Type: application/json' \  
    -d '{"input": ["hello world"], "model": "my-model"}'  
    

[See OpenAI SDK/Langchain/etc. examples](/docs/proxy/user_keys#embeddings)

## Send Video URL to VLLM​

Example Implementation from VLLM [here](https://github.com/vllm-project/vllm/pull/10020)

  * (Unified) Files Message
  * (VLLM-specific) Video Message

Use this to send a video url to VLLM + Gemini in the same format, using OpenAI's `files` message type.

There are two ways to send a video url to VLLM:

  1. Pass the video url directly

    
    
    {"type": "file", "file": {"file_id": video_url}},  
    

  2. Pass the video data as base64

    
    
    {"type": "file", "file": {"file_data": f"data:video/mp4;base64,{video_data_base64}"}}  
    

  * SDK
  * PROXY

    
    
    from litellm import completion  
      
    messages=[  
        {  
            "role": "user",  
            "content": [  
                {  
                    "type": "text",  
                    "text": "Summarize the following video"  
                },  
                {  
                    "type": "file",  
                    "file": {  
                        "file_id": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  
                    }  
                }  
            ]  
        }  
    ]  
      
    # call vllm   
    os.environ["HOSTED_VLLM_API_BASE"] = "https://hosted-vllm-api.co"  
    os.environ["HOSTED_VLLM_API_KEY"] = "" # [optional], if your VLLM server requires an API key  
    response = completion(  
        model="hosted_vllm/qwen", # pass the vllm model name  
        messages=messages,  
    )  
      
    # call gemini   
    os.environ["GEMINI_API_KEY"] = "your-gemini-api-key"  
    response = completion(  
        model="gemini/gemini-1.5-flash", # pass the gemini model name  
        messages=messages,  
    )  
      
    print(response)  
    

  1. Setup config.yaml

    
    
    model_list:  
        - model_name: my-model  
          litellm_params:  
            model: hosted_vllm/qwen  # add hosted_vllm/ prefix to route as OpenAI provider  
            api_base: https://hosted-vllm-api.co      # add api base for OpenAI compatible provider  
        - model_name: my-gemini-model  
          litellm_params:  
            model: gemini/gemini-1.5-flash  # add gemini/ prefix to route as Google AI Studio provider  
            api_key: os.environ/GEMINI_API_KEY  
    

  2. Start the proxy

    
    
    $ litellm --config /path/to/config.yaml  
      
    # RUNNING on http://0.0.0.0:4000  
    

  3. Test it!

    
    
    curl -X POST http://0.0.0.0:4000/chat/completions \  
    -H "Authorization: Bearer sk-1234" \  
    -H "Content-Type: application/json" \  
    -d '{  
        "model": "my-model",  
        "messages": [  
            {"role": "user", "content":   
                [  
                    {"type": "text", "text": "Summarize the following video"},  
                    {"type": "file", "file": {"file_id": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}}  
                ]  
            }  
        ]  
    }'  
    

Use this to send a video url to VLLM in it's native message format (`video_url`).

There are two ways to send a video url to VLLM:

  1. Pass the video url directly

    
    
    {"type": "video_url", "video_url": {"url": video_url}},  
    

  2. Pass the video data as base64

    
    
    {"type": "video_url", "video_url": {"url": f"data:video/mp4;base64,{video_data_base64}"}}  
    

  * SDK
  * PROXY

    
    
    from litellm import completion  
      
    response = completion(  
                model="hosted_vllm/qwen", # pass the vllm model name  
                messages=[  
                    {  
                        "role": "user",  
                        "content": [  
                            {  
                                "type": "text",  
                                "text": "Summarize the following video"  
                            },  
                            {  
                                "type": "video_url",  
                                "video_url": {  
                                    "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  
                                }  
                            }  
                        ]  
                    }  
                ],  
                api_base="https://hosted-vllm-api.co")  
      
    print(response)  
    

  1. Setup config.yaml

    
    
    model_list:  
        - model_name: my-model  
          litellm_params:  
            model: hosted_vllm/qwen  # add hosted_vllm/ prefix to route as OpenAI provider  
            api_base: https://hosted-vllm-api.co      # add api base for OpenAI compatible provider  
    

  2. Start the proxy

    
    
    $ litellm --config /path/to/config.yaml  
      
    # RUNNING on http://0.0.0.0:4000  
    

  3. Test it!

    
    
    curl -X POST http://0.0.0.0:4000/chat/completions \  
    -H "Authorization: Bearer sk-1234" \  
    -H "Content-Type: application/json" \  
    -d '{  
        "model": "my-model",  
        "messages": [  
            {"role": "user", "content":   
                [  
                    {"type": "text", "text": "Summarize the following video"},  
                    {"type": "video_url", "video_url": {"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}}  
                ]  
            }  
        ]  
    }'  
    

## (Deprecated) for `vllm pip package`​

### Using - `litellm.completion`​
    
    
    pip install litellm vllm  
    
    
    
    import litellm   
      
    response = litellm.completion(  
                model="vllm/facebook/opt-125m", # add a vllm prefix so litellm knows the custom_llm_provider==vllm  
                messages=messages,  
                temperature=0.2,  
                max_tokens=80)  
      
    print(response)  
    

### Batch Completion​
    
    
    from litellm import batch_completion  
      
    model_name = "facebook/opt-125m"  
    provider = "vllm"  
    messages = [[{"role": "user", "content": "Hey, how's it going"}] for _ in range(5)]  
      
    response_list = batch_completion(  
                model=model_name,   
                custom_llm_provider=provider, # can easily switch to huggingface, replicate, together ai, sagemaker, etc.  
                messages=messages,  
                temperature=0.2,  
                max_tokens=80,  
            )  
    print(response_list)  
    

### Prompt Templates​

For models with special prompt templates (e.g. Llama2), we format the prompt to fit their template.

**What if we don't support a model you need?** You can also specify you're own custom prompt formatting, in case we don't have your model covered yet.

**Does this mean you have to specify a prompt for all models?** No. By default we'll concatenate your message content to make a prompt (expected format for Bloom, T-5, Llama-2 base models, etc.)

**Default Prompt Template**
    
    
    def default_pt(messages):  
        return " ".join(message["content"] for message in messages)  
    

[Code for how prompt templates work in LiteLLM](https://github.com/BerriAI/litellm/blob/main/litellm/llms/prompt_templates/factory.py)

#### Models we already have Prompt Templates for​

Model Name| Works for Models| Function Call  
---|---|---  
meta-llama/Llama-2-7b-chat| All meta-llama llama2 chat models| `completion(model='vllm/meta-llama/Llama-2-7b', messages=messages, api_base="your_api_endpoint")`  
tiiuae/falcon-7b-instruct| All falcon instruct models| `completion(model='vllm/tiiuae/falcon-7b-instruct', messages=messages, api_base="your_api_endpoint")`  
mosaicml/mpt-7b-chat| All mpt chat models| `completion(model='vllm/mosaicml/mpt-7b-chat', messages=messages, api_base="your_api_endpoint")`  
codellama/CodeLlama-34b-Instruct-hf| All codellama instruct models| `completion(model='vllm/codellama/CodeLlama-34b-Instruct-hf', messages=messages, api_base="your_api_endpoint")`  
WizardLM/WizardCoder-Python-34B-V1.0| All wizardcoder models| `completion(model='vllm/WizardLM/WizardCoder-Python-34B-V1.0', messages=messages, api_base="your_api_endpoint")`  
Phind/Phind-CodeLlama-34B-v2| All phind-codellama models| `completion(model='vllm/Phind/Phind-CodeLlama-34B-v2', messages=messages, api_base="your_api_endpoint")`  
  
#### Custom prompt templates​
    
    
    # Create your own custom prompt template works   
    litellm.register_prompt_template(  
    	model="togethercomputer/LLaMA-2-7B-32K",  
    	roles={  
                "system": {  
                    "pre_message": "[INST] <<SYS>>\n",  
                    "post_message": "\n<</SYS>>\n [/INST]\n"  
                },  
                "user": {   
                    "pre_message": "[INST] ",  
                    "post_message": " [/INST]\n"  
                },   
                "assistant": {  
                    "pre_message": "\n",  
                    "post_message": "\n",  
                }  
            } # tell LiteLLM how you want to map the openai messages to this model  
    )  
      
    def test_vllm_custom_model():  
        model = "vllm/togethercomputer/LLaMA-2-7B-32K"  
        response = completion(model=model, messages=messages)  
        print(response['choices'][0]['message']['content'])  
        return response  
      
    test_vllm_custom_model()  
    

[Implementation Code](https://github.com/BerriAI/litellm/blob/6b3cb1898382f2e4e80fd372308ea232868c78d1/litellm/utils.py#L1414)

  * Usage - litellm.completion (calling OpenAI compatible endpoint)
  * Usage - LiteLLM Proxy Server (calling OpenAI compatible endpoint)
  * Embeddings
  * Send Video URL to VLLM
  * (Deprecated) for `vllm pip package`
    * Using - `litellm.completion`
    * Batch Completion
    * Prompt Templates