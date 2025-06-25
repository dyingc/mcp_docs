# Managing Prompt Settings | 🦜️🛠️ LangSmith

On this page

The LangSmith playground enables you to control various settings for your prompt. These include the model configuration, tool settings, and prompt formatting.

![Prompt Settings](/assets/images/prompt_settings-041cc4809434e305f3f297add3d1999e.png)

## Model Configurations​

Model configurations are the set of parameters against which your prompt is run. For example, they include the provider, model, and temperature, among others. The LangSmith playground allows you to save and manage your model configurations, making it easy to reuse preferred settings across multiple prompts and sessions.

### Creating Saved Configurations​

  1. Adjust the model configuration as desired
  2. Click the `Save As` button in the top bar
  3. Enter a name and optional description for your configuration and confirm.

Your configuration is now saved and ready to be accessed by anyone in your organization's workspace. All saved configurations are available in the `Model configuration` dropdown.

### Default Configurations​

Once you have created a saved configuration, you can optionally set it as your default, so any new prompt you create will automatically use this configuration. To set a configuration as your default, click the `Set as default` button next to the dropdown.

![Setting Default Configuration](/assets/images/set_default_config-af0255a161071a2d21c74155951fb9e6.png)

### Editing Configurations​

  * To rename or update the description: Click the configuration name or description and make your changes.

  * To update the current configuration's parameters: Make any desired to the parameters and click the `Save` button at the top.

### Deleting Configurations​

  1. Select the configuration you want to remove
  2. Click the trash can icon to delete it

## Tool Settings​

Tools enable your LLM to perform tasks like searching the web, looking up information, and more. Here you can manage the ways your LLM can utilize and access the tools you have defined in your prompt. Learn more about tools [here](/prompt_engineering/concepts#tools).

## Prompt Formatting​

For information on chat and completion prompts, see [here](/prompt_engineering/concepts#chat-vs-completion). For information about prompt templating and using variables, see [here](/prompt_engineering/concepts#f-string-vs-mustache).

## Extra Parameters​

The **Extra Parameters** field allows you to pass additional model parameters that aren't directly supported in the LangSmith interface. This is particularly useful in two scenarios:

  1. When model providers release new parameters that haven't yet been integrated into the LangSmith interface. You can specify these parameters in JSON format to use them right away.

![Extra Params](/assets/images/extra_params-544de3114ed19a30449bf3e17c4767fd.png)

  2. When troubleshooting parameter-related errors in the playground. If you receive an error about unnecessary parameters (more common when using LangChainJS for run tracing), you can use this field to remove the extra parameters.

![Extra Params](/assets/images/extra_params_error-0be24963963b558ce279124404e0117b.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Model Configurations
    * Creating Saved Configurations
    * Default Configurations
    * Editing Configurations
    * Deleting Configurations
  * Tool Settings
  * Prompt Formatting
  * Extra Parameters

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)