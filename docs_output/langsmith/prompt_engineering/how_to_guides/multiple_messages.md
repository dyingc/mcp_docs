# How to use multiple messages in the playground | 🦜️🛠️ LangSmith

On this page

This how-to guide walks you through the various ways you can set up the playground for multi-turn conversations, which will allow you to test different tool configurations and system prompts against longer threads of messages.

![](/assets/images/multiturn_diagram-a1dbc6180bf819d625af42eece802b0b.png)

## From an existing run​

First, ensure you have properly [traced](/observability) a multi-turn conversation, and then navigate to your tracing project. Once you get to your tracing project simply open the run, select the LLM call, and open it in the playground as follows:

![](/assets/images/multiturn_from_run-ac1a7c1e0f9e5cedf61ac6eaeb9ca540.gif)

You can then edit the system prompt, tweak the tools and/or output schema and observe how the output of the multi-turn conversation changes.

## From a dataset​

Before starting, make sure you have [set up your dataset](/evaluation/how_to_guides/manage_datasets_in_application). Since you want to evaluate multi-turn conversations, make sure there is a key in your inputs that contains a list of messages.

Once you have created your dataset, head to the playground and [load your dataset](/evaluation/how_to_guides/manage_datasets_in_application#from-the-prompt-playground) to evaluate.

Then, add a messages list variable to your prompt, making sure to name it the same as the key in your inputs that contains the list of messages:

![](/assets/images/multiturn_from_dataset-d1acbc18bd4b13f8b69889fc24383c1e.gif)

When you run your prompt, the messages from each example will be added as a list in place of the 'Messages List' variable.

## Manually​

There are two ways to manually create multi-turn conversations. The first way is by simply appending messages to the prompt:

![](/assets/images/multiturn_manual-9751aa036ce3bfdb663b24b5120a2091.gif)

This is helpful for quick iteration, but is rigid since the multi-turn conversation is hardcoded. Instead, if you want your prompt to work with any multi-turn conversation you can add a 'Messages List' variable and add your multi-turn conversation there:

![](/assets/images/multiturn_manual_list-340c009a4029f2a007e6e868a2eb8526.gif)

This allows you to just tweak the system prompt or the tools, while allowing any multi-turn conversation to take the place of the `Messages List` variable, allowing you to reuse this prompt across various runs.

## Next Steps​

Now that you know how to set up the playground for multi-turn interactions, you can either manually inspect and judge the outputs, or you can [add evaluators](/evaluation/how_to_guides#define-an-evaluator) to classify results.

You can also read [these how-to guides](/prompt_engineering/how_to_guides#playground) to learn more about how to use the playground to run evaluations.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * From an existing run
  * From a dataset
  * Manually
  * Next Steps

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)