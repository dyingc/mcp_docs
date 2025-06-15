# Messages - Model Context Protocol

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

    * [Overview](/specification/2024-11-05/basic)
    * [Lifecycle](/specification/2024-11-05/basic/lifecycle)
    * [Messages](/specification/2024-11-05/basic/messages)
    * [Transports](/specification/2024-11-05/basic/transports)
    * Utilities

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

Base Protocol

Messages

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

**Protocol Revision** : 2024-11-05

All messages in MCP **MUST** follow the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification. The protocol defines three types of messages:

## 

​

Requests

Requests are sent from the client to the server or vice versa.

Copy
    
    
    {
      jsonrpc: "2.0";
      id: string | number;
      method: string;
      params?: {
        [key: string]: unknown;
      };
    }
    

  * Requests **MUST** include a string or integer ID.
  * Unlike base JSON-RPC, the ID **MUST NOT** be `null`.
  * The request ID **MUST NOT** have been previously used by the requestor within the same session.

## 

​

Responses

Responses are sent in reply to requests.

Copy
    
    
    {
      jsonrpc: "2.0";
      id: string | number;
      result?: {
        [key: string]: unknown;
      }
      error?: {
        code: number;
        message: string;
        data?: unknown;
      }
    }
    

  * Responses **MUST** include the same ID as the request they correspond to.
  * Either a `result` or an `error` **MUST** be set. A response **MUST NOT** set both.
  * Error codes **MUST** be integers.

## 

​

Notifications

Notifications are sent from the client to the server or vice versa. They do not expect a response.

Copy
    
    
    {
      jsonrpc: "2.0";
      method: string;
      params?: {
        [key: string]: unknown;
      };
    }
    

  * Notifications **MUST NOT** include an ID.

Was this page helpful?

YesNo

[Lifecycle](/specification/2024-11-05/basic/lifecycle)[Transports](/specification/2024-11-05/basic/transports)

On this page

  * Requests
  * Responses
  * Notifications

Assistant

Responses are generated using AI and may contain mistakes.