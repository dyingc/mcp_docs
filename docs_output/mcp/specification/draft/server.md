# Overview - Model Context Protocol

[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](/)

Search...

⌘K

* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [Ruby SDK](https://github.com/modelcontextprotocol/ruby-sdk)
* [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)

##### 2025-03-26 (Latest)

  * [Specification](/specification/2025-03-26)
  * [Key Changes](/specification/2025-03-26/changelog)
  * [Architecture](/specification/2025-03-26/architecture)
  * Base Protocol

  * Client Features

  * Server Features

##### 2024-11-05

  * [Specification](/specification/2024-11-05)
  * [Architecture](/specification/2024-11-05/architecture)
  * Base Protocol

  * Client Features

  * Server Features

##### draft

  * [Specification](/specification/draft)
  * [Key Changes](/specification/draft/changelog)
  * [Architecture](/specification/draft/architecture)
  * Base Protocol

  * Client Features

  * Server Features

    * [Overview](/specification/draft/server)
    * [Prompts](/specification/draft/server/prompts)
    * [Resources](/specification/draft/server/resources)
    * [Tools](/specification/draft/server/tools)
    * Utilities

##### Resources

  * [Versioning](/specification/versioning)
  * [Contributions](/specification/contributing)

[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](/)

Search...

⌘K

Search...

Navigation

Server Features

Overview

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

**Protocol Revision** : draft

Servers provide the fundamental building blocks for adding context to language models via MCP. These primitives enable rich interactions between clients, servers, and language models:

  * **Prompts** : Pre-defined templates or instructions that guide language model interactions
  * **Resources** : Structured data or content that provides additional context to the model
  * **Tools** : Executable functions that allow models to perform actions or retrieve information

Each primitive can be summarized in the following control hierarchy:

Primitive| Control| Description| Example  
---|---|---|---  
Prompts| User-controlled| Interactive templates invoked by user choice| Slash commands, menu options  
Resources| Application-controlled| Contextual data attached and managed by the client| File contents, git history  
Tools| Model-controlled| Functions exposed to the LLM to take actions| API POST requests, file writing  
  
Explore these key primitives in more detail below:

## [Prompts](/specification/draft/server/prompts)## [Resources](/specification/draft/server/resources)## [Tools](/specification/draft/server/tools)

Was this page helpful?

YesNo

[Elicitation](/specification/draft/client/elicitation)[Prompts](/specification/draft/server/prompts)

Assistant

Responses are generated using AI and may contain mistakes.