# Create an account and API key | 🦜️🛠️ LangSmith

On this page

## Create an account​

To get started with LangSmith, you need to create an account. You can sign up for a free account [here](https://smith.langchain.com). We support logging in with Google, GitHub, and email.

![](/assets/images/create_account-0f1187e246adb36940a04b89ac2c28a4.png)

## API keys​

LangSmith supports two types of API keys: Service Keys and Personal Access Tokens. Both types of tokens can be used to authenticate requests to the LangSmith API, but they have different use cases.

Read more about the differences between Service Keys and Personal Access Tokens under [admin concepts](/administration/concepts)

## Create an API key​

To log traces and run evaluations with LangSmith, you will need to create an API key to authenticate your requests. Currently, an API key is scoped to a workspace, so you will need to create an API key for each workspace you want to use.

To create either type of API key head to the [Settings page](https://smith.langchain.com/settings), then scroll to the **API Keys** section. Then click **Create API Key.**

note

The API key will be shown only once, so make sure to copy it and store it in a safe place.

![](/assets/images/create_api_key-5fab98924105622c8db8d23924f0a1dc.png)

## Configure the SDK​

You may set the following environment variables in addition to `LANGSMITH_API_KEY`.  
These are only required if using the EU instance.

`LANGSMITH_ENDPOINT=``https://api.smith.langchain.com`

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Create an account
  * API keys
  * Create an API key
  * Configure the SDK

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)