# Log user feedback using the SDK | 🦜️🛠️ LangSmith

On this page

Key concepts

  * [Conceptual guide on tracing and feedback](/observability/concepts)
  * [Reference guide on feedback data format](/reference/data_formats/feedback_data_format)

LangSmith makes it easy to attach feedback to traces. This feedback can come from users, annotators, automated evaluators, etc., and is crucial for monitoring and evaluating applications.

## Use [create_feedback()](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client#langsmith.client.Client.create_feedback) / [createFeedback()](https://docs.smith.langchain.com/reference/js/classes/client.Client#createfeedback)​

Here we'll walk through how to log feedback using the SDK.

Child runs

You can attach user feedback to ANY child run of a trace, not just the trace (root run) itself. This is useful for critiquing specific steps of the LLM application, such as the retrieval step or generation step of a RAG pipeline.

Non-blocking creation (Python only)

The Python client will automatically background feedback creation if you pass `trace_id=` to [create_feedback()](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client#langsmith.client.Client.create_feedback). This is essential for low-latency environments, where you want to make sure your application isn't blocked on feedback creation.

  * Python
  * TypeScript

Requires `langsmith >= 0.3.43`
    
    
    from langsmith import trace, traceable, Client  
      
    @traceable  
    def foo(x):  
        return {"y": x * 2}  
      
    @traceable  
    def bar(y):  
        return {"z": y - 1}  
      
    client = Client()  
      
    inputs = {"x": 1}  
    with trace(name="foobar", inputs=inputs) as root_run:  
        result = foo(**inputs)  
        result = bar(**result)  
        root_run.outputs = result  
        trace_id = root_run.id  
        child_runs = root_run.child_runs  
      
    # Provide feedback for a trace (a.k.a. a root run)  
    client.create_feedback(  
        key="user_feedback",  
        score=1,  
        trace_id=trace_id,  
        comment="the user said that ..."  
    )  
      
    # Provide feedback for a child run  
    foo_run_id = [run for run in child_runs if run.name == "foo"][0].id  
    client.create_feedback(  
        key="correctness",  
        score=0,  
        run_id=foo_run_id,  
        # trace_id= is optional but recommended to enable batched and backgrounded   
        # feedback ingestion.  
        trace_id=trace_id,  
    )  
    
    
    
    import { Client } from "langsmith";  
    const client = new Client();  
      
    // ... Run your application and get the run_id...  
    // This information can be the result of a user-facing feedback form  
      
    await client.createFeedback(  
    runId,  
    "feedback-key",  
    {  
        score: 1.0,  
        comment: "comment",  
    }  
    );  
    

You can even log feedback for in-progress runs using `create_feedback() / createFeedback()`. See [this guide](/observability/how_to_guides/access_current_span) for how to get the run ID of an in-progress run.

To learn more about how to filter traces based on various attributes, including user feedback, see [this guide](/observability/how_to_guides/filter_traces_in_application).

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Use create_feedback() / createFeedback()

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)