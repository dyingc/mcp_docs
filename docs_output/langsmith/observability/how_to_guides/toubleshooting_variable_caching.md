# Toubleshooting variable caching | 🦜️🛠️ LangSmith

On this page

If you’re not seeing traces in your tracing project or notice traces logged to the wrong project/workspace, the issue might be due to LangSmith’s default environment variable caching. This is especially common when running LangSmith within a Jupyter notebook. Follow these steps to diagnose and resolve the issue:

## 1\. Verify Your Environment Variables​

First, check that the environment variables are set correctly by running:
    
    
    import os  
      
    print(os.getenv("LANGSMITH_PROJECT"))  
    print(os.getenv("LANGSMITH_TRACING_V2"))  
    print(os.getenv("LANGSMITH_ENDPOINT"))  
    print(os.getenv("LANGSMITH_API_KEY"))  
    

If the output does not match what’s defined in your .env file, it’s likely due to environment variable caching.

## 2\. Clear the cache​

Clear the cached environment variables with the following command:
    
    
    utils.get_env_var.cache_clear()  
    

## 3\. Reload the Environment Variables​

Reload your environment variables from the .env file by executing:
    
    
    from dotenv import load_dotenv  
    import os  
    load_dotenv(<path to .env file>, override=True)  
    

After reloading, your environment variables should be set correctly.

If you continue to experience issues, please reach out to us via a shared Slack channel or email support (available for Plus and Enterprise plans), or in [LangChain's community Slack](https://langchaincommunity.slack.com/)(sign up [here](https://www.langchain.com/join-community) if you're not already a member).

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * 1\. Verify Your Environment Variables
  * 2\. Clear the cache
  * 3\. Reload the Environment Variables

  *[/]: Positional-only parameter separator (PEP 570)