# Trace with Instructor (Python only) | 🦜️🛠️ LangSmith

We provide a convenient integration with [Instructor](https://jxnl.github.io/instructor/), a popular open-source library for generating structured outputs with LLMs.

In order to use, you first need to set your LangSmith API key.
    
    
    export LANGSMITH_API_KEY=<your-api-key>  
    

Next, you will need to install the LangSmith SDK:
    
    
    pip install -U langsmith  
    

Wrap your OpenAI client with `langsmith.wrappers.wrap_openai`
    
    
    from openai import OpenAI  
    from langsmith import wrappers  
      
    client = wrappers.wrap_openai(OpenAI())  
    

After this, you can patch the wrapped OpenAI client using `instructor`:
    
    
    import instructor  
      
    client = instructor.patch(client)  
    

Now, you can use `instructor` as you normally would, but now everything is logged to LangSmith!
    
    
    from pydantic import BaseModel  
      
      
    class UserDetail(BaseModel):  
        name: str  
        age: int  
      
      
    user = client.chat.completions.create(  
        model="gpt-4o-mini",  
        response_model=UserDetail,  
        messages=[  
            {"role": "user", "content": "Extract Jason is 25 years old"},  
        ]  
    )  
    

Oftentimes, you use `instructor` inside of other functions. You can get nested traces by using this wrapped client and decorating those functions with `@traceable`. Please see [this guide](/observability/how_to_guides/annotate_code) for more information on how to annotate your code for tracing with the `@traceable` decorator.
    
    
    # You can customize the run name with the `name` keyword argument  
    @traceable(name="Extract User Details")  
    def my_function(text: str) -> UserDetail:  
        return client.chat.completions.create(  
            model="gpt-4o-mini",  
            response_model=UserDetail,  
            messages=[  
                {"role": "user", "content": f"Extract {text}"},  
            ]  
        )  
      
      
    my_function("Jason is 25 years old")  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)