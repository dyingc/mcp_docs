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

##### Get Started

  * [Introduction](/introduction)
  * Quickstart

  * [Example Servers](/examples)
  * [Example Clients](/clients)
  * [FAQs](/faqs)

##### Tutorials

  * [Building MCP with LLMs](/tutorials/building-mcp-with-llms)
  * [Debugging](/docs/tools/debugging)
  * [Inspector](/docs/tools/inspector)

##### Concepts

  * [Core architecture](/docs/concepts/architecture)
  * [Resources](/docs/concepts/resources)
  * [Prompts](/docs/concepts/prompts)
  * [Tools](/docs/concepts/tools)
  * [Sampling](/docs/concepts/sampling)
  * [Roots](/docs/concepts/roots)
  * [Transports](/docs/concepts/transports)

##### Development

  * [Roadmap](/development/roadmap)
  * [Contributing](/development/contributing)

[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](/)

Search...

⌘K

Search...

Navigation

Concepts

Tools

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

Tools are a powerful primitive in the Model Context Protocol (MCP) that enable servers to expose executable functionality to clients. Through tools, LLMs can interact with external systems, perform computations, and take actions in the real world.

Tools are designed to be **model-controlled** , meaning that tools are exposed from servers to clients with the intention of the AI model being able to automatically invoke them (with a human in the loop to grant approval).

## 

​

Overview

Tools in MCP allow servers to expose executable functions that can be invoked by clients and used by LLMs to perform actions. Key aspects of tools include:

  * **Discovery** : Clients can list available tools through the `tools/list` endpoint
  * **Invocation** : Tools are called using the `tools/call` endpoint, where servers perform the requested operation and return results
  * **Flexibility** : Tools can range from simple calculations to complex API interactions

Like [resources](/docs/concepts/resources), tools are identified by unique names and can include descriptions to guide their usage. However, unlike resources, tools represent dynamic operations that can modify state or interact with external systems.

## 

​

Tool definition structure

Each tool is defined with the following structure:

Copy
    
    
    {
      name: string;          // Unique identifier for the tool
      description?: string;  // Human-readable description
      inputSchema: {         // JSON Schema for the tool's parameters
        type: "object",
        properties: { ... }  // Tool-specific parameters
      },
      annotations?: {        // Optional hints about tool behavior
        title?: string;      // Human-readable title for the tool
        readOnlyHint?: boolean;    // If true, the tool does not modify its environment
        destructiveHint?: boolean; // If true, the tool may perform destructive updates
        idempotentHint?: boolean;  // If true, repeated calls with same args have no additional effect
        openWorldHint?: boolean;   // If true, tool interacts with external entities
      }
    }
    

## 

​

Implementing tools

Here’s an example of implementing a basic tool in an MCP server:

  * TypeScript
  * Python

Copy
    
    
    const server = new Server({
      name: "example-server",
      version: "1.0.0"
    }, {
      capabilities: {
        tools: {}
      }
    });
    
    // Define available tools
    server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [{
          name: "calculate_sum",
          description: "Add two numbers together",
          inputSchema: {
            type: "object",
            properties: {
              a: { type: "number" },
              b: { type: "number" }
            },
            required: ["a", "b"]
          }
        }]
      };
    });
    
    // Handle tool execution
    server.setRequestHandler(CallToolRequestSchema, async (request) => {
      if (request.params.name === "calculate_sum") {
        const { a, b } = request.params.arguments;
        return {
          content: [
            {
              type: "text",
              text: String(a + b)
            }
          ]
        };
      }
      throw new Error("Tool not found");
    });
    

Copy
    
    
    const server = new Server({
      name: "example-server",
      version: "1.0.0"
    }, {
      capabilities: {
        tools: {}
      }
    });
    
    // Define available tools
    server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [{
          name: "calculate_sum",
          description: "Add two numbers together",
          inputSchema: {
            type: "object",
            properties: {
              a: { type: "number" },
              b: { type: "number" }
            },
            required: ["a", "b"]
          }
        }]
      };
    });
    
    // Handle tool execution
    server.setRequestHandler(CallToolRequestSchema, async (request) => {
      if (request.params.name === "calculate_sum") {
        const { a, b } = request.params.arguments;
        return {
          content: [
            {
              type: "text",
              text: String(a + b)
            }
          ]
        };
      }
      throw new Error("Tool not found");
    });
    

