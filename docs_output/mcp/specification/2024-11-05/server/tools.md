# Tools - Model Context Protocol

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

Server Features

Tools

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

**Protocol Revision** : 2024-11-05

The Model Context Protocol (MCP) allows servers to expose tools that can be invoked by language models. Tools enable models to interact with external systems, such as querying databases, calling APIs, or performing computations. Each tool is uniquely identified by a name and includes metadata describing its schema.

## 

​

User Interaction Model

Tools in MCP are designed to be **model-controlled** , meaning that the language model can discover and invoke tools automatically based on its contextual understanding and the user’s prompts.

However, implementations are free to expose tools through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model.

For trust & safety and security, there **SHOULD** always be a human in the loop with the ability to deny tool invocations.

Applications **SHOULD** :

  * Provide UI that makes clear which tools are being exposed to the AI model
  * Insert clear visual indicators when tools are invoked
  * Present confirmation prompts to the user for operations, to ensure a human is in the loop

## 

​

Capabilities

Servers that support tools **MUST** declare the `tools` capability:

Copy
    
    
    {
      "capabilities": {
        "tools": {
          "listChanged": true
        }
      }
    }
    

`listChanged` indicates whether the server will emit notifications when the list of available tools changes.

## 

​

Protocol Messages

### 

​

Listing Tools

To discover available tools, clients send a `tools/list` request. This operation supports [pagination](/specification/2024-11-05/server/utilities/pagination).

**Request:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/list",
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
        "tools": [
          {
            "name": "get_weather",
            "description": "Get current weather information for a location",
            "inputSchema": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "City name or zip code"
                }
              },
              "required": ["location"]
            }
          }
        ],
        "nextCursor": "next-page-cursor"
      }
    }
    

### 

​

Calling Tools

To invoke a tool, clients send a `tools/call` request:

**Request:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 2,
      "method": "tools/call",
      "params": {
        "name": "get_weather",
        "arguments": {
          "location": "New York"
        }
      }
    }
    

**Response:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 2,
      "result": {
        "content": [
          {
            "type": "text",
            "text": "Current weather in New York:\nTemperature: 72°F\nConditions: Partly cloudy"
          }
        ],
        "isError": false
      }
    }
    

### 

​

List Changed Notification

When the list of available tools changes, servers that declared the `listChanged` capability **SHOULD** send a notification:

Copy
    
    
    {
      "jsonrpc": "2.0",
      "method": "notifications/tools/list_changed"
    }
    

## 

​

Message Flow

## 

​

Data Types

### 

​

Tool

A tool definition includes:

  * `name`: Unique identifier for the tool
  * `description`: Human-readable description of functionality
  * `inputSchema`: JSON Schema defining expected parameters

### 

​

Tool Result

Tool results can contain multiple content items of different types:

#### 

​

Text Content

Copy
    
    
    {
      "type": "text",
      "text": "Tool result text"
    }
    

#### 

​

Image Content

Copy
    
    
    {
      "type": "image",
      "data": "base64-encoded-data",
      "mimeType": "image/png"
    }
    

#### 

​

Embedded Resources

[Resources](/specification/2024-11-05/server/resources) **MAY** be embedded, to provide additional context or data, behind a URI that can be subscribed to or fetched again by the client later:

Copy
    
    
    {
      "type": "resource",
      "resource": {
        "uri": "resource://example",
        "mimeType": "text/plain",
        "text": "Resource content"
      }
    }
    

## 

​

Error Handling

Tools use two error reporting mechanisms:

  1. **Protocol Errors** : Standard JSON-RPC errors for issues like:

     * Unknown tools
     * Invalid arguments
     * Server errors
  2. **Tool Execution Errors** : Reported in tool results with `isError: true`:

     * API failures
     * Invalid input data
     * Business logic errors

Example protocol error:

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 3,
      "error": {
        "code": -32602,
        "message": "Unknown tool: invalid_tool_name"
      }
    }
    

Example tool execution error:

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 4,
      "result": {
        "content": [
          {
            "type": "text",
            "text": "Failed to fetch weather data: API rate limit exceeded"
          }
        ],
        "isError": true
      }
    }
    

## 

​

Security Considerations

  1. Servers **MUST** :

     * Validate all tool inputs
     * Implement proper access controls
     * Rate limit tool invocations
     * Sanitize tool outputs
  2. Clients **SHOULD** :

     * Prompt for user confirmation on sensitive operations
     * Show tool inputs to the user before calling the server, to avoid malicious or accidental data exfiltration
     * Validate tool results before passing to LLM
     * Implement timeouts for tool calls
     * Log tool usage for audit purposes

Was this page helpful?

YesNo

[Resources](/specification/2024-11-05/server/resources)[Completion](/specification/2024-11-05/server/utilities/completion)

On this page

  * User Interaction Model
  * Capabilities
  * Protocol Messages
  * Listing Tools
  * Calling Tools
  * List Changed Notification
  * Message Flow
  * Data Types
  * Tool
  * Tool Result
  * Text Content
  * Image Content
  * Embedded Resources
  * Error Handling
  * Security Considerations

Assistant

Responses are generated using AI and may contain mistakes.