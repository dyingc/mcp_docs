# How to define a summary evaluator | 🦜️🛠️ LangSmith

On this page

Some metrics can only be defined on the entire experiment level as opposed to the individual runs of the experiment. For example, you may want to compute the overall pass rate or f1 score of your evaluation target across all examples in the dataset. These are called `summary_evaluators`.

## Basic example​

Here, we'll compute the f1-score, which is a combination of precision and recall.

This sort of metric can only be computed over all of the examples in our experiment, so our evaluator takes in a list of outputs, and a list of reference_outputs.

  * Python
  * TypeScript

    
    
    def f1_score_summary_evaluator(outputs: list[dict], reference_outputs: list[dict]) -> dict:  
        true_positives = 0  
        false_positives = 0  
        false_negatives = 0  
        for output_dict, reference_output_dict in zip(outputs, reference_outputs):  
            output = output_dict["class"]  
            reference_output = reference_output_dict["class"]  
            if output == "Toxic" and reference_output == "Toxic":  
                true_positives += 1  
            elif output == "Toxic" and reference_output == "Not toxic":  
                false_positives += 1  
            elif output == "Not toxic" and reference_output == "Toxic":  
                false_negatives += 1  
      
        if true_positives == 0:  
            return {"key": "f1_score", "score": 0.0}  
      
        precision = true_positives / (true_positives + false_positives)  
        recall = true_positives / (true_positives + false_negatives)  
        f1_score = 2 * (precision * recall) / (precision + recall)  
        return {"key": "f1_score", "score": f1_score}  
    
    
    
    function f1ScoreSummaryEvaluator({ outputs, referenceOutputs }: { outputs: Record<string, any>[], referenceOutputs: Record<string, any>[] }) {  
      let truePositives = 0;  
      let falsePositives = 0;  
      let falseNegatives = 0;  
        
      for (let i = 0; i < outputs.length; i++) {  
        const output = outputs[i]["class"];  
        const referenceOutput = referenceOutputs[i]["class"];  
          
        if (output === "Toxic" && referenceOutput === "Toxic") {  
          truePositives += 1;  
        } else if (output === "Toxic" && referenceOutput === "Not toxic") {  
          falsePositives += 1;  
        } else if (output === "Not toxic" && referenceOutput === "Toxic") {  
          falseNegatives += 1;  
        }  
      }  
        
      if (truePositives === 0) {  
        return { key: "f1_score", score: 0.0 };  
      }  
        
      const precision = truePositives / (truePositives + falsePositives);  
      const recall = truePositives / (truePositives + falseNegatives);  
      const f1Score = 2 * (precision * recall) / (precision + recall);  
        
      return { key: "f1_score", score: f1Score };  
    }  
    

You can then pass this evaluator to the `evaluate` method as follows:

  * Python
  * TypeScript

    
    
    from langsmith import Client  
      
    ls_client = Client()  
    dataset = ls_client.clone_public_dataset(  
      "https://smith.langchain.com/public/3d6831e6-1680-4c88-94df-618c8e01fc55/d"  
    )  
      
    def bad_classifier(inputs: dict) -> dict:  
      return {"class": "Not toxic"}  
        
    def correct(outputs: dict, reference_outputs: dict) -> bool:  
      """Row-level correctness evaluator."""  
      return outputs["class"] == reference_outputs["label"]  
      
    results = ls_client.evaluate(  
        bad_classified,  
        data=dataset,  
        evaluators=[correct],  
        summary_evaluators=[pass_50],  
    )  
    
    
    
    import { Client } from "langsmith";  
    import { evaluate } from "langsmith/evaluation";  
    import type { EvaluationResult } from "langsmith/evaluation";  
      
    const client = new Client();  
    const datasetName = "Toxic queries";  
    const dataset = await client.clonePublicDataset(  
      "https://smith.langchain.com/public/3d6831e6-1680-4c88-94df-618c8e01fc55/d",  
      { datasetName: datasetName }  
    );  
      
    function correct({ outputs, referenceOutputs }: { outputs: Record<string, any>, referenceOutputs?: Record<string, any> }): EvaluationResult {  
      const score = outputs["class"] === referenceOutputs?["label"];  
      return { key: "correct", score };  
    }  
      
    function badClassifier(inputs: Record<string, any>): { class: string } {  
      return { class: "Not toxic" };  
    }  
      
    await evaluate(badClassifier, {  
      data: datasetName,  
      evaluators: [correct],  
      summaryEvaluators: [summaryEval],  
      experimentPrefix: "Toxic Queries",  
    });  
    

In the LangSmith UI, you'll the summary evaluator's score displayed with the corresponding key.

![](/assets/images/summary_eval-20d1a3d5cd63a91009dc3854a14077e1.png)

## Summary evaluator args​

Summary evaluator functions must have specific argument names. They can take any subset of the following arguments:

  * `inputs: list[dict]`: A list of the inputs corresponding to a single example in a dataset.
  * `outputs: list[dict]`: A list of the dict outputs produced by each experiment on the given inputs.
  * `reference_outputs/referenceOutputs: list[dict]`: A list of the reference outputs associated with the example, if available.
  * `runs: list[Run]`: A list of the full [Run](/reference/data_formats/run_data_format) objects generated by the two experiments on the given example. Use this if you need access to intermediate steps or metadata about each run.
  * `examples: list[Example]`: All of the dataset [Example](/reference/data_formats/example_data_format) objects, including the example inputs, outputs (if available), and metdata (if available).

## Summary evaluator output​

Summary evaluators are expected to return one of the following types:

Python and JS/TS

  * `dict`: dicts of the form `{"score": ..., "name": ...}` allow you to pass a numeric or boolean score and metric name.

Currently Python only

  * `int | float | bool`: this is interepreted as an continuous metric that can be averaged, sorted, etc. The function name is used as the name of the metric.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Basic example
  * Summary evaluator args
  * Summary evaluator output

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)