Copy
    
    
    app = Server("example-server")
    
    @app.list_tools()
    async def list_tools() -> list[types.Tool]:
        return [
            types.Tool(
                name="calculate_sum",
                description="Add two numbers together",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "a": {"type": "number"},
                        "b": {"type": "number"}
                    },
                    "required": ["a", "b"]
                }
            )
        ]
    
    @app.call_tool()
    async def call_tool(
        name: str,
        arguments: dict
    ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
        if name == "calculate_sum":
            a = arguments["a"]
            b = arguments["b"]
            result = a + b
            return [types.TextContent(type="text", text=str(result))]
        raise ValueError(f"Tool not found: {name}")
    

## 

​

Example tool patterns

Here are some examples of types of tools that a server could provide:

### 

​

System operations

Tools that interact with the local system:

Copy
    
    
    {
      name: "execute_command",
      description: "Run a shell command",
      inputSchema: {
        type: "object",
        properties: {
          command: { type: "string" },
          args: { type: "array", items: { type: "string" } }
        }
      }
    }
    

### 

​

API integrations

Tools that wrap external APIs:

Copy
    
    
    {
      name: "github_create_issue",
      description: "Create a GitHub issue",
      inputSchema: {
        type: "object",
        properties: {
          title: { type: "string" },
          body: { type: "string" },
          labels: { type: "array", items: { type: "string" } }
        }
      }
    }
    

### 

​

Data processing

Tools that transform or analyze data:

Copy
    
    
    {
      name: "analyze_csv",
      description: "Analyze a CSV file",
      inputSchema: {
        type: "object",
        properties: {
          filepath: { type: "string" },
          operations: {
            type: "array",
            items: {
              enum: ["sum", "average", "count"]
            }
          }
        }
      }
    }
    

## 

​

Best practices

When implementing tools:

  1. Provide clear, descriptive names and descriptions
  2. Use detailed JSON Schema definitions for parameters
  3. Include examples in tool descriptions to demonstrate how the model should use them
  4. Implement proper error handling and validation
  5. Use progress reporting for long operations
  6. Keep tool operations focused and atomic
  7. Document expected return value structures
  8. Implement proper timeouts
  9. Consider rate limiting for resource-intensive operations
  10. Log tool usage for debugging and monitoring

## 

​

Security considerations

When exposing tools:

### 

​

Input validation

  * Validate all parameters against the schema
  * Sanitize file paths and system commands
  * Validate URLs and external identifiers
  * Check parameter sizes and ranges
  * Prevent command injection

### 

​

Access control

  * Implement authentication where needed
  * Use appropriate authorization checks
  * Audit tool usage
  * Rate limit requests
  * Monitor for abuse

### 

​

Error handling

  * Don’t expose internal errors to clients
  * Log security-relevant errors
  * Handle timeouts appropriately
  * Clean up resources after errors
  * Validate return values

## 

​

Tool discovery and updates

MCP supports dynamic tool discovery:

  1. Clients can list available tools at any time
  2. Servers can notify clients when tools change using `notifications/tools/list_changed`
  3. Tools can be added or removed during runtime
  4. Tool definitions can be updated (though this should be done carefully)

## 

​

Error handling

Tool errors should be reported within the result object, not as MCP protocol-level errors. This allows the LLM to see and potentially handle the error. When a tool encounters an error:

  1. Set `isError` to `true` in the result
  2. Include error details in the `content` array

Here’s an example of proper error handling for tools:

  * TypeScript
  * Python

Copy
    
    
    try {
      // Tool operation
      const result = performOperation();
      return {
        content: [
          {
            type: "text",
            text: `Operation successful: ${result}`
          }
        ]
      };
    } catch (error) {
      return {
        isError: true,
        content: [
          {
            type: "text",
            text: `Error: ${error.message}`
          }
        ]
      };
    }
    

Copy
    
    
    try {
      // Tool operation
      const result = performOperation();
      return {
        content: [
          {
            type: "text",
            text: `Operation successful: ${result}`
          }
        ]
      };
    } catch (error) {
      return {
        isError: true,
        content: [
          {
            type: "text",
            text: `Error: ${error.message}`
          }
        ]
      };
    }
    

Copy
    
    
    try:
        # Tool operation
        result = perform_operation()
        return types.CallToolResult(
            content=[
                types.TextContent(
                    type="text",
                    text=f"Operation successful: {result}"
                )
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[
                types.TextContent(
                    type="text",
                    text=f"Error: {str(error)}"
                )
            ]
        )
    

This approach allows the LLM to see that an error occurred and potentially take corrective action or request human intervention.

## 

​

Tool annotations

Tool annotations provide additional metadata about a tool’s behavior, helping clients understand how to present and manage tools. These annotations are hints that describe the nature and impact of a tool, but should not be relied upon for security decisions.

### 

​

Purpose of tool annotations

Tool annotations serve several key purposes:

  1. Provide UX-specific information without affecting model context
  2. Help clients categorize and present tools appropriately
  3. Convey information about a tool’s potential side effects
  4. Assist in developing intuitive interfaces for tool approval

### 

​

Available tool annotations

The MCP specification defines the following annotations for tools:

Annotation| Type| Default| Description  
---|---|---|---  
`title`| string| -| A human-readable title for the tool, useful for UI display  
`readOnlyHint`| boolean| false| If true, indicates the tool does not modify its environment  
`destructiveHint`| boolean| true| If true, the tool may perform destructive updates (only meaningful when `readOnlyHint` is false)  
`idempotentHint`| boolean| false| If true, calling the tool repeatedly with the same arguments has no additional effect (only meaningful when `readOnlyHint` is false)  
`openWorldHint`| boolean| true| If true, the tool may interact with an “open world” of external entities  
  
### 

​

Example usage

Here’s how to define tools with annotations for different scenarios:

Copy
    
    
    // A read-only search tool
    {
      name: "web_search",
      description: "Search the web for information",
      inputSchema: {
        type: "object",
        properties: {
          query: { type: "string" }
        },
        required: ["query"]
      },
      annotations: {
        title: "Web Search",
        readOnlyHint: true,
        openWorldHint: true
      }
    }
    
    // A destructive file deletion tool
    {
      name: "delete_file",
      description: "Delete a file from the filesystem",
      inputSchema: {
        type: "object",
        properties: {
          path: { type: "string" }
        },
        required: ["path"]
      },
      annotations: {
        title: "Delete File",
        readOnlyHint: false,
        destructiveHint: true,
        idempotentHint: true,
        openWorldHint: false
      }
    }
    
    // A non-destructive database record creation tool
    {
      name: "create_record",
      description: "Create a new record in the database",
      inputSchema: {
        type: "object",
        properties: {
          table: { type: "string" },
          data: { type: "object" }
        },
        required: ["table", "data"]
      },
      annotations: {
        title: "Create Database Record",
        readOnlyHint: false,
        destructiveHint: false,
        idempotentHint: false,
        openWorldHint: false
      }
    }
    

### 

​

Integrating annotations in server implementation

  * TypeScript
  * Python

Copy
    
    
    server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [{
          name: "calculate_sum",
          description: "Add two numbers together",
          inputSchema: {
            type: "object",
            properties: {
              a: { type: "number" },
              b: { type: "number" }
            },
            required: ["a", "b"]
          },
          annotations: {
            title: "Calculate Sum",
            readOnlyHint: true,
            openWorldHint: false
          }
        }]
      };
    });
    

Copy
    
    
    server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [{
          name: "calculate_sum",
          description: "Add two numbers together",
          inputSchema: {
            type: "object",
            properties: {
              a: { type: "number" },
              b: { type: "number" }
            },
            required: ["a", "b"]
          },
          annotations: {
            title: "Calculate Sum",
            readOnlyHint: true,
            openWorldHint: false
          }
        }]
      };
    });
    

Copy
    
    
    from mcp.server.fastmcp import FastMCP
    
    mcp = FastMCP("example-server")
    
    @mcp.tool(
        annotations={
            "title": "Calculate Sum",
            "readOnlyHint": True,
            "openWorldHint": False
        }
    )
    async def calculate_sum(a: float, b: float) -> str:
        """Add two numbers together.
    
        Args:
            a: First number to add
            b: Second number to add
        """
        result = a + b
        return str(result)
    

### 

​

Best practices for tool annotations

  1. **Be accurate about side effects** : Clearly indicate whether a tool modifies its environment and whether those modifications are destructive.

  2. **Use descriptive titles** : Provide human-friendly titles that clearly describe the tool’s purpose.

  3. **Indicate idempotency properly** : Mark tools as idempotent only if repeated calls with the same arguments truly have no additional effect.

  4. **Set appropriate open/closed world hints** : Indicate whether a tool interacts with a closed system (like a database) or an open system (like the web).

  5. **Remember annotations are hints** : All properties in ToolAnnotations are hints and not guaranteed to provide a faithful description of tool behavior. Clients should never make security-critical decisions based solely on annotations.

## 

​

Testing tools

A comprehensive testing strategy for MCP tools should cover:

  * **Functional testing** : Verify tools execute correctly with valid inputs and handle invalid inputs appropriately
  * **Integration testing** : Test tool interaction with external systems using both real and mocked dependencies
  * **Security testing** : Validate authentication, authorization, input sanitization, and rate limiting
  * **Performance testing** : Check behavior under load, timeout handling, and resource cleanup
  * **Error handling** : Ensure tools properly report errors through the MCP protocol and clean up resources

Was this page helpful?

YesNo

[Prompts](/docs/concepts/prompts)[Sampling](/docs/concepts/sampling)

On this page

  * Overview
  * Tool definition structure
  * Implementing tools
  * Example tool patterns
  * System operations
  * API integrations
  * Data processing
  * Best practices
  * Security considerations
  * Input validation
  * Access control
  * Error handling
  * Tool discovery and updates
  * Error handling
  * Tool annotations
  * Purpose of tool annotations
  * Available tool annotations
  * Example usage
  * Integrating annotations in server implementation
  * Best practices for tool annotations
  * Testing tools

Assistant

Responses are generated using AI and may contain mistakes.