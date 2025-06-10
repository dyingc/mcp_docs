# DeepL node documentation | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.deepl.md "Edit this page")

# DeepL node#

Use the DeepL node to automate work in DeepL, and integrate DeepL with other applications. n8n has built-in support for a wide range of DeepL features, including translating languages.

On this page, you'll find a list of operations the DeepL node supports and links to more resources.

Credentials

Refer to [DeepL credentials](../../credentials/deepl/) for guidance on setting up authentication. 

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](../../../../advanced-ai/examples/using-the-fromai-function/).

## Operations#

  * Language
    * Translate data

## Templates and examples#

**Translate PDF documents from Google drive folder with DeepL**

by Milorad Filipovic

[View template details](https://n8n.io/workflows/2179-translate-pdf-documents-from-google-drive-folder-with-deepl/)

**Translate cocktail instructions using DeepL**

by Harshil Agrawal

[View template details](https://n8n.io/workflows/998-translate-cocktail-instructions-using-deepl/)

**Real-time Chat Translation with DeepL**

by Ghufran Ridhawi

[View template details](https://n8n.io/workflows/4532-real-time-chat-translation-with-deepl/)

[Browse DeepL integration templates](https://n8n.io/integrations/deepl/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported#

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node: 

  1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
  2. Select the service you want to connect to.
  3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top