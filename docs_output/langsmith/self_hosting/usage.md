# Using your self-hosted instance of LangSmith | 🦜️🛠️ LangSmith

On this page

This guide will walk you through the process of using your self-hosted instance of LangSmith.

Self-Hosted LangSmith Instance Required

This guide assumes you have already deployed a self-hosted LangSmith instance. If you have not, please refer to the [kubernetes deployment guide](/self_hosting/installation/kubernetes) or the [docker deployment guide](/self_hosting/installation/docker).

### Configuring the application you want to use with LangSmith​

LangSmith has a single API for interacting with both the hub and the LangSmith backend.

  1. Once you have deployed your instance, you can access the LangSmith UI at `http://<host>`.
  2. The LangSmith API will be available at `http://<host>/api/v1`

To use the API of your instance, you will need to set the following environment variables in your application:
    
    
    LANGSMITH_ENDPOINT=http://<host>/api/v1  
    LANGSMITH_API_KEY=foo # Set to a legitimate API key if using OAuth  
    

You can also configure these variables directly in the LangSmith SDK client:
    
    
    import langsmith  
      
    langsmith_client = langsmith.Client(  
        api_key='<api_key>',  
        api_url='http://<host>/api/v1',  
    )  
    

After setting the above, you should be able to run your code and see the results in your self-hosted instance. We recommend running through the [_quickstart guide_](https://docs.smith.langchain.com/#quick-start) to get a feel for how to use LangSmith.

### API Reference​

To access the API reference, navigate to `http://<host>/api/docs` in your browser.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Configuring the application you want to use with LangSmith
  * API Reference

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)