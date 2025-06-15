# Progress - Model Context Protocol

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

Progress

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

**Protocol Revision** : 2024-11-05

The Model Context Protocol (MCP) supports optional progress tracking for long-running operations through notification messages. Either side can send progress notifications to provide updates about operation status.

## 

​

Progress Flow

When a party wants to _receive_ progress updates for a request, it includes a `progressToken` in the request metadata.

  * Progress tokens **MUST** be a string or integer value
  * Progress tokens can be chosen by the sender using any means, but **MUST** be unique across all active requests.

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "some_method",
      "params": {
        "_meta": {
          "progressToken": "abc123"
        }
      }
    }
    

The receiver **MAY** then send progress notifications containing:

  * The original progress token
  * The current progress value so far
  * An optional “total” value

Copy
    
    
    {
      "jsonrpc": "2.0",
      "method": "notifications/progress",
      "params": {
        "progressToken": "abc123",
        "progress": 50,
        "total": 100
      }
    }
    

  * The `progress` value **MUST** increase with each notification, even if the total is unknown.
  * The `progress` and the `total` values **MAY** be floating point.

## 

​

Behavior Requirements

  1. Progress notifications **MUST** only reference tokens that:

     * Were provided in an active request
     * Are associated with an in-progress operation
  2. Receivers of progress requests **MAY** :

     * Choose not to send any progress notifications
     * Send notifications at whatever frequency they deem appropriate
     * Omit the total value if unknown

## 

​

Implementation Notes

  * Senders and receivers **SHOULD** track active progress tokens
  * Both parties **SHOULD** implement rate limiting to prevent flooding
  * Progress notifications **MUST** stop after completion

Was this page helpful?

YesNo

[Ping](/specification/2024-11-05/basic/utilities/ping)[Roots](/specification/2024-11-05/client/roots)

On this page

  * Progress Flow
  * Behavior Requirements
  * Implementation Notes

Assistant

Responses are generated using AI and may contain mistakes.