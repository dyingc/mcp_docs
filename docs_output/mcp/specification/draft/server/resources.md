# Resources - Model Context Protocol

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

Resources

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

**Protocol Revision** : draft

The Model Context Protocol (MCP) provides a standardized way for servers to expose resources to clients. Resources allow servers to share data that provides context to language models, such as files, database schemas, or application-specific information. Each resource is uniquely identified by a [URI](https://datatracker.ietf.org/doc/html/rfc3986).

## 

​

User Interaction Model

Resources in MCP are designed to be **application-driven** , with host applications determining how to incorporate context based on their needs.

For example, applications could:

  * Expose resources through UI elements for explicit selection, in a tree or list view
  * Allow the user to search through and filter available resources
  * Implement automatic context inclusion, based on heuristics or the AI model’s selection

However, implementations are free to expose resources through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model.

## 

​

Capabilities

Servers that support resources **MUST** declare the `resources` capability:

Copy
    
    
    {
      "capabilities": {
        "resources": {
          "subscribe": true,
          "listChanged": true
        }
      }
    }
    

The capability supports two optional features:

  * `subscribe`: whether the client can subscribe to be notified of changes to individual resources.
  * `listChanged`: whether the server will emit notifications when the list of available resources changes.

Both `subscribe` and `listChanged` are optional—servers can support neither, either, or both:

Copy
    
    
    {
      "capabilities": {
        "resources": {} // Neither feature supported
      }
    }
    

Copy
    
    
    {
      "capabilities": {
        "resources": {
          "subscribe": true // Only subscriptions supported
        }
      }
    }
    

Copy
    
    
    {
      "capabilities": {
        "resources": {
          "listChanged": true // Only list change notifications supported
        }
      }
    }
    

## 

​

Protocol Messages

### 

​

Listing Resources

To discover available resources, clients send a `resources/list` request. This operation supports [pagination](/specification/draft/server/utilities/pagination).

**Request:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "resources/list",
      "params": {
        "cursor": "optional-cursor-value"
      }
    }
    

**Response:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": {
        "resources": [
          {
            "uri": "file:///project/src/main.rs",
            "name": "main.rs",
            "title": "Rust Software Application Main File",
            "description": "Primary application entry point",
            "mimeType": "text/x-rust"
          }
        ],
        "nextCursor": "next-page-cursor"
      }
    }
    

### 

​

Reading Resources

To retrieve resource contents, clients send a `resources/read` request:

**Request:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 2,
      "method": "resources/read",
      "params": {
        "uri": "file:///project/src/main.rs"
      }
    }
    

**Response:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 2,
      "result": {
        "contents": [
          {
            "uri": "file:///project/src/main.rs",
            "name": "main.rs",
            "title": "Rust Software Application Main File",
            "mimeType": "text/x-rust",
            "text": "fn main() {\n    println!(\"Hello world!\");\n}"
          }
        ]
      }
    }
    

### 

​

Resource Templates

Resource templates allow servers to expose parameterized resources using [URI templates](https://datatracker.ietf.org/doc/html/rfc6570). Arguments may be auto-completed through [the completion API](/specification/draft/server/utilities/completion).

**Request:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 3,
      "method": "resources/templates/list"
    }
    

**Response:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 3,
      "result": {
        "resourceTemplates": [
          {
            "uriTemplate": "file:///{path}",
            "name": "Project Files",
            "title": "📁 Project Files",
            "description": "Access files in the project directory",
            "mimeType": "application/octet-stream"
          }
        ]
      }
    }
    

### 

​

List Changed Notification

When the list of available resources changes, servers that declared the `listChanged` capability **SHOULD** send a notification:

Copy
    
    
    {
      "jsonrpc": "2.0",
      "method": "notifications/resources/list_changed"
    }
    

### 

​

Subscriptions

The protocol supports optional subscriptions to resource changes. Clients can subscribe to specific resources and receive notifications when they change:

**Subscribe Request:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 4,
      "method": "resources/subscribe",
      "params": {
        "uri": "file:///project/src/main.rs"
      }
    }
    

**Update Notification:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "method": "notifications/resources/updated",
      "params": {
        "uri": "file:///project/src/main.rs",
        "title": "Rust Software Application Main File"
      }
    }
    

## 

​

Message Flow

## 

​

Data Types

### 

​

Resource

A resource definition includes:

  * `uri`: Unique identifier for the resource
  * `name`: The name of the resource.
  * `title`: Optional human-readable name of the resource for display purposes.
  * `description`: Optional description
  * `mimeType`: Optional MIME type
  * `size`: Optional size in bytes

### 

​

Resource Contents

Resources can contain either text or binary data:

#### 

​

Text Content

Copy
    
    
    {
      "uri": "file:///example.txt",
      "name": "example.txt",
      "title": "Example Text File",
      "mimeType": "text/plain",
      "text": "Resource content"
    }
    

#### 

​

Binary Content

Copy
    
    
    {
      "uri": "file:///example.png",
      "name": "example.png",
      "title": "Example Image",
      "mimeType": "image/png",
      "blob": "base64-encoded-data"
    }
    

## 

​

Common URI Schemes

The protocol defines several standard URI schemes. This list not exhaustive—implementations are always free to use additional, custom URI schemes.

### 

​

https://

Used to represent a resource available on the web.

Servers **SHOULD** use this scheme only when the client is able to fetch and load the resource directly from the web on its own—that is, it doesn’t need to read the resource via the MCP server.

For other use cases, servers **SHOULD** prefer to use another URI scheme, or define a custom one, even if the server will itself be downloading resource contents over the internet.

### 

​

file://

Used to identify resources that behave like a filesystem. However, the resources do not need to map to an actual physical filesystem.

MCP servers **MAY** identify file:// resources with an [XDG MIME type](https://specifications.freedesktop.org/shared-mime-info-spec/0.14/ar01s02.html#id-1.3.14), like `inode/directory`, to represent non-regular files (such as directories) that don’t otherwise have a standard MIME type.

### 

​

git://

Git version control integration.

### 

​

Custom URI Schemes

Custom URI schemes **MUST** be in accordance with [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986), taking the above guidance in to account.

## 

​

Error Handling

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:

  * Resource not found: `-32002`
  * Internal errors: `-32603`

Example error:

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 5,
      "error": {
        "code": -32002,
        "message": "Resource not found",
        "data": {
          "uri": "file:///nonexistent.txt"
        }
      }
    }
    

## 

​

Security Considerations

  1. Servers **MUST** validate all resource URIs
  2. Access controls **SHOULD** be implemented for sensitive resources
  3. Binary data **MUST** be properly encoded
  4. Resource permissions **SHOULD** be checked before operations

Was this page helpful?

YesNo

[Prompts](/specification/draft/server/prompts)[Tools](/specification/draft/server/tools)

On this page

  * User Interaction Model
  * Capabilities
  * Protocol Messages
  * Listing Resources
  * Reading Resources
  * Resource Templates
  * List Changed Notification
  * Subscriptions
  * Message Flow
  * Data Types
  * Resource
  * Resource Contents
  * Text Content
  * Binary Content
  * Common URI Schemes
  * https://
  * file://
  * git://
  * Custom URI Schemes
  * Error Handling
  * Security Considerations

Assistant

Responses are generated using AI and may contain mistakes.