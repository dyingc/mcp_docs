# Prompt Engineering Quick Start (UI) | 🦜️🛠️ LangSmith

On this page

This quick start will walk through how to create, test, and iterate on prompts in LangSmith.

QuickStart

This tutorial uses the UI for prompt engineering, if you are interested in using the SDK instead, read [this guide](/prompt_engineering/quickstarts/quickstart_sdk).

## 1\. Setup​

The only setup needed for this guide is to make sure you have signed up for a [LangSmith](https://langsmith.com) account.

## 2\. Create a prompt​

To create a prompt in LangSmith, navigate to the **Prompts** section of the left-hand sidebar and click on the “+ New Prompt” button. You can then modify the prompt by editing/adding messages and input variables.

![](/assets/images/create_prompt_ui-cbf004294a153b92d9bf31e05c31cb9e.gif)

## 3\. Test a prompt​

To test a prompt, set the model configuration you want to use, add your LLM provider's API key, specify the prompt input values you want to test, and then click "Start".

To learn about more options for configuring your prompt in the playground, check out this [guide](/prompt_engineering/how_to_guides/managing_model_configurations). If you are interested in testing how your prompt performs over a dataset instead of individual examples, read [this page](/evaluation?mode=ui).

![](/assets/images/test_prompt_ui-2e14355570ca743ccd19a947d859a2c3.gif)

## 4\. Save a prompt​

One you have run some tests and made your desired changes to your prompt you can click the “Save” button to save your prompt for future use.

![](/assets/images/save_prompt_ui-1b8e22452b7e60bd004a3415abbfe21b.gif)

## 5\. Iterate on a prompt​

LangSmith makes it easy to iterate on prompts with your entire team. Members of your workspace can select a prompt to iterate on in the playground, and once they are happy with their changes, they can simply save it as a new commit.

To improve your prompts:

  * We recommend referencing the documentation provided by your model provider for best practices in prompt creation, such as [Best practices for prompt engineering with the OpenAI API](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api) and [Gemini’s Introduction to prompt design](https://ai.google.dev/gemini-api/docs/prompting-intro).

  * To help with iterating on your prompts in LangSmith, we've created Prompt Canvas — an interactive tool to build and optimize your prompts. Learn about how to use [Prompt Canvas](/prompt_engineering/concepts#prompt-canvas).

![](/assets/images/save_prompt_commit_ui-4769dd50d77ded4d8b0647b6cf6d0fd8.gif)

You can also tag specific commits to mark important moments in your commit history:

![](/assets/images/tag_prompt_ui-c03cd8243cce44568982a85e64ce6b20.gif)

## 6\. Next steps​

  * Learn more about how to store and manage prompts using the Prompt Hub in [these how-to guides](/prompt_engineering/how_to_guides#prompt-hub)
  * Learn more about how to use the playground for prompt engineering in [these how-to guides](/prompt_engineering/how_to_guides#playground)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * 1\. Setup
  * 2\. Create a prompt
  * 3\. Test a prompt
  * 4\. Save a prompt
  * 5\. Iterate on a prompt
  * 6\. Next steps