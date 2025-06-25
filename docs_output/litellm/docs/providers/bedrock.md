# AWS Bedrock | liteLLM

On this page

ALL Bedrock models (Anthropic, Meta, Deepseek, Mistral, Amazon, etc.) are Supported

Property| Details  
---|---  
Description| Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs).  
Provider Route on LiteLLM| `bedrock/`, `bedrock/converse/`, `bedrock/invoke/`, `bedrock/converse_like/`, `bedrock/llama/`, `bedrock/deepseek_r1/`  
Provider Doc| [Amazon Bedrock ↗](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)  
Supported OpenAI Endpoints| `/chat/completions`, `/completions`, `/embeddings`, `/images/generations`  
Rerank Endpoint| `/rerank`  
Pass-through Endpoint| [Supported](/docs/pass_through/bedrock)  
  
LiteLLM requires `boto3` to be installed on your system for Bedrock requests
    
    
    pip install boto3>=1.28.57  
    

info

For **Amazon Nova Models** : Bump to v1.53.5+

info

LiteLLM uses boto3 to handle authentication. All these options are supported - <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#credentials>.

## Usage​

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BerriAI/litellm/blob/main/cookbook/LiteLLM_Bedrock.ipynb)
    
    
    import os  
    from litellm import completion  
      
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
    response = completion(  
      model="bedrock/anthropic.claude-3-sonnet-20240229-v1:0",  
      messages=[{ "content": "Hello, how are you?","role": "user"}]  
    )  
    

## LiteLLM Proxy Usage​

Here's how to call Bedrock with the LiteLLM Proxy Server

### 1\. Setup config.yaml​
    
    
    model_list:  
      - model_name: bedrock-claude-3-5-sonnet  
        litellm_params:  
          model: bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0  
          aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID  
          aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY  
          aws_region_name: os.environ/AWS_REGION_NAME  
    

All possible auth params:
    
    
    aws_access_key_id: Optional[str],  
    aws_secret_access_key: Optional[str],  
    aws_session_token: Optional[str],  
    aws_region_name: Optional[str],  
    aws_session_name: Optional[str],  
    aws_profile_name: Optional[str],  
    aws_role_name: Optional[str],  
    aws_web_identity_token: Optional[str],  
    aws_bedrock_runtime_endpoint: Optional[str],  
    

### 2\. Start the proxy​
    
    
    litellm --config /path/to/config.yaml  
    

