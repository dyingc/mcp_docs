# Running an evaluation from the prompt playground | 🦜️🛠️ LangSmith

On this page

LangSmith allows you to run evaluations directly in the [prompt playground](/prompt_engineering/concepts#prompt-playground). The prompt playground allows you to test your prompt and/or model configuration over a series of inputs to see how well it scores across different contexts or scenarios, without having to write any code.

Before you run an evaluation, you need to have an [existing dataset](/evaluation/concepts#datasets). Learn how to [create a dataset from the UI](/evaluation/how_to_guides/manage_datasets_in_application#set-up-your-dataset).

If you prefer to run experiments in code, visit [run an evaluation using the SDK](/evaluation/how_to_guides/evaluate_llm_application).

![](/assets/images/playground_experiment-82c9290c515102da892c5a5c261d4e2e.gif)

## Create an experiment in the prompt playground​

  1. **Navigate to the playground** by clicking **Playground** in the sidebar.
  2. **Add a prompt** by selecting an existing saved a prompt or creating a new one.
  3. **Select a dataset** from the **Test over dataset** dropdown

  * Note that the keys in the dataset input must match the input variables of the prompt. For example, in the above video the selected dataset has inputs with the key "blog", which correctly match the input variable of the prompt.
  * There is a maximum of 15 input variables allowed in the prompt playground.

  4. **Start the experiment** by clicking on the **Start** or CMD+Enter. This will run the prompt over all the examples in the dataset and create an entry for the experiment in the dataset details page. We recommend committing the prompt to the prompt hub before starting the experiment so that it can be easily referenced later when reviewing your experiment.
  5. **View the full results** by clicking **View full experiment**. This will take you to the experiment details page where you can see the results of the experiment.

## Add evaluation scores to the experiment​

Evaluate your experiment over specific critera by adding evaluators. Add LLM-as-a-judge or custom code evaluators in the playground using the **+Evaluator** button.

To learn more about adding evaluators in via UI, visit [how to define an LLM-as-a-judge evaluator](/evaluation/how_to_guides/llm_as_judge).

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Create an experiment in the prompt playground
  * Add evaluation scores to the experiment

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)