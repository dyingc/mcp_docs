# Log traces to specific project | 🦜️🛠️ LangSmith

On this page

You can change the destination project of your traces both statically through environment variables and dynamically at runtime.

## Set the destination project statically​

As mentioned in the [Tracing Concepts](/observability/concepts#projects) section, LangSmith uses the concept of a `Project` to group traces. If left unspecified, the project is set to `default`. You can set the `LANGSMITH_PROJECT` environment variable to configure a custom project name for an entire application run. This should be done before executing your application.
    
    
    export LANGSMITH_PROJECT=my-custom-project  
    

SDK compatibility in JS

The `LANGSMITH_PROJECT` flag is only supported in JS SDK versions >= 0.2.16, use `LANGCHAIN_PROJECT` instead if you are using an older version.

If the project specified does not exist, it will be created automatically when the first trace is ingested.

## Set the destination project dynamically​

You can also set the project name at program runtime in various ways, depending on how you are [annotating your code for tracing](/observability/how_to_guides/annotate_code). This is useful when you want to log traces to different projects within the same application.

note

Setting the project name dynamically using one of the below methods overrides the project name set by the `LANGSMITH_PROJECT` environment variable.

  * Python
  * TypeScript

    
    
    import openai  
    from langsmith import traceable  
    from langsmith.run_trees import RunTree  
      
    client = openai.Client()  
      
    messages = [  
      {"role": "system", "content": "You are a helpful assistant."},  
      {"role": "user", "content": "Hello!"}  
    ]  
      
    # Use the @traceable decorator with the 'project_name' parameter to log traces to LangSmith  
    # Ensure that the LANGSMITH_TRACING environment variables is set for @traceable to work  
    @traceable(  
      run_type="llm",  
      name="OpenAI Call Decorator",  
      project_name="My Project"  
    )  
    def call_openai(  
      messages: list[dict], model: str = "gpt-4o-mini"  
    ) -> str:  
      return client.chat.completions.create(  
          model=model,  
          messages=messages,  
      ).choices[0].message.content  
      
    # Call the decorated function  
    call_openai(messages)  
      
    # You can also specify the Project via the project_name parameter  
    # This will override the project_name specified in the @traceable decorator  
    call_openai(  
      messages,  
      langsmith_extra={"project_name": "My Overridden Project"},  
    )  
      
    # The wrapped OpenAI client accepts all the same langsmith_extra parameters  
    # as @traceable decorated functions, and logs traces to LangSmith automatically.  
    # Ensure that the LANGSMITH_TRACING environment variables is set for the wrapper to work.  
    from langsmith import wrappers  
    wrapped_client = wrappers.wrap_openai(client)  
    wrapped_client.chat.completions.create(  
      model="gpt-4o-mini",  
      messages=messages,  
      langsmith_extra={"project_name": "My Project"},  
    )  
      
      
    # Alternatively, create a RunTree object  
    # You can set the project name using the project_name parameter  
    rt = RunTree(  
      run_type="llm",  
      name="OpenAI Call RunTree",  
      inputs={"messages": messages},  
      project_name="My Project"  
    )  
    chat_completion = client.chat.completions.create(  
      model="gpt-4o-mini",  
      messages=messages,  
    )  
    # End and submit the run  
    rt.end(outputs=chat_completion)  
    rt.post()  
    
    
    
    import OpenAI from "openai";  
    import { traceable } from "langsmith/traceable";  
    import { wrapOpenAI } from "langsmith/wrappers";  
    import { RunTree} from "langsmith";  
      
    const client = new OpenAI();  
      
    const messages = [  
      {role: "system", content: "You are a helpful assistant."},  
      {role: "user", content: "Hello!"}  
    ];  
      
    const traceableCallOpenAI = traceable(async (messages: {role: string, content: string}[], model: string) => {  
      const completion = await client.chat.completions.create({  
          model: model,  
          messages: messages,  
      });  
      return completion.choices[0].message.content;  
    },{  
      run_type: "llm",  
      name: "OpenAI Call Traceable",  
      project_name: "My Project"  
    });  
    // Call the traceable function  
    await traceableCallOpenAI(messages, "gpt-4o-mini");  
      
    // Create and use a RunTree object  
    const rt = new RunTree({  
      run_type: "llm",  
      name: "OpenAI Call RunTree",  
      inputs: { messages },  
      project_name: "My Project"  
    });  
    await rt.postRun();  
      
    // Execute a chat completion and handle it within RunTree  
    rt.end({outputs: chatCompletion});  
    await rt.patchRun();  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Set the destination project statically
  * Set the destination project dynamically

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)