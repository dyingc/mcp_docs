# Creating and Managing Datasets in the UI | 🦜️🛠️ LangSmith

On this page

[Datasets](/evaluation/concepts#datasets) enable you to perform repeatable evaluations over time using consistent data. Datasets are made up of [examples](/evaluation/concepts#examples), which store inputs, outputs, and optionally, reference outputs.

Recommended Reading

For more information on datasets, evaluations and examples, read the [concepts guide on evaluation and datasets](/evaluation/concepts#datasets-and-examples).

This guide outlines the various methods for creating and editing datasets in LangSmith's UI.

## Create a dataset and add examples​

### Manually from a tracing project​

A common pattern for constructing datasets is to convert notable traces from your application into dataset examples. This approach requires that you have [tracing to LangSmith configured](/observability/how_to_guides#tracing-configuration).

tip

A powerful technique to build datasets is to filter-down into the most interesting traces, such as traces that were tagged with poor user feedback, and add them to a dataset. For tips on how to filter traces, see the [filtering traces](/observability/how_to_guides/filter_traces_in_application) guide.

There are two ways to manually add data from a tracing projects to datasets.

  1. Multi-select runs from the runs table:

![Multi-select runs](/assets/images/multiselect_add_to_dataset-032bf091161634acb71dc7060806d538.png)

  2. Navigate to the run details page and click `Add to -> Dataset` on the top right corner:

![Add to dataset](/assets/images/add_to..dataset-a5ad64c85cfa95f376b45b3e4da50de6.png)

When you select a dataset from the run details page, a modal will pop up letting you know if any [transformations](/reference/evaluation/dataset_transformations) were applied or if schema validation failed. For example, the screenshot below shows a dataset that is using transformations to optimize for collecting LLM runs.

![](/assets/images/confirmation-6ccb70467ab3b9b6fa443542be3b2eed.png)

You can then optionally edit the run before adding it to the dataset.

### Automatically from a tracing project​

You can use [run rules](/observability/how_to_guides/rules) to automatically add traces to a dataset based on certain conditions. For example, you could add all traces that are [tagged](/observability/concepts#tags) with a specific use case or have a [low feedback score](/observability/concepts#feedback).

### From examples in an Annotation Queue​

tip

If you rely on subject matter experts to build meaningful datasets, use [annotation queues](/evaluation/how_to_guides/annotation_queues) to provide a streamlined view for reviewiers. Human reviewers can optionally modify the inputs/outputs/reference outputs from a trace before it is added to the dataset.

Annotation queues are can be optionally configured with a default dataset, though you can add runs to any dataset by using the dataset switcher on the bottom of the screen. Once you select the right dataset, click **Add to Dataset** or hit the hot key `D` to add the run to it.

Any modifications you make to the run in your annotation queue will carry over to the dataset, and all metadata associated with the run will also be copied.

![](/assets/images/add_to_dataset_from_aq-408cc394da41a056a445db618006da4b.png)

Note you can also set up rules to add runs that meet specific criteria to an annotation queue using [automation rules](/observability/how_to_guides/rules).

### From the Prompt Playground​

On the [**Prompt Playground**](/prompt_engineering/concepts#prompt-playground) page, select **Set up Evaluation** , click **+New** if you're starting a new dataset or select from an existing dataset.

note

Creating datasets inline in the playground is not supported for datasets that have nested keys. In order to add/edit examples with nested keys, you must edit [from the datasets page](/evaluation/how_to_guides/manage_datasets_in_application#from-the-datasets-page).

To edit the examples:

  * Use **+Row** to add a new example to the dataset
  * Delete an example using the **⋮** dropdown on the right hand side of the table
  * If you're creating a reference-free dataset remove the "Reference Output" column using the **x** button in the column. Note: this action is not reversable.

![Create a dataset in the playground](/assets/images/playground_dataset-16e4c1414dc5c0f4ef49aad407ea61bd.png)

### Import a dataset from a CSV or JSONL file​

On the **Datasets & Experiments** page, click **+New Dataset** , then **Import** an existing dataset from CSV or JSONL file.

### Create a new dataset from the dataset page​

On the **Datasets & Experiments** page, click **+New Dataset** , then **Create an empty dataset**. You can optionally create a [dataset schema](/evaluation/how_to_guides/manage_datasets_in_application#create-a-dataset-schema) to validate your dataset.

Then to add examples inline, go to the **Examples** tab, and click **\+ Example`**. This will let you define examples in JSON inline.

#### Add synthetic examples created by an LLM via the Datasets UI​

If you have a schema defined on your dataset, when you click `+ Example` you'll see an option to `Generate examples`. This will use an LLM to create synthetic examples.

You have to do the following:

  1. **Select few-shot examples** : Choose a set of examples to guide the LLM's generation. You can manually select these examples from your dataset or use the automatic selection option.
  2. **Specify the number of examples** : Enter the number of synthetic examples you want to generate.
  3. **Configure API Key** : Ensure your OpenAI API key is entered at the "API Key" link. ![Generate Synthetic Examples](/assets/images/generate_synthetic_examples_create-56bd15927775ccf275ad925b18d3e6c8.png)

After clicking "Generate," the examples will appear on the page. You can choose which examples to add to your dataset, with the option to edit them before finalizing. Each example will be validated against your specified dataset schema and tagged as "synthetic" in the source metadata. ![Generate Synthetic Examples](/assets/images/generate_synthetic_examples_pane-81203111cd8bbd1477dd85c8de6864cd.png)

## Manage a Dataset​

### Create a dataset schema​

LangSmith datasets store arbitrary JSON objects. We recommend (but do not require) that you define a schema for your dataset to ensure that they confirm to a specific JSON schema. Dataset schemas are defined with standard [JSON schema](https://json-schema.org/), with the addition of a few [prebuilt types](/reference/data_formats/dataset_json_types) that make it easier to type common primitives like messages and tools.

Certain fields in your schema have a `+ Transformations` option. Transformations are preprocessing steps that, if enabled, update your examples when you add them to the dataset. For example the `convert to OpenAI messages` transformation will convert message-like objects, like LangChain messages, to OpenAI message format.

For the full list of available transformations, see [our reference](/reference/evaluation/dataset_transformations).

note

If you plan to collect production traces in your dataset from LangChain [ChatModels](https://python.langchain.com/docs/concepts/chat_models/) or from OpenAI calls using the [LangSmith OpenAI wrapper](/observability/how_to_guides/annotate_code#wrap-the-openai-client), we offer a prebuilt Chat Model schema that converts messages and tools into industry standard openai formats that can be used downstream with any model for testing. You can also customize the template settings to match your use case.

Please see the [dataset transformations reference](/reference/evaluation/dataset_transformations) for more information.

### Create and manage dataset splits​

Dataset splits are divisions of your dataset that you can use to segment your data. For example, it is common in machine learning workflows to split datasets into training, validation, and test sets. This can be useful to prevent overfitting - where a model performs well on the training data but poorly on unseen data. In evaluation workflows, it can be useful to do this when you have a dataset with multiple categories that you may want to evaluate separately; or if you are testing a new use case that you may want to include in your dataset in the future, but want to keep separate for now. Note that the same effect can be achieved manually via metadata - but we expect splits to be used for higher level organization of your dataset to split it into separate groups for evaluation, whereas metadata would be used more for storing information on your examples like tags and information about its origin.

In machine learning, it is best practice to keep your splits separate (each example belongs to exactly one split). However, we allow you to select multiple splits for the same example in LangSmith because it can make sense for some evaluation workflows - for example, if an example falls into multiple categories on which you may want to evaluate your application.

In order to create and manage splits in the app, you can select some examples in your dataset and click "Add to Split". From the resulting popup menu, you can select and unselect splits for the selected examples, or create a new split.

![Add to Split](/assets/images/add_to_split2-c6b072fe5df6ce8a004f5bc4b2c75ae7.png)

### Edit example metadata​

You can add metadata to your examples by clicking on an example and then clicking "Edit" on the top righthand side of the popover. From this page, you can update/delete existing metadata, or add new metadata. You may use this to store information about your examples, such as tags or version info, which you can then [group by](/evaluation/how_to_guides/analyze_single_experiment#group-results-by-metadata) when analyzing experiment results or [filter by](/evaluation/how_to_guides/manage_datasets_programmatically#list-examples-by-metadata) when you call `list_examples` in the SDK.

![Add Metadata](/assets/images/add_metadata-100a332ca8f6421a6f43c88361181f66.gif)

### Filter examples​

You can filter examples by split, metadata key/value or perform full-text search over examples. These filtering options are available to the top left of the examples table.

  * **Filter by split** : Select split > Select a split to filter by
  * **Filter by metadata** : Filters > Select "Metadata" from the dropdown > Select the metadata key and value to filter on
  * **Full-text search** : Filters > Select "Full Text" from the dropdown > Enter your search criteria

You may add multiple filters, and only examples that satisfy all of the filters will be displayed in the table.

![Filters Applied to Examples](/assets/images/filters_applied-ea9d9457977560cf69b45c3698740744.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Create a dataset and add examples
    * Manually from a tracing project
    * Automatically from a tracing project
    * From examples in an Annotation Queue
    * From the Prompt Playground
    * Import a dataset from a CSV or JSONL file
    * Create a new dataset from the dataset page
  * Manage a Dataset
    * Create a dataset schema
    * Create and manage dataset splits
    * Edit example metadata
    * Filter examples

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)