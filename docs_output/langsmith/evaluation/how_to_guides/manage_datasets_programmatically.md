# How to manage datasets programmatically | 🦜️🛠️ LangSmith

On this page

You can use the Python and TypeScript SDK to manage datasets programmatically. This includes creating, updating, and deleting datasets, as well as adding examples to them.

## Create a dataset​

### Create a dataset from list of values​

The most flexible way to make a dataset using the client is by creating examples from a list of inputs and optional outputs. Below is an example.

Note that you can add arbitrary metadata to each example, such as a note or a source. The metadata is stored as a dictionary.

Bulk example creation

If you have many examples to create, consider using the `create_examples`/`createExamples` method to create multiple examples in a single request. If creating a single example, you can use the `create_example`/`createExample` method.

  * Python
  * TypeScript

    
    
    from langsmith import Client  
      
    examples = [  
    {  
      "inputs": {"question": "What is the largest mammal?"},  
      "outputs": {"answer": "The blue whale"},  
      "metadata": {"source": "Wikipedia"},  
    },  
    {  
      "inputs": {"question": "What do mammals and birds have in common?"},  
      "outputs": {"answer": "They are both warm-blooded"},  
      "metadata": {"source": "Wikipedia"},  
    },  
    {  
      "inputs": {"question": "What are reptiles known for?"},  
      "outputs": {"answer": "Having scales"},  
      "metadata": {"source": "Wikipedia"},  
    },  
    {  
      "inputs": {"question": "What's the main characteristic of amphibians?"},  
      "outputs": {"answer": "They live both in water and on land"},  
      "metadata": {"source": "Wikipedia"},  
    },  
    ]  
      
    client = Client()  
    dataset_name = "Elementary Animal Questions"  
      
    # Storing inputs in a dataset lets us  
    # run chains and LLMs over a shared set of examples.  
    dataset = client.create_dataset(  
      dataset_name=dataset_name, description="Questions and answers about animal phylogenetics.",  
    )  
      
    # Prepare inputs, outputs, and metadata for bulk creation  
    client.create_examples(  
      dataset_id=dataset.id,  
      examples=examples  
    )  
    
    
    
    import { Client } from "langsmith";  
      
    const client = new Client();  
      
    const exampleInputs: [string, string][] = [  
    ["What is the largest mammal?", "The blue whale"],  
    ["What do mammals and birds have in common?", "They are both warm-blooded"],  
    ["What are reptiles known for?", "Having scales"],  
    [  
      "What's the main characteristic of amphibians?",  
      "They live both in water and on land",  
    ],  
    ];  
      
    const datasetName = "Elementary Animal Questions";  
      
    // Storing inputs in a dataset lets us  
    // run chains and LLMs over a shared set of examples.  
    const dataset = await client.createDataset(datasetName, {  
    description: "Questions and answers about animal phylogenetics",  
    });  
      
    // Prepare inputs, outputs, and metadata for bulk creation  
    const inputs = exampleInputs.map(([inputPrompt]) => ({ question: inputPrompt }));  
    const outputs = exampleInputs.map(([, outputAnswer]) => ({ answer: outputAnswer }));  
    const metadata = exampleInputs.map(() => ({ source: "Wikipedia" }));  
      
    // Use the bulk createExamples method  
    await client.createExamples({  
    inputs,  
    outputs,  
    metadata,  
    datasetId: dataset.id,  
    });  
    

### Create a dataset from traces​

To create datasets from the runs (spans) of your traces, you can use the same approach. For **many** more examples of how to fetch and filter runs, see the [export traces](/observability/how_to_guides/export_traces) guide. Below is an example:

  * Python
  * TypeScript

    
    
    from langsmith import Client  
      
    client = Client()  
    dataset_name = "Example Dataset"  
      
    # Filter runs to add to the dataset  
    runs = client.list_runs(  
      project_name="my_project",  
      is_root=True,  
      error=False,  
    )  
      
    dataset = client.create_dataset(dataset_name, description="An example dataset")  
      
    # Prepare inputs and outputs for bulk creation  
    examples = [{"inputs": run.inputs, "outputs": run.outputs} for run in runs]  
      
    # Use the bulk create_examples method  
    client.create_examples(  
      dataset_id=dataset.id,  
      examples=examples  
    )  
    
    
    
    import { Client, Run } from "langsmith";  
    const client = new Client();  
      
    const datasetName = "Example Dataset";  
    // Filter runs to add to the dataset  
    const runs: Run[] = [];  
    for await (const run of client.listRuns({  
    projectName: "my_project",  
    isRoot: 1,  
    error: false,  
    })) {  
    runs.push(run);  
    }  
      
    const dataset = await client.createDataset(datasetName, {  
    description: "An example dataset",  
    dataType: "kv",  
    });  
      
    // Prepare inputs and outputs for bulk creation  
    const inputs = runs.map(run => run.inputs);  
    const outputs = runs.map(run => run.outputs ?? {});  
      
    // Use the bulk createExamples method  
    await client.createExamples({  
    inputs,  
    outputs,  
    datasetId: dataset.id,  
    });  
    

