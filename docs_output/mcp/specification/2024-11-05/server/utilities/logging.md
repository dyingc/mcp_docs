# Logging - Model Context Protocol

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

Logging

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

**Protocol Revision** : 2024-11-05

The Model Context Protocol (MCP) provides a standardized way for servers to send structured log messages to clients. Clients can control logging verbosity by setting minimum log levels, with servers sending notifications containing severity levels, optional logger names, and arbitrary JSON-serializable data.

## 

​

User Interaction Model

Implementations are free to expose logging through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model.

## 

​

Capabilities

Servers that emit log message notifications **MUST** declare the `logging` capability:

Copy
    
    
    {
      "capabilities": {
        "logging": {}
      }
    }
    

## 

​

Log Levels

The protocol follows the standard syslog severity levels specified in [RFC 5424](https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1):

Level| Description| Example Use Case  
---|---|---  
debug| Detailed debugging information| Function entry/exit points  
info| General informational messages| Operation progress updates  
notice| Normal but significant events| Configuration changes  
warning| Warning conditions| Deprecated feature usage  
error| Error conditions| Operation failures  
critical| Critical conditions| System component failures  
alert| Action must be taken immediately| Data corruption detected  
emergency| System is unusable| Complete system failure  
  
## 

​

Protocol Messages

### 

​

Setting Log Level

To configure the minimum log level, clients **MAY** send a `logging/setLevel` request:

**Request:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "logging/setLevel",
      "params": {
        "level": "info"
      }
    }
    

### 

​

Log Message Notifications

Servers send log messages using `notifications/message` notifications:

Copy
    
    
    {
      "jsonrpc": "2.0",
      "method": "notifications/message",
      "params": {
        "level": "error",
        "logger": "database",
        "data": {
          "error": "Connection failed",
          "details": {
            "host": "localhost",
            "port": 5432
          }
        }
      }
    }
    

## 

​

Message Flow

## 

​

Error Handling

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:

  * Invalid log level: `-32602` (Invalid params)
  * Configuration errors: `-32603` (Internal error)

## 

​

Implementation Considerations

  1. Servers **SHOULD** :

     * Rate limit log messages
     * Include relevant context in data field
     * Use consistent logger names
     * Remove sensitive information
  2. Clients **MAY** :

     * Present log messages in the UI
     * Implement log filtering/search
     * Display severity visually
     * Persist log messages

## 

​

Security

  1. Log messages **MUST NOT** contain:

     * Credentials or secrets
     * Personal identifying information
     * Internal system details that could aid attacks
  2. Implementations **SHOULD** :

     * Rate limit messages
     * Validate all data fields
     * Control log access
     * Monitor for sensitive content

Was this page helpful?

YesNo

[Completion](/specification/2024-11-05/server/utilities/completion)[Pagination](/specification/2024-11-05/server/utilities/pagination)

On this page

  * User Interaction Model
  * Capabilities
  * Log Levels
  * Protocol Messages
  * Setting Log Level
  * Log Message Notifications
  * Message Flow
  * Error Handling
  * Implementation Considerations
  * Security

Assistant

Responses are generated using AI and may contain mistakes.