# Prompts - Model Context Protocol

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

Prompts

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

Prompts enable servers to define reusable prompt templates and workflows that clients can easily surface to users and LLMs. They provide a powerful way to standardize and share common LLM interactions.

Prompts are designed to be **user-controlled** , meaning they are exposed from servers to clients with the intention of the user being able to explicitly select them for use.

## 

​

Overview

Prompts in MCP are predefined templates that can:

  * Accept dynamic arguments
  * Include context from resources
  * Chain multiple interactions
  * Guide specific workflows
  * Surface as UI elements (like slash commands)

## 

​

Prompt structure

Each prompt is defined with:

Copy
    
    
    {
      name: string;              // Unique identifier for the prompt
      description?: string;      // Human-readable description
      arguments?: [              // Optional list of arguments
        {
          name: string;          // Argument identifier
          description?: string;  // Argument description
          required?: boolean;    // Whether argument is required
        }
      ]
    }
    

## 

​

Discovering prompts

Clients can discover available prompts through the `prompts/list` endpoint:

Copy
    
    
    // Request
    {
      method: "prompts/list";
    }
    
    // Response
    {
      prompts: [
        {
          name: "analyze-code",
          description: "Analyze code for potential improvements",
          arguments: [
            {
              name: "language",
              description: "Programming language",
              required: true,
            },
          ],
        },
      ];
    }
    

## 

​

Using prompts

To use a prompt, clients make a `prompts/get` request:

Copy
    
    
    // Request
    {
      method: "prompts/get",
      params: {
        name: "analyze-code",
        arguments: {
          language: "python"
        }
      }
    }
    
    // Response
    {
      description: "Analyze Python code for potential improvements",
      messages: [
        {
          role: "user",
          content: {
            type: "text",
            text: "Please analyze the following Python code for potential improvements:\n\n```python\ndef calculate_sum(numbers):\n    total = 0\n    for num in numbers:\n        total = total + num\n    return total\n\nresult = calculate_sum([1, 2, 3, 4, 5])\nprint(result)\n```"
          }
        }
      ]
    }
    

## 

​

Dynamic prompts

Prompts can be dynamic and include:

### 

​

Embedded resource context

Copy
    
    
    {
      "name": "analyze-project",
      "description": "Analyze project logs and code",
      "arguments": [
        {
          "name": "timeframe",
          "description": "Time period to analyze logs",
          "required": true
        },
        {
          "name": "fileUri",
          "description": "URI of code file to review",
          "required": true
        }
      ]
    }
    

When handling the `prompts/get` request:

Copy
    
    
    {
      "messages": [
        {
          "role": "user",
          "content": {
            "type": "text",
            "text": "Analyze these system logs and the code file for any issues:"
          }
        },
        {
          "role": "user",
          "content": {
            "type": "resource",
            "resource": {
              "uri": "logs://recent?timeframe=1h",
              "text": "[2024-03-14 15:32:11] ERROR: Connection timeout in network.py:127\n[2024-03-14 15:32:15] WARN: Retrying connection (attempt 2/3)\n[2024-03-14 15:32:20] ERROR: Max retries exceeded",
              "mimeType": "text/plain"
            }
          }
        },
        {
          "role": "user",
          "content": {
            "type": "resource",
            "resource": {
              "uri": "file:///path/to/code.py",
              "text": "def connect_to_service(timeout=30):\n    retries = 3\n    for attempt in range(retries):\n        try:\n            return establish_connection(timeout)\n        except TimeoutError:\n            if attempt == retries - 1:\n                raise\n            time.sleep(5)\n\ndef establish_connection(timeout):\n    # Connection implementation\n    pass",
              "mimeType": "text/x-python"
            }
          }
        }
      ]
    }
    

### 

​

Multi-step workflows

