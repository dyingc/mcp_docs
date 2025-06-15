# Pagination - Model Context Protocol

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

    * [Overview](/specification/2024-11-05/server)
    * [Prompts](/specification/2024-11-05/server/prompts)
    * [Resources](/specification/2024-11-05/server/resources)
    * [Tools](/specification/2024-11-05/server/tools)
    * Utilities

      * [Completion](/specification/2024-11-05/server/utilities/completion)
      * [Logging](/specification/2024-11-05/server/utilities/logging)
      * [Pagination](/specification/2024-11-05/server/utilities/pagination)

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

Utilities

Pagination

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

**Protocol Revision** : 2024-11-05

The Model Context Protocol (MCP) supports paginating list operations that may return large result sets. Pagination allows servers to yield results in smaller chunks rather than all at once.

Pagination is especially important when connecting to external services over the internet, but also useful for local integrations to avoid performance issues with large data sets.

## 

​

Pagination Model

Pagination in MCP uses an opaque cursor-based approach, instead of numbered pages.

  * The **cursor** is an opaque string token, representing a position in the result set
  * **Page size** is determined by the server, and clients **MUST NOT** assume a fixed page size

## 

​

Response Format

Pagination starts when the server sends a **response** that includes:

  * The current page of results
  * An optional `nextCursor` field if more results exist

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": "123",
      "result": {
        "resources": [...],
        "nextCursor": "eyJwYWdlIjogM30="
      }
    }
    

## 

​

Request Format

After receiving a cursor, the client can _continue_ paginating by issuing a request including that cursor:

Copy
    
    
    {
      "jsonrpc": "2.0",
      "method": "resources/list",
      "params": {
        "cursor": "eyJwYWdlIjogMn0="
      }
    }
    

## 

​

Pagination Flow

## 

​

Operations Supporting Pagination

The following MCP operations support pagination:

  * `resources/list` \- List available resources
  * `resources/templates/list` \- List resource templates
  * `prompts/list` \- List available prompts
  * `tools/list` \- List available tools

## 

​

Implementation Guidelines

  1. Servers **SHOULD** :

     * Provide stable cursors
     * Handle invalid cursors gracefully
  2. Clients **SHOULD** :

     * Treat a missing `nextCursor` as the end of results
     * Support both paginated and non-paginated flows
  3. Clients **MUST** treat cursors as opaque tokens:

     * Don’t make assumptions about cursor format
     * Don’t attempt to parse or modify cursors
     * Don’t persist cursors across sessions

## 

​

Error Handling

Invalid cursors **SHOULD** result in an error with code -32602 (Invalid params).

Was this page helpful?

YesNo

[Logging](/specification/2024-11-05/server/utilities/logging)[Specification](/specification/draft)

On this page

  * Pagination Model
  * Response Format
  * Request Format
  * Pagination Flow
  * Operations Supporting Pagination
  * Implementation Guidelines
  * Error Handling

Assistant

Responses are generated using AI and may contain mistakes.