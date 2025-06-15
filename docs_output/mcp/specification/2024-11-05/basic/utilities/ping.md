# Ping - Model Context Protocol

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

      * [Cancellation](/specification/2024-11-05/basic/utilities/cancellation)
      * [Ping](/specification/2024-11-05/basic/utilities/ping)
      * [Progress](/specification/2024-11-05/basic/utilities/progress)
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

Utilities

Ping

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

**Protocol Revision** : 2024-11-05

The Model Context Protocol includes an optional ping mechanism that allows either party to verify that their counterpart is still responsive and the connection is alive.

## 

​

Overview

The ping functionality is implemented through a simple request/response pattern. Either the client or server can initiate a ping by sending a `ping` request.

## 

​

Message Format

A ping request is a standard JSON-RPC request with no parameters:

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": "123",
      "method": "ping"
    }
    

## 

​

Behavior Requirements

  1. The receiver **MUST** respond promptly with an empty response:

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": "123",
      "result": {}
    }
    

  2. If no response is received within a reasonable timeout period, the sender **MAY** :
     * Consider the connection stale
     * Terminate the connection
     * Attempt reconnection procedures

## 

​

Usage Patterns

## 

​

Implementation Considerations

  * Implementations **SHOULD** periodically issue pings to detect connection health
  * The frequency of pings **SHOULD** be configurable
  * Timeouts **SHOULD** be appropriate for the network environment
  * Excessive pinging **SHOULD** be avoided to reduce network overhead

## 

​

Error Handling

  * Timeouts **SHOULD** be treated as connection failures
  * Multiple failed pings **MAY** trigger connection reset
  * Implementations **SHOULD** log ping failures for diagnostics

Was this page helpful?

YesNo

[Cancellation](/specification/2024-11-05/basic/utilities/cancellation)[Progress](/specification/2024-11-05/basic/utilities/progress)

On this page

  * Overview
  * Message Format
  * Behavior Requirements
  * Usage Patterns
  * Implementation Considerations
  * Error Handling

Assistant

Responses are generated using AI and may contain mistakes.