Copy
    
    
    const debugWorkflow = {
      name: "debug-error",
      async getMessages(error: string) {
        return [
          {
            role: "user",
            content: {
              type: "text",
              text: `Here's an error I'm seeing: ${error}`,
            },
          },
          {
            role: "assistant",
            content: {
              type: "text",
              text: "I'll help analyze this error. What have you tried so far?",
            },
          },
          {
            role: "user",
            content: {
              type: "text",
              text: "I've tried restarting the service, but the error persists.",
            },
          },
        ];
      },
    };
    

## 

​

Example implementation

Here’s a complete example of implementing prompts in an MCP server:

  * TypeScript
  * Python

Copy
    
    
    import { Server } from "@modelcontextprotocol/sdk/server";
    import {
      ListPromptsRequestSchema,
      GetPromptRequestSchema
    } from "@modelcontextprotocol/sdk/types";
    
    const PROMPTS = {
      "git-commit": {
        name: "git-commit",
        description: "Generate a Git commit message",
        arguments: [
          {
            name: "changes",
            description: "Git diff or description of changes",
            required: true
          }
        ]
      },
      "explain-code": {
        name: "explain-code",
        description: "Explain how code works",
        arguments: [
          {
            name: "code",
            description: "Code to explain",
            required: true
          },
          {
            name: "language",
            description: "Programming language",
            required: false
          }
        ]
      }
    };
    
    const server = new Server({
      name: "example-prompts-server",
      version: "1.0.0"
    }, {
      capabilities: {
        prompts: {}
      }
    });
    
    // List available prompts
    server.setRequestHandler(ListPromptsRequestSchema, async () => {
      return {
        prompts: Object.values(PROMPTS)
      };
    });
    
    // Get specific prompt
    server.setRequestHandler(GetPromptRequestSchema, async (request) => {
      const prompt = PROMPTS[request.params.name];
      if (!prompt) {
        throw new Error(`Prompt not found: ${request.params.name}`);
      }
    
      if (request.params.name === "git-commit") {
        return {
          messages: [
            {
              role: "user",
              content: {
                type: "text",
                text: `Generate a concise but descriptive commit message for these changes:\n\n${request.params.arguments?.changes}`
              }
            }
          ]
        };
      }
    
      if (request.params.name === "explain-code") {
        const language = request.params.arguments?.language || "Unknown";
        return {
          messages: [
            {
              role: "user",
              content: {
                type: "text",
                text: `Explain how this ${language} code works:\n\n${request.params.arguments?.code}`
              }
            }
          ]
        };
      }
    
      throw new Error("Prompt implementation not found");
    });
    

Copy
    
    
    import { Server } from "@modelcontextprotocol/sdk/server";
    import {
      ListPromptsRequestSchema,
      GetPromptRequestSchema
    } from "@modelcontextprotocol/sdk/types";
    
    const PROMPTS = {
      "git-commit": {
        name: "git-commit",
        description: "Generate a Git commit message",
        arguments: [
          {
            name: "changes",
            description: "Git diff or description of changes",
            required: true
          }
        ]
      },
      "explain-code": {
        name: "explain-code",
        description: "Explain how code works",
        arguments: [
          {
            name: "code",
            description: "Code to explain",
            required: true
          },
          {
            name: "language",
            description: "Programming language",
            required: false
          }
        ]
      }
    };
    
    const server = new Server({
      name: "example-prompts-server",
      version: "1.0.0"
    }, {
      capabilities: {
        prompts: {}
      }
    });
    
    // List available prompts
    server.setRequestHandler(ListPromptsRequestSchema, async () => {
      return {
        prompts: Object.values(PROMPTS)
      };
    });
    
    // Get specific prompt
    server.setRequestHandler(GetPromptRequestSchema, async (request) => {
      const prompt = PROMPTS[request.params.name];
      if (!prompt) {
        throw new Error(`Prompt not found: ${request.params.name}`);
      }
    
      if (request.params.name === "git-commit") {
        return {
          messages: [
            {
              role: "user",
              content: {
                type: "text",
                text: `Generate a concise but descriptive commit message for these changes:\n\n${request.params.arguments?.changes}`
              }
            }
          ]
        };
      }
    
      if (request.params.name === "explain-code") {
        const language = request.params.arguments?.language || "Unknown";
        return {
          messages: [
            {
              role: "user",
              content: {
                type: "text",
                text: `Explain how this ${language} code works:\n\n${request.params.arguments?.code}`
              }
            }
          ]
        };
      }
    
      throw new Error("Prompt implementation not found");
    });
    

