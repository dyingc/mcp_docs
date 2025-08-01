# Transports - Model Context Protocol

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

    * [Overview](/specification/2025-03-26/basic)
    * [Lifecycle](/specification/2025-03-26/basic/lifecycle)
    * [Transports](/specification/2025-03-26/basic/transports)
    * [Authorization](/specification/2025-03-26/basic/authorization)
    * Utilities

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

Base Protocol

Transports

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

**Protocol Revision** : 2025-03-26

MCP uses JSON-RPC to encode messages. JSON-RPC messages **MUST** be UTF-8 encoded.

The protocol currently defines two standard transport mechanisms for client-server communication:

  1. [stdio](/_sites/modelcontextprotocol.io/specification/2025-03-26/basic/transports#stdio), communication over standard in and standard out
  2. [Streamable HTTP](/_sites/modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http)

Clients **SHOULD** support stdio whenever possible.

It is also possible for clients and servers to implement [custom transports](/_sites/modelcontextprotocol.io/specification/2025-03-26/basic/transports#custom-transports) in a pluggable fashion.

## 

​

stdio

In the **stdio** transport:

  * The client launches the MCP server as a subprocess.
  * The server reads JSON-RPC messages from its standard input (`stdin`) and sends messages to its standard output (`stdout`).
  * Messages may be JSON-RPC requests, notifications, responses—or a JSON-RPC [batch](https://www.jsonrpc.org/specification#batch) containing one or more requests and/or notifications.
  * Messages are delimited by newlines, and **MUST NOT** contain embedded newlines.
  * The server **MAY** write UTF-8 strings to its standard error (`stderr`) for logging purposes. Clients **MAY** capture, forward, or ignore this logging.
  * The server **MUST NOT** write anything to its `stdout` that is not a valid MCP message.
  * The client **MUST NOT** write anything to the server’s `stdin` that is not a valid MCP message.

## 

​

Streamable HTTP

This replaces the [HTTP+SSE transport](/specification/2024-11-05/basic/transports#http-with-sse) from protocol version 2024-11-05. See the [backwards compatibility](/_sites/modelcontextprotocol.io/specification/2025-03-26/basic/transports#backwards-compatibility) guide below.

In the **Streamable HTTP** transport, the server operates as an independent process that can handle multiple client connections. This transport uses HTTP POST and GET requests. Server can optionally make use of [Server-Sent Events](https://en.wikipedia.org/wiki/Server-sent_events) (SSE) to stream multiple server messages. This permits basic MCP servers, as well as more feature-rich servers supporting streaming and server-to-client notifications and requests.

The server **MUST** provide a single HTTP endpoint path (hereafter referred to as the **MCP endpoint**) that supports both POST and GET methods. For example, this could be a URL like `https://example.com/mcp`.

#### 

​

Security Warning

When implementing Streamable HTTP transport:

  1. Servers **MUST** validate the `Origin` header on all incoming connections to prevent DNS rebinding attacks
  2. When running locally, servers **SHOULD** bind only to localhost (127.0.0.1) rather than all network interfaces (0.0.0.0)
  3. Servers **SHOULD** implement proper authentication for all connections

Without these protections, attackers could use DNS rebinding to interact with local MCP servers from remote websites.

### 

​

Sending Messages to the Server

Every JSON-RPC message sent from the client **MUST** be a new HTTP POST request to the MCP endpoint.

  1. The client **MUST** use HTTP POST to send JSON-RPC messages to the MCP endpoint.
  2. The client **MUST** include an `Accept` header, listing both `application/json` and `text/event-stream` as supported content types.
  3. The body of the POST request **MUST** be one of the following:
     * A single JSON-RPC _request_ , _notification_ , or _response_
     * An array [batching](https://www.jsonrpc.org/specification#batch) one or more _requests and/or notifications_
     * An array [batching](https://www.jsonrpc.org/specification#batch) one or more _responses_
  4. If the input consists solely of (any number of) JSON-RPC _responses_ or _notifications_ :
     * If the server accepts the input, the server **MUST** return HTTP status code 202 Accepted with no body.
     * If the server cannot accept the input, it **MUST** return an HTTP error status code (e.g., 400 Bad Request). The HTTP response body **MAY** comprise a JSON-RPC _error response_ that has no `id`.
  5. If the input contains any number of JSON-RPC _requests_ , the server **MUST** either return `Content-Type: text/event-stream`, to initiate an SSE stream, or `Content-Type: application/json`, to return one JSON object. The client **MUST** support both these cases.
  6. If the server initiates an SSE stream:
     * The SSE stream **SHOULD** eventually include one JSON-RPC _response_ per each JSON-RPC _request_ sent in the POST body. These _responses_ **MAY** be [batched](https://www.jsonrpc.org/specification#batch).
     * The server **MAY** send JSON-RPC _requests_ and _notifications_ before sending a JSON-RPC _response_. These messages **SHOULD** relate to the originating client _request_. These _requests_ and _notifications_ **MAY** be [batched](https://www.jsonrpc.org/specification#batch).
     * The server **SHOULD NOT** close the SSE stream before sending a JSON-RPC _response_ per each received JSON-RPC _request_ , unless the [session](/_sites/modelcontextprotocol.io/specification/2025-03-26/basic/transports#session-management) expires.
     * After all JSON-RPC _responses_ have been sent, the server **SHOULD** close the SSE stream.
     * Disconnection **MAY** occur at any time (e.g., due to network conditions). Therefore:
       * Disconnection **SHOULD NOT** be interpreted as the client cancelling its request.
       * To cancel, the client **SHOULD** explicitly send an MCP `CancelledNotification`.
       * To avoid message loss due to disconnection, the server **MAY** make the stream [resumable](/_sites/modelcontextprotocol.io/specification/2025-03-26/basic/transports#resumability-and-redelivery).

### 

​

Listening for Messages from the Server

  1. The client **MAY** issue an HTTP GET to the MCP endpoint. This can be used to open an SSE stream, allowing the server to communicate to the client, without the client first sending data via HTTP POST.
  2. The client **MUST** include an `Accept` header, listing `text/event-stream` as a supported content type.
  3. The server **MUST** either return `Content-Type: text/event-stream` in response to this HTTP GET, or else return HTTP 405 Method Not Allowed, indicating that the server does not offer an SSE stream at this endpoint.
  4. If the server initiates an SSE stream:
     * The server **MAY** send JSON-RPC _requests_ and _notifications_ on the stream. These _requests_ and _notifications_ **MAY** be [batched](https://www.jsonrpc.org/specification#batch).
     * These messages **SHOULD** be unrelated to any concurrently-running JSON-RPC _request_ from the client.
     * The server **MUST NOT** send a JSON-RPC _response_ on the stream **unless** [resuming](/_sites/modelcontextprotocol.io/specification/2025-03-26/basic/transports#resumability-and-redelivery) a stream associated with a previous client request.
     * The server **MAY** close the SSE stream at any time.
     * The client **MAY** close the SSE stream at any time.

### 

​

Multiple Connections

  1. The client **MAY** remain connected to multiple SSE streams simultaneously.
  2. The server **MUST** send each of its JSON-RPC messages on only one of the connected streams; that is, it **MUST NOT** broadcast the same message across multiple streams.
     * The risk of message loss **MAY** be mitigated by making the stream [resumable](/_sites/modelcontextprotocol.io/specification/2025-03-26/basic/transports#resumability-and-redelivery).

### 

​

Resumability and Redelivery

To support resuming broken connections, and redelivering messages that might otherwise be lost:

  1. Servers **MAY** attach an `id` field to their SSE events, as described in the [SSE standard](https://html.spec.whatwg.org/multipage/server-sent-events.html#event-stream-interpretation).
     * If present, the ID **MUST** be globally unique across all streams within that [session](/_sites/modelcontextprotocol.io/specification/2025-03-26/basic/transports#session-management)—or all streams with that specific client, if session management is not in use.
  2. If the client wishes to resume after a broken connection, it **SHOULD** issue an HTTP GET to the MCP endpoint, and include the [`Last-Event-ID`](https://html.spec.whatwg.org/multipage/server-sent-events.html#the-last-event-id-header) header to indicate the last event ID it received.
     * The server **MAY** use this header to replay messages that would have been sent after the last event ID, _on the stream that was disconnected_ , and to resume the stream from that point.
     * The server **MUST NOT** replay messages that would have been delivered on a different stream.

In other words, these event IDs should be assigned by servers on a _per-stream_ basis, to act as a cursor within that particular stream.

### 

​

Session Management

An MCP “session” consists of logically related interactions between a client and a server, beginning with the [initialization phase](/specification/2025-03-26/basic/lifecycle). To support servers which want to establish stateful sessions:

  1. A server using the Streamable HTTP transport **MAY** assign a session ID at initialization time, by including it in an `Mcp-Session-Id` header on the HTTP response containing the `InitializeResult`.
     * The session ID **SHOULD** be globally unique and cryptographically secure (e.g., a securely generated UUID, a JWT, or a cryptographic hash).
     * The session ID **MUST** only contain visible ASCII characters (ranging from 0x21 to 0x7E).
  2. If an `Mcp-Session-Id` is returned by the server during initialization, clients using the Streamable HTTP transport **MUST** include it in the `Mcp-Session-Id` header on all of their subsequent HTTP requests.
     * Servers that require a session ID **SHOULD** respond to requests without an `Mcp-Session-Id` header (other than initialization) with HTTP 400 Bad Request.
  3. The server **MAY** terminate the session at any time, after which it **MUST** respond to requests containing that session ID with HTTP 404 Not Found.
  4. When a client receives HTTP 404 in response to a request containing an `Mcp-Session-Id`, it **MUST** start a new session by sending a new `InitializeRequest` without a session ID attached.
  5. Clients that no longer need a particular session (e.g., because the user is leaving the client application) **SHOULD** send an HTTP DELETE to the MCP endpoint with the `Mcp-Session-Id` header, to explicitly terminate the session.
     * The server **MAY** respond to this request with HTTP 405 Method Not Allowed, indicating that the server does not allow clients to terminate sessions.

### 

​

Sequence Diagram

### 

​

Backwards Compatibility

Clients and servers can maintain backwards compatibility with the deprecated [HTTP+SSE transport](/specification/2024-11-05/basic/transports#http-with-sse) (from protocol version 2024-11-05) as follows:

**Servers** wanting to support older clients should:

  * Continue to host both the SSE and POST endpoints of the old transport, alongside the new “MCP endpoint” defined for the Streamable HTTP transport.
    * It is also possible to combine the old POST endpoint and the new MCP endpoint, but this may introduce unneeded complexity.

**Clients** wanting to support older servers should:

  1. Accept an MCP server URL from the user, which may point to either a server using the old transport or the new transport.
  2. Attempt to POST an `InitializeRequest` to the server URL, with an `Accept` header as defined above:
     * If it succeeds, the client can assume this is a server supporting the new Streamable HTTP transport.
     * If it fails with an HTTP 4xx status code (e.g., 405 Method Not Allowed or 404 Not Found):
       * Issue a GET request to the server URL, expecting that this will open an SSE stream and return an `endpoint` event as the first event.
       * When the `endpoint` event arrives, the client can assume this is a server running the old HTTP+SSE transport, and should use that transport for all subsequent communication.

## 

​

Custom Transports

Clients and servers **MAY** implement additional custom transport mechanisms to suit their specific needs. The protocol is transport-agnostic and can be implemented over any communication channel that supports bidirectional message exchange.

Implementers who choose to support custom transports **MUST** ensure they preserve the JSON-RPC message format and lifecycle requirements defined by MCP. Custom transports **SHOULD** document their specific connection establishment and message exchange patterns to aid interoperability.

Was this page helpful?

YesNo

[Lifecycle](/specification/2025-03-26/basic/lifecycle)[Authorization](/specification/2025-03-26/basic/authorization)

On this page

  * stdio
  * Streamable HTTP
  * Security Warning
  * Sending Messages to the Server
  * Listening for Messages from the Server
  * Multiple Connections
  * Resumability and Redelivery
  * Session Management
  * Sequence Diagram
  * Backwards Compatibility
  * Custom Transports

Assistant

Responses are generated using AI and may contain mistakes.