### Create a dataset from a CSV file​

In this section, we will demonstrate how you can create a dataset by uploading a CSV file.

First, ensure your CSV file is properly formatted with columns that represent your input and output keys. These keys will be utilized to map your data properly during the upload. You can specify an optional name and description for your dataset. Otherwise, the file name will be used as the dataset name and no description will be provided.

  * Python
  * TypeScript

    
    
    from langsmith import Client  
    import os  
      
    client = Client()  
      
    csv_file = 'path/to/your/csvfile.csv'  
    input_keys = ['column1', 'column2'] # replace with your input column names  
    output_keys = ['output1', 'output2'] # replace with your output column names  
      
    dataset = client.upload_csv(  
      csv_file=csv_file,  
      input_keys=input_keys,  
      output_keys=output_keys,  
      name="My CSV Dataset",  
      description="Dataset created from a CSV file"  
      data_type="kv"  
    )  
    
    
    
    import { Client } from "langsmith";  
      
    const client = new Client();  
      
    const csvFile = 'path/to/your/csvfile.csv';  
    const inputKeys = ['column1', 'column2']; // replace with your input column names  
    const outputKeys = ['output1', 'output2']; // replace with your output column names  
      
    const dataset = await client.uploadCsv({  
      csvFile: csvFile,  
      fileName: "My CSV Dataset",  
      inputKeys: inputKeys,  
      outputKeys: outputKeys,  
      description: "Dataset created from a CSV file",  
      dataType: "kv"  
    });  
    

### Create a dataset from pandas DataFrame (Python only)​

The python client offers an additional convenience method to upload a dataset from a pandas dataframe.
    
    
    from langsmith import Client  
    import os  
    import pandas as pd  
      
    client = Client()  
      
    df = pd.read_parquet('path/to/your/myfile.parquet')  
    input_keys = ['column1', 'column2'] # replace with your input column names  
    output_keys = ['output1', 'output2'] # replace with your output column names  
      
    dataset = client.upload_dataframe(  
        df=df,  
        input_keys=input_keys,  
        output_keys=output_keys,  
        name="My Parquet Dataset",  
        description="Dataset created from a parquet file",  
        data_type="kv" # The default  
    )  
    

## Fetch datasets​

You can programmatically fetch datasets from LangSmith using the `list_datasets`/`listDatasets` method in the Python and TypeScript SDKs. Below are some common calls.

Prerequisites

Initialize the client before running the below code snippets.

  * Python
  * TypeScript

    
    
    from langsmith import Client  
      
    client = Client()  
    
    
    
    import { Client } from "langsmith";  
      
    const client = new Client();  
    

### Query all datasets​

  * Python
  * TypeScript

    
    
    datasets = client.list_datasets()  
    
    
    
    const datasets = await client.listDatasets();  
    

### List datasets by name​

If you want to search by the exact name, you can do the following:

  * Python
  * TypeScript

    
    
    datasets = client.list_datasets(dataset_name="My Test Dataset 1")  
    
    
    
    const datasets = await client.listDatasets({datasetName: "My Test Dataset 1"});  
    

If you want to do a case-invariant substring search, try the following:

  * Python
  * TypeScript

    
    
    datasets = client.list_datasets(dataset_name_contains="some substring")  
    
    
    
    const datasets = await client.listDatasets({datasetNameContains: "some substring"});  
    

### List datasets by type​

You can filter datasets by type. Below is an example querying for chat datasets.

  * Python
  * TypeScript

    
    
    datasets = client.list_datasets(data_type="chat")  
    
    
    
    const datasets = await client.listDatasets({dataType: "chat"});  
    

## Fetch examples​

You can programmatically fetch examples from LangSmith using the `list_examples`/`listExamples` method in the Python and TypeScript SDKs. Below are some common calls.

Prerequisites

Initialize the client before running the below code snippets.

  * Python
  * TypeScript

    
    
    from langsmith import Client  
      
    client = Client()  
    
    
    
    import { Client } from "langsmith";  
      
    const client = new Client();  
    

### List all examples for a dataset​

You can filter by dataset ID:

  * Python
  * TypeScript

    
    
    examples = client.list_examples(dataset_id="c9ace0d8-a82c-4b6c-13d2-83401d68e9ab")  
    
    
    
    const examples = await client.listExamples({datasetId: "c9ace0d8-a82c-4b6c-13d2-83401d68e9ab"});  
    

Or you can filter by dataset name (this must exactly match the dataset name you want to query)

  * Python
  * TypeScript

    
    
    examples = client.list_examples(dataset_name="My Test Dataset")  
    
    
    
    const examples = await client.listExamples({datasetName: "My test Dataset"});  
    