Copy
    
    
    from mcp.server import Server
    import mcp.types as types
    
    # Define available prompts
    PROMPTS = {
        "git-commit": types.Prompt(
            name="git-commit",
            description="Generate a Git commit message",
            arguments=[
                types.PromptArgument(
                    name="changes",
                    description="Git diff or description of changes",
                    required=True
                )
            ],
        ),
        "explain-code": types.Prompt(
            name="explain-code",
            description="Explain how code works",
            arguments=[
                types.PromptArgument(
                    name="code",
                    description="Code to explain",
                    required=True
                ),
                types.PromptArgument(
                    name="language",
                    description="Programming language",
                    required=False
                )
            ],
        )
    }
    
    # Initialize server
    app = Server("example-prompts-server")
    
    @app.list_prompts()
    async def list_prompts() -> list[types.Prompt]:
        return list(PROMPTS.values())
    
    @app.get_prompt()
    async def get_prompt(
        name: str, arguments: dict[str, str] | None = None
    ) -> types.GetPromptResult:
        if name not in PROMPTS:
            raise ValueError(f"Prompt not found: {name}")
    
        if name == "git-commit":
            changes = arguments.get("changes") if arguments else ""
            return types.GetPromptResult(
                messages=[
                    types.PromptMessage(
                        role="user",
                        content=types.TextContent(
                            type="text",
                            text=f"Generate a concise but descriptive commit message "
                            f"for these changes:\n\n{changes}"
                        )
                    )
                ]
            )
    
        if name == "explain-code":
            code = arguments.get("code") if arguments else ""
            language = arguments.get("language", "Unknown") if arguments else "Unknown"
            return types.GetPromptResult(
                messages=[
                    types.PromptMessage(
                        role="user",
                        content=types.TextContent(
                            type="text",
                            text=f"Explain how this {language} code works:\n\n{code}"
                        )
                    )
                ]
            )
    
        raise ValueError("Prompt implementation not found")
    

## 

​

Best practices

When implementing prompts:

  1. Use clear, descriptive prompt names
  2. Provide detailed descriptions for prompts and arguments
  3. Validate all required arguments
  4. Handle missing arguments gracefully
  5. Consider versioning for prompt templates
  6. Cache dynamic content when appropriate
  7. Implement error handling
  8. Document expected argument formats
  9. Consider prompt composability
  10. Test prompts with various inputs

## 

​

UI integration

Prompts can be surfaced in client UIs as:

  * Slash commands
  * Quick actions
  * Context menu items
  * Command palette entries
  * Guided workflows
  * Interactive forms

## 

​

Updates and changes

Servers can notify clients about prompt changes:

  1. Server capability: `prompts.listChanged`
  2. Notification: `notifications/prompts/list_changed`
  3. Client re-fetches prompt list

## 

​

Security considerations

When implementing prompts:

  * Validate all arguments
  * Sanitize user input
  * Consider rate limiting
  * Implement access controls
  * Audit prompt usage
  * Handle sensitive data appropriately
  * Validate generated content
  * Implement timeouts
  * Consider prompt injection risks
  * Document security requirements

Was this page helpful?

YesNo

[Resources](/docs/concepts/resources)[Tools](/docs/concepts/tools)

On this page

  * Overview
  * Prompt structure
  * Discovering prompts
  * Using prompts
  * Dynamic prompts
  * Embedded resource context
  * Multi-step workflows
  * Example implementation
  * Best practices
  * UI integration
  * Updates and changes
  * Security considerations

Assistant

Responses are generated using AI and may contain mistakes.