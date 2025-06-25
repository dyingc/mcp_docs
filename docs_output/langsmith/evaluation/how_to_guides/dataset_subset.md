# How to evaluate on a split / filtered view of a dataset | 🦜️🛠️ LangSmith

On this page

Recommended reading

Before diving into this content, it might be helpful to read:

  * [guide on fetching examples](/evaluation/how_to_guides/manage_datasets_programmatically#fetch-examples).
  * [guide on creating/managing dataset splits](/evaluation/how_to_guides/manage_datasets_in_application#create-and-manage-dataset-splits)

## Evaluate on a filtered view of a dataset​

You can use the `list_examples` / `listExamples` method to fetch a subset of examples from a dataset to evaluate on. You can refer to guide above to learn more about the different ways to fetch examples.

One common workflow is to fetch examples that have a certain metadata key-value pair.

  * Python
  * TypeScript

    
    
    from langsmith import evaluate  
      
    results = evaluate(  
        lambda inputs: label_text(inputs["text"]),  
        data=client.list_examples(dataset_name=dataset_name, metadata={"desired_key": "desired_value"}),  
        evaluators=[correct_label],  
        experiment_prefix="Toxic Queries",  
    )  
    
    
    
    import { evaluate } from "langsmith/evaluation";  
      
    await evaluate((inputs) => labelText(inputs["input"]), {  
      data: langsmith.listExamples({  
        datasetName: datasetName,  
        metadata: {"desired_key": "desired_value"},  
      }),  
      evaluators: [correctLabel],  
      experimentPrefix: "Toxic Queries",  
    });  
    

For more advanced filtering capabilities see this [how-to guide](/evaluation/how_to_guides/manage_datasets_programmatically#list-examples-by-structured-filter).

## Evaluate on a dataset split​

You can use the `list_examples` / `listExamples` method to evaluate on one or multiple splits of your dataset. The `splits` param takes a list of the splits you would like to evaluate.

  * Python
  * TypeScript

    
    
    from langsmith import evaluate  
      
    results = evaluate(  
        lambda inputs: label_text(inputs["text"]),  
        data=client.list_examples(dataset_name=dataset_name, splits=["test", "training"]),  
        evaluators=[correct_label],  
        experiment_prefix="Toxic Queries",  
    )  
    
    
    
    import { evaluate } from "langsmith/evaluation";  
      
    await evaluate((inputs) => labelText(inputs["input"]), {  
      data: langsmith.listExamples({  
        datasetName: datasetName,  
        splits: ["test", "training"],  
      }),  
      evaluators: [correctLabel],  
      experimentPrefix: "Toxic Queries",  
    });  
    

## Related​

  * Learn more about how to fetch views of a dataset [here](/evaluation/how_to_guides/manage_datasets_programmatically#fetch-datasets)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Evaluate on a filtered view of a dataset
  * Evaluate on a dataset split
  * Related

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)