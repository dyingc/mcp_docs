# How to handle model rate limits | 🦜️🛠️ LangSmith

On this page

A common issue when running large evaluation jobs is running into third-party API rate limits, usually from model providers. There are a few ways to deal with rate limits.

## Using `langchain` RateLimiters (Python only)​

If you're using `langchain` Python ChatModels in your application or evaluators, you can add rate limiters to your model(s) that will add client-side control of the frequency with which requests are sent to the model provider API to avoid rate limit errors.

  * Python

    
    
    from langchain.chat_models import init_chat_model  
    from langchain_core.rate_limiters import InMemoryRateLimiter  
      
    rate_limiter = InMemoryRateLimiter(  
        requests_per_second=0.1,  # <-- Super slow! We can only make a request once every 10 seconds!!  
        check_every_n_seconds=0.1,  # Wake up every 100 ms to check whether allowed to make a request,  
        max_bucket_size=10,  # Controls the maximum burst size.  
    )  
      
    llm = init_chat_model("gpt-4o", rate_limiter=rate_limiter)  
      
    def app(inputs: dict) -> dict:  
        response = llm.invoke(...)  
        ...  
      
    def evaluator(inputs: dict, outputs: dict, reference_outputs: dict) -> dict:  
        response = llm.invoke(...)  
        ...  
    

See the [langchain](https://python.langchain.com/docs/how_to/chat_model_rate_limiting/) documentation for more on how to configure rate limiters.

## Retrying with exponential backoff​

A very common way to deal with rate limit errors is retrying with exponential backoff. Retrying with exponential backoff means repeatedly retrying failed requests with an (exponentially) increasing wait time between each retry. This continues until either the request succeeds or a maximum number of requests is made.

#### With `langchain`​

If you're using `langchain` components you can add retries to all model calls with the `.with_retry(...)` / `.withRetry()` method:

  * Python
  * TypeScript

    
    
    from langchain import init_chat_model  
      
    llm_with_retry = init_chat_model("gpt-4o-mini").with_retry(stop_after_attempt=6)  
    
    
    
    import { initChatModel } from "langchain/chat_models/universal";  
      
    const llm = await initChatModel("gpt-4o", {  
        modelProvider: "openai",  
    });  
      
    const llmWithRetry = llm.withRetry({ stopAfterAttept: 2 });  
    

See the `langchain` [Python](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel.with_retry) and [JS](https://v03.api.js.langchain.com/classes/_langchain_core.language_models_chat_models.BaseChatModel.html#withRetry) API references for more.

#### Without `langchain`​

If you're not using `langchain` you can use other libraries like `tenacity` (Python) or `backoff` (Python) to implement retries with exponential backoff, or you can implement it from scratch. See some examples of how to do this in the [OpenAI docs](https://platform.openai.com/docs/guides/rate-limits#retrying-with-exponential-backoff).

## Limiting max_concurrency​

Limiting the number of concurrent calls you're making to your application and evaluators is another way to decrease the frequency of model calls you're making, and in that way avoid rate limit errors. `max_concurrency` can be set directly on the [evaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate) / [aevaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._arunner.aevaluate) functions. This parallelizes evaluation by effectively splitting the dataset across threads.

  * Python
  * TypeScript

    
    
    from langsmith import aevaluate  
        
    results = await aevaluate(  
        ...  
        max_concurrency=4,  
    )  
    
    
    
    import { evaluate } from "langsmith/evaluation";  
      
    await evaluate(..., {  
      ...,  
      maxConcurrency: 4,  
    });  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Using `langchain` RateLimiters (Python only)
  * Retrying with exponential backoff
  * Limiting max_concurrency

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)