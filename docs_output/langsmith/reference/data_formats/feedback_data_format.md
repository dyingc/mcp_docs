# Feedback data format | 🦜️🛠️ LangSmith

Recommended Reading

Before diving into this content, it might be helpful to read the following:

  * [Conceptual guide on tracing and feedback](/observability/concepts)

**Feedback** is LangSmith's way of storing the criteria and scores from evaluation on a particular trace or intermediate run (span). Feedback can be produced from a variety of ways, such as:

  1. [Sent up along with a trace](/evaluation/how_to_guides/attach_user_feedback) from the LLM application
  2. Generated by a user in the app [inline](/evaluation/how_to_guides/annotate_traces_inline) or in an [annotation queue](/evaluation/how_to_guides/annotation_queues)
  3. Generated by an automatic evaluator during [offline evaluation](/evaluation/how_to_guides/evaluate_llm_application)
  4. Generated by an [online evaluator](/observability/how_to_guides/online_evaluations)

Feedback is stored in a simple format with the following fields:

Field Name| Type| Description  
---|---|---  
id| UUID| Unique identifier for the record itself  
created_at| datetime| Timestamp when the record was created  
modified_at| datetime| Timestamp when the record was last modified  
session_id| UUID| Unique identifier for the experiment or tracing project the run was a part of  
run_id| UUID| Unique identifier for a specific run within a session  
key| string| A key describing the criteria of the feedback, eg "correctness"  
score| number| Numerical score associated with the feedback key  
value| string| Reserved for storing a value associated with the score. Useful for categorical feedback.  
comment| string| Any comment or annotation associated with the record. This can be a justification for the score given.  
correction| object| Reserved for storing correction details, if any  
feedback_source| object| Object containing information about the feedback source  
feedback_source.type| string| The type of source where the feedback originated, eg "api", "app", "evaluator"  
feedback_source.metadata| object| Reserved for additional metadata, currently  
feedback_source.user_id| UUID| Unique identifier for the user providing feedback  
  
Here is an example JSON representation of a feedback record in the above format:
    
    
    {  
      "created_at": "2024-05-05T23:23:11.077838",  
      "modified_at": "2024-05-05T23:23:11.232962",  
      "session_id": "c919298b-0af2-4517-97a2-0f98ed4a48f8",  
      "run_id": "e26174e5-2190-4566-b970-7c3d9a621baa",  
      "key": "correctness",  
      "score": 1.0,  
      "value": null,  
      "comment": "I gave this score because the answer was correct.",  
      "correction": null,  
      "id": "62104630-c7f5-41dc-8ee2-0acee5c14224",  
      "feedback_source": {  
        "type": "app",  
        "metadata": null,  
        "user_id": "ad52b092-1346-42f4-a934-6e5521562fab"  
      }  
    }  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)