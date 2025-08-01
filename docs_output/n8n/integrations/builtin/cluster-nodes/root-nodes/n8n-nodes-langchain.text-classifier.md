# Text Classifier node documentation | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier.md "Edit this page")

# Text Classifier node#

Use the Text Classifier node to classify (categorize) incoming data. Using the categories provided in the parameters (see below), each item is passed to the model to determine its category.

On this page, you'll find the node parameters for the Text Classifier node, and links to more resources.

## Node parameters#

  * **Input Prompt** defines the input to classify. This is usually an expression that references a field from the input items. For example, this could be `{{ $json.chatInput }}` if the input is a chat trigger. By default it references the `text` field.
  * **Categories** : Add the categories that you want to classify your input as. Categories have a name and a description. Use the description to tell the model what the category means. This is important if the meaning isn't obvious. You can add as many categories as you like.

## Node options#

  * **Allow Multiple Classes To Be True** : You can configure the classifier to always output a single class per item (turned off), or allow the model to select multiple classes (turned on).
  * **When No Clear Match** : Define what happens if the model can't find a good match for an item. There are two options:
    * **Discard Item** (the default): If the node doesn't detect any of the categories, it drops the item.
    * **Output on Extra, 'Other' Branch** : Creates a separate output branch called **Other**. When the node doesn't detect any of the categories, it outputs items in this branch.
  * **System Prompt Template** : Use this option to change the system prompt that's used for the classification. It uses the `{categories}` placeholder for the categories.

  * **Enable Auto-Fixing** : When enabled, the node automatically fixes model outputs to ensure they match the expected format. Do this by sending the schema parsing error to the LLM and asking it to fix it.

## Related resources#

View n8n's [Advanced AI](../../../../../advanced-ai/) documentation.

## AI glossary#

  * **completion** : Completions are the responses generated by a model like GPT.
  * **hallucinations** : Hallucination in AI is when an LLM (large language model) mistakenly perceives patterns or objects that don't exist.
  * **vector database** : A vector database stores mathematical representations of information. Use with embeddings and retrievers to create a database that your AI can access when answering questions.
  * **vector store** : A vector store, or vector database, stores mathematical representations of information. Use with embeddings and retrievers to create a database that your AI can access when answering questions.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top