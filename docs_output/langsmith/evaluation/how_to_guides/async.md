# How to run an evaluation asynchronously | 🦜️🛠️ LangSmith

On this page

Key concepts

[Evaluations](/evaluation/concepts#applying-evaluations) | [Evaluators](/evaluation/concepts#evaluators) | [Datasets](/evaluation/concepts#datasets) | [Experiments](/evaluation/concepts#experiments)

We can run evaluations asynchronously via the SDK using [aevaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._arunner.aevaluate), which accepts all of the same arguments as [evaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate) but expects the application function to be asynchronous. You can learn more about how to use the `evaluate()` function [here](/evaluation/how_to_guides/evaluate_llm_application).

Python only

This guide is only relevant when using the Python SDK. In JS/TS the `evaluate()` function is already async. You can see how to use it [here](/evaluation/how_to_guides/evaluate_llm_application).

## Use `aevaluate()`​

  * Python

Requires `langsmith>=0.3.13`
    
    
    from langsmith import wrappers, Client  
    from openai import AsyncOpenAI  
      
    # Optionally wrap the OpenAI client to trace all model calls.  
    oai_client = wrappers.wrap_openai(AsyncOpenAI())  
      
    # Optionally add the 'traceable' decorator to trace the inputs/outputs of this function.  
    @traceable  
    async def researcher_app(inputs: dict) -> str:  
        instructions = """You are an excellent researcher. Given a high-level research idea, \  
      
    list 5 concrete questions that should be investigated to determine if the idea is worth pursuing."""  
      
        response = await oai_client.chat.completions.create(  
            model="gpt-4o-mini",  
            messages=[  
                {"role": "system", "content": instructions},  
                {"role": "user", "content": inputs["idea"]},  
            ],  
        )  
        return response.choices[0].message.content  
      
    # Evaluator functions can be sync or async  
    def concise(inputs: dict, outputs: dict) -> bool:  
        return len(outputs["output"]) < 3 * len(inputs["idea"])  
      
    ls_client = Client()  
      
    ideas = [  
        "universal basic income",   
        "nuclear fusion",   
        "hyperloop",   
        "nuclear powered rockets",  
    ]  
    dataset = ls_client.create_dataset("research ideas")  
    ls_client.create_examples(  
        dataset_name=dataset.name,  
        examples=[{"inputs": {"idea": i}} for i in ideas],  
    )  
      
    # Can equivalently use the 'aevaluate' function directly:  
    # from langsmith import aevaluate  
    # await aevaluate(...)  
    results = await ls_client.aevaluate(  
        researcher_app,  
        data=dataset,  
        evaluators=[concise],  
        # Optional, add concurrency.  
        max_concurrency=2,  # Optional, add concurrency.  
        experiment_prefix="gpt-4o-mini-baseline"  # Optional, random by default.  
    )  
    

## Related​

  * [Run an evaluation (synchronously)](/evaluation/how_to_guides/evaluate_llm_application)
  * [Handle model rate limits](/evaluation/how_to_guides/rate_limiting)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Use `aevaluate()`
  * Related

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)