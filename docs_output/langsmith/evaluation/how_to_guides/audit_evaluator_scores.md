# How to audit evaluator scores | 🦜️🛠️ LangSmith

On this page

LLM-as-a-judge evaluators don't always get it right. Because of this, it is often useful for a human to manually audit the scores left by an evaluator and correct them where necessary. LangSmith allows you to make corrections on evaluator scores in the UI or SDK.

## In the comparison view​

In the comparison view, you may click on any feedback tag to bring up the feedback details. From there, click the "edit" icon on the right to bring up the corrections view. You may then type in your desired score in the text box under "Make correction". If you would like, you may also attach an explanation to your correction. This is useful if you are using a [few-shot evaluator](/evaluation/how_to_guides/create_few_shot_evaluators) and will be automatically inserted into your few-shot examples in place of the `few_shot_explanation` prompt variable.

![Audit Evaluator Comparison View](/assets/images/corrections_comparison_view-2a14c3ed9bc9cf527a436e3abefe0eb2.png)

## In the runs table​

In the runs table, find the "Feedback" column and click on the feedback tag to bring up the feedback details. Again, click the "edit" icon on the right to bring up the corrections view.

![Audit Evaluator Runs Table](/assets/images/corrections_runs_table-90fb6a2f9788b4a36f5f14883bde4e89.png)

## In the SDK​

Corrections can be made via the SDK's `update_feedback` function, with the `correction` dict. You must specify a `score` key which corresponds to a number for it to be rendered in the UI.

  * Python
  * TypeScript

    
    
    import langsmith  
      
    client = langsmith.Client()  
    client.update_feedback(  
      my_feedback_id,  
      correction={  
          "score": 1,  
      },  
    )  
    
    
    
    import { Client } from 'langsmith';  
      
    const client = new Client();  
    await client.updateFeedback(  
      myFeedbackId,  
      {  
          correction: {  
              score: 1,  
          }  
      }  
    )  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * In the comparison view
  * In the runs table
  * In the SDK

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)