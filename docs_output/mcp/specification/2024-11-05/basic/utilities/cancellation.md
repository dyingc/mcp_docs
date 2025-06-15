# Cancellation - Model Context Protocol

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

Cancellation

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

**Protocol Revision** : 2024-11-05

The Model Context Protocol (MCP) supports optional cancellation of in-progress requests through notification messages. Either side can send a cancellation notification to indicate that a previously-issued request should be terminated.

## 

​

Cancellation Flow

When a party wants to cancel an in-progress request, it sends a `notifications/cancelled` notification containing:

  * The ID of the request to cancel
  * An optional reason string that can be logged or displayed

Copy
    
    
    {
      "jsonrpc": "2.0",
      "method": "notifications/cancelled",
      "params": {
        "requestId": "123",
        "reason": "User requested cancellation"
      }
    }
    

## 

​

Behavior Requirements

  1. Cancellation notifications **MUST** only reference requests that:
     * Were previously issued in the same direction
     * Are believed to still be in-progress
  2. The `initialize` request **MUST NOT** be cancelled by clients
  3. Receivers of cancellation notifications **SHOULD** :
     * Stop processing the cancelled request
     * Free associated resources
     * Not send a response for the cancelled request
  4. Receivers **MAY** ignore cancellation notifications if:
     * The referenced request is unknown
     * Processing has already completed
     * The request cannot be cancelled
  5. The sender of the cancellation notification **SHOULD** ignore any response to the request that arrives afterward

## 

​

Timing Considerations

Due to network latency, cancellation notifications may arrive after request processing has completed, and potentially after a response has already been sent.

Both parties **MUST** handle these race conditions gracefully:

## 

​

Implementation Notes

  * Both parties **SHOULD** log cancellation reasons for debugging
  * Application UIs **SHOULD** indicate when cancellation is requested

## 

​

Error Handling

Invalid cancellation notifications **SHOULD** be ignored:

  * Unknown request IDs
  * Already completed requests
  * Malformed notifications

This maintains the “fire and forget” nature of notifications while allowing for race conditions in asynchronous communication.

Was this page helpful?

YesNo

[Transports](/specification/2024-11-05/basic/transports)[Ping](/specification/2024-11-05/basic/utilities/ping)

On this page

  * Cancellation Flow
  * Behavior Requirements
  * Timing Considerations
  * Implementation Notes
  * Error Handling

Assistant

Responses are generated using AI and may contain mistakes.