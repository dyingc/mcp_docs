# How to define an LLM-as-a-judge evaluator | 🦜️🛠️ LangSmith

Key concepts

  * [LLM-as-a-judge evaluator](/evaluation/concepts#llm-as-judge)

LLM applications can be challenging to evaluate since they often generate conversational text with no single correct answer.

This guide shows you how to define an LLM-as-a-judge evaluator for [offline evaluation](/evaluation/concepts#offline-evaluation) using either the LangSmith SDK or the UI. Note: To run evaluations in real-time on your production traces, refer to [setting up online evaluations](/observability/how_to_guides/online_evaluations#configure-llm-as-judge-evaluators).

  * SDK
  * UI

## Pre-built evaluators​

Pre-built evaluators are a useful starting point for setting up evaluations. Refer to [pre-built evaluators](/evaluation/how_to_guides/prebuilt_evaluators) for how to use pre-built evaluators with LangSmith.

## Create your own LLM-as-a-judge evaluator​

For complete control of evaluator logic, create your own LLM-as-a-judge evaluator and run it using the LangSmith SDK ([Python](https://docs.smith.langchain.com/reference/python/reference) / [TypeScript](https://docs.smith.langchain.com/reference/js)).

  * Python

Requires `langsmith>=0.2.0`
    
    
    from langsmith import evaluate, traceable, wrappers, Client  
    from openai import OpenAI  
    # Assumes you've installed pydantic  
    from pydantic import BaseModel  
      
    # Optionally wrap the OpenAI client to trace all model calls.  
    oai_client = wrappers.wrap_openai(OpenAI())  
        
    def valid_reasoning(inputs: dict, outputs: dict) -> bool:  
      """Use an LLM to judge if the reasoning and the answer are consistent."""  
      
      instructions = """\  
      
    Given the following question, answer, and reasoning, determine if the reasoning \  
    for the answer is logically valid and consistent with question and the answer.\  
    """  
      
      class Response(BaseModel):  
        reasoning_is_valid: bool  
      
      msg = f"Question: {inputs['question']}\nAnswer: {outputs['answer']}\nReasoning: {outputs['reasoning']}"  
      response = oai_client.beta.chat.completions.parse(  
        model="gpt-4o",  
        messages=[{"role": "system", "content": instructions,}, {"role": "user", "content": msg}],  
        response_format=Response  
      )  
      return response.choices[0].message.parsed.reasoning_is_valid  
      
    # Optionally add the 'traceable' decorator to trace the inputs/outputs of this function.  
    @traceable  
    def dummy_app(inputs: dict) -> dict:  
      return {"answer": "hmm i'm not sure", "reasoning": "i didn't understand the question"}  
      
    ls_client = Client()  
    dataset = ls_client.create_dataset("big questions")  
    examples = [  
      {"inputs": {"question": "how will the universe end"}},  
      {"inputs": {"question": "are we alone"}},  
    ]  
    ls_client.create_examples(dataset_id=dataset.id, examples=examples)  
      
    results = evaluate(  
      dummy_app,  
      data=dataset,  
      evaluators=[valid_reasoning]  
    )  
    

See [here](/evaluation/how_to_guides/custom_evaluator) for more on how to write a custom evaluator.

## Pre-built evaluators​

Pre-built evaluators are a useful starting point when setting up evaluations. The LangSmith UI supports the following pre-built evaluators:

  * **Hallucination** : Detect factually incorrect outputs. Requires a reference output.
  * **Correctness** : Check semantic similarity to a reference.
  * **Conciseness** : Evaluate whether an answer is a concise response to a question.
  * **Code checker** : Verify correctness of code answers.

You can configure these evaluators::

  * When running an evaluation using the [playground](/prompt_engineering/concepts#prompt-playground)
  * As part of a dataset to [automatically run experiments over a dataset](/evaluation/how_to_guides/bind_evaluator_to_dataset)
  * When running an [online evaluation](/observability/how_to_guides/online_evaluations#configure-llm-as-judge-evaluators)

## Customize your LLM-as-a-judge evaluator​

Add specific instructions for your LLM-as-a-judge evalutor prompt and configure which parts of the input/output/reference output should be passed to the evaluator.

![](/assets/images/playground_evaluator-3758d5cbed9fcb836ca929b9d7d93a1e.gif)

### Select/create the evaluator​

  * In the playground or from a dataset: Select the **+Evaluator** button
  * From a tracing project: Select **Add rules** , configure your rule and select **Apply evaluator**

Select the **Create your own evaluator option**. Alternativley, you may start by selecting a pre-built evaluator and editing it.

### Configure the evaluator​

#### Prompt​

Create a new prompt, or choose an existing prompt from the [prompt hub](/prompt_engineering/quickstarts/quickstart_ui).

  * **Create your own prompt** : Create a custom prompt inline.

  * **Pull a prompt from the prompt hub** : Use the **Select a prompt** dropdown to select from an existing prompt. You can't edit these prompts directly within the prompt editor, but you can view the prompt and the schema it uses. To make changes, edit the prompt in the playground and commit the version, and then pull in your new prompt in the evaluator.

#### Model​

Select the desired model from the provided options.

#### Mapping variables​

Use variable mapping to indicate the variables that are passed into your evaluator prompt from your run or example. To aid with variable mapping, an example (or run) is provided for reference. Click on the the variables in your prompt and use the dropdown to map them to the relevant parts of the input, output, or reference output.

To add prompt variables type the variable with double curly brackets `{{prompt_var}}` if using mustache formatting (the default) or single curly brackets `{prompt_var}` if using f-string formatting.

You may remove variables as needed. For example if you are evaluating a metric such as conciseness, you typically don't need a reference output so you may remove that variable.

#### Preview​

Previewing the prompt will show you of what the formatted prompt will look like using the reference run and dataset example shown on the right.

#### Improve your evaluator with few-shot examples​

To better align the LLM-as-a-judge evaluator to human preferences, LangSmith allows you to collect [human corrections](/evaluation/how_to_guides/create_few_shot_evaluators#make-corrections) on evaluator scores. With this selection enabled, corrections are then inserted automatically as few-shot examples into your prompt.

Learn [how to set up few-shot examples and make corrections](/evaluation/how_to_guides/create_few_shot_evaluators).

#### Feedback configuration​

Feedback configuration is the scoring criteria that your LLM-as-a-judge evaluator will use. Think of this as the rubric that your evaluator will grade based on. Scores will be added as [feedback](/observability/concepts#feedback) to a run or example. Defining feedback for your evaluator:

  1. **Name the feedback key** : This is the name that will appear when viewing evaluation results. Names should be unique across experiments.

  2. **Add a description** : Describe what the feedback represents.

  3. **Choose a feedback type** :

  * **Boolean** : True/false feedback.
  * **Categorical** : Select from predefined categories.
  * **Continuous** : Numerical scoring within a specified range.

Behind the scenes, feedback configuration is added as [structured output](https://python.langchain.com/docs/concepts/structured_outputs/) to the LLM-as-a-judge prompt. If you're using an existing prompt from the hub, you must add an output schema to the prompt before configuring an evaluator to use it. Each top-level key in the output schema will be treated as a separate piece of feedback.

### Save the evaluator​

Once your are finished configuring, save your changes.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)