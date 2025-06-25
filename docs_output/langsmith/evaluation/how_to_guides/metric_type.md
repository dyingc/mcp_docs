# How to return categorical vs numerical metrics | 🦜️🛠️ LangSmith

On this page

LangSmith supports both categorical and numerical metrics, and you can return either when writing a [custom evaluator](/evaluation/how_to_guides/custom_evaluator).

For an evaluator result to be logged as a numerical metric, it must returned as:

  * (Python only) an `int`, `float`, or `bool`
  * a dict of the form `{"key": "metric_name", "score": int | float | bool}`

For an evaluator result to be logged as a categorical metric, it must be returned as:

  * (Python only) a `str`
  * a dict of the form `{"key": "metric_name", "value": str | int | float | bool}`

Here are some examples:

  * Python
  * TypeScript

Requires `langsmith>=0.2.0`
    
    
    def numerical_metric(inputs: dict, outputs: dict, reference_outputs: dict) -> float:  
        # Evaluation logic...  
          
        return 0.8  
          
        # Equivalently  
        # return {"score": 0.8}  
      
        # Or  
        # return {"key": "numerical_metric", "score": 0.8}  
      
    def categorical_metric(inputs: dict, outputs: dict, reference_outputs: dict) -> str:  
        # Evaluation logic...  
      
        return "english"  
      
        # Equivalently  
        # return {"key": "categorical_metric", "score": "english"}  
      
        # Or  
        # return {"score": "english"}  
    

Support for multiple scores is available in `langsmith@0.1.32` and higher
    
    
    import type { Run, Example } from "langsmith/schemas";  
      
    function numericalMetric(run: Run, example: Example) {  
      // Your evaluation logic here  
      return { key: "numerical_metric", score: 0.8};  
    }  
      
    function categoricalMetric(run: Run, example: Example) {  
      // Your evaluation logic here  
      return { key: "categorical_metric", value: "english"};  
    }  
    

## Related​

  * [Return multiple metrics in one evaluator](/evaluation/how_to_guides/multiple_scores)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Related

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)