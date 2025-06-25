# Comet Opik - Logging + Evals | liteLLM

On this page

Opik is an open source end-to-end [LLM Evaluation Platform](https://www.comet.com/site/products/opik/?utm_source=litelllm&utm_medium=docs&utm_content=intro_paragraph) that helps developers track their LLM prompts and responses during both development and production. Users can define and run evaluations to test their LLMs apps before deployment to check for hallucinations, accuracy, context retrevial, and more!

info

We want to learn how we can make the callbacks better! Meet the LiteLLM [founders](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version) or join our [discord](https://discord.gg/wuPM9dRgDw)

## Pre-Requisites​

You can learn more about setting up Opik in the [Opik quickstart guide](https://www.comet.com/docs/opik/quickstart/). You can also learn more about self-hosting Opik in our [self-hosting guide](https://www.comet.com/docs/opik/self-host/local_deployment).

## Quick Start​

Use just 4 lines of code, to instantly log your responses **across all providers** with Opik

Get your Opik API Key by signing up [here](https://www.comet.com/signup?utm_source=litelllm&utm_medium=docs&utm_content=api_key_cell)!
    
    
    import litellm  
    litellm.callbacks = ["opik"]  
    

Full examples:

  * SDK
  * Proxy

    
    
    import litellm  
    import os  
      
    # Configure the Opik API key or call opik.configure()  
    os.environ["OPIK_API_KEY"] = ""  
    os.environ["OPIK_WORKSPACE"] = ""  
      
    # LLM provider API Keys:  
    os.environ["OPENAI_API_KEY"] = ""  
      
    # set "opik" as a callback, litellm will send the data to an Opik server (such as comet.com)  
    litellm.callbacks = ["opik"]  
      
    # openai call  
    response = litellm.completion(  
        model="gpt-3.5-turbo",  
        messages=[  
            {"role": "user", "content": "Why is tracking and evaluation of LLMs important?"}  
        ]  
    )  
    

If you are using liteLLM within a function tracked using Opik's `@track` decorator, you will need provide the `current_span_data` field in the metadata attribute so that the LLM call is assigned to the correct trace:
    
    
    from opik import track  
    from opik.opik_context import get_current_span_data  
    import litellm  
      
    litellm.callbacks = ["opik"]  
      
    @track()  
    def streaming_function(input):  
        messages = [{"role": "user", "content": input}]  
        response = litellm.completion(  
            model="gpt-3.5-turbo",  
            messages=messages,  
            metadata = {  
                "opik": {  
                    "current_span_data": get_current_span_data(),  
                    "tags": ["streaming-test"],  
                },  
            }  
        )  
        return response  
      
    response = streaming_function("Why is tracking and evaluation of LLMs important?")  
    chunks = list(response)  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: gpt-3.5-turbo-testing  
        litellm_params:  
          model: gpt-3.5-turbo  
          api_key: os.environ/OPENAI_API_KEY  
      
    litellm_settings:  
      callbacks: ["opik"]  
      
    environment_variables:  
      OPIK_API_KEY: ""  
      OPIK_WORKSPACE: ""  
    

  2. Run proxy

    
    
    litellm --config config.yaml  
    

  3. Test it!

    
    
    curl -L -X POST 'http://0.0.0.0:4000/v1/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
      "model": "gpt-3.5-turbo-testing",  
      "messages": [  
        {  
          "role": "user",  
          "content": "What's the weather like in Boston today?"  
        }  
      ]  
    }'  
    

## Opik-Specific Parameters​

These can be passed inside metadata with the `opik` key.

### Fields​

  * `project_name` \- Name of the Opik project to send data to.
  * `current_span_data` \- The current span data to be used for tracing.
  * `tags` \- Tags to be used for tracing.

### Usage​

  * SDK
  * Proxy

    
    
    from opik import track  
    from opik.opik_context import get_current_span_data  
    import litellm  
      
    litellm.callbacks = ["opik"]  
      
    messages = [{"role": "user", "content": input}]  
    response = litellm.completion(  
        model="gpt-3.5-turbo",  
        messages=messages,  
        metadata = {  
            "opik": {  
                "current_span_data": get_current_span_data(),  
                "tags": ["streaming-test"],  
            },  
        }  
    )  
    return response  
    
    
    
    curl -L -X POST 'http://0.0.0.0:4000/v1/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
      "model": "gpt-3.5-turbo-testing",  
      "messages": [  
        {  
          "role": "user",  
          "content": "What's the weather like in Boston today?"  
        }  
      ],  
      "metadata": {  
        "opik": {  
          "current_span_data": "...",  
          "tags": ["streaming-test"],  
        },  
      }  
    }'  
    

## Support & Talk to Founders​

  * [Schedule Demo 👋](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version)
  * [Community Discord 💭](https://discord.gg/wuPM9dRgDw)
  * Our numbers 📞 +1 (770) 8783-106 / ‭+1 (412) 618-6238‬
  * Our emails ✉️ [ishaan@berri.ai](mailto:ishaan@berri.ai) / [krrish@berri.ai](mailto:krrish@berri.ai)

  * Pre-Requisites
  * Quick Start
  * Opik-Specific Parameters
    * Fields
    * Usage
  * Support & Talk to Founders