### List examples by id​

You can also list multiple examples all by ID.

  * Python
  * TypeScript

    
    
    example_ids = [  
    '734fc6a0-c187-4266-9721-90b7a025751a',  
    'd6b4c1b9-6160-4d63-9b61-b034c585074f',  
    '4d31df4e-f9c3-4a6e-8b6c-65701c2fed13',  
    ]  
    examples = client.list_examples(example_ids=example_ids)  
    
    
    
      
    const exampleIds = [  
    "734fc6a0-c187-4266-9721-90b7a025751a",  
    "d6b4c1b9-6160-4d63-9b61-b034c585074f",  
    "4d31df4e-f9c3-4a6e-8b6c-65701c2fed13",  
    ];  
    const examples = await client.listExamples({exampleIds: exampleIds});  
    

### List examples by metadata​

You can also filter examples by metadata. Below is an example querying for examples with a specific metadata key-value pair. Under the hood, we check to see if the example's metadata contains the key-value pair(s) you specify.

For example, if you have an example with metadata `{"foo": "bar", "baz": "qux"}`, both `{foo: bar}` and `{baz: qux}` would match, as would `{foo: bar, baz: qux}`.

  * Python
  * TypeScript

    
    
    examples = client.list_examples(dataset_name=dataset_name, metadata={"foo": "bar"})  
    
    
    
    const examples = await client.listExamples({datasetName: datasetName, metadata: {foo: "bar"}});  
    

### List examples by structured filter​

Similar to how you can use the structured filter query language to [fetch runs](/observability/how_to_guides/export_traces#use-filter-query-language), you can use it to fetch examples.

note

This is currently only available in v0.1.83 and later of the Python SDK and v0.1.35 and later of the TypeScript SDK.

Additionally, the structured filter query language is only supported for `metadata` fields.

You can use the `has` operator to fetch examples with metadata fields that contain specific key/value pairs and the `exists` operator to fetch examples with metadata fields that contain a specific key. Additionally, you can also chain multiple filters together using the `and` operator and negate a filter using the `not` operator.

  * Python
  * TypeScript

    
    
    examples = client.list_examples(  
      dataset_name=dataset_name,  
      filter='and(not(has(metadata, \'{"foo": "bar"}\')), exists(metadata, "tenant_id"))'  
    )  
    
    
    
    const examples = await client.listExamples({datasetName: datasetName, filter: 'and(not(has(metadata, \'{"foo": "bar"}\')), exists(metadata, "tenant_id"))'});  
    

## Update examples​

### Update single example​

You can programmatically update examples from LangSmith using the `update_example`/`updateExample` method in the Python and TypeScript SDKs. Below is an example.

  * Python
  * TypeScript

    
    
    client.update_example(  
      example_id=example.id,  
      inputs={"input": "updated input"},  
      outputs={"output": "updated output"},  
      metadata={"foo": "bar"},  
      split="train"  
    )  
    
    
    
    await client.updateExample(example.id, {  
    inputs: { input: "updated input" },  
    outputs: { output: "updated output" },  
    metadata: { "foo": "bar" },  
    split: "train",  
    })  
    

### Bulk update examples​

You can also programmatically update multiple examples in a single request with the `update_examples`/`updateExamples` method in the Python and TypeScript SDKs. Below is an example.

  * Python
  * TypeScript

    
    
    client.update_examples(  
      example_ids=[example.id, example_2.id],  
      inputs=[{"input": "updated input 1"}, {"input": "updated input 2"}],  
      outputs=[  
          {"output": "updated output 1"},  
          {"output": "updated output 2"},  
      ],  
      metadata=[{"foo": "baz"}, {"foo": "qux"}],  
      splits=[["training", "foo"], "training"] # Splits can be arrays or standalone strings  
    )  
    
    
    
    await client.updateExamples([  
    {  
      id: example.id,  
      inputs: { input: "updated input 1" },  
      outputs: { output: "updated output 1" },  
      metadata: { foo: "baz" },  
      split: ["training", "foo"] // Splits can be arrays or standalone strings  
    },  
    {  
      id: example2.id,  
      inputs: { input: "updated input 2" },  
      outputs: { output: "updated output 2" },  
      metadata: { foo: "qux" },  
      split: "training"  
    },  
    ])  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Create a dataset
    * Create a dataset from list of values
    * Create a dataset from traces
    * Create a dataset from a CSV file
    * Create a dataset from pandas DataFrame (Python only)
  * Fetch datasets
    * Query all datasets
    * List datasets by name
    * List datasets by type
  * Fetch examples
    * List all examples for a dataset
    * List examples by id
    * List examples by metadata
    * List examples by structured filter
  * Update examples
    * Update single example
    * Bulk update examples

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)