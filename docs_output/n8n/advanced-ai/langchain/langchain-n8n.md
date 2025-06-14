# LangChain concepts in n8n | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/advanced-ai/langchain/langchain-n8n.md "Edit this page")

# LangChain concepts in n8n#

This page explains how LangChain concepts and features map to n8n nodes.

This page includes lists of the LangChain-focused nodes in n8n. You can use any n8n node in a workflow where you interact with LangChain, to link LangChain to other services. The LangChain features uses n8n's [Cluster nodes](../../../integrations/builtin/cluster-nodes/).

n8n implements LangChain JS

This feature is n8n's implementation of [LangChain's JavaScript framework](https://js.langchain.com/docs/get_started/introduction).

## Trigger nodes#

[Chat Trigger](../../../integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/)

## Cluster nodes#

[Cluster nodes](../../../glossary/#cluster-node-n8n) are node groups that work together to provide functionality in an n8n workflow. Instead of using a single node, you use a [root node](../../../glossary/#root-node-n8n) and one or more [sub-nodes](../../../glossary/#sub-node-n8n) that extend the functionality of the node.

![Screenshot of a workflow with a root node and two sub-nodes](../../../_images/integrations/builtin/cluster-nodes/root-sub-nodes.png)

### Root nodes#

Each cluster starts with one [root node](../../../glossary/#root-node-n8n).

#### Chains#

A [chain](../../../glossary/#ai-chain) is a series of LLMs, and related tools, linked together to support functionality that can't be provided by a single LLM alone.

Available nodes:

  * [Basic LLM Chain](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm/)
  * [Retrieval Q&A Chain](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/)
  * [Summarization Chain](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization/)
  * [Sentiment Analysis](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis/)
  * [Text Classifier](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier/)

Learn more about [chaining in LangChain](https://js.langchain.com/docs/concepts/lcel).

#### Agents#

> An [agent](../../../glossary/#ai-agent) has access to a suite of tools, and determines which ones to use depending on the user input. Agents can use multiple tools, and use the output of one tool as the input to the next. [Source](https://github.com/langchain-ai/langchainjs/blob/def3a26c054575e1ed40b9062087e8c0a8899633/docs/core_docs/docs/modules/agents/index.mdx)

Available nodes:

  * [Agent](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/)

Learn more about [Agents in LangChain](https://js.langchain.com/docs/concepts/agents).

#### Vector stores#

[Vector stores](../../../glossary/#ai-vector-store) store embedded data, and perform vector searches on it.

  * [Simple Vector Store](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory/)
  * [PGVector Vector Store](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector/)
  * [Pinecone Vector Store](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone/)
  * [Qdrant Vector Store](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant/)
  * [Supabase Vector Store](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase/)
  * [Zep Vector Store](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorezep/)

Learn more about [Vector stores in LangChain](https://js.langchain.com/docs/concepts/vectorstores/).

#### Miscellaneous#

Utility nodes.

[LangChain Code](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code/): import LangChain. This means if there is functionality you need that n8n hasn't created a node for, you can still use it.

### Sub-nodes#

Each root node can have one or more [sub-nodes](../../../glossary/#sub-node-n8n) attached to it.

#### Document loaders#

Document loaders add data to your chain as documents. The data source can be a file or web service.

Available nodes:

  * [Default Document Loader](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader/)
  * [GitHub Document Loader](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader/)

Learn more about [Document loaders in LangChain](https://js.langchain.com/docs/concepts/document_loaders).

#### Language models#

[LLMs (large language models)](../../../glossary/#large-language-model-llm) are programs that analyze datasets. They're the key element of working with AI.

Available nodes:

  * [Anthropic Chat Model](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic/)
  * [AWS Bedrock Chat Model](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock/)
  * [Cohere Model](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere/)
  * [Hugging Face Inference Model](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference/)
  * [Mistral Cloud Chat Model](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud/)
  * [Ollama Chat Model](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/)
  * [Ollama Model](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/)
  * [OpenAI Chat Model](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/)

Learn more about [Language models in LangChain](https://js.langchain.com/docs/concepts/chat_models).

#### Memory#

[Memory](../../../glossary/#ai-memory) retains information about previous queries in a series of queries. For example, when a user interacts with a chat model, it's useful if your application can remember and call on the full conversation, not just the most recent query entered by the user.

Available nodes:

  * [Motorhead](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead/)
  * [Redis Chat Memory](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat/)
  * [Postgres Chat Memory](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat/)
  * [Simple Memory](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/)
  * [Xata](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata/)
  * [Zep](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep/)

Learn more about [Memory in LangChain](https://langchain-ai.github.io/langgraphjs/concepts/memory/).

#### Output parsers#

Output parsers take the text generated by an LLM and format it to match the structure you require.

Available nodes:

  * [Auto-fixing Output Parser](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing/)
  * [Item List Output Parser](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist/)
  * [Structured Output Parser](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/)

Learn more about [Output parsers in LangChain](https://js.langchain.com/docs/concepts/output_parsers/).

#### Retrievers#

  * [Contextual Compression Retriever](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression/)
  * [MultiQuery Retriever](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery/)
  * [Vector Store Retriever](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore/)
  * [Workflow Retriever](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow/)

#### Text splitters#

Text splitters break down data (documents), making it easier for the LLM to process the information and return accurate results.

Available nodes:

  * [Character Text Splitter](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter/)
  * [Recursive Character Text Splitter](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter/)
  * [Token Splitter](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittertokensplitter/)

n8n's text splitter nodes implements parts of [LangChain's text_splitter API](https://js.langchain.com/docs/concepts/text_splitters/).

#### Tools#

Utility [tools](../../../glossary/#ai-tool).

  * [Calculator](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcalculator/)
  * [Code Tool](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode/)
  * [SerpAPI](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi/)
  * [Think Tool](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink/)
  * [Vector Store Tool](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore/)
  * [Wikipedia](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia/)
  * [Wolfram|Alpha](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha/)
  * [Workflow Tool](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow/)

#### Embeddings#

> [Embeddings](../../../glossary/#ai-embedding) capture the "relatedness" of text, images, video, or other types of information. ([source](https://supabase.com/docs/guides/ai/concepts))

Available nodes:

  * [Embeddings AWS Bedrock](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock/)
  * [Embeddings Cohere](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere/)
  * [Embeddings Google PaLM](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm/)
  * [Embeddings Hugging Face Inference](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference/)
  * [Embeddings Mistral Cloud](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud/)
  * [Embeddings Ollama](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama/)
  * [Embeddings OpenAI](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai/)

Learn more about [Text embeddings in LangChain](https://js.langchain.com/docs/concepts/embedding_models/).

#### Miscellaneous#

  * [Chat Memory Manager](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager/)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top