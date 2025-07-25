# Logfire | liteLLM

On this page

Logfire is open Source Observability & Analytics for LLM Apps Detailed production traces and a granular view on quality, cost and latency

info

We want to learn how we can make the callbacks better! Meet the LiteLLM [founders](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version) or join our [discord](https://discord.gg/wuPM9dRgDw)

## Pre-Requisites​

Ensure you have installed the following packages to use this integration
    
    
    pip install litellm  
      
    pip install opentelemetry-api==1.25.0  
    pip install opentelemetry-sdk==1.25.0  
    pip install opentelemetry-exporter-otlp==1.25.0  
    

## Quick Start​

Get your Logfire token from [Logfire](https://logfire.pydantic.dev/)
    
    
    litellm.callbacks = ["logfire"]  
    
    
    
    # pip install logfire  
    import litellm  
    import os  
      
    # from https://logfire.pydantic.dev/  
    os.environ["LOGFIRE_TOKEN"] = ""  
      
    # LLM API Keys  
    os.environ['OPENAI_API_KEY']=""  
      
    # set logfire as a callback, litellm will send the data to logfire  
    litellm.success_callback = ["logfire"]  
      
    # openai call  
    response = litellm.completion(  
      model="gpt-3.5-turbo",  
      messages=[  
        {"role": "user", "content": "Hi 👋 - i'm openai"}  
      ]  
    )  
    

## Support & Talk to Founders​

  * [Schedule Demo 👋](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version)
  * [Community Discord 💭](https://discord.gg/wuPM9dRgDw)
  * Our numbers 📞 +1 (770) 8783-106 / ‭+1 (412) 618-6238‬
  * Our emails ✉️ [ishaan@berri.ai](mailto:ishaan@berri.ai) / [krrish@berri.ai](mailto:krrish@berri.ai)

  * Pre-Requisites
  * Quick Start
  * Support & Talk to Founders