### 3\. Test it​

  * Curl Request
  * OpenAI v1.0.0+
  * Langchain

    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
    --header 'Content-Type: application/json' \  
    --data ' {  
          "model": "bedrock-claude-v1",  
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
    response = client.chat.completions.create(model="bedrock-claude-v1", messages = [  
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
        model = "bedrock-claude-v1",  
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
    

## Set temperature, top p, etc.​

  * SDK
  * PROXY

    
    
    import os  
    from litellm import completion  
      
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
    response = completion(  
      model="bedrock/anthropic.claude-3-sonnet-20240229-v1:0",  
      messages=[{ "content": "Hello, how are you?","role": "user"}],  
      temperature=0.7,  
      top_p=1  
    )  
    

**Set on yaml**
    
    
     model_list:  
      - model_name: bedrock-claude-v1  
        litellm_params:  
          model: bedrock/anthropic.claude-instant-v1  
          temperature: <your-temp>  
          top_p: <your-top-p>  
    

**Set on request**
    
    
      
     import openai  
    client = openai.OpenAI(  
        api_key="anything",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    # request sent to model set on litellm proxy, `litellm --model`  
    response = client.chat.completions.create(model="bedrock-claude-v1", messages = [  
        {  
            "role": "user",  
            "content": "this is a test request, write a short poem"  
        }  
    ],  
    temperature=0.7,  
    top_p=1  
    )  
      
    print(response)  
      
    

## Pass provider-specific params​

If you pass a non-openai param to litellm, we'll assume it's provider-specific and send it as a kwarg in the request body. [See more](/docs/completion/input#provider-specific-params)

  * SDK
  * PROXY

    
    
    import os  
    from litellm import completion  
      
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
    response = completion(  
      model="bedrock/anthropic.claude-3-sonnet-20240229-v1:0",  
      messages=[{ "content": "Hello, how are you?","role": "user"}],  
      top_k=1 # 👈 PROVIDER-SPECIFIC PARAM  
    )  
    

**Set on yaml**
    
    
     model_list:  
      - model_name: bedrock-claude-v1  
        litellm_params:  
          model: bedrock/anthropic.claude-instant-v1  
          top_k: 1 # 👈 PROVIDER-SPECIFIC PARAM  
    

**Set on request**
    
    
      
     import openai  
    client = openai.OpenAI(  
        api_key="anything",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    # request sent to model set on litellm proxy, `litellm --model`  
    response = client.chat.completions.create(model="bedrock-claude-v1", messages = [  
        {  
            "role": "user",  
            "content": "this is a test request, write a short poem"  
        }  
    ],  
    temperature=0.7,  
    extra_body={  
        top_k=1 # 👈 PROVIDER-SPECIFIC PARAM  
    }  
    )  
      
    print(response)  
      
    

## Usage - Function Calling / Tool calling​

LiteLLM supports tool calling via Bedrock's Converse and Invoke API's.

  * SDK
  * PROXY

    
    
    from litellm import completion  
      
    # set env  
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
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
        model="bedrock/anthropic.claude-3-sonnet-20240229-v1:0",  
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
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: bedrock-claude-3-7  
        litellm_params:  
          model: bedrock/us.anthropic.claude-3-7-sonnet-20250219-v1:0 # for bedrock invoke, specify `bedrock/invoke/<model>`  
    

  2. Start proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
    curl http://0.0.0.0:4000/v1/chat/completions \  
    -H "Content-Type: application/json" \  
    -H "Authorization: Bearer $LITELLM_API_KEY" \  
    -d '{  
      "model": "bedrock-claude-3-7",  
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
      
    

## Usage - Vision​
    
    
    from litellm import completion  
      
    # set env  
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
      
    def encode_image(image_path):  
        import base64  
      
        with open(image_path, "rb") as image_file:  
            return base64.b64encode(image_file.read()).decode("utf-8")  
      
      
    image_path = "../proxy/cached_logo.jpg"  
    # Getting the base64 string  
    base64_image = encode_image(image_path)  
    resp = litellm.completion(  
        model="bedrock/anthropic.claude-3-sonnet-20240229-v1:0",  
        messages=[  
            {  
                "role": "user",  
                "content": [  
                    {"type": "text", "text": "Whats in this image?"},  
                    {  
                        "type": "image_url",  
                        "image_url": {  
                            "url": "data:image/jpeg;base64," + base64_image  
                        },  
                    },  
                ],  
            }  
        ],  
    )  
    print(f"\nResponse: {resp}")  
    

## Usage - 'thinking' / 'reasoning content'​

This is currently only supported for Anthropic's Claude 3.7 Sonnet + Deepseek R1.

Works on v1.61.20+.

Returns 2 new fields in `message` and `delta` object:

  * `reasoning_content` \- string - The reasoning content of the response
  * `thinking_blocks` \- list of objects (Anthropic only) - The thinking blocks of the response

Each object has the following fields:

  * `type` \- Literal["thinking"] - The type of thinking block
  * `thinking` \- string - The thinking of the response. Also returned in `reasoning_content`
  * `signature` \- string - A base64 encoded string, returned by Anthropic.

The `signature` is required by Anthropic on subsequent calls, if 'thinking' content is passed in (only required to use `thinking` with tool calling). [Learn more](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#understanding-thinking-blocks)

  * SDK
  * PROXY

    
    
    from litellm import completion  
      
    # set env  
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
      
    resp = completion(  
        model="bedrock/us.anthropic.claude-3-7-sonnet-20250219-v1:0",  
        messages=[{"role": "user", "content": "What is the capital of France?"}],  
        reasoning_effort="low",  
    )  
      
    print(resp)  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: bedrock-claude-3-7  
        litellm_params:  
          model: bedrock/us.anthropic.claude-3-7-sonnet-20250219-v1:0  
          reasoning_effort: "low" # 👈 EITHER HERE OR ON REQUEST  
    

  2. Start proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
    curl http://0.0.0.0:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer <YOUR-LITELLM-KEY>" \  
      -d '{  
        "model": "bedrock-claude-3-7",  
        "messages": [{"role": "user", "content": "What is the capital of France?"}],  
        "reasoning_effort": "low" # 👈 EITHER HERE OR ON CONFIG.YAML  
      }'  
    

**Expected Response**

Same as [Anthropic API response](/docs/providers/anthropic#usage---thinking--reasoning_content).
    
    
    {  
        "id": "chatcmpl-c661dfd7-7530-49c9-b0cc-d5018ba4727d",  
        "created": 1740640366,  
        "model": "us.anthropic.claude-3-7-sonnet-20250219-v1:0",  
        "object": "chat.completion",  
        "system_fingerprint": null,  
        "choices": [  
            {  
                "finish_reason": "stop",  
                "index": 0,  
                "message": {  
                    "content": "The capital of France is Paris. It's not only the capital city but also the largest city in France, serving as the country's major cultural, economic, and political center.",  
                    "role": "assistant",  
                    "tool_calls": null,  
                    "function_call": null,  
                    "reasoning_content": "The capital of France is Paris. This is a straightforward factual question.",  
                    "thinking_blocks": [  
                        {  
                            "type": "thinking",  
                            "thinking": "The capital of France is Paris. This is a straightforward factual question.",  
                            "signature": "EqoBCkgIARABGAIiQL2UoU0b1OHYi+yCHpBY7U6FQW8/FcoLewocJQPa2HnmLM+NECy50y44F/kD4SULFXi57buI9fAvyBwtyjlOiO0SDE3+r3spdg6PLOo9PBoMma2ku5OTAoR46j9VIjDRlvNmBvff7YW4WI9oU8XagaOBSxLPxElrhyuxppEn7m6bfT40dqBSTDrfiw4FYB4qEPETTI6TA6wtjGAAqmFqKTo="  
                        }  
                    ]  
                }  
            }  
        ],  
        "usage": {  
            "completion_tokens": 64,  
            "prompt_tokens": 42,  
            "total_tokens": 106,  
            "completion_tokens_details": null,  
            "prompt_tokens_details": null  
        }  
    }  
    

### Pass `thinking` to Anthropic models​

Same as [Anthropic API response](/docs/providers/anthropic#usage---thinking--reasoning_content).

## Usage - Structured Output / JSON mode​

  * SDK
  * PROXY

    
    
    from litellm import completion  
    import os   
    from pydantic import BaseModel  
      
    # set env  
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
    class CalendarEvent(BaseModel):  
      name: str  
      date: str  
      participants: list[str]  
      
    class EventsList(BaseModel):  
        events: list[CalendarEvent]  
      
    response = completion(  
      model="bedrock/anthropic.claude-3-7-sonnet-20250219-v1:0", # specify invoke via `bedrock/invoke/anthropic.claude-3-7-sonnet-20250219-v1:0`  
      response_format=EventsList,  
      messages=[  
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},  
        {"role": "user", "content": "Who won the world series in 2020?"}  
      ],  
    )  
    print(response.choices[0].message.content)  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: bedrock-claude-3-7  
        litellm_params:  
          model: bedrock/us.anthropic.claude-3-7-sonnet-20250219-v1:0 # specify invoke via `bedrock/invoke/<model_name>`   
          aws_access_key_id: os.environ/CUSTOM_AWS_ACCESS_KEY_ID  
          aws_secret_access_key: os.environ/CUSTOM_AWS_SECRET_ACCESS_KEY  
          aws_region_name: os.environ/CUSTOM_AWS_REGION_NAME  
    

  2. Start proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
    curl http://0.0.0.0:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer $LITELLM_KEY" \  
      -d '{  
        "model": "bedrock-claude-3-7",  
        "messages": [  
          {  
            "role": "system",  
            "content": "You are a helpful assistant designed to output JSON."  
          },  
          {  
            "role": "user",  
            "content": "Who won the worlde series in 2020?"  
          }  
        ],  
        "response_format": {  
          "type": "json_schema",  
          "json_schema": {  
            "name": "math_reasoning",  
            "description": "reason about maths",  
            "schema": {  
              "type": "object",  
              "properties": {  
                "steps": {  
                  "type": "array",  
                  "items": {  
                    "type": "object",  
                    "properties": {  
                      "explanation": { "type": "string" },  
                      "output": { "type": "string" }  
                    },  
                    "required": ["explanation", "output"],  
                    "additionalProperties": false  
                  }  
                },  
                "final_answer": { "type": "string" }  
              },  
              "required": ["steps", "final_answer"],  
              "additionalProperties": false  
            },  
            "strict": true  
          }  
        }  
      }'  
    

## Usage - Latency Optimized Inference​

Valid from v1.65.1+

  * SDK
  * PROXY

    
    
    from litellm import completion  
      
    response = completion(  
        model="bedrock/anthropic.claude-3-7-sonnet-20250219-v1:0",  
        messages=[{"role": "user", "content": "What is the capital of France?"}],  
        performanceConfig={"latency": "optimized"},  
    )  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: bedrock-claude-3-7  
        litellm_params:  
          model: bedrock/us.anthropic.claude-3-7-sonnet-20250219-v1:0  
          performanceConfig: {"latency": "optimized"} # 👈 EITHER HERE OR ON REQUEST  
    

  2. Start proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
    curl http://0.0.0.0:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer $LITELLM_KEY" \  
      -d '{  
        "model": "bedrock-claude-3-7",  
        "messages": [{"role": "user", "content": "What is the capital of France?"}],  
        "performanceConfig": {"latency": "optimized"} # 👈 EITHER HERE OR ON CONFIG.YAML  
      }'  
    

## Usage - Bedrock Guardrails​

Example of using [Bedrock Guardrails with LiteLLM](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-converse-api.html)

  * LiteLLM SDK
  * Proxy on request
  * Proxy on config.yaml

    
    
    from litellm import completion  
      
    # set env  
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
    response = completion(  
        model="anthropic.claude-v2",  
        messages=[  
            {  
                "content": "where do i buy coffee from? ",  
                "role": "user",  
            }  
        ],  
        max_tokens=10,  
        guardrailConfig={  
            "guardrailIdentifier": "ff6ujrregl1q", # The identifier (ID) for the guardrail.  
            "guardrailVersion": "DRAFT",           # The version of the guardrail.  
            "trace": "disabled",                   # The trace behavior for the guardrail. Can either be "disabled" or "enabled"  
        },  
    )  
    
    
    
      
    import openai  
    client = openai.OpenAI(  
        api_key="anything",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    # request sent to model set on litellm proxy, `litellm --model`  
    response = client.chat.completions.create(model="anthropic.claude-v2", messages = [  
        {  
            "role": "user",  
            "content": "this is a test request, write a short poem"  
        }  
    ],  
    temperature=0.7,  
    extra_body={  
        "guardrailConfig": {  
            "guardrailIdentifier": "ff6ujrregl1q", # The identifier (ID) for the guardrail.  
            "guardrailVersion": "DRAFT",           # The version of the guardrail.  
            "trace": "disabled",                   # The trace behavior for the guardrail. Can either be "disabled" or "enabled"  
        },  
    }  
    )  
      
    print(response)  
    

  1. Update config.yaml

    
    
    model_list:  
      - model_name: bedrock-claude-v1  
        litellm_params:  
          model: bedrock/anthropic.claude-instant-v1  
          aws_access_key_id: os.environ/CUSTOM_AWS_ACCESS_KEY_ID  
          aws_secret_access_key: os.environ/CUSTOM_AWS_SECRET_ACCESS_KEY  
          aws_region_name: os.environ/CUSTOM_AWS_REGION_NAME  
          guardrailConfig: {  
            "guardrailIdentifier": "ff6ujrregl1q", # The identifier (ID) for the guardrail.  
            "guardrailVersion": "DRAFT",           # The version of the guardrail.  
            "trace": "disabled",                   # The trace behavior for the guardrail. Can either be "disabled" or "enabled"  
        }  
      
    

  2. Start proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
      
    import openai  
    client = openai.OpenAI(  
        api_key="anything",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    # request sent to model set on litellm proxy, `litellm --model`  
    response = client.chat.completions.create(model="bedrock-claude-v1", messages = [  
        {  
            "role": "user",  
            "content": "this is a test request, write a short poem"  
        }  
    ],  
    temperature=0.7  
    )  
      
    print(response)  
    

## Usage - "Assistant Pre-fill"​

If you're using Anthropic's Claude with Bedrock, you can "put words in Claude's mouth" by including an `assistant` role message as the last item in the `messages` array.

> [!IMPORTANT] The returned completion will _**not**_ include your "pre-fill" text, since it is part of the prompt itself. Make sure to prefix Claude's completion with your pre-fill.
    
    
    import os  
    from litellm import completion  
      
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
    messages = [  
        {"role": "user", "content": "How do you say 'Hello' in German? Return your answer as a JSON object, like this:\n\n{ \"Hello\": \"Hallo\" }"},  
        {"role": "assistant", "content": "{"},  
    ]  
    response = completion(model="bedrock/anthropic.claude-v2", messages=messages)  
    

### Example prompt sent to Claude​
    
    
      
    Human: How do you say 'Hello' in German? Return your answer as a JSON object, like this:  
      
    { "Hello": "Hallo" }  
      
    Assistant: {  
    

## Usage - "System" messages​

If you're using Anthropic's Claude 2.1 with Bedrock, `system` role messages are properly formatted for you.
    
    
    import os  
    from litellm import completion  
      
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
    messages = [  
        {"role": "system", "content": "You are a snarky assistant."},  
        {"role": "user", "content": "How do I boil water?"},  
    ]  
    response = completion(model="bedrock/anthropic.claude-v2:1", messages=messages)  
    

### Example prompt sent to Claude​
    
    
    You are a snarky assistant.  
      
    Human: How do I boil water?  
      
    Assistant:  
    

## Usage - Streaming​
    
    
    import os  
    from litellm import completion  
      
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
    response = completion(  
      model="bedrock/anthropic.claude-instant-v1",  
      messages=[{ "content": "Hello, how are you?","role": "user"}],  
      stream=True  
    )  
    for chunk in response:  
      print(chunk)  
    

#### Example Streaming Output Chunk​
    
    
    {  
      "choices": [  
        {  
          "finish_reason": null,  
          "index": 0,  
          "delta": {  
            "content": "ase can appeal the case to a higher federal court. If a higher federal court rules in a way that conflicts with a ruling from a lower federal court or conflicts with a ruling from a higher state court, the parties involved in the case can appeal the case to the Supreme Court. In order to appeal a case to the Sup"  
          }  
        }  
      ],  
      "created": null,  
      "model": "anthropic.claude-instant-v1",  
      "usage": {  
        "prompt_tokens": null,  
        "completion_tokens": null,  
        "total_tokens": null  
      }  
    }  
    

## Cross-region inferencing​

LiteLLM supports Bedrock [cross-region inferencing](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) across all [supported bedrock models](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html).

  * SDK
  * PROXY

    
    
    from litellm import completion   
    import os   
      
      
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
      
    litellm.set_verbose = True #  👈 SEE RAW REQUEST   
      
    response = completion(  
        model="bedrock/us.anthropic.claude-3-haiku-20240307-v1:0",  
        messages=messages,  
        max_tokens=10,  
        temperature=0.1,  
    )  
      
    print("Final Response: {}".format(response))  
    

#### 1\. Setup config.yaml​
    
    
    model_list:  
      - model_name: bedrock-claude-haiku  
        litellm_params:  
          model: bedrock/us.anthropic.claude-3-haiku-20240307-v1:0  
          aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID  
          aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY  
          aws_region_name: os.environ/AWS_REGION_NAME  
    

#### 2\. Start the proxy​
    
    
    litellm --config /path/to/config.yaml  
    

#### 3\. Test it​

  * Curl Request
  * OpenAI v1.0.0+
  * Langchain

    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
    --header 'Content-Type: application/json' \  
    --data ' {  
          "model": "bedrock-claude-haiku",  
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
    response = client.chat.completions.create(model="bedrock-claude-haiku", messages = [  
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
        model = "bedrock-claude-haiku",  
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
    

## Set 'converse' / 'invoke' route​

info

Supported from LiteLLM Version `v1.53.5`

LiteLLM defaults to the `invoke` route. LiteLLM uses the `converse` route for Bedrock models that support it.

To explicitly set the route, do `bedrock/converse/<model>` or `bedrock/invoke/<model>`.

E.g.

  * SDK
  * PROXY

    
    
    from litellm import completion  
      
    completion(model="bedrock/converse/us.amazon.nova-pro-v1:0")  
    
    
    
    model_list:  
      - model_name: bedrock-model  
        litellm_params:  
          model: bedrock/converse/us.amazon.nova-pro-v1:0  
    

## Alternate user/assistant messages​

Use `user_continue_message` to add a default user message, for cases (e.g. Autogen) where the client might not follow alternating user/assistant messages starting and ending with a user message.
    
    
    model_list:  
      - model_name: "bedrock-claude"  
        litellm_params:  
          model: "bedrock/anthropic.claude-instant-v1"  
          user_continue_message: {"role": "user", "content": "Please continue"}  
    

OR

just set `litellm.modify_params=True` and LiteLLM will automatically handle this with a default user_continue_message.
    
    
    model_list:  
      - model_name: "bedrock-claude"  
        litellm_params:  
          model: "bedrock/anthropic.claude-instant-v1"  
      
    litellm_settings:  
       modify_params: true  
    

Test it!
    
    
    curl -X POST 'http://0.0.0.0:4000/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
        "model": "bedrock-claude",  
        "messages": [{"role": "assistant", "content": "Hey, how's it going?"}]  
    }'  
    

## Usage - PDF / Document Understanding​

LiteLLM supports Document Understanding for Bedrock models - [AWS Bedrock Docs](https://docs.aws.amazon.com/nova/latest/userguide/modalities-document.html).

info

LiteLLM supports ALL Bedrock document types -

E.g.: "pdf", "csv", "doc", "docx", "xls", "xlsx", "html", "txt", "md"

You can also pass these as either `image_url` or `base64`

### url​

  * SDK
  * PROXY

    
    
    from litellm.utils import supports_pdf_input, completion  
      
    # set aws credentials  
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
      
    # pdf url  
    image_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"  
      
    # Download the file  
    response = requests.get(url)  
    file_data = response.content  
      
    encoded_file = base64.b64encode(file_data).decode("utf-8")  
      
    # model  
    model = "bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0"  
      
    image_content = [  
        {"type": "text", "text": "What's this file about?"},  
        {  
            "type": "file",  
            "file": {  
                "file_data": f"data:application/pdf;base64,{encoded_file}", # 👈 PDF  
            }  
        },  
    ]  
      
      
    if not supports_pdf_input(model, None):  
        print("Model does not support image input")  
      
    response = completion(  
        model=model,  
        messages=[{"role": "user", "content": image_content}],  
    )  
    assert response is not None  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: bedrock-model  
        litellm_params:  
          model: bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0  
          aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID  
          aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY  
          aws_region_name: os.environ/AWS_REGION_NAME  
    

  2. Start the proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
    curl -X POST 'http://0.0.0.0:4000/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
        "model": "bedrock-model",  
        "messages": [  
            {"role": "user", "content": {"type": "text", "text": "What's this file about?"}},  
            {  
                "type": "file",  
                "file": {  
                    "file_data": f"data:application/pdf;base64,{encoded_file}", # 👈 PDF  
                }  
            }  
        ]  
    }'  
    

### base64​

  * SDK
  * PROXY

    
    
    from litellm.utils import supports_pdf_input, completion  
      
    # set aws credentials  
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
      
    # pdf url  
    image_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"  
    response = requests.get(url)  
    file_data = response.content  
      
    encoded_file = base64.b64encode(file_data).decode("utf-8")  
    base64_url = f"data:application/pdf;base64,{encoded_file}"  
      
    # model  
    model = "bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0"  
      
    image_content = [  
        {"type": "text", "text": "What's this file about?"},  
        {  
            "type": "image_url",  
            "image_url": base64_url, # OR {"url": base64_url}  
        },  
    ]  
      
      
    if not supports_pdf_input(model, None):  
        print("Model does not support image input")  
      
    response = completion(  
        model=model,  
        messages=[{"role": "user", "content": image_content}],  
    )  
    assert response is not None  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: bedrock-model  
        litellm_params:  
          model: bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0  
          aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID  
          aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY  
          aws_region_name: os.environ/AWS_REGION_NAME  
    

  2. Start the proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
    curl -X POST 'http://0.0.0.0:4000/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
        "model": "bedrock-model",  
        "messages": [  
            {"role": "user", "content": {"type": "text", "text": "What's this file about?"}},  
            {  
                "type": "image_url",  
                "image_url": "data:application/pdf;base64,{b64_encoded_file}",  
            }  
        ]  
    }'  
    

## Bedrock Imported Models (Deepseek, Deepseek R1)​

### Deepseek R1​

This is a separate route, as the chat template is different.

Property| Details  
---|---  
Provider Route| `bedrock/deepseek_r1/{model_arn}`  
Provider Documentation| [Bedrock Imported Models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html), [Deepseek Bedrock Imported Model](https://aws.amazon.com/blogs/machine-learning/deploy-deepseek-r1-distilled-llama-models-with-amazon-bedrock-custom-model-import/)  
  
  * SDK
  * Proxy

    
    
    from litellm import completion  
    import os  
      
    response = completion(  
        model="bedrock/deepseek_r1/arn:aws:bedrock:us-east-1:086734376398:imported-model/r4c4kewx2s0n",  # bedrock/deepseek_r1/{your-model-arn}  
        messages=[{"role": "user", "content": "Tell me a joke"}],  
    )  
    

**1\. Add to config**
    
    
     model_list:  
        - model_name: DeepSeek-R1-Distill-Llama-70B  
          litellm_params:  
            model: bedrock/deepseek_r1/arn:aws:bedrock:us-east-1:086734376398:imported-model/r4c4kewx2s0n  
      
    

**2\. Start proxy**
    
    
     litellm --config /path/to/config.yaml  
      
    # RUNNING at http://0.0.0.0:4000  
    

**3\. Test it!**
    
    
     curl --location 'http://0.0.0.0:4000/chat/completions' \  
          --header 'Authorization: Bearer sk-1234' \  
          --header 'Content-Type: application/json' \  
          --data '{  
                "model": "DeepSeek-R1-Distill-Llama-70B", # 👈 the 'model_name' in config  
                "messages": [  
                    {  
                    "role": "user",  
                    "content": "what llm are you"  
                    }  
                ],  
            }'  
    

### Deepseek (not R1)​

Property| Details  
---|---  
Provider Route| `bedrock/llama/{model_arn}`  
Provider Documentation| [Bedrock Imported Models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html), [Deepseek Bedrock Imported Model](https://aws.amazon.com/blogs/machine-learning/deploy-deepseek-r1-distilled-llama-models-with-amazon-bedrock-custom-model-import/)  
  
Use this route to call Bedrock Imported Models that follow the `llama` Invoke Request / Response spec

  * SDK
  * Proxy

    
    
    from litellm import completion  
    import os  
      
    response = completion(  
        model="bedrock/llama/arn:aws:bedrock:us-east-1:086734376398:imported-model/r4c4kewx2s0n",  # bedrock/llama/{your-model-arn}  
        messages=[{"role": "user", "content": "Tell me a joke"}],  
    )  
    

**1\. Add to config**
    
    
     model_list:  
        - model_name: DeepSeek-R1-Distill-Llama-70B  
          litellm_params:  
            model: bedrock/llama/arn:aws:bedrock:us-east-1:086734376398:imported-model/r4c4kewx2s0n  
      
    

**2\. Start proxy**
    
    
     litellm --config /path/to/config.yaml  
      
    # RUNNING at http://0.0.0.0:4000  
    

**3\. Test it!**
    
    
     curl --location 'http://0.0.0.0:4000/chat/completions' \  
          --header 'Authorization: Bearer sk-1234' \  
          --header 'Content-Type: application/json' \  
          --data '{  
                "model": "DeepSeek-R1-Distill-Llama-70B", # 👈 the 'model_name' in config  
                "messages": [  
                    {  
                    "role": "user",  
                    "content": "what llm are you"  
                    }  
                ],  
            }'  
    

## Provisioned throughput models​

To use provisioned throughput Bedrock models pass

  * `model=bedrock/<base-model>`, example `model=bedrock/anthropic.claude-v2`. Set `model` to any of the Supported AWS models
  * `model_id=provisioned-model-arn`

Completion
    
    
    import litellm  
    response = litellm.completion(  
        model="bedrock/anthropic.claude-instant-v1",  
        model_id="provisioned-model-arn",  
        messages=[{"content": "Hello, how are you?", "role": "user"}]  
    )  
    

Embedding
    
    
    import litellm  
    response = litellm.embedding(  
        model="bedrock/amazon.titan-embed-text-v1",  
        model_id="provisioned-model-arn",  
        input=["hi"],  
    )  
    

## Supported AWS Bedrock Models​

LiteLLM supports ALL Bedrock models.

Here's an example of using a bedrock model with LiteLLM. For a complete list, refer to the [model cost map](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json)

Model Name| Command  
---|---  
Deepseek R1| `completion(model='bedrock/us.deepseek.r1-v1:0', messages=messages)`  
Anthropic Claude-V3.5 Sonnet| `completion(model='bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0', messages=messages)`  
Anthropic Claude-V3 sonnet| `completion(model='bedrock/anthropic.claude-3-sonnet-20240229-v1:0', messages=messages)`  
Anthropic Claude-V3 Haiku| `completion(model='bedrock/anthropic.claude-3-haiku-20240307-v1:0', messages=messages)`  
Anthropic Claude-V3 Opus| `completion(model='bedrock/anthropic.claude-3-opus-20240229-v1:0', messages=messages)`  
Anthropic Claude-V2.1| `completion(model='bedrock/anthropic.claude-v2:1', messages=messages)`  
Anthropic Claude-V2| `completion(model='bedrock/anthropic.claude-v2', messages=messages)`  
Anthropic Claude-Instant V1| `completion(model='bedrock/anthropic.claude-instant-v1', messages=messages)`  
Meta llama3-1-405b| `completion(model='bedrock/meta.llama3-1-405b-instruct-v1:0', messages=messages)`  
Meta llama3-1-70b| `completion(model='bedrock/meta.llama3-1-70b-instruct-v1:0', messages=messages)`  
Meta llama3-1-8b| `completion(model='bedrock/meta.llama3-1-8b-instruct-v1:0', messages=messages)`  
Meta llama3-70b| `completion(model='bedrock/meta.llama3-70b-instruct-v1:0', messages=messages)`  
Meta llama3-8b| `completion(model='bedrock/meta.llama3-8b-instruct-v1:0', messages=messages)`  
Amazon Titan Lite| `completion(model='bedrock/amazon.titan-text-lite-v1', messages=messages)`  
Amazon Titan Express| `completion(model='bedrock/amazon.titan-text-express-v1', messages=messages)`  
Cohere Command| `completion(model='bedrock/cohere.command-text-v14', messages=messages)`  
AI21 J2-Mid| `completion(model='bedrock/ai21.j2-mid-v1', messages=messages)`  
AI21 J2-Ultra| `completion(model='bedrock/ai21.j2-ultra-v1', messages=messages)`  
AI21 Jamba-Instruct| `completion(model='bedrock/ai21.jamba-instruct-v1:0', messages=messages)`  
Meta Llama 2 Chat 13b| `completion(model='bedrock/meta.llama2-13b-chat-v1', messages=messages)`  
Meta Llama 2 Chat 70b| `completion(model='bedrock/meta.llama2-70b-chat-v1', messages=messages)`  
Mistral 7B Instruct| `completion(model='bedrock/mistral.mistral-7b-instruct-v0:2', messages=messages)`  
Mixtral 8x7B Instruct| `completion(model='bedrock/mistral.mixtral-8x7b-instruct-v0:1', messages=messages)`  
  
## Bedrock Embedding​

### API keys​

This can be set as env variables or passed as **params to litellm.embedding()**
    
    
    import os  
    os.environ["AWS_ACCESS_KEY_ID"] = ""        # Access key  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""    # Secret access key  
    os.environ["AWS_REGION_NAME"] = ""           # us-east-1, us-east-2, us-west-1, us-west-2  
    

### Usage​
    
    
    from litellm import embedding  
    response = embedding(  
        model="bedrock/amazon.titan-embed-text-v1",  
        input=["good morning from litellm"],  
    )  
    print(response)  
    

## Supported AWS Bedrock Embedding Models​

Model Name| Usage| Supported Additional OpenAI params  
---|---|---  
Titan Embeddings V2| `embedding(model="bedrock/amazon.titan-embed-text-v2:0", input=input)`| [here](https://github.com/BerriAI/litellm/blob/f5905e100068e7a4d61441d7453d7cf5609c2121/litellm/llms/bedrock/embed/amazon_titan_v2_transformation.py#L59)  
Titan Embeddings - V1| `embedding(model="bedrock/amazon.titan-embed-text-v1", input=input)`| [here](https://github.com/BerriAI/litellm/blob/f5905e100068e7a4d61441d7453d7cf5609c2121/litellm/llms/bedrock/embed/amazon_titan_g1_transformation.py#L53)  
Titan Multimodal Embeddings| `embedding(model="bedrock/amazon.titan-embed-image-v1", input=input)`| [here](https://github.com/BerriAI/litellm/blob/f5905e100068e7a4d61441d7453d7cf5609c2121/litellm/llms/bedrock/embed/amazon_titan_multimodal_transformation.py#L28)  
Cohere Embeddings - English| `embedding(model="bedrock/cohere.embed-english-v3", input=input)`| [here](https://github.com/BerriAI/litellm/blob/f5905e100068e7a4d61441d7453d7cf5609c2121/litellm/llms/bedrock/embed/cohere_transformation.py#L18)  
Cohere Embeddings - Multilingual| `embedding(model="bedrock/cohere.embed-multilingual-v3", input=input)`| [here](https://github.com/BerriAI/litellm/blob/f5905e100068e7a4d61441d7453d7cf5609c2121/litellm/llms/bedrock/embed/cohere_transformation.py#L18)  
  
### Advanced - [Drop Unsupported Params](https://docs.litellm.ai/docs/completion/drop_params#openai-proxy-usage)​

### Advanced - [Pass model/provider-specific Params](https://docs.litellm.ai/docs/completion/provider_specific_params#proxy-usage)​

## Image Generation​

Use this for stable diffusion, and amazon nova canvas on bedrock

### Usage​

  * SDK
  * PROXY

    
    
    import os  
    from litellm import image_generation  
      
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
    response = image_generation(  
                prompt="A cute baby sea otter",  
                model="bedrock/stability.stable-diffusion-xl-v0",  
            )  
    print(f"response: {response}")  
    

**Set optional params**
    
    
     import os  
    from litellm import image_generation  
      
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
    response = image_generation(  
                prompt="A cute baby sea otter",  
                model="bedrock/stability.stable-diffusion-xl-v0",  
                ### OPENAI-COMPATIBLE ###  
                size="128x512", # width=128, height=512  
                ### PROVIDER-SPECIFIC ### see `AmazonStabilityConfig` in bedrock.py for all params  
                seed=30  
            )  
    print(f"response: {response}")  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: amazon.nova-canvas-v1:0  
        litellm_params:  
          model: bedrock/amazon.nova-canvas-v1:0  
          aws_region_name: "us-east-1"  
          aws_secret_access_key: my-key # OPTIONAL - all boto3 auth params supported  
          aws_secret_access_id: my-id # OPTIONAL - all boto3 auth params supported  
    

  2. Start proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
    curl -L -X POST 'http://0.0.0.0:4000/v1/images/generations' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer $LITELLM_VIRTUAL_KEY' \  
    -d '{  
        "model": "amazon.nova-canvas-v1:0",  
        "prompt": "A cute baby sea otter"  
    }'  
    

## Supported AWS Bedrock Image Generation Models​

Model Name| Function Call  
---|---  
Stable Diffusion 3 - v0| `embedding(model="bedrock/stability.stability.sd3-large-v1:0", prompt=prompt)`  
Stable Diffusion - v0| `embedding(model="bedrock/stability.stable-diffusion-xl-v0", prompt=prompt)`  
Stable Diffusion - v0| `embedding(model="bedrock/stability.stable-diffusion-xl-v1", prompt=prompt)`  
  
## Rerank API​

Use Bedrock's Rerank API in the Cohere `/rerank` format.

Supported Cohere Rerank Params

  * `model` \- the foundation model ARN
  * `query` \- the query to rerank against
  * `documents` \- the list of documents to rerank
  * `top_n` \- the number of results to return

  * SDK
  * PROXY

    
    
    from litellm import rerank  
    import os   
      
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
    response = rerank(  
        model="bedrock/arn:aws:bedrock:us-west-2::foundation-model/amazon.rerank-v1:0", # provide the model ARN - get this here https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_foundation_models.html  
        query="hello",  
        documents=["hello", "world"],  
        top_n=2,  
    )  
      
    print(response)  
    

  1. Setup config.yaml

    
    
    model_list:  
        - model_name: bedrock-rerank  
          litellm_params:  
            model: bedrock/arn:aws:bedrock:us-west-2::foundation-model/amazon.rerank-v1:0  
            aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID  
            aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY  
            aws_region_name: os.environ/AWS_REGION_NAME  
    

  2. Start proxy server

    
    
    litellm --config config.yaml  
      
    # RUNNING on http://0.0.0.0:4000  
    

  3. Test it!

    
    
    curl http://0.0.0.0:4000/rerank \  
      -H "Authorization: Bearer sk-1234" \  
      -H "Content-Type: application/json" \  
      -d '{  
        "model": "bedrock-rerank",  
        "query": "What is the capital of the United States?",  
        "documents": [  
            "Carson City is the capital city of the American state of Nevada.",  
            "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",  
            "Washington, D.C. is the capital of the United States.",  
            "Capital punishment has existed in the United States since before it was a country."  
        ],  
        "top_n": 3  
      
      
      }'  
    

## Bedrock Application Inference Profile​

Use Bedrock Application Inference Profile to track costs for projects on AWS.

You can either pass it in the model name - `model="bedrock/arn:...` or as a separate `model_id="arn:..` param.

### Set via `model_id`​

  * SDK
  * PROXY

    
    
    from litellm import completion  
    import os   
      
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
    response = completion(  
        model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",  
        messages=[{"role": "user", "content": "Hello, how are you?"}],  
        model_id="arn:aws:bedrock:eu-central-1:000000000000:application-inference-profile/a0a0a0a0a0a0",  
    )  
      
    print(response)  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: anthropic-claude-3-5-sonnet  
        litellm_params:  
          model: bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0  
          # You have to set the ARN application inference profile in the model_id parameter  
          model_id: arn:aws:bedrock:eu-central-1:000000000000:application-inference-profile/a0a0a0a0a0a0  
    

  2. Start proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
    curl -L -X POST 'http://0.0.0.0:4000/v1/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer $LITELLM_API_KEY' \  
    -d '{  
      "model": "anthropic-claude-3-5-sonnet",  
      "messages": [  
        {  
          "role": "user",  
          "content": [  
            {  
              "type": "text",  
              "text": "List 5 important events in the XIX century"  
            }  
          ]  
        }  
      ]  
    }'  
    

## Boto3 - Authentication​

### Passing credentials as parameters - Completion()​

Pass AWS credentials as parameters to litellm.completion
    
    
    import os  
    from litellm import completion  
      
    response = completion(  
                model="bedrock/anthropic.claude-instant-v1",  
                messages=[{ "content": "Hello, how are you?","role": "user"}],  
                aws_access_key_id="",  
                aws_secret_access_key="",  
                aws_region_name="",  
    )  
    

### Passing extra headers + Custom API Endpoints​

This can be used to override existing headers (e.g. `Authorization`) when calling custom api endpoints

  * SDK
  * PROXY

    
    
    import os  
    import litellm  
    from litellm import completion  
      
    litellm.set_verbose = True # 👈 SEE RAW REQUEST  
      
    response = completion(  
                model="bedrock/anthropic.claude-instant-v1",  
                messages=[{ "content": "Hello, how are you?","role": "user"}],  
                aws_access_key_id="",  
                aws_secret_access_key="",  
                aws_region_name="",  
                aws_bedrock_runtime_endpoint="https://my-fake-endpoint.com",  
                extra_headers={"key": "value"}  
    )  
    

  1. Setup config.yaml

    
    
    model_list:  
        - model_name: bedrock-model  
          litellm_params:  
            model: bedrock/anthropic.claude-instant-v1  
            aws_access_key_id: "",  
            aws_secret_access_key: "",  
            aws_region_name: "",  
            aws_bedrock_runtime_endpoint: "https://my-fake-endpoint.com",  
            extra_headers: {"key": "value"}  
    

  2. Start proxy

    
    
    litellm --config /path/to/config.yaml --detailed_debug  
    

  3. Test it!

    
    
    curl -X POST 'http://0.0.0.0:4000/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
        "model": "bedrock-model",  
        "messages": [  
          {  
            "role": "system",  
            "content": "You are a helpful math tutor. Guide the user through the solution step by step."  
          },  
          {  
            "role": "user",  
            "content": "how can I solve 8x + 7 = -23"  
          }  
        ]  
    }'  
    

### SSO Login (AWS Profile)​

  * Set `AWS_PROFILE` environment variable
  * Make bedrock completion call

    
    
    import os  
    from litellm import completion  
      
    response = completion(  
                model="bedrock/anthropic.claude-instant-v1",  
                messages=[{ "content": "Hello, how are you?","role": "user"}]  
    )  
    

or pass `aws_profile_name`:
    
    
    import os  
    from litellm import completion  
      
    response = completion(  
                model="bedrock/anthropic.claude-instant-v1",  
                messages=[{ "content": "Hello, how are you?","role": "user"}],  
                aws_profile_name="dev-profile",  
    )  
    

### STS (Role-based Auth)​

  * Set `aws_role_name` and `aws_session_name`

LiteLLM Parameter| Boto3 Parameter| Description| Boto3 Documentation  
---|---|---|---  
`aws_access_key_id`| `aws_access_key_id`| AWS access key associated with an IAM user or role| [Credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)  
`aws_secret_access_key`| `aws_secret_access_key`| AWS secret key associated with the access key| [Credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)  
`aws_role_name`| `RoleArn`| The Amazon Resource Name (ARN) of the role to assume| [AssumeRole API](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.assume_role)  
`aws_session_name`| `RoleSessionName`| An identifier for the assumed role session| [AssumeRole API](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.assume_role)  
  
Make the bedrock completion call

  * SDK
  * PROXY

    
    
    from litellm import completion  
      
    response = completion(  
                model="bedrock/anthropic.claude-instant-v1",  
                messages=messages,  
                max_tokens=10,  
                temperature=0.1,  
                aws_role_name=aws_role_name,  
                aws_session_name="my-test-session",  
            )  
    

If you also need to dynamically set the aws user accessing the role, add the additional args in the completion()/embedding() function
    
    
    from litellm import completion  
      
    response = completion(  
                model="bedrock/anthropic.claude-instant-v1",  
                messages=messages,  
                max_tokens=10,  
                temperature=0.1,  
                aws_region_name=aws_region_name,  
                aws_access_key_id=aws_access_key_id,  
                aws_secret_access_key=aws_secret_access_key,  
                aws_role_name=aws_role_name,  
                aws_session_name="my-test-session",  
            )  
    
    
    
    model_list:  
      - model_name: bedrock/*  
        litellm_params:  
          model: bedrock/*  
          aws_role_name: arn:aws:iam::888602223428:role/iam_local_role # AWS RoleArn  
          aws_session_name: "bedrock-session" # AWS RoleSessionName  
          aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID # [OPTIONAL - not required if using role]  
          aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY # [OPTIONAL - not required if using role]  
    

Text to Image :
    
    
    curl -L -X POST 'http://0.0.0.0:4000/v1/images/generations' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer $LITELLM_VIRTUAL_KEY' \  
    -d '{  
        "model": "amazon.nova-canvas-v1:0",  
        "prompt": "A cute baby sea otter"  
    }'  
    

Color Guided Generation:
    
    
    curl -L -X POST 'http://0.0.0.0:4000/v1/images/generations' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer $LITELLM_VIRTUAL_KEY' \  
    -d '{  
        "model": "amazon.nova-canvas-v1:0",  
        "prompt": "A cute baby sea otter",  
        "taskType": "COLOR_GUIDED_GENERATION",  
        "colorGuidedGenerationParams":{"colors":["#FFFFFF"]}  
    }'  
    

Model Name| Function Call  
---|---  
Stable Diffusion 3 - v0| `image_generation(model="bedrock/stability.stability.sd3-large-v1:0", prompt=prompt)`  
Stable Diffusion - v0| `image_generation(model="bedrock/stability.stable-diffusion-xl-v0", prompt=prompt)`  
Stable Diffusion - v1| `image_generation(model="bedrock/stability.stable-diffusion-xl-v1", prompt=prompt)`  
Amazon Nova Canvas - v0| `image_generation(model="bedrock/amazon.nova-canvas-v1:0", prompt=prompt)`  
  
### Passing an external BedrockRuntime.Client as a parameter - Completion()​

This is a deprecated flow. Boto3 is not async. And boto3.client does not let us make the http call through httpx. Pass in your aws params through the method above 👆. [See Auth Code](https://github.com/BerriAI/litellm/blob/55a20c7cce99a93d36a82bf3ae90ba3baf9a7f89/litellm/llms/bedrock_httpx.py#L284) [Add new auth flow](https://github.com/BerriAI/litellm/issues)

warning

Experimental - 2024-Jun-23: `aws_access_key_id`, `aws_secret_access_key`, and `aws_session_token` will be extracted from boto3.client and be passed into the httpx client

Pass an external BedrockRuntime.Client object as a parameter to litellm.completion. Useful when using an AWS credentials profile, SSO session, assumed role session, or if environment variables are not available for auth.

Create a client from session credentials:
    
    
    import boto3  
    from litellm import completion  
      
    bedrock = boto3.client(  
                service_name="bedrock-runtime",  
                region_name="us-east-1",  
                aws_access_key_id="",  
                aws_secret_access_key="",  
                aws_session_token="",  
    )  
      
    response = completion(  
                model="bedrock/anthropic.claude-instant-v1",  
                messages=[{ "content": "Hello, how are you?","role": "user"}],  
                aws_bedrock_client=bedrock,  
    )  
    

Create a client from AWS profile in `~/.aws/config`:
    
    
    import boto3  
    from litellm import completion  
      
    dev_session = boto3.Session(profile_name="dev-profile")  
    bedrock = dev_session.client(  
                service_name="bedrock-runtime",  
                region_name="us-east-1",  
    )  
      
    response = completion(  
                model="bedrock/anthropic.claude-instant-v1",  
                messages=[{ "content": "Hello, how are you?","role": "user"}],  
                aws_bedrock_client=bedrock,  
    )  
    

## Calling via Internal Proxy (not bedrock url compatible)​

Use the `bedrock/converse_like/model` endpoint to call bedrock converse model via your internal proxy.

  * SDK
  * LiteLLM Proxy

    
    
    from litellm import completion  
      
    response = completion(  
        model="bedrock/converse_like/some-model",  
        messages=[{"role": "user", "content": "What's AWS?"}],  
        api_key="sk-1234",  
        api_base="https://some-api-url/models",  
        extra_headers={"test": "hello world"},  
    )  
    

  1. Setup config.yaml

    
    
    model_list:  
        - model_name: anthropic-claude  
          litellm_params:  
            model: bedrock/converse_like/some-model  
            api_base: https://some-api-url/models  
    

  2. Start proxy server

    
    
    litellm --config config.yaml  
      
    # RUNNING on http://0.0.0.0:4000  
    

  3. Test it!

    
    
    curl -X POST 'http://0.0.0.0:4000/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
        "model": "anthropic-claude",  
        "messages": [  
          {  
            "role": "system",  
            "content": "You are a helpful math tutor. Guide the user through the solution step by step."  
          },  
          { "content": "Hello, how are you?", "role": "user" }  
        ]  
    }'  
    

**Expected Output URL**
    
    
    https://some-api-url/models  
    

  * Usage
  * LiteLLM Proxy Usage
    * 1\. Setup config.yaml
    * 2\. Start the proxy
    * 3\. Test it
  * Set temperature, top p, etc.
  * Pass provider-specific params
  * Usage - Function Calling / Tool calling
  * Usage - Vision
  * Usage - 'thinking' / 'reasoning content'
    * Pass `thinking` to Anthropic models
  * Usage - Structured Output / JSON mode
  * Usage - Latency Optimized Inference
  * Usage - Bedrock Guardrails
  * Usage - "Assistant Pre-fill"
    * Example prompt sent to Claude
  * Usage - "System" messages
    * Example prompt sent to Claude
  * Usage - Streaming
  * Cross-region inferencing
  * Set 'converse' / 'invoke' route
  * Alternate user/assistant messages
  * Usage - PDF / Document Understanding
    * url
    * base64
  * Bedrock Imported Models (Deepseek, Deepseek R1)
    * Deepseek R1
    * Deepseek (not R1)
  * Provisioned throughput models
  * Supported AWS Bedrock Models
  * Bedrock Embedding
    * API keys
    * Usage
  * Supported AWS Bedrock Embedding Models
    * Advanced - Drop Unsupported Params
    * Advanced - Pass model/provider-specific Params
  * Image Generation
    * Usage
  * Supported AWS Bedrock Image Generation Models
  * Rerank API
  * Bedrock Application Inference Profile
    * Set via `model_id`
  * Boto3 - Authentication
    * Passing credentials as parameters - Completion()
    * Passing extra headers + Custom API Endpoints
    * SSO Login (AWS Profile)
    * STS (Role-based Auth)
    * Passing an external BedrockRuntime.Client as a parameter - Completion()
  * Calling via Internal Proxy (not bedrock url compatible)