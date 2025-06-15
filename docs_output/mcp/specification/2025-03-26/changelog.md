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

2025-03-26 (Latest)

Key Changes

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

This document lists changes made to the Model Context Protocol (MCP) specification since the previous revision, [2024-11-05](/specification/2024-11-05).

## 

​

Major changes

  1. Added a comprehensive **[authorization framework](/specification/2025-03-26/basic/authorization)** based on OAuth 2.1 (PR [#133](https://github.com/modelcontextprotocol/specification/pull/133))
  2. Replaced the previous HTTP+SSE transport with a more flexible **[Streamable HTTP transport](/specification/2025-03-26/basic/transports#streamable-http)** (PR [#206](https://github.com/modelcontextprotocol/specification/pull/206))
  3. Added support for JSON-RPC **[batching](https://www.jsonrpc.org/specification#batch)** (PR [#228](https://github.com/modelcontextprotocol/specification/pull/228))
  4. Added comprehensive **tool annotations** for better describing tool behavior, like whether it is read-only or destructive (PR [#185](https://github.com/modelcontextprotocol/specification/pull/185))

## 

​

Other schema changes

  * Added `message` field to `ProgressNotification` to provide descriptive status updates
  * Added support for audio data, joining the existing text and image content types
  * Added `completions` capability to explicitly indicate support for argument autocompletion suggestions

See [the updated schema](https://github.com/modelcontextprotocol/specification/tree/main/schema/2025-03-26/schema.ts) for more details.

## 

​

Full changelog

For a complete list of all changes that have been made since the last protocol revision, [see GitHub](https://github.com/modelcontextprotocol/specification/compare/2024-11-05...2025-03-26).

Was this page helpful?

YesNo

[Specification](/specification/2025-03-26)[Architecture](/specification/2025-03-26/architecture)

On this page

  * Major changes
  * Other schema changes
  * Full changelog

Assistant

Responses are generated using AI and may contain mistakes.