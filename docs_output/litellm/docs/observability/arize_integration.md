# Arize AI | liteLLM

On this page

AI Observability and Evaluation Platform

tip

This is community maintained, Please make an issue if you run into a bug <https://github.com/BerriAI/litellm>

## Pre-Requisites​

Make an account on [Arize AI](https://app.arize.com/auth/login)

## Quick Start​

Use just 2 lines of code, to instantly log your responses **across all providers** with arize

You can also use the instrumentor option instead of the callback, which you can find [here](https://docs.arize.com/arize/llm-tracing/tracing-integrations-auto/litellm).
    
    
    litellm.callbacks = ["arize"]  
    
    
    
      
    import litellm  
    import os  
      
    os.environ["ARIZE_SPACE_KEY"] = ""  
    os.environ["ARIZE_API_KEY"] = ""  
      
    # LLM API Keys  
    os.environ['OPENAI_API_KEY']=""  
      
    # set arize as a callback, litellm will send the data to arize  
    litellm.callbacks = ["arize"]  
       
    # openai call  
    response = litellm.completion(  
      model="gpt-3.5-turbo",  
      messages=[  
        {"role": "user", "content": "Hi 👋 - i'm openai"}  
      ]  
    )  
    

### Using with LiteLLM Proxy​

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: gpt-4  
        litellm_params:  
          model: openai/fake  
          api_key: fake-key  
          api_base: https://exampleopenaiendpoint-production.up.railway.app/  
      
    litellm_settings:  
      callbacks: ["arize"]  
      
    general_settings:  
      master_key: "sk-1234" # can also be set as an environment variable  
      
    environment_variables:  
        ARIZE_SPACE_KEY: "d0*****"  
        ARIZE_API_KEY: "141a****"  
        ARIZE_ENDPOINT: "https://otlp.arize.com/v1" # OPTIONAL - your custom arize GRPC api endpoint  
        ARIZE_HTTP_ENDPOINT: "https://otlp.arize.com/v1" # OPTIONAL - your custom arize HTTP api endpoint. Set either this or ARIZE_ENDPOINT or Neither (defaults to https://otlp.arize.com/v1 on grpc)  
    

  2. Start the proxy

    
    
    litellm --config config.yaml  
    

  3. Test it!

    
    
    curl -X POST 'http://0.0.0.0:4000/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{ "model": "gpt-4", "messages": [{"role": "user", "content": "Hi 👋 - i'm openai"}]}'  
    

## Pass Arize Space/Key per-request​

Supported parameters:

  * `arize_api_key`
  * `arize_space_key`

  * SDK
  * PROXY

    
    
    import litellm  
    import os  
      
    # LLM API Keys  
    os.environ['OPENAI_API_KEY']=""  
      
    # set arize as a callback, litellm will send the data to arize  
    litellm.callbacks = ["arize"]  
       
    # openai call  
    response = litellm.completion(  
      model="gpt-3.5-turbo",  
      messages=[  
        {"role": "user", "content": "Hi 👋 - i'm openai"}  
      ],  
      arize_api_key=os.getenv("ARIZE_SPACE_2_API_KEY"),  
      arize_space_key=os.getenv("ARIZE_SPACE_2_KEY"),  
    )  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: gpt-4  
        litellm_params:  
          model: openai/fake  
          api_key: fake-key  
          api_base: https://exampleopenaiendpoint-production.up.railway.app/  
      
    litellm_settings:  
      callbacks: ["arize"]  
      
    general_settings:  
      master_key: "sk-1234" # can also be set as an environment variable  
    

  2. Start the proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

  * CURL
  * OpenAI Python

    
    
    curl -X POST 'http://0.0.0.0:4000/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
      "model": "gpt-4",  
      "messages": [{"role": "user", "content": "Hi 👋 - i'm openai"}],  
      "arize_api_key": "ARIZE_SPACE_2_API_KEY",  
      "arize_space_key": "ARIZE_SPACE_2_KEY"  
    }'  
    
    
    
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
        extra_body={  
          "arize_api_key": "ARIZE_SPACE_2_API_KEY",  
          "arize_space_key": "ARIZE_SPACE_2_KEY"  
        }  
    )  
      
    print(response)  
    

## Support & Talk to Founders​

  * [Schedule Demo 👋](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version)
  * [Community Discord 💭](https://discord.gg/wuPM9dRgDw)
  * Our numbers 📞 +1 (770) 8783-106 / ‭+1 (412) 618-6238‬
  * Our emails ✉️ [ishaan@berri.ai](mailto:ishaan@berri.ai) / [krrish@berri.ai](mailto:krrish@berri.ai)

  * Pre-Requisites
  * Quick Start
    * Using with LiteLLM Proxy
  * Pass Arize Space/Key per-request
  * Support & Talk to Founders