# Key Changes - Model Context Protocol

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

##### Resources

  * [Versioning](/specification/versioning)
  * [Contributions](/specification/contributing)

[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](/)

Search...

⌘K

Search...

Navigation

draft

Key Changes

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

This document lists changes made to the Model Context Protocol (MCP) specification since the previous revision, [2025-03-26](/specification/2025-03-26).

## 

​

Major changes

  1. Removed support for JSON-RPC **[batching](https://www.jsonrpc.org/specification#batch)** (PR [#416](https://github.com/modelcontextprotocol/specification/pull/416))
  2. Added support for [structured tool output](/specification/draft/server/tools#structured-content) (PR [#371](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/371))
  3. Classified MCP servers as [OAuth Resource Servers](/specification/draft/basic/authorization#authorization-server-discovery), adding protected resource metadata to discover the corresponding Authorization server. (PR [#338](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/338))
  4. Clarified [security considerations](/specification/draft/basic/authorization#security-considerations) and best practices in the authorization spec and in a new [security best practices page](/specification/draft/basic/security_best_practices).
  5. Added support for **[elicitation](/specification/draft/client/elicitation)** , enabling servers to request additional information from users during interactions. (PR [#382](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/382))
  6. Added support for **[resource links](/specification/draft/server/tools#resource-links)** in tool call results. (PR [#603](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/603))

## 

​

Other schema changes

## 

​

Full changelog

For a complete list of all changes that have been made since the last protocol revision, [see GitHub](https://github.com/modelcontextprotocol/specification/compare/2025-03-26...draft).

Was this page helpful?

YesNo

[Specification](/specification/draft)[Architecture](/specification/draft/architecture)

On this page

  * Major changes
  * Other schema changes
  * Full changelog

Assistant

Responses are generated using AI and may contain mistakes.