# Supabase Vector Store node documentation | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase.md "Edit this page")

# Supabase Vector Store node#

Use the Supabase Vector Store to interact with your Supabase database as [vector store](../../../../../glossary/#ai-vector-store). You can insert documents into a vector database, get documents from a vector database, retrieve documents to provide them to a retriever connected to a [chain](../../../../../glossary/#ai-chain), or connect it directly to an [agent](../../../../../glossary/#ai-agent) to use as a [tool](../../../../../glossary/#ai-tool).

On this page, you'll find the node parameters for the Supabase node, and links to more resources.

Credentials

You can find authentication information for this node [here](../../../credentials/supabase/).

Parameter resolution in sub-nodes

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Supabase provides a [quickstart for setting up your vector store](https://supabase.com/docs/guides/ai/langchain?database-method=sql). If you use settings other than the defaults in the quickstart, this may affect parameter settings in n8n. Make sure you understand what you're doing.

## Node usage patterns#

You can use the Supabase Vector Store node in the following patterns.

### Use as a regular node to insert, update, and retrieve documents#

You can use the Supabase Vector Store as a regular node to insert, update, or get documents. This pattern places the Supabase Vector Store in the regular connection flow without using an agent.

You can see an example of this in scenario 1 of [this template](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/).

### Connect directly to an AI agent as a tool#

You can connect the Supabase Vector Store node directly to the tool connector of an [AI agent](../n8n-nodes-langchain.agent/) to use a vector store as a resource when answering queries.

Here, the connection would be: AI agent (tools connector) -> Supabase Vector Store node.

### Use a retriever to fetch documents#

You can use the [Vector Store Retriever](../../sub-nodes/n8n-nodes-langchain.retrievervectorstore/) node with the Supabase Vector Store node to fetch documents from the Supabase Vector Store node. This is often used with the [Question and Answer Chain](../n8n-nodes-langchain.chainretrievalqa/) node to fetch documents from the vector store that match the given chat input.

An [example of the connection flow](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/) (the example uses Pinecone, but the pattern in the same) would be: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> Supabase Vector Store.

### Use the Vector Store Question Answer Tool to answer questions#

Another pattern uses the [Vector Store Question Answer Tool](../../sub-nodes/n8n-nodes-langchain.toolvectorstore/) to summarize results and answer questions from the Supabase Vector Store node. Rather than connecting the Supabase Vector Store directly as a tool, this pattern uses a tool specifically designed to summarizes data in the vector store.

The [connections flow](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/) in this case would look like this: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> Supabase Vector store.

## Node parameters#

### Operation Mode#

This Vector Store node has five modes: **Get Many** , **Insert Documents** , **Retrieve Documents (As Vector Store for Chain/Tool)** , **Retrieve Documents (As Tool for AI Agent)** , and **Update Documents**. The mode you select determines the operations you can perform with the node and what inputs and outputs are available.

#### Get Many#

In this mode, you can retrieve multiple documents from your vector database by providing a prompt. The prompt will be embedded and used for similarity search. The node will return the documents that are most similar to the prompt with their similarity score. This is useful if you want to retrieve a list of similar documents and pass them to an agent as additional context. 

#### Insert Documents#

Use Insert Documents mode to insert new documents into your vector database.

#### Retrieve Documents (As Vector Store for Chain/Tool)#

Use Retrieve Documents (As Vector Store for Chain/Tool) mode with a vector-store retriever to retrieve documents from a vector database and provide them to the retriever connected to a chain. In this mode you must connect the node to a retriever node or root node.

#### Retrieve Documents (As Tool for AI Agent)#

Use Retrieve Documents (As Tool for AI Agent) mode to use the vector store as a tool resource when answering queries. When formulating responses, the agent uses the vector store when the vector store name and description match the question details.

#### Update Documents#

Use Update Documents mode to update documents in a vector database by ID. Fill in the **ID** with the ID of the embedding entry to update.

### Get Many parameters#

  * **Table Name** : Enter the Supabase table to use.
  * **Prompt** : Enter the search query.
  * **Limit** : Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.

### Insert Documents parameters#

  * **Table Name** : Enter the Supabase table to use.

### Retrieve Documents (As Vector Store for Chain/Tool) parameters#

  * **Table Name** : Enter the Supabase table to use.

### Retrieve Documents (As Tool for AI Agent) parameters#

  * **Name** : The name of the vector store.
  * **Description** : Explain to the LLM what this tool does. A good, specific description allows LLMs to produce expected results more often.
  * **Table Name** : Enter the Supabase table to use.
  * **Limit** : Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.

### Update Documents#

  * **Table Name** : Enter the Supabase table to use.
  * **ID** : The ID of an embedding entry.

## Node options#

### Query Name#

The name of the matching function you set up in Supabase. If you follow the [Supabase quickstart](https://supabase.com/docs/guides/ai/langchain?database-method=sql), this will be `match_documents`.

### Metadata Filter#

Available in **Get Many** mode. When searching for data, use this to match with metadata associated with the document.

This is an `AND` query. If you specify more than one metadata filter field, all of them must match.

When inserting data, the metadata is set using the document loader. Refer to [Default Data Loader](../../sub-nodes/n8n-nodes-langchain.documentdefaultdataloader/) for more information on loading documents.

## Templates and examples#

**AI Agent To Chat With Files In Supabase Storage**

by Mark Shcherbakov

[View template details](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/)

**Supabase Insertion & Upsertion & Retrieval**

by Ria

[View template details](https://n8n.io/workflows/2395-supabase-insertion-and-upsertion-and-retrieval/)

**Document Q &A Chatbot with Gemini AI and Supabase Vector Search for Telegram**

by Mohammad Ghaffarifar

[View template details](https://n8n.io/workflows/3940-document-qanda-chatbot-with-gemini-ai-and-supabase-vector-search-for-telegram/)

[Browse Supabase Vector Store integration templates](https://n8n.io/integrations/supabase-vector-store/), or [search all templates](https://n8n.io/workflows/)

## Related resources#

Refer to [LangChain's Supabase documentation](https://js.langchain.com/docs/integrations/vectorstores/supabase/) for more information about the service.

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