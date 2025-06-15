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

Tools

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

**Protocol Revision** : draft

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

To discover available tools, clients send a `tools/list` request. This operation supports [pagination](/specification/draft/server/utilities/pagination).

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
            "title": "Weather Information Provider",
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
  * `title`: Optional human-readable name of the tool for display purposes.
  * `description`: Human-readable description of functionality
  * `inputSchema`: JSON Schema defining expected parameters
  * `outputSchema`: Optional JSON Schema defining expected output structure
  * `annotations`: optional properties describing tool behavior

For trust & safety and security, clients **MUST** consider tool annotations to be untrusted unless they come from trusted servers.

### 

​

Tool Result

Tool results may contain [**structured**](/_sites/modelcontextprotocol.io/specification/draft/server/tools#structured-content) or **unstructured** content.

**Unstructured** content is returned in the `content` field of a result, and can contain multiple content items of different types:

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

Audio Content

Copy
    
    
    {
      "type": "audio",
      "data": "base64-encoded-audio-data",
      "mimeType": "audio/wav"
    }
    

#### 

​

Resource Links

A tool **MAY** return links to [Resources](/specification/draft/server/resources), to provide additional context or data. In this case, the tool will return a URI that can be subscribed to or fetched by the client:

Copy
    
    
    {
      "type": "resource_link",
      "uri": "file:///project/src/main.rs",
      "name": "main.rs",
      "description": "Primary application entry point",
      "mimeType": "text/x-rust"
    }
    

Resource links returned by tools are not guaranteed to appear in the results of a `resources/list` request.

#### 

​

Embedded Resources

[Resources](/specification/draft/server/resources) **MAY** be embedded to provide additional context or data using a suitable [URI scheme](./resources#common-uri-schemes). Servers that use embedded resources **SHOULD** implement the `resources` capability:

Copy
    
    
    {
      "type": "resource",
      "resource": {
        "uri": "file:///project/src/main.rs",
        "title": "Project Rust Main File",
        "mimeType": "text/x-rust",
        "text": "fn main() {\n    println!(\"Hello world!\");\n}"
      }
    }
    

#### 

​

Structured Content

**Structured** content is returned as a JSON object in the `structuredContent` field of a result.

For backwards compatibility, a tool that returns structured content SHOULD also return functionally equivalent unstructured content. (For example, serialized JSON can be returned in a `TextContent` block.)

#### 

​

Output Schema

Tools may also provide an output schema for validation of structured results. If an output schema is provided:

  * Servers **MUST** provide structured results that conform to this schema.
  * Clients **SHOULD** validate structured results against this schema.

Example tool with output schema:

Copy
    
    
    {
      "name": "get_weather_data",
      "title": "Weather Data Retriever",
      "description": "Get current weather data for a location",
      "inputSchema": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "City name or zip code"
          }
        },
        "required": ["location"]
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "temperature": {
            "type": "number",
            "description": "Temperature in celsius"
          },
          "conditions": {
            "type": "string",
            "description": "Weather conditions description"
          },
          "humidity": {
            "type": "number",
            "description": "Humidity percentage"
          }
        },
        "required": ["temperature", "conditions", "humidity"]
      }
    }
    

Example valid response for this tool:

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 5,
      "result": {
        "content": [
          {
            "type": "text",
            "text": "{\"temperature\": 22.5, \"conditions\": \"Partly cloudy\", \"humidity\": 65}"
          }
        ],
        "structuredContent": {
          "temperature": 22.5,
          "conditions": "Partly cloudy",
          "humidity": 65
        }
      }
    }
    

Providing an output schema helps clients and LLMs understand and properly handle structured tool outputs by:

  * Enabling strict schema validation of responses
  * Providing type information for better integration with programming languages
  * Guiding clients and LLMs to properly parse and utilize the returned data
  * Supporting better documentation and developer experience

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

[Resources](/specification/draft/server/resources)[Completion](/specification/draft/server/utilities/completion)

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
  * Audio Content
  * Resource Links
  * Embedded Resources
  * Structured Content
  * Output Schema
  * Error Handling
  * Security Considerations

Assistant

Responses are generated using AI and may contain mistakes.