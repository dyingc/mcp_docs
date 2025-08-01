# Embeddings HuggingFace Inference node documentation | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference.md "Edit this page")

# Embeddings HuggingFace Inference node#

Use the Embeddings HuggingFace Inference node to generate [embeddings](../../../../../glossary/#ai-embedding) for a given text.

On this page, you'll find the node parameters for the Embeddings HuggingFace Inference, and links to more resources.

Credentials

You can find authentication information for this node [here](../../../credentials/huggingface/).

Parameter resolution in sub-nodes

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

## Node parameters#

  * **Model** : Select the model to use to generate the embedding.

Refer to the [Hugging Face models documentation](https://huggingface.co/models?other=embeddings) for available models.

## Node options#

  * **Custom Inference Endpoint** : Enter the URL of your deployed model, hosted by HuggingFace. If you set this, n8n ignores the **Model Name**.

Refer to [HuggingFace's guide to inference](https://huggingface.co/inference-endpoints) for more information.

## Templates and examples#

**Building Your First WhatsApp Chatbot**

by Jimleuk

[View template details](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)

**Ask questions about a PDF using AI**

by David Roberts

[View template details](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)

**Chat with PDF docs using AI (quoting sources)**

by David Roberts

[View template details](https://n8n.io/workflows/2165-chat-with-pdf-docs-using-ai-quoting-sources/)

[Browse Embeddings HuggingFace Inference integration templates](https://n8n.io/integrations/embeddings-hugging-face-inference/), or [search all templates](https://n8n.io/workflows/)

## Related resources#

Refer to [Langchain's HuggingFace Inference embeddings documentation](https://js.langchain.com/docs/integrations/text_embedding/hugging_face_inference/) for more information about the service.

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