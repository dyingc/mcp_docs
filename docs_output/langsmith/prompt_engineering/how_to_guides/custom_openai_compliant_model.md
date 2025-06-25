# Run the playground against an OpenAI-compliant model provider/proxy | 🦜️🛠️ LangSmith

On this page

The LangSmith playground allows you to use any model that is compliant with the OpenAI API. You can utilize your model by setting the Proxy Provider for `OpenAI` in the playground.

## Deploy an OpenAI compliant model​

Many providers offer OpenAI compliant models or proxy services. Some examples of this include:

  * [LiteLLM Proxy](https://github.com/BerriAI/litellm?tab=readme-ov-file#quick-start-proxy---cli)
  * [Ollama](https://ollama.com/)

You can use these providers to deploy your model and get an API endpoint that is compliant with the OpenAI API.

Take a look at the full [specification](https://platform.openai.com/docs/api-reference/chat) for more information.

## Use the model in the LangSmith Playground​

Once you have deployed a model server, you can use it in the LangSmith Playground. Enter the playground and select the `Proxy Provider` inside the `OpenAI` modal.

![OpenAI Proxy Provider](/assets/images/openai_proxy_provider-69efe92e79a8bff3d690cec9493d22d2.png)

If everything is set up correctly, you should see the model's response in the playground. You can also use this functionality to invoke downstream pipelines as well.

See how to store your model configuration for later use [here](/prompt_engineering/how_to_guides/managing_model_configurations).

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Deploy an OpenAI compliant model
  * Use the model in the LangSmith Playground

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)