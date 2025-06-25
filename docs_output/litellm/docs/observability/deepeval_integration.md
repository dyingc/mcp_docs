# 🔭 DeepEval - Open-Source Evals with Tracing | liteLLM

On this page

### What is DeepEval?​

[DeepEval](https://deepeval.com) is an open-source evaluation framework for LLMs ([Github](https://github.com/confident-ai/deepeval)).

### What is Confident AI?​

[Confident AI](https://documentation.confident-ai.com) (the _**deepeval**_ platfrom) offers an Observatory for teams to trace and monitor LLM applications. Think Datadog for LLM apps. The observatory allows you to:

  * Detect and debug issues in your LLM applications in real-time
  * Search and analyze historical generation data with powerful filters
  * Collect human feedback on model responses
  * Run evaluations to measure and improve performance
  * Track costs and latency to optimize resource usage

### Quickstart​
    
    
    import os  
    import time  
    import litellm  
      
      
    os.environ['OPENAI_API_KEY']='<your-openai-api-key>'  
    os.environ['CONFIDENT_API_KEY']='<your-confident-api-key>'  
      
    litellm.success_callback = ["deepeval"]  
    litellm.failure_callback = ["deepeval"]  
      
    try:  
        response = litellm.completion(  
            model="gpt-3.5-turbo",  
            messages=[  
                {"role": "user", "content": "What's the weather like in San Francisco?"}  
            ],  
        )  
    except Exception as e:  
        print(e)  
      
    print(response)  
    

info

You can obtain your `CONFIDENT_API_KEY` by logging into [Confident AI](https://app.confident-ai.com/project) platform.

## Support & Talk with Deepeval team​

  * [Confident AI Docs 📝](https://documentation.confident-ai.com)
  * [Platform 🚀](https://confident-ai.com)
  * [Community Discord 💭](https://discord.gg/wuPM9dRgDw)
  * Support ✉️ [support@confident-ai.com](mailto:support@confident-ai.com)

  * What is DeepEval?
  * What is Confident AI?
  * Quickstart
  * Support & Talk with Deepeval team