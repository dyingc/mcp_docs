# Completion - Model Context Protocol

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

      * [Completion](/specification/draft/server/utilities/completion)
      * [Logging](/specification/draft/server/utilities/logging)
      * [Pagination](/specification/draft/server/utilities/pagination)

##### Resources

  * [Versioning](/specification/versioning)
  * [Contributions](/specification/contributing)

[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](/)

Search...

⌘K

Search...

Navigation

Utilities

Completion

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

**Protocol Revision** : draft

The Model Context Protocol (MCP) provides a standardized way for servers to offer argument autocompletion suggestions for prompts and resource URIs. This enables rich, IDE-like experiences where users receive contextual suggestions while entering argument values.

## 

​

User Interaction Model

Completion in MCP is designed to support interactive user experiences similar to IDE code completion.

For example, applications may show completion suggestions in a dropdown or popup menu as users type, with the ability to filter and select from available options.

However, implementations are free to expose completion through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model.

## 

​

Capabilities

Servers that support completions **MUST** declare the `completions` capability:

Copy
    
    
    {
      "capabilities": {
        "completions": {}
      }
    }
    

## 

​

Protocol Messages

### 

​

Requesting Completions

To get completion suggestions, clients send a `completion/complete` request specifying what is being completed through a reference type:

**Request:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "completion/complete",
      "params": {
        "ref": {
          "type": "ref/prompt",
          "name": "code_review"
        },
        "argument": {
          "name": "language",
          "value": "py"
        }
      }
    }
    

**Response:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": {
        "completion": {
          "values": ["python", "pytorch", "pyside"],
          "total": 10,
          "hasMore": true
        }
      }
    }
    

For prompts or URI templates with multiple arguments, clients should resolve them in the order they are presented by the server, and include each previous completion in the `context.arguments` object to provide context for subsequent requests.

**Request:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "completion/complete",
      "params": {
        "ref": {
          "type": "ref/prompt",
          "name": "code_review"
        },
        "argument": {
          "name": "framework",
          "value": "fla"
        },
        "context": {
          "arguments": {
            "language": "python"
          }
        }
      }
    }
    

**Response:**

Copy
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": {
        "completion": {
          "values": ["flask"],
          "total": 1,
          "hasMore": false
        }
      }
    }
    

### 

​

Reference Types

The protocol supports two types of completion references:

Type| Description| Example  
---|---|---  
`ref/prompt`| References a prompt by name| `{"type": "ref/prompt", "name": "code_review"}`  
`ref/resource`| References a resource URI| `{"type": "ref/resource", "uri": "file:///{path}"}`  
  
### 

​

Completion Results

Servers return an array of completion values ranked by relevance, with:

  * Maximum 100 items per response
  * Optional total number of available matches
  * Boolean indicating if additional results exist

## 

​

Message Flow

## 

​

Data Types

### 

​

CompleteRequest

  * `ref`: A `PromptReference` or `ResourceReference`
  * `argument`: Object containing:
    * `name`: Argument name
    * `value`: Current value
  * `context`: Object containing:
    * `arguments`: A mapping of already-resolved argument names to their values.

### 

​

CompleteResult

  * `completion`: Object containing:
    * `values`: Array of suggestions (max 100)
    * `total`: Optional total matches
    * `hasMore`: Additional results flag

## 

​

Error Handling

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:

  * Method not found: `-32601` (Capability not supported)
  * Invalid prompt name: `-32602` (Invalid params)
  * Missing required arguments: `-32602` (Invalid params)
  * Internal errors: `-32603` (Internal error)

## 

​

Implementation Considerations

  1. Servers **SHOULD** :

     * Return suggestions sorted by relevance
     * Implement fuzzy matching where appropriate
     * Rate limit completion requests
     * Validate all inputs
  2. Clients **SHOULD** :

     * Debounce rapid completion requests
     * Cache completion results where appropriate
     * Handle missing or partial results gracefully

## 

​

Security

Implementations **MUST** :

  * Validate all completion inputs
  * Implement appropriate rate limiting
  * Control access to sensitive suggestions
  * Prevent completion-based information disclosure

Was this page helpful?

YesNo

[Tools](/specification/draft/server/tools)[Logging](/specification/draft/server/utilities/logging)

On this page

  * User Interaction Model
  * Capabilities
  * Protocol Messages
  * Requesting Completions
  * Reference Types
  * Completion Results
  * Message Flow
  * Data Types
  * CompleteRequest
  * CompleteResult
  * Error Handling
  * Implementation Considerations
  * Security

Assistant

Responses are generated using AI and may contain mistakes.