# Add metadata and tags to traces | 🦜️🛠️ LangSmith

LangSmith supports sending arbitrary metadata and tags along with traces.

Tags are strings that can be used to categorize or label a trace. Metadata is a dictionary of key-value pairs that can be used to store additional information about a trace.

Both are useful for associating additional information with a trace, such as the environment in which it was executed, the user who initiated it, or an internal correlation ID. For more information on tags and metadata, see the [Concepts](/observability/concepts#tags) page. For information on how to query traces and runs by metadata and tags, see the [Filter traces in the application](/observability/how_to_guides/filter_traces_in_application) page.

  * Python
  * TypeScript

    
    
    import openai  
    import langsmith as ls  
    from langsmith.wrappers import wrap_openai  
    client = openai.Client()  
      
    messages = [  
      {"role": "system", "content": "You are a helpful assistant."},  
      {"role": "user", "content": "Hello!"}  
    ]  
      
    # You can set metadata & tags **statically** when decorating a function  
    # Use the @traceable decorator with tags and metadata  
    # Ensure that the LANGSMITH_TRACING environment variables are set for @traceable to work  
    @ls.traceable(  
      run_type="llm",  
      name="OpenAI Call Decorator",  
      tags=["my-tag"],  
      metadata={"my-key": "my-value"}  
    )  
    def call_openai(  
      messages: list[dict], model: str = "gpt-4o-mini"  
    ) -> str:  
      # You can also dynamically set metadata on the parent run:  
      rt = ls.get_current_run_tree()  
      rt.metadata["some-conditional-key"] = "some-val"  
      rt.tags.extend(["another-tag"])  
      return client.chat.completions.create(  
          model=model,  
          messages=messages,  
      ).choices[0].message.content  
      
    call_openai(  
      messages,  
      # To add at **invocation time**, when calling the function.  
      # via the langsmith_extra parameter  
      langsmith_extra={"tags": ["my-other-tag"], "metadata": {"my-other-key": "my-value"}}  
    )  
      
    # Alternatively, you can use the context manager  
    with ls.trace(  
          name="OpenAI Call Trace",  
          run_type="llm",  
          inputs={"messages": messages},  
          tags=["my-tag"],  
          metadata={"my-key": "my-value"},  
      ) as rt:  
          chat_completion = client.chat.completions.create(  
              model="gpt-4o-mini",  
              messages=messages,  
          )  
          rt.metadata["some-conditional-key"] = "some-val"  
          rt.end(outputs={"output": chat_completion})  
      
      
    # You can use the same techniques with the wrapped client  
    patched_client = wrap_openai(  
      client, tracing_extra={"metadata": {"my-key": "my-value"}, "tags": ["a-tag"]}  
    )  
    chat_completion = patched_client.chat.completions.create(  
      model="gpt-4o-mini",  
      messages=messages,  
      langsmith_extra={  
          "tags": ["my-other-tag"],  
          "metadata": {"my-other-key": "my-value"},  
      },  
    )  
    
    
    
    import OpenAI from "openai";  
    import { traceable, getCurrentRunTree } from "langsmith/traceable";  
    import { wrapOpenAI } from "langsmith/wrappers";  
      
    const client = wrapOpenAI(new OpenAI());  
      
    const messages: OpenAI.Chat.ChatCompletionMessageParam[] = [  
    { role: "system", content: "You are a helpful assistant." },  
    { role: "user", content: "Hello!" },  
    ];  
      
    const traceableCallOpenAI = traceable(  
    async (messages: OpenAI.Chat.ChatCompletionMessageParam[]) => {  
    const completion = await client.chat.completions.create({  
    model: "gpt-4o-mini",  
    messages,  
    });  
    const runTree = getCurrentRunTree();  
    runTree.extra.metadata = {  
    ...runTree.extra.metadata,  
    someKey: "someValue",  
    };  
    runTree.tags = [...(runTree.tags ?? []), "runtime-tag"];  
    return completion.choices[0].message.content;  
    },  
    {  
    run_type: "llm",  
    name: "OpenAI Call Traceable",  
    tags: ["my-tag"],  
    metadata: { "my-key": "my-value" },  
    }  
    );  
    // Call the traceable function  
    await traceableCallOpenAI(messages);  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)