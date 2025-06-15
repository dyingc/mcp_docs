# Example Servers - Model Context Protocol

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

Get Started

Example Servers

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

This page showcases various Model Context Protocol (MCP) servers that demonstrate the protocol’s capabilities and versatility. These servers enable Large Language Models (LLMs) to securely access tools and data sources.

## 

​

Reference implementations

These official reference servers demonstrate core MCP features and SDK usage:

### 

​

Current reference servers

  * **[Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** \- Secure file operations with configurable access controls
  * **[Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)** \- Web content fetching and conversion optimized for LLM usage
  * **[Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)** \- Knowledge graph-based persistent memory system
  * **[Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)** \- Dynamic problem-solving through thought sequences

### 

​

Archived servers (historical reference)

⚠️ **Note** : The following servers have been moved to the [servers-archived repository](https://github.com/modelcontextprotocol/servers-archived) and are no longer actively maintained. They are provided for historical reference only.

#### 

​

Data and file systems

  * **[PostgreSQL](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres)** \- Read-only database access with schema inspection capabilities
  * **[SQLite](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/sqlite)** \- Database interaction and business intelligence features
  * **[Google Drive](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gdrive)** \- File access and search capabilities for Google Drive

#### 

​

Development tools

  * **[Git](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/git)** \- Tools to read, search, and manipulate Git repositories
  * **[GitHub](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/github)** \- Repository management, file operations, and GitHub API integration
  * **[GitLab](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gitlab)** \- GitLab API integration enabling project management
  * **[Sentry](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/sentry)** \- Retrieving and analyzing issues from Sentry.io

#### 

​

Web and browser automation

  * **[Brave Search](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/brave-search)** \- Web and local search using Brave’s Search API
  * **[Puppeteer](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer)** \- Browser automation and web scraping capabilities

#### 

​

Productivity and communication

  * **[Slack](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/slack)** \- Channel management and messaging capabilities
  * **[Google Maps](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/google-maps)** \- Location services, directions, and place details

#### 

​

AI and specialized tools

  * **[EverArt](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/everart)** \- AI image generation using various models
  * **[AWS KB Retrieval](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/aws-kb-retrieval-server)** \- Retrieval from AWS Knowledge Base using Bedrock Agent Runtime

## 

​

Official integrations

Visit the [MCP Servers Repository (Official Integrations section)](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#%EF%B8%8F-official-integrations) for a list of MCP servers maintained by companies for their platforms.

## 

​

Community implementations

Visit the [MCP Servers Repository (Community section)](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) for a list of MCP servers maintained by community members.

## 

​

Getting started

### 

​

Using reference servers

TypeScript-based servers can be used directly with `npx`:

Copy
    
    
    npx -y @modelcontextprotocol/server-memory
    

Python-based servers can be used with `uvx` (recommended) or `pip`:

Copy
    
    
    # Using uvx
    uvx mcp-server-git
    
    # Using pip
    pip install mcp-server-git
    python -m mcp_server_git
    

### 

​

Configuring with Claude

To use an MCP server with Claude, add it to your configuration:

Copy
    
    
    {
      "mcpServers": {
        "memory": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-memory"]
        },
        "filesystem": {
          "command": "npx",
          "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "/path/to/allowed/files"
          ]
        },
        "github": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-github"],
          "env": {
            "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
          }
        }
      }
    }
    

## 

​

Additional resources

Visit the [MCP Servers Repository (Resources section)](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-resources) for a collection of other resources and projects related to MCP.

Visit our [GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions) to engage with the MCP community.

Was this page helpful?

YesNo

[For Claude Desktop Users](/quickstart/user)[Example Clients](/clients)

On this page

  * Reference implementations
  * Current reference servers
  * Archived servers (historical reference)
  * Data and file systems
  * Development tools
  * Web and browser automation
  * Productivity and communication
  * AI and specialized tools
  * Official integrations
  * Community implementations
  * Getting started
  * Using reference servers
  * Configuring with Claude
  * Additional resources

Assistant

Responses are generated using AI and may contain mistakes.