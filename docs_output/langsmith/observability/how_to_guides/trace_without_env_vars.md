# Trace without setting environment variables | 🦜️🛠️ LangSmith

As mentioned in other guides, the following environment variables allow you to configure tracing enabled, the api endpoint, the api key, and the tracing project:

  * `LANGSMITH_TRACING`
  * `LANGSMITH_API_KEY`
  * `LANGSMITH_ENDPOINT`
  * `LANGSMITH_PROJECT`

In some environments, it is not possible to set environment variables. In these cases, you can set the tracing configuration programmatically.

Recently changed behavior

Due to a number of asks for finer-grained control of tracing using the `trace` context manager, **we changed the behavior** of `with trace` to honor the `LANGSMITH_TRACING` environment variable in version **0.1.95** of the Python SDK. You can find more details in the [release notes](https://github.com/langchain-ai/langsmith-sdk/releases/tag/v0.1.95). The recommended way to disable/enable tracing without setting environment variables is to use the `with tracing_context` context manager, as shown in the example below.

  * Python
  * TypeScript

The recommended way to do this in Python is to use the `tracing_context` context manager. This works for both code annotated with `traceable` and code within the `trace` context manager.
    
    
    import openai  
    from langsmith import Client, tracing_context, traceable  
    from langsmith.wrappers import wrap_openai  
      
    langsmith_client = Client(  
      api_key="YOUR_LANGSMITH_API_KEY",  # This can be retrieved from a secrets manager  
      api_url="https://api.smith.langchain.com",  # Update appropriately for self-hosted installations or the EU region  
    )  
      
    client = wrap_openai(openai.Client())  
      
    @traceable(run_type="tool", name="Retrieve Context")  
    def my_tool(question: str) -> str:  
      return "During this morning's meeting, we solved all world conflict."  
      
    @traceable  
    def chat_pipeline(question: str):  
      context = my_tool(question)  
      messages = [  
          { "role": "system", "content": "You are a helpful assistant. Please respond to the user's request only based on the given context." },  
          { "role": "user", "content": f"Question: {question}  
    Context: {context}"}  
      ]  
      chat_completion = client.chat.completions.create(  
          model="gpt-4o-mini", messages=messages  
      )  
      return chat_completion.choices[0].message.content  
      
    # Can set to False to disable tracing here without changing code structure  
    with tracing_context(enabled=True):  
      # Use langsmith_extra to pass in a custom client  
      chat_pipeline("Can you summarize this morning's meetings?", langsmith_extra={"client": langsmith_client})  
    

In TypeScript, you can pass in both the client and the `tracingEnabled` flag to the `traceable` decorator.
    
    
    import { Client } from "langsmith";  
    import { traceable } from "langsmith/traceable";  
    import { wrapOpenAI } from "langsmith/wrappers";  
    import { OpenAI } from "openai";  
      
    const client = new Client({  
        apiKey: "YOUR_API_KEY",  // This can be retrieved from a secrets manager  
        apiUrl: "https://api.smith.langchain.com",  // Update appropriately for self-hosted installations or the EU region  
    });  
      
    const openai = wrapOpenAI(new OpenAI());  
      
    const tool = traceable((question: string) => {  
        return "During this morning's meeting, we solved all world conflict.";  
    }, { name: "Retrieve Context", runType: "tool" });  
      
    const pipeline = traceable(  
        async (question: string) => {  
            const context = await tool(question);  
              
            const completion = await openai.chat.completions.create({  
                model: "gpt-4o-mini",  
                messages: [  
                    { role: "system" as const, content: "You are a helpful assistant. Please respond to the user's request only based on the given context." },  
                    { role: "user" as const, content: `Question: ${question}\nContext: ${context}`}  
                ]  
            });  
              
            return completion.choices[0].message.content;  
          
        },   
        { name: "Chat", client, tracingEnabled: true }  
    );  
      
    await pipeline("Can you summarize this morning's meetings?");  
    

If you prefer a video tutorial, check out the [Alternative Ways to Trace video](https://academy.langchain.com/pages/intro-to-langsmith-preview) from the Introduction to LangSmith Course.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)