# Query traces | 🦜️🛠️ LangSmith

On this page

Recommended Reading

Before diving into this content, it might be helpful to read the following:

  * [Run (span) data format](/reference/data_formats/run_data_format)
  * [LangSmith API Reference](https://api.smith.langchain.com/redoc)
  * [LangSmith trace query syntax](/reference/data_formats/trace_query_syntax)

note

If you are looking to export a large volume of traces, we recommend that you use the [Bulk Data Export](/observability/how_to_guides/data_export) functionality, as it will better handle large data volumes and will support automatic retries and parallelization across partitions.

The recommended way to query runs (the span data in LangSmith traces) is to use the `list_runs` method in the SDK or `/runs/query` endpoint in the API.

LangSmith stores traces in a simple format that is specified in the [Run (span) data format](/reference/data_formats/run_data_format).

## Use filter arguments​

For simple queries, you don't have to rely on our query syntax. You can use the filter arguments specified in the [filter arguments reference](/reference/data_formats/trace_query_syntax#filter-arguments).

Prerequisites

Initialize the client before running the below code snippets.

  * Python
  * TypeScript

    
    
    from langsmith import Client  
      
    client = Client()  
    
    
    
    import { Client, Run } from "langsmith";  
      
    const client = new Client();  
    

Below are some examples of ways to list runs using keyword arguments:

### List all runs in a project​

  * Python
  * TypeScript

    
    
    project_runs = client.list_runs(project_name="<your_project>")  
    
    
    
    // Download runs in a project  
    const projectRuns: Run[] = [];  
    for await (const run of client.listRuns({  
    projectName: "<your_project>",  
    })) {  
    projectRuns.push(run);  
    };  
    

### List LLM and Chat runs in the last 24 hours​

  * Python
  * TypeScript

    
    
    todays_llm_runs = client.list_runs(  
      project_name="<your_project>",  
      start_time=datetime.now() - timedelta(days=1),  
      run_type="llm",  
    )  
    
    
    
    const todaysLlmRuns: Run[] = [];  
    for await (const run of client.listRuns({  
    projectName: "<your_project>",  
    startTime: new Date(Date.now() - 1000 * 60 * 60 * 24),  
    runType: "llm",  
    })) {  
    todaysLlmRuns.push(run);  
    };  
    

### List root runs in a project​

Root runs are runs that have no parents. These are assigned a value of `True` for `is_root`. You can use this to filter for root runs.

  * Python
  * TypeScript

    
    
    root_runs = client.list_runs(  
      project_name="<your_project>",  
      is_root=True  
    )  
    
    
    
    const rootRuns: Run[] = [];  
    for await (const run of client.listRuns({  
    projectName: "<your_project>",  
    isRoot: 1,  
    })) {  
    rootRuns.push(run);  
    };  
    

### List runs without errors​

  * Python
  * TypeScript

    
    
    correct_runs = client.list_runs(project_name="<your_project>", error=False)  
    
    
    
    const correctRuns: Run[] = [];  
    for await (const run of client.listRuns({  
    projectName: "<your_project>",  
    error: false,  
    })) {  
    correctRuns.push(run);  
    };  
    

### List runs by run ID​

Ignores Other Arguments

If you provide a list of run IDs in the way described above, it will ignore all other filtering arguments like `project_name`, `run_type`, etc. and directly return the runs matching the given IDs.

If you have a list of run IDs, you can list them directly:

  * Python
  * TypeScript

    
    
    run_ids = ['a36092d2-4ad5-4fb4-9c0d-0dba9a2ed836','9398e6be-964f-4aa4-8ae9-ad78cd4b7074']  
    selected_runs = client.list_runs(id=run_ids)  
    
    
    
    const runIds = [  
    "a36092d2-4ad5-4fb4-9c0d-0dba9a2ed836",  
    "9398e6be-964f-4aa4-8ae9-ad78cd4b7074",  
    ];  
    const selectedRuns: Run[] = [];  
    for await (const run of client.listRuns({  
    id: runIds,  
    })) {  
    selectedRuns.push(run);  
    };  
    

## Use filter query language​

For more complex queries, you can use the query language described in the [filter query language reference](/reference/data_formats/trace_query_syntax#filter-query-language).

### List all root runs in a conversational thread​

This is the way to fetch runs in a conversational thread. For more information on setting up threads, refer to our [how-to guide on setting up threads](/observability/how_to_guides/threads). Threads are grouped by setting a shared thread ID. The LangSmith UI lets you use any one of the following three metadata keys: `session_id`, `conversation_id`, or `thread_id`. The following query matches on any of them.

  * Python
  * TypeScript

    
    
    group_key = "<your_thread_id>"  
    filter_string = f'and(in(metadata_key, ["session_id","conversation_id","thread_id"]), eq(metadata_value, "{group_key}"))'  
    thread_runs = client.list_runs(  
      project_name="<your_project>",  
      filter=filter_string,  
      is_root=True  
    )  
    
    
    
    const groupKey = "<your_thread_id>";  
    const filterString = `and(in(metadata_key, ["session_id","conversation_id","thread_id"]), eq(metadata_value, "${groupKey}"))`;  
    const threadRuns: Run[] = [];  
    for await (const run of client.listRuns({  
    projectName: "<your_project>",  
    filter: filterString,  
    isRoot: true  
    })) {  
    threadRuns.push(run);  
    };  
    

### List all runs called "extractor" whose root of the trace was assigned feedback "user_score" score of 1​

  * Python
  * TypeScript

    
    
    client.list_runs(  
      project_name="<your_project>",  
      filter='eq(name, "extractor")',  
      trace_filter='and(eq(feedback_key, "user_score"), eq(feedback_score, 1))'  
    )  
    
    
    
    client.listRuns({  
    projectName: "<your_project>",  
    filter: 'eq(name, "extractor")',  
    traceFilter: 'and(eq(feedback_key, "user_score"), eq(feedback_score, 1))'  
    })  
    

### List runs with "star_rating" key whose score is greater than 4​

  * Python
  * TypeScript

    
    
    client.list_runs(  
      project_name="<your_project>",  
      filter='and(eq(feedback_key, "star_rating"), gt(feedback_score, 4))'  
    )  
    
    
    
    client.listRuns({  
    projectName: "<your_project>",  
    filter: 'and(eq(feedback_key, "star_rating"), gt(feedback_score, 4))'  
    })  
    

### List runs that took longer than 5 seconds to complete​

  * Python
  * TypeScript

    
    
    client.list_runs(project_name="<your_project>", filter='gt(latency, "5s")')  
    
    
    
    client.listRuns({projectName: "<your_project>", filter: 'gt(latency, "5s")'})  
    

### List all runs where `total_tokens` is greater than 5000​

  * Python
  * TypeScript

    
    
    client.list_runs(project_name="<your_project>", filter='gt(total_tokens, 5000)')  
    
    
    
    client.listRuns({projectName: "<your_project>", filter: 'gt(total_tokens, 5000)'})  
    

### List all runs that have "error" not equal to null​

  * Python
  * TypeScript

    
    
    client.list_runs(project_name="<your_project>", filter='neq(error, null)')  
    
    
    
    client.listRuns({projectName: "<your_project>", filter: 'neq(error, null)'})  
    

### List all runs where `start_time` is greater than a specific timestamp​

  * Python
  * TypeScript

    
    
    client.list_runs(project_name="<your_project>", filter='gt(start_time, "2023-07-15T12:34:56Z")')  
    
    
    
    client.listRuns({projectName: "<your_project>", filter: 'gt(start_time, "2023-07-15T12:34:56Z")'})  
    

### List all runs that contain the string "substring"​

  * Python
  * TypeScript

    
    
    client.list_runs(project_name="<your_project>", filter='search("substring")')  
    
    
    
    client.listRuns({projectName: "<your_project>", filter: 'search("substring")'})  
    

### List all runs that are tagged with the git hash "2aa1cf4"​

  * Python
  * TypeScript

    
    
    client.list_runs(project_name="<your_project>", filter='has(tags, "2aa1cf4")')  
    
    
    
    client.listRuns({projectName: "<your_project>", filter: 'has(tags, "2aa1cf4")'})  
    

### List all "chain" type runs that took more than 10 seconds and​

had `total_tokens` greater than 5000

  * Python
  * TypeScript

    
    
    client.list_runs(  
    project_name="<your_project>",  
    filter='and(eq(run_type, "chain"), gt(latency, 10), gt(total_tokens, 5000))'  
    )  
    
    
    
    client.listRuns({  
    projectName: "<your_project>",  
    filter: 'and(eq(run_type, "chain"), gt(latency, 10), gt(total_tokens, 5000))'  
    })  
    

### List all runs that started after a specific timestamp and either​

have "error" not equal to null or a "Correctness" feedback score equal to 0

  * Python
  * TypeScript

    
    
    client.list_runs(  
    project_name="<your_project>",  
    filter='and(gt(start_time, "2023-07-15T12:34:56Z"), or(neq(error, null), and(eq(feedback_key, "Correctness"), eq(feedback_score, 0.0))))'  
    )  
    
    
    
    client.listRuns({  
    projectName: "<your_project>",  
    filter: 'and(gt(start_time, "2023-07-15T12:34:56Z"), or(neq(error, null), and(eq(feedback_key, "Correctness"), eq(feedback_score, 0.0))))'  
    })  
    

### Complex query: List all runs where `tags` include "experimental" or "beta" and​

`latency` is greater than 2 seconds

  * Python
  * TypeScript

    
    
    client.list_runs(  
    project_name="<your_project>",  
    filter='and(or(has(tags, "experimental"), has(tags, "beta")), gt(latency, 2))'  
    )  
    
    
    
    client.listRuns({  
    projectName: "<your_project>",  
    filter: 'and(or(has(tags, "experimental"), has(tags, "beta")), gt(latency, 2))'  
    })  
    

### Search trace trees by full text You can use the `search()` function without​

any specific field to do a full text search across all string fields in a run. This allows you to quickly find traces that match a search term.

  * Python
  * TypeScript

    
    
    client.list_runs(  
    project_name="<your_project>",  
    filter='search("image classification")'  
    )  
    
    
    
    client.listRuns({  
    projectName: "<your_project>",  
    filter: 'search("image classification")'  
    })  
    

### Check for presence of metadata​

If you want to check for the presence of metadata, you can use the `eq` operator, optionally with an `and` statement to match by value. This is useful if you want to log more structured information about your runs.

  * Python
  * TypeScript

    
    
      
    to_search = {  
      "user_id": ""  
    }  
      
    # Check for any run with the "user_id" metadata key  
    client.list_runs(  
    project_name="default",  
    filter="eq(metadata_key, 'user_id')"  
    )  
    # Check for runs with user_id=4070f233-f61e-44eb-bff1-da3c163895a3  
    client.list_runs(  
    project_name="default",  
    filter="and(eq(metadata_key, 'user_id'), eq(metadata_value, '4070f233-f61e-44eb-bff1-da3c163895a3'))"  
    )  
    
    
    
    // Check for any run with the "user_id" metadata key  
    client.listRuns({  
    projectName: 'default',  
    filter: `eq(metadata_key, 'user_id')`  
    });  
    // Check for runs with user_id=4070f233-f61e-44eb-bff1-da3c163895a3  
    client.listRuns({  
    projectName: 'default',  
    filter: `and(eq(metadata_key, 'user_id'), eq(metadata_value, '4070f233-f61e-44eb-bff1-da3c163895a3'))`  
    });  
    

### Check for environment details in metadata.​

A common pattern is to add environment information to your traces via metadata. If you want to filter for runs containing environment metadata, you can use the same pattern as above:

  * Python
  * TypeScript

    
    
    client.list_runs(  
    project_name="default",  
    filter="and(eq(metadata_key, 'environment'), eq(metadata_value, 'production'))"  
    )  
    
    
    
    client.listRuns({  
    projectName: 'default',  
    filter: `and(eq(metadata_key, 'environment'), eq(metadata_value, 'production'))`  
    });  
    

### Check for conversation ID in metadata​

Another common way to associate traces in the same conversation is by using a shared conversation ID. If you want to filter runs based on a conversation ID in this way, you can search for that ID in the metadata.

  * Python
  * TypeScript

    
    
    client.list_runs(  
    project_name="default",  
    filter="and(eq(metadata_key, 'conversation_id'), eq(metadata_value, 'a1b2c3d4-e5f6-7890'))"  
    )  
    
    
    
    client.listRuns({  
    projectName: 'default',  
    filter: `and(eq(metadata_key, 'conversation_id'), eq(metadata_value, 'a1b2c3d4-e5f6-7890'))`  
    });  
    

### Negative filtering on key-value pairs​

You can use negative filtering on metadata, input, and output key-value pairs to exclude specific runs from your results. Here are some examples for metadata key-value pairs but the same logic applies to input and output key-value pairs.

  * Python
  * TypeScript

    
    
    # Find all runs where the metadata does not contain a "conversation_id" key  
    client.list_runs(  
    project_name="default",  
    filter="and(neq(metadata_key, 'conversation_id'))"  
    )  
      
    # Find all runs where the conversation_id in metadata is not "a1b2c3d4-e5f6-7890"  
      
    client.list_runs(  
    project_name="default",  
    filter="and(eq(metadata_key, 'conversation_id'), neq(metadata_value, 'a1b2c3d4-e5f6-7890'))"  
    )  
      
    # Find all runs where there is no "conversation_id" metadata key and the "a1b2c3d4-e5f6-7890" value is not present  
      
    client.list_runs(  
    project_name="default",  
    filter="and(neq(metadata_key, 'conversation_id'), neq(metadata_value, 'a1b2c3d4-e5f6-7890'))"  
    )  
      
    # Find all runs where the conversation_id metadata key is not present but the "a1b2c3d4-e5f6-7890" value is present  
      
    client.list_runs(  
    project_name="default",  
    filter="and(neq(metadata_key, 'conversation_id'), eq(metadata_value, 'a1b2c3d4-e5f6-7890'))"  
    )  
    
    
    
      
    // Find all runs where the metadata does not contain a "conversation_id" key  
    client.listRuns({  
    projectName: 'default',  
    filter: `and(neq(metadata_key, 'conversation_id'))`  
    });  
      
      // Find all runs where the conversation_id in metadata is not "a1b2c3d4-e5f6-7890"  
      client.listRuns({  
        projectName: 'default',  
        filter: `and(eq(metadata_key, 'conversation_id'), neq(metadata_value, 'a1b2c3d4-e5f6-7890'))`  
      });  
      
      // Find all runs where there is no "conversation_id" metadata key and the "a1b2c3d4-e5f6-7890" value is not present  
      client.listRuns({  
        projectName: 'default',  
        filter: `and(neq(metadata_key, 'conversation_id'), neq(metadata_value, 'a1b2c3d4-e5f6-7890'))`  
      });  
      
      // Find all runs where the conversation_id metadata key is not present but the "a1b2c3d4-e5f6-7890" value is present  
      client.listRuns({  
        projectName: 'default',  
            filter: `and(neq(metadata_key, 'conversation_id'), eq(metadata_value, 'a1b2c3d4-e5f6-7890'))`  
          });  
    

### Combine multiple filters​

If you want to combine multiple conditions to refine your search, you can use the `and` operator along with other filtering functions. Here's how you can search for runs named "ChatOpenAI" that also have a specific `conversation_id` in their metadata:

  * Python
  * TypeScript

    
    
    client.list_runs(  
    project_name="default",  
    filter="and(eq(name, 'ChatOpenAI'), eq(metadata_key, 'conversation_id'), eq(metadata_value, '69b12c91-b1e2-46ce-91de-794c077e8151'))"  
    )  
    
    
    
    client.listRuns({  
    projectName: 'default',  
    filter: `and(eq(name, 'ChatOpenAI'), eq(metadata_key, 'conversation_id'), eq(metadata_value, '69b12c91-b1e2-46ce-91de-794c077e8151'))`  
    });  
    

### Tree Filter​

List all runs named "RetrieveDocs" whose root run has a "user_score" feedback of 1 and any run in the full trace is named "ExpandQuery".

This type of query is useful if you want to extract a specific run conditional on various states or steps being reached within the trace.

  * Python
  * TypeScript

    
    
    client.list_runs(  
      project_name="<your_project>",  
      filter='eq(name, "RetrieveDocs")',  
      trace_filter='and(eq(feedback_key, "user_score"), eq(feedback_score, 1))',  
      tree_filter='eq(name, "ExpandQuery")'  
    )  
    
    
    
    client.listRuns({  
    projectName: "<your_project>",  
    filter: 'eq(name, "RetrieveDocs")',  
    traceFilter: 'and(eq(feedback_key, "user_score"), eq(feedback_score, 1))',  
    treeFilter: 'eq(name, "ExpandQuery")'  
    })  
    

### Advanced: export flattened trace view with child tool usage​

The following Python example demonstrates how to export a flattened view of traces, including information on the tools (from nested runs) used by the agent within each trace. This can be used to analyze the behavior of your agents across multiple traces.

This example queries all tool runs within a specified number of days and groups them by their parent (root) run ID. It then fetches the relevant information for each root run, such as the run name, inputs, outputs, and combines that information with the child run information.

To optimize the query, the example:

  1. Selects only the necessary fields when querying tool runs to reduce query time.
  2. Fetches root runs in batches while processing tool runs concurrently.

  * Python

    
    
    from collections import defaultdict  
    from concurrent.futures import Future, ThreadPoolExecutor  
    from datetime import datetime, timedelta  
      
    from langsmith import Client  
    from tqdm.auto import tqdm  
      
    client = Client()  
    project_name = "my-project"  
    num_days = 30  
      
    # List all tool runs  
    tool_runs = client.list_runs(  
      project_name=project_name,  
      start_time=datetime.now() - timedelta(days=num_days),  
      run_type="tool",  
      # We don't need to fetch inputs, outputs, and other values that # may increase the query time  
      select=["trace_id", "name", "run_type"],  
    )  
      
    data = []  
    futures: list[Future] = []  
    trace_cursor = 0  
    trace_batch_size = 50  
      
    tool_runs_by_parent = defaultdict(lambda: defaultdict(set))  
    # Do not exceed rate limit  
    with ThreadPoolExecutor(max_workers=2) as executor:  
      # Group tool runs by parent run ID  
      for run in tqdm(tool_runs):  
          # Collect all tools invoked within a given trace  
          tool_runs_by_parent[run.trace_id]["tools_involved"].add(run.name)  
          # maybe send a batch of parent run IDs to the server  
          # this lets us query for the root runs in batches  
          # while still processing the tool runs  
          if len(tool_runs_by_parent) % trace_batch_size == 0:  
              if this_batch := list(tool_runs_by_parent.keys())[  
                  trace_cursor : trace_cursor + trace_batch_size  
              ]:  
                  trace_cursor += trace_batch_size  
                  futures.append(  
                      executor.submit(  
                          client.list_runs,  
                          project_name=project_name,  
                          run_ids=this_batch,  
                          select=["name", "inputs", "outputs", "run_type"],  
                      )  
                  )  
      if this_batch := list(tool_runs_by_parent.keys())[trace_cursor:]:  
          futures.append(  
              executor.submit(  
                  client.list_runs,  
                  project_name=project_name,  
                  run_ids=this_batch,  
                  select=["name", "inputs", "outputs", "run_type"],  
              )  
          )  
      
    for future in tqdm(futures):  
      root_runs = future.result()  
      for root_run in root_runs:  
          root_data = tool_runs_by_parent[root_run.id]  
          data.append(  
              {  
                  "run_id": root_run.id,  
                  "run_name": root_run.name,  
                  "run_type": root_run.run_type,  
                  "inputs": root_run.inputs,  
                  "outputs": root_run.outputs,  
                  "tools_involved": list(root_data["tools_involved"]),  
              }  
          )  
      
    # (Optional): Convert to a pandas DataFrame  
      
    import pandas as pd  
      
    df = pd.DataFrame(data)  
    df.head()  
    

### Advanced: export retriever IO for traces with feedback​

This query is useful if you want to fine-tune embeddings or diagnose end-to-end system performance issues based on retriever behavior. The following Python example demonstrates how to export retriever inputs and outputs within traces that have a specific feedback score.

  * Python

    
    
    from collections import defaultdict  
    from concurrent.futures import Future, ThreadPoolExecutor  
    from datetime import datetime, timedelta  
      
    import pandas as pd  
    from langsmith import Client  
    from tqdm.auto import tqdm  
      
    client = Client()  
    project_name = "your-project-name"  
    num_days = 1  
      
    # List all tool runs  
    retriever_runs = client.list_runs(  
      project_name=project_name,  
      start_time=datetime.now() - timedelta(days=num_days),  
      run_type="retriever",  
      # This time we do want to fetch the inputs and outputs, since they  
      # may be adjusted by query expansion steps.  
      select=["trace_id", "name", "run_type", "inputs", "outputs"],  
      trace_filter='eq(feedback_key, "user_score")',  
    )  
      
    data = []  
    futures: list[Future] = []  
    trace_cursor = 0  
    trace_batch_size = 50  
      
    retriever_runs_by_parent = defaultdict(lambda: defaultdict(list))  
    # Do not exceed rate limit  
    with ThreadPoolExecutor(max_workers=2) as executor:  
      # Group retriever runs by parent run ID  
      for run in tqdm(retriever_runs):  
          # Collect all retriever calls invoked within a given trace  
          for k, v in run.inputs.items():  
              retriever_runs_by_parent[run.trace_id][f"retriever.inputs.{k}"].append(v)  
          for k, v in (run.outputs or {}).items():  
              # Extend the docs  
              retriever_runs_by_parent[run.trace_id][f"retriever.outputs.{k}"].extend(v)  
          # maybe send a batch of parent run IDs to the server  
          # this lets us query for the root runs in batches  
          # while still processing the retriever runs  
          if len(retriever_runs_by_parent) % trace_batch_size == 0:  
              if this_batch := list(retriever_runs_by_parent.keys())[  
                  trace_cursor : trace_cursor + trace_batch_size  
              ]:  
                  trace_cursor += trace_batch_size  
                  futures.append(  
                      executor.submit(  
                          client.list_runs,  
                          project_name=project_name,  
                          run_ids=this_batch,  
                          select=[  
                              "name",  
                              "inputs",  
                              "outputs",  
                              "run_type",  
                              "feedback_stats",  
                          ],  
                      )  
                  )  
      if this_batch := list(retriever_runs_by_parent.keys())[trace_cursor:]:  
          futures.append(  
              executor.submit(  
                  client.list_runs,  
                  project_name=project_name,  
                  run_ids=this_batch,  
                  select=["name", "inputs", "outputs", "run_type"],  
              )  
          )  
      
    for future in tqdm(futures):  
      root_runs = future.result()  
      for root_run in root_runs:  
          root_data = retriever_runs_by_parent[root_run.id]  
          feedback = {  
              f"feedback.{k}": v.get("avg")  
              for k, v in (root_run.feedback_stats or {}).items()  
          }  
          inputs = {f"inputs.{k}": v for k, v in root_run.inputs.items()}  
          outputs = {f"outputs.{k}": v for k, v in (root_run.outputs or {}).items()}  
          data.append(  
              {  
                  "run_id": root_run.id,  
                  "run_name": root_run.name,  
                  **inputs,  
                  **outputs,  
                  **feedback,  
                  **root_data,  
              }  
          )  
      
    # (Optional): Convert to a pandas DataFrame  
    import pandas as pd  
    df = pd.DataFrame(data)  
    df.head()  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Use filter arguments
    * List all runs in a project
    * List LLM and Chat runs in the last 24 hours
    * List root runs in a project
    * List runs without errors
    * List runs by run ID
  * Use filter query language
    * List all root runs in a conversational thread
    * List all runs called "extractor" whose root of the trace was assigned feedback "user_score" score of 1
    * List runs with "star_rating" key whose score is greater than 4
    * List runs that took longer than 5 seconds to complete
    * List all runs where `total_tokens` is greater than 5000
    * List all runs that have "error" not equal to null
    * List all runs where `start_time` is greater than a specific timestamp
    * List all runs that contain the string "substring"
    * List all runs that are tagged with the git hash "2aa1cf4"
    * List all "chain" type runs that took more than 10 seconds and
    * List all runs that started after a specific timestamp and either
    * Complex query: List all runs where `tags` include "experimental" or "beta" and
    * Search trace trees by full text You can use the `search()` function without
    * Check for presence of metadata
    * Check for environment details in metadata.
    * Check for conversation ID in metadata
    * Negative filtering on key-value pairs
    * Combine multiple filters
    * Tree Filter
    * Advanced: export flattened trace view with child tool usage
    * Advanced: export retriever IO for traces with feedback

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)