# How to run an evaluation | 🦜️🛠️ LangSmith

On this page

Key concepts

[Evaluations](/evaluation/concepts#applying-evaluations) | [Evaluators](/evaluation/concepts#evaluators) | [Datasets](/evaluation/concepts#datasets)

In this guide we'll go over how to evaluate an application using the [evaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate) method in the LangSmith SDK.

Running large jobs

For larger evaluation jobs in Python we recommend using [aevaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._arunner.aevaluate), the asynchronous version of [evaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate). It is still worthwhile to read this guide first, as the two have identical interfaces, before reading the how-to guide on [running an evaluation asynchronously](/evaluation/how_to_guides/async).

In JS/TS evaluate() is already asynchronous so no separate method is needed.

It is also important to configure the `max_concurrency`/`maxConcurrency` arg when running large jobs. This parallelizes evaluation by effectively splitting the dataset across threads.

## Define an application​

First we need an application to evaluate. Let's create a simple toxicity classifier for this example.

  * Python
  * TypeScript

    
    
    from langsmith import traceable, wrappers  
    from openai import OpenAI  
      
    # Optionally wrap the OpenAI client to trace all model calls.  
    oai_client = wrappers.wrap_openai(OpenAI())  
      
    # Optionally add the 'traceable' decorator to trace the inputs/outputs of this function.  
    @traceable  
    def toxicity_classifier(inputs: dict) -> dict:  
        instructions = (  
          "Please review the user query below and determine if it contains any form of toxic behavior, "  
          "such as insults, threats, or highly negative comments. Respond with 'Toxic' if it does "  
          "and 'Not toxic' if it doesn't."  
        )  
        messages = [  
            {"role": "system", "content": instructions},  
            {"role": "user", "content": inputs["text"]},  
        ]  
        result = oai_client.chat.completions.create(  
            messages=messages, model="gpt-4o-mini", temperature=0  
        )  
        return {"class": result.choices[0].message.content}  
    
    
    
    import { OpenAI } from "openai";  
    import { wrapOpenAI } from "langsmith/wrappers";  
    import { traceable } from "langsmith/traceable";  
      
    // Optionally wrap the OpenAI client to trace all model calls.  
    const oaiClient = wrapOpenAI(new OpenAI());  
      
    // Optionally add the 'traceable' wrapper to trace the inputs/outputs of this function.  
    const toxicityClassifier = traceable(  
      async (text: string) => {  
        const result = await oaiClient.chat.completions.create({  
          messages: [  
            {   
              role: "system",  
              content: "Please review the user query below and determine if it contains any form of toxic behavior, such as insults, threats, or highly negative comments. Respond with 'Toxic' if it does, and 'Not toxic' if it doesn't.",  
            },  
            { role: "user", content: text },  
          ],  
          model: "gpt-4o-mini",  
          temperature: 0,  
        });  
          
        return result.choices[0].message.content;  
      },  
      { name: "toxicityClassifier" }  
    );  
    

We've optionally enabled tracing to capture the inputs and outputs of each step in the pipeline. To understand how to annotate your code for tracing, please refer to [this guide](/observability/how_to_guides/annotate_code).

## Create or select a dataset​

We need a [Dataset](/evaluation/concepts#datasets) to evaluate our application on. Our dataset will contain labeled [examples](/evaluation/concepts#examples) of toxic and non-toxic text.

  * Python
  * TypeScript

Requires `langsmith>=0.3.13`
    
    
    from langsmith import Client  
      
    ls_client = Client()  
      
    examples = [  
      {  
        "inputs": {"text": "Shut up, idiot"},   
        "outputs": {"label": "Toxic"},  
      },  
      {  
        "inputs": {"text": "You're a wonderful person"},  
        "outputs": {"label": "Not toxic"},  
      },  
      {  
        "inputs": {"text": "This is the worst thing ever"},   
        "outputs": {"label": "Toxic"},  
      },  
      {  
        "inputs": {"text": "I had a great day today"},   
        "outputs": {"label": "Not toxic"},  
      },  
      {  
        "inputs": {"text": "Nobody likes you"},   
        "outputs": {"label": "Toxic"},  
      },  
      {  
        "inputs": {"text": "This is unacceptable. I want to speak to the manager."},  
        "outputs": {"label": "Not toxic"},  
      },  
    ]  
      
    dataset = ls_client.create_dataset(dataset_name="Toxic Queries")  
    ls_client.create_examples(  
      dataset_id=dataset.id,   
      examples=examples,  
    )  
    
    
    
    import { Client } from "langsmith";  
      
    const langsmith = new Client();  
      
    // create a dataset  
    const labeledTexts = [  
      ["Shut up, idiot", "Toxic"],  
      ["You're a wonderful person", "Not toxic"],  
      ["This is the worst thing ever", "Toxic"],  
      ["I had a great day today", "Not toxic"],  
      ["Nobody likes you", "Toxic"],  
      ["This is unacceptable. I want to speak to the manager.", "Not toxic"],  
    ];  
      
    const [inputs, outputs] = labeledTexts.reduce<  
      [Array<{ input: string }>, Array<{ outputs: string }>]  
    >(  
      ([inputs, outputs], item) => [  
        [...inputs, { input: item[0] }],  
        [...outputs, { outputs: item[1] }],  
      ],  
      [[], []]  
    );  
      
    const datasetName = "Toxic Queries";  
    const toxicDataset = await langsmith.createDataset(datasetName);  
    await langsmith.createExamples({ inputs, outputs, datasetId: toxicDataset.id });  
    

See [here](/evaluation/how_to_guides/#dataset-management) for more on dataset management.

## Define an evaluator​

tip

You can also check out LangChain's open source evaluation package [openevals](https://github.com/langchain-ai/openevals) for common pre-built evaluators.

[Evaluators](/evaluation/concepts#evaluators) are functions for scoring your application's outputs. They take in the example inputs, actual outputs, and, when present, the reference outputs. Since we have labels for this task, our evaluator can directly check if the actual outputs match the reference outputs.

  * Python
  * TypeScript

Requires `langsmith>=0.3.13`
    
    
    def correct(inputs: dict, outputs: dict, reference_outputs: dict) -> bool:  
        return outputs["class"] == reference_outputs["label"]  
    

Requires `langsmith>=0.2.9`
    
    
    import type { EvaluationResult } from "langsmith/evaluation";  
      
    function correct({  
      outputs,  
      referenceOutputs,  
    }: {  
      outputs: Record<string, any>;  
      referenceOutputs?: Record<string, any>;  
    }): EvaluationResult {  
      const score = outputs.output === referenceOutputs?.outputs;  
      return { key: "correct", score };  
    }  
    

See [here](/evaluation/how_to_guides/#define-an-evaluator) for more on how to define evaluators.

## Run the evaluation​

We'll use the [evaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate) / [aevaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._arunner.aevaluate) methods to run the evaluation.

The key arguments are:

  * a target function that takes an input dictionary and returns an output dictionary. The `example.inputs` field of each [Example](/reference/data_formats/example_data_format) is what gets passed to the target function. In this case our `toxicity_classifier` is already set up to take in example inputs so we can use it directly.
  * `data` \- the name OR UUID of the LangSmith dataset to evaluate on, or an iterator of examples
  * `evaluators` \- a list of evaluators to score the outputs of the function

  * Python
  * TypeScript

Requires `langsmith>=0.3.13`
    
    
    # Can equivalently use the 'evaluate' function directly:  
    # from langsmith import evaluate; evaluate(...)  
    results = ls_client.evaluate(  
        toxicity_classifier,  
        data=dataset.name,  
        evaluators=[correct],  
        experiment_prefix="gpt-4o-mini, baseline",  # optional, experiment name prefix  
        description="Testing the baseline system.",  # optional, experiment description  
        max_concurrency=4, # optional, add concurrency  
    )  
    
    
    
    import { evaluate } from "langsmith/evaluation";  
      
    await evaluate((inputs) => toxicityClassifier(inputs["input"]), {  
      data: datasetName,  
      evaluators: [correct],  
      experimentPrefix: "gpt-4o-mini, baseline",  // optional, experiment name prefix  
      maxConcurrency: 4, // optional, add concurrency  
    });  
    

See [here](/evaluation/how_to_guides/#run-an-evaluation) for other ways to kick off evaluations and [here](/evaluation/how_to_guides/#configure-an-evaluation-job) for how to configure evaluation jobs.

## Explore the results​

Each invocation of `evaluate()` creates an [Experiment](/evaluation/concepts#experiments) which can be viewed in the LangSmith UI or queried via the SDK. Evaluation scores are stored against each actual output as feedback.

_If you've annotated your code for tracing, you can open the trace of each row in a side panel view._

![](/assets/images/view_experiment-6328bb0fb0d033a49b381d84a3f9b1e8.gif)

## Reference code​

Click to see a consolidated code snippet

  * Python
  * TypeScript

Requires `langsmith>=0.3.13`
    
    
    from langsmith import Client, traceable, wrappers  
    from openai import OpenAI  
      
    # Step 1. Define an application  
    oai_client = wrappers.wrap_openai(OpenAI())  
      
    @traceable  
    def toxicity_classifier(inputs: dict) -> str:  
        system = (  
          "Please review the user query below and determine if it contains any form of toxic behavior, "  
          "such as insults, threats, or highly negative comments. Respond with 'Toxic' if it does "  
          "and 'Not toxic' if it doesn't."  
        )  
        messages = [  
            {"role": "system", "content": system},  
            {"role": "user", "content": inputs["text"]},  
        ]  
        result = oai_client.chat.completions.create(  
            messages=messages, model="gpt-4o-mini", temperature=0  
        )  
        return result.choices[0].message.content  
      
    # Step 2. Create a dataset  
    ls_client = Client()  
      
    dataset = ls_client.create_dataset(dataset_name="Toxic Queries")  
    examples = [  
      {  
        "inputs": {"text": "Shut up, idiot"},   
        "outputs": {"label": "Toxic"},  
      },  
      {  
        "inputs": {"text": "You're a wonderful person"},  
        "outputs": {"label": "Not toxic"},  
      },  
      {  
        "inputs": {"text": "This is the worst thing ever"},   
        "outputs": {"label": "Toxic"},  
      },  
      {  
        "inputs": {"text": "I had a great day today"},   
        "outputs": {"label": "Not toxic"},  
      },  
      {  
        "inputs": {"text": "Nobody likes you"},   
        "outputs": {"label": "Toxic"},  
      },  
      {  
        "inputs": {"text": "This is unacceptable. I want to speak to the manager."},  
        "outputs": {"label": "Not toxic"},  
      },  
    ]  
    ls_client.create_examples(  
      dataset_id=dataset.id,  
      examples=examples,  
    )  
      
    # Step 3. Define an evaluator  
    def correct(inputs: dict, outputs: dict, reference_outputs: dict) -> bool:  
        return outputs["output"] == reference_outputs["label"]  
      
    # Step 4. Run the evaluation  
    # Client.evaluate() and evaluate() behave the same.  
    results = ls_client.evaluate(  
        toxicity_classifier,  
        data=dataset.name,  
        evaluators=[correct],  
        experiment_prefix="gpt-4o-mini, simple",  # optional, experiment name prefix  
        description="Testing the baseline system.",  # optional, experiment description  
        max_concurrency=4,  # optional, add concurrency  
    )  
    
    
    
    import { OpenAI } from "openai";  
    import { Client } from "langsmith";  
    import { evaluate, EvaluationResult } from "langsmith/evaluation";  
    import type { Run, Example } from "langsmith/schemas";  
    import { traceable } from "langsmith/traceable";  
    import { wrapOpenAI } from "langsmith/wrappers";  
      
      
    const oaiClient = wrapOpenAI(new OpenAI());  
      
    const toxicityClassifier = traceable(  
      async (text: string) => {  
        const result = await oaiClient.chat.completions.create({  
          messages: [  
            {  
              role: "system",  
              content: "Please review the user query below and determine if it contains any form of toxic behavior, such as insults, threats, or highly negative comments. Respond with 'Toxic' if it does, and 'Not toxic' if it doesn't.",  
            },  
            { role: "user", content: text },  
          ],  
          model: "gpt-4o-mini",  
          temperature: 0,  
        });  
      
        return result.choices[0].message.content;  
      },  
      { name: "toxicityClassifier" }  
    );  
      
    const langsmith = new Client();  
      
    // create a dataset  
    const labeledTexts = [  
      ["Shut up, idiot", "Toxic"],  
      ["You're a wonderful person", "Not toxic"],  
      ["This is the worst thing ever", "Toxic"],  
      ["I had a great day today", "Not toxic"],  
      ["Nobody likes you", "Toxic"],  
      ["This is unacceptable. I want to speak to the manager.", "Not toxic"],  
    ];  
      
    const [inputs, outputs] = labeledTexts.reduce<  
      [Array<{ input: string }>, Array<{ outputs: string }>]  
    >(  
      ([inputs, outputs], item) => [  
        [...inputs, { input: item[0] }],  
        [...outputs, { outputs: item[1] }],  
      ],  
      [[], []]  
    );  
      
    const datasetName = "Toxic Queries";  
    const toxicDataset = await langsmith.createDataset(datasetName);  
    await langsmith.createExamples({ inputs, outputs, datasetId: toxicDataset.id });  
      
    // Row-level evaluator  
    function correct({  
      outputs,  
      referenceOutputs,  
    }: {  
      outputs: Record<string, any>;  
      referenceOutputs?: Record<string, any>;  
    }): EvaluationResult {  
      const score = outputs.output === referenceOutputs?.outputs;  
      return { key: "correct", score };  
    }  
      
    await evaluate((inputs) => toxicityClassifier(inputs["input"]), {  
      data: datasetName,  
      evaluators: [correct],  
      experimentPrefix: "gpt-4o-mini, simple",  // optional, experiment name prefix  
      maxConcurrency: 4, // optional, add concurrency  
    });  
    

## Related​

  * [Run an evaluation asynchronously](/evaluation/how_to_guides/async)
  * [Run an evaluation via the REST API](/evaluation/how_to_guides/run_evals_api_only)
  * [Run an evaluation from the prompt playground](/evaluation/how_to_guides/run_evaluation_from_prompt_playground)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Define an application
  * Create or select a dataset
  * Define an evaluator
  * Run the evaluation
  * Explore the results
  * Reference code
  * Related

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)