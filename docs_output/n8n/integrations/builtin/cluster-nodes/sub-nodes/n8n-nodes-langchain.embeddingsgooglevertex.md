# Embeddings Google Vertex node documentation | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex.md "Edit this page")

# Embeddings Google Vertex node#

Use the Embeddings Google Vertex node to generate [embeddings](../../../../../glossary/#ai-embedding) for a given text.

On this page, you'll find the node parameters for the Embeddings Google Vertex node, and links to more resources.

Credentials

You can find authentication information for this node [here](../../../credentials/google/service-account/).

Parameter resolution in sub-nodes

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

## Node parameters#

  * **Model** : Select the model to use to generate the embedding.

Learn more about available embedding models in [Google VertexAI embeddings API documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api).

## Templates and examples#

**Ask questions about a PDF using AI**

by David Roberts

[View template details](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)

**Chat with PDF docs using AI (quoting sources)**

by David Roberts

[View template details](https://n8n.io/workflows/2165-chat-with-pdf-docs-using-ai-quoting-sources/)

**RAG Chatbot for Company Documents using Google Drive and Gemini**

by Mihai Farcas

[View template details](https://n8n.io/workflows/2753-rag-chatbot-for-company-documents-using-google-drive-and-gemini/)

[Browse Embeddings Google Vertex integration templates](https://n8n.io/integrations/embeddings-google-vertex/), or [search all templates](https://n8n.io/workflows/)

## Related resources#

Refer to [LangChain's Google Generative AI embeddings documentation](https://js.langchain.com/docs/integrations/text_embedding/google_generativeai) for more information about the service.

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