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

    * [Overview](/specification/draft/basic)
    * [Lifecycle](/specification/draft/basic/lifecycle)
    * [Transports](/specification/draft/basic/transports)
    * [Authorization](/specification/draft/basic/authorization)
    * [Security Best Practices](/specification/draft/basic/security_best_practices)
    * Utilities

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

Overview

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

**Protocol Revision** : draft

The Model Context Protocol consists of several key components that work together:

  * **Base Protocol** : Core JSON-RPC message types
  * **Lifecycle Management** : Connection initialization, capability negotiation, and session control
  * **Server Features** : Resources, prompts, and tools exposed by servers
  * **Client Features** : Sampling and root directory lists provided by clients
  * **Utilities** : Cross-cutting concerns like logging and argument completion

All implementations **MUST** support the base protocol and lifecycle management components. Other components **MAY** be implemented based on the specific needs of the application.

These protocol layers establish clear separation of concerns while enabling rich interactions between clients and servers. The modular design allows implementations to support exactly the features they need.

## 

​

Messages

All messages between MCP clients and servers **MUST** follow the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification. The protocol defines these types of messages:

### 

​

Requests

Requests are sent from the client to the server or vice versa, to initiate an operation.

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

### 

​

Responses

Responses are sent in reply to requests, containing the result or error of the operation.

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
  * **Responses** are further sub-categorized as either **successful results** or **errors**. Either a `result` or an `error` **MUST** be set. A response **MUST NOT** set both.
  * Results **MAY** follow any JSON object structure, while errors **MUST** include an error code and message at minimum.
  * Error codes **MUST** be integers.

### 

​

Notifications

Notifications are sent from the client to the server or vice versa, as a one-way message. The receiver **MUST NOT** send a response.

Copy
    
    
    {
      jsonrpc: "2.0";
      method: string;
      params?: {
        [key: string]: unknown;
      };
    }
    

  * Notifications **MUST NOT** include an ID.

## 

​

Auth

MCP provides an [Authorization](/specification/draft/basic/authorization) framework for use with HTTP. Implementations using an HTTP-based transport **SHOULD** conform to this specification, whereas implementations using STDIO transport **SHOULD NOT** follow this specification, and instead retrieve credentials from the environment.

Additionally, clients and servers **MAY** negotiate their own custom authentication and authorization strategies.

For further discussions and contributions to the evolution of MCP’s auth mechanisms, join us in [GitHub Discussions](https://github.com/modelcontextprotocol/specification/discussions) to help shape the future of the protocol!

## 

​

Schema

The full specification of the protocol is defined as a [TypeScript schema](https://github.com/modelcontextprotocol/specification/blob/main/schema/draft/schema.ts). This is the source of truth for all protocol messages and structures.

There is also a [JSON Schema](https://github.com/modelcontextprotocol/specification/blob/main/schema/draft/schema.json), which is automatically generated from the TypeScript source of truth, for use with various automated tooling.

Was this page helpful?

YesNo

[Architecture](/specification/draft/architecture)[Lifecycle](/specification/draft/basic/lifecycle)

On this page

  * Messages
  * Requests
  * Responses
  * Notifications
  * Auth
  * Schema

Assistant

Responses are generated using AI and may contain mistakes.