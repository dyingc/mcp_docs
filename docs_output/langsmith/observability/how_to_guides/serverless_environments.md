# Trace JS functions in serverless environments | 🦜️🛠️ LangSmith

On this page  
  
note

This section is relevant for those using the LangSmith JS SDK version 0.2.0 and higher. If you are tracing using LangChain.js or LangGraph.js in serverless environments, see [this guide](https://js.langchain.com/docs/how_to/callbacks_serverless).

When tracing JavaScript functions, LangSmith will trace runs in the background by default to avoid adding latency. In serverless environments where the execution context may be terminated abruptly, it's important to ensure that all tracing data is properly flushed before the function completes.

To make sure this occurs, you can either:

  * Set an environment variable named `LANGSMITH_TRACING_BACKGROUND` to `"false"`. This will cause your traced functions to wait for tracing to complete before returning.
    * Note that this is named differently from the [environment variable](https://js.langchain.com/docs/how_to/callbacks_serverless) in LangChain.js because LangSmith can be used without LangChain.
  * Pass a custom client into your traced runs and `await` the `client.awaitPendingTraceBatches();` method.

Here's an example of using `awaitPendingTraceBatches` alongside the [`traceable`](/observability/how_to_guides/annotate_code) method:
    
    
    import { Client } from "langsmith";  
    import { traceable } from "langsmith/traceable";  
      
    const langsmithClient = new Client({});  
      
    const tracedFn = traceable(  
      async () => {  
        return "Some return value";  
      },  
      {  
        client: langsmithClient,  
      }  
    );  
      
    const res = await tracedFn();  
      
    await langsmithClient.awaitPendingTraceBatches();  
    

## Rate limits at high concurrency​

By default, the LangSmith client will batch operations as your traced run executions, sending a new batch every few milliseconds.

This works well in most situations, but if your traced function is long-running and you have very high concurrency, you may also hit rate limits related to overall request count.

If you are seeing rate limit errors related to this, you can try setting `manualFlushMode: true` in your client like this:
    
    
    import { Client } from "langsmith";  
      
    const langsmithClient = new Client({  
      manualFlushMode: true,  
    });  
      
    const myTracedFunc = traceable(  
      async () => {  
        // Your logic here...  
      },  
      { client: langsmithClient }  
    );  
    

And then manually calling `client.flush()` like this before your serverless function closes:
    
    
    try {  
      await myTracedFunc();  
    } finally {  
      await langsmithClient.flush();  
    }  
    

Note that this will prevent runs from appearing in the LangSmith UI until you call `.flush()`.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Rate limits at high concurrency

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)