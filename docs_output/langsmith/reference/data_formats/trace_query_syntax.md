# Trace query syntax | 🦜️🛠️ LangSmith

On this page

Using the `list_runs` method in the SDK or `/runs/query` endpoint in the API, you can filter runs to analyze and export.

## Filter arguments​

Keys| Description  
---|---  
`project_id` / `project_name`| The project(s) to fetch runs from - can be a single project or a list of projects.  
`trace_id`| Fetch runs that are part of a specific trace.  
`run_type`| The type of run to get, such as `llm`, `chain`, `tool`, `retriever`, etc.  
`dataset_name` / `dataset_id`| Fetch runs that are associated with an example row in the specified dataset. This is useful for comparing prompts or models over a given dataset.  
`reference_example_id`| Fetch runs that are associated with a specific example row. This is useful for comparing prompts or models on a given input.  
`parent_run_id`| Fetch runs that are children of a given run. This is useful for fetching runs grouped together using the context manager or for fetching an agent trajectory.  
`error`| Fetch runs that errored or did not error.  
`run_ids`| Fetch runs with a given list of run ids. Note: **This will ignore all other filtering arguments.**  
`filter`| Fetch runs that match a given structured filter statement. See the guide below for more information.  
`trace_filter`| Filter to apply to the ROOT run in the trace tree. This is meant to be used in conjunction with the regular `filter` parameter to let you filter runs by attributes of the root run within a trace.  
`tree_filter`| Filter to apply to OTHER runs in the trace tree, including sibling and child runs. This is meant to be used in conjunction with the regular `filter` parameter to let you filter runs by attributes of any run within a trace.  
`is_root`| Only return root runs.  
`select`| Select the fields to return in the response. By default, all fields are returned.  
`query` (_experimental_)| Natural language query, which translates your query into a filter statement.  
  
## Filter query language​

LangSmith supports powerful filtering capabilities with a filter query language to permit complex filtering operations when fetching runs.

The filtering grammar is based on common comparators on fields in the run object. Supported comparators include:

  * `gte` (greater than or equal to)
  * `gt` (greater than)
  * `lte` (less than or equal to)
  * `lt` (less than)
  * `eq` (equal to)
  * `neq` (not equal to)
  * `has` (check if run contains a tag or metadata json blob)
  * `search` (search for a substring in a string field)

Additionally, you can combine multiple comparisons through `and` and `or` operators.

These can be applied on fields of the run object, such as its `id`, `name`, `run_type`, `start_time` / `end_time`, `latency`, `total_tokens`, `error`, `execution_order`, `tags`, and any associated feedback through `feedback_key` and `feedback_score`.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Filter arguments
  * Filter query language

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)