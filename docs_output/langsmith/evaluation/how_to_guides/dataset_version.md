# How to evaluate on a specific dataset version | 🦜️🛠️ LangSmith

On this page

Recommended reading

Before diving into this content, it might be helpful to read the [guide on versioning datasets](/evaluation/how_to_guides/version_datasets). Additionally, it might be helpful to read the [guide on fetching examples](/evaluation/how_to_guides/manage_datasets_programmatically#fetch-examples).

## Using `list_examples`​

You can take advantage of the fact that `evaluate` / `aevaluate` allows passing in an iterable of examples to evaluate on a particular version of a dataset. Simply use `list_examples` / `listExamples` to fetch examples from a particular version tag using `as_of` / `asOf` and pass that in to the `data` argument.

  * Python
  * TypeScript

    
    
    from langsmith import Client  
      
    ls_client = Client()  
      
    # Assumes actual outputs have a 'class' key.  
    # Assumes example outputs have a 'label' key.  
    def correct(outputs: dict, reference_outputs: dict) -> bool:  
      return outputs["class"] == reference_outputs["label"]  
      
    results = ls_client.evaluate(  
        lambda inputs: {"class": "Not toxic"},  
        # Pass in filtered data here:  
        data=ls_client.list_examples(  
          dataset_name="Toxic Queries",  
          as_of="latest",  # specify version here  
        ),  
        evaluators=[correct],  
    )  
    
    
    
    import { evaluate } from "langsmith/evaluation";  
      
    await evaluate((inputs) => labelText(inputs["input"]), {  
      data: langsmith.listExamples({  
        datasetName: datasetName,  
        asOf: "latest",  
      }),  
      evaluators: [correctLabel],  
    });  
    

## Related​

  * Learn more about how to fetch views of a dataset [here](/evaluation/how_to_guides/manage_datasets_programmatically#fetch-datasets)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Using `list_examples`
  * Related

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)