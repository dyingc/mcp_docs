# /mcp [BETA] - Model Context Protocol | liteLLM

On this page

LiteLLM Proxy provides an MCP Gateway that allows you to use a fixed endpoint for all MCP tools and control MCP access by Key, Team.

LiteLLM MCP Architecture: Use MCP tools with all LiteLLM supported models

## Overview​

Feature| Description  
---|---  
MCP Operations| • List Tools  
• Call Tools  
Supported MCP Transports| • Streamable HTTP  
• SSE  
LiteLLM Permission Management| ✨ Enterprise Only  
• By Key  
• By Team  
• By Organization  
  
## Adding your MCP​

  * LiteLLM UI
  * config.yaml

On the LiteLLM UI, Navigate to "MCP Servers" and click "Add New MCP Server".

On this form, you should enter your MCP Server URL and the transport you want to use.

LiteLLM supports the following MCP transports:

  * Streamable HTTP
  * SSE (Server-Sent Events)

Add your MCP servers directly in your `config.yaml` file:

config.yaml
    
    
    model_list:  
      - model_name: gpt-4o  
        litellm_params:  
          model: openai/gpt-4o  
          api_key: sk-xxxxxxx  
      
    mcp_servers:  
      # HTTP Streamable Server  
      deepwiki_mcp:  
        url: "https://mcp.deepwiki.com/mcp"  
      # SSE Server  
      zapier_mcp:  
        url: "https://actions.zapier.com/mcp/sk-akxxxxx/sse"  
        
      # Full configuration with all optional fields  
      my_http_server:  
        url: "https://my-mcp-server.com/mcp"  
        transport: "http"  
        description: "My custom MCP server"  
        auth_type: "api_key"  
        spec_version: "2025-03-26"  
    

**Configuration Options:**

  * **Server Name** : Use any descriptive name for your MCP server (e.g., `zapier_mcp`, `deepwiki_mcp`)
  * **URL** : The endpoint URL for your MCP server (required)
  * **Transport** : Optional transport type (defaults to `sse`)
    * `sse` \- SSE (Server-Sent Events) transport
    * `http` \- Streamable HTTP transport
  * **Description** : Optional description for the server
  * **Auth Type** : Optional authentication type
  * **Spec Version** : Optional MCP specification version (defaults to `2025-03-26`)

## Using your MCP​

  * OpenAI API
  * LiteLLM Proxy
  * Cursor IDE
  * Streamable HTTP
  * Python FastMCP

#### Connect via OpenAI Responses API​

Use the OpenAI Responses API to connect to your LiteLLM MCP server:

cURL Example
    
    
    curl --location 'https://api.openai.com/v1/responses' \  
    --header 'Content-Type: application/json' \  
    --header "Authorization: Bearer $OPENAI_API_KEY" \  
    --data '{  
        "model": "gpt-4o",  
        "tools": [  
            {  
                "type": "mcp",  
                "server_label": "litellm",  
                "server_url": "<your-litellm-proxy-base-url>/mcp",  
                "require_approval": "never",  
                "headers": {  
                    "x-litellm-api-key": "Bearer YOUR_LITELLM_API_KEY"  
                }  
            }  
        ],  
        "input": "Run available tools",  
        "tool_choice": "required"  
    }'  
    

#### Connect via LiteLLM Proxy Responses API​

Use this when calling LiteLLM Proxy for LLM API requests to `/v1/responses` endpoint.

cURL Example
    
    
    curl --location '<your-litellm-proxy-base-url>/v1/responses' \  
    --header 'Content-Type: application/json' \  
    --header "Authorization: Bearer $LITELLM_API_KEY" \  
    --data '{  
        "model": "gpt-4o",  
        "tools": [  
            {  
                "type": "mcp",  
                "server_label": "litellm",  
                "server_url": "<your-litellm-proxy-base-url>/mcp",  
                "require_approval": "never",  
                "headers": {  
                    "x-litellm-api-key": "Bearer YOUR_LITELLM_API_KEY"  
                }  
            }  
        ],  
        "input": "Run available tools",  
        "tool_choice": "required"  
    }'  
    

#### Connect via Cursor IDE​

Use tools directly from Cursor IDE with LiteLLM MCP:

**Setup Instructions:**

  1. **Open Cursor Settings** : Use `⇧+⌘+J` (Mac) or `Ctrl+Shift+J` (Windows/Linux)
  2. **Navigate to MCP Tools** : Go to the "MCP Tools" tab and click "New MCP Server"
  3. **Add Configuration** : Copy and paste the JSON configuration below, then save with `Cmd+S` or `Ctrl+S`

Cursor MCP Configuration
    
    
    {  
      "mcpServers": {  
        "LiteLLM": {  
          "url": "<your-litellm-proxy-base-url>/mcp",  
          "headers": {  
            "x-litellm-api-key": "Bearer $LITELLM_API_KEY"  
          }  
        }  
      }  
    }  
    

#### Connect via Streamable HTTP Transport​

Connect to LiteLLM MCP using HTTP transport. Compatible with any MCP client that supports HTTP streaming:

**Server URL:**
    
    
     <your-litellm-proxy-base-url>/mcp  
    

**Headers:**
    
    
     x-litellm-api-key: Bearer YOUR_LITELLM_API_KEY  
    

This URL can be used with any MCP client that supports HTTP transport. Refer to your client documentation to determine the appropriate transport method.

#### Connect via Python FastMCP Client​

Use the Python FastMCP client to connect to your LiteLLM MCP server:

**Installation:**

Install FastMCP
    
    
    pip install fastmcp  
    

or with uv:

Install with uv
    
    
    uv pip install fastmcp  
    

**Usage:**

Python FastMCP Example
    
    
    import asyncio  
    import json  
      
    from fastmcp import Client  
    from fastmcp.client.transports import StreamableHttpTransport  
      
    # Create the transport with your LiteLLM MCP server URL  
    server_url = "<your-litellm-proxy-base-url>/mcp"  
    transport = StreamableHttpTransport(  
        server_url,  
        headers={  
            "x-litellm-api-key": "Bearer YOUR_LITELLM_API_KEY"  
        }  
    )  
      
    # Initialize the client with the transport  
    client = Client(transport=transport)  
      
      
    async def main():  
        # Connection is established here  
        print("Connecting to LiteLLM MCP server...")  
        async with client:  
            print(f"Client connected: {client.is_connected()}")  
      
            # Make MCP calls within the context  
            print("Fetching available tools...")  
            tools = await client.list_tools()  
      
            print(f"Available tools: {json.dumps([t.name for t in tools], indent=2)}")  
              
            # Example: Call a tool (replace 'tool_name' with an actual tool name)  
            if tools:  
                tool_name = tools[0].name  
                print(f"Calling tool: {tool_name}")  
                  
                # Call the tool with appropriate arguments  
                result = await client.call_tool(tool_name, arguments={})  
                print(f"Tool result: {result}")  
      
      
    # Run the example  
    if __name__ == "__main__":  
        asyncio.run(main())  
    

## Using your MCP with client side credentials​

Use this if you want to pass a client side authentication token to LiteLLM to then pass to your MCP to auth to your MCP.

You can specify your MCP auth token using the header `x-mcp-auth`. LiteLLM will forward this token to your MCP server for authentication.

  * OpenAI API
  * LiteLLM Proxy
  * Cursor IDE
  * Streamable HTTP
  * Python FastMCP

#### Connect via OpenAI Responses API with MCP Auth​

Use the OpenAI Responses API and include the `x-mcp-auth` header for your MCP server authentication:

cURL Example with MCP Auth
    
    
    curl --location 'https://api.openai.com/v1/responses' \  
    --header 'Content-Type: application/json' \  
    --header "Authorization: Bearer $OPENAI_API_KEY" \  
    --data '{  
        "model": "gpt-4o",  
        "tools": [  
            {  
                "type": "mcp",  
                "server_label": "litellm",  
                "server_url": "<your-litellm-proxy-base-url>/mcp",  
                "require_approval": "never",  
                "headers": {  
                    "x-litellm-api-key": "Bearer YOUR_LITELLM_API_KEY",  
                    "x-mcp-auth": YOUR_MCP_AUTH_TOKEN  
                }  
            }  
        ],  
        "input": "Run available tools",  
        "tool_choice": "required"  
    }'  
    

#### Connect via LiteLLM Proxy Responses API with MCP Auth​

Use this when calling LiteLLM Proxy for LLM API requests to `/v1/responses` endpoint with MCP authentication:

cURL Example with MCP Auth
    
    
    curl --location '<your-litellm-proxy-base-url>/v1/responses' \  
    --header 'Content-Type: application/json' \  
    --header "Authorization: Bearer $LITELLM_API_KEY" \  
    --data '{  
        "model": "gpt-4o",  
        "tools": [  
            {  
                "type": "mcp",  
                "server_label": "litellm",  
                "server_url": "<your-litellm-proxy-base-url>/mcp",  
                "require_approval": "never",  
                "headers": {  
                    "x-litellm-api-key": "Bearer YOUR_LITELLM_API_KEY",  
                    "x-mcp-auth": "YOUR_MCP_AUTH_TOKEN"  
                }  
            }  
        ],  
        "input": "Run available tools",  
        "tool_choice": "required"  
    }'  
    

#### Connect via Cursor IDE with MCP Auth​

Use tools directly from Cursor IDE with LiteLLM MCP and include your MCP authentication token:

**Setup Instructions:**

  1. **Open Cursor Settings** : Use `⇧+⌘+J` (Mac) or `Ctrl+Shift+J` (Windows/Linux)
  2. **Navigate to MCP Tools** : Go to the "MCP Tools" tab and click "New MCP Server"
  3. **Add Configuration** : Copy and paste the JSON configuration below, then save with `Cmd+S` or `Ctrl+S`

Cursor MCP Configuration with Auth
    
    
    {  
      "mcpServers": {  
        "LiteLLM": {  
          "url": "<your-litellm-proxy-base-url>/mcp",  
          "headers": {  
            "x-litellm-api-key": "Bearer $LITELLM_API_KEY",  
            "x-mcp-auth": "$MCP_AUTH_TOKEN"  
          }  
        }  
      }  
    }  
    

#### Connect via Streamable HTTP Transport with MCP Auth​

Connect to LiteLLM MCP using HTTP transport with MCP authentication:

**Server URL:**
    
    
     <your-litellm-proxy-base-url>/mcp  
    

**Headers:**
    
    
     x-litellm-api-key: Bearer YOUR_LITELLM_API_KEY  
    x-mcp-auth: Bearer YOUR_MCP_AUTH_TOKEN  
    

This URL can be used with any MCP client that supports HTTP transport. The `x-mcp-auth` header will be forwarded to your MCP server for authentication.

#### Connect via Python FastMCP Client with MCP Auth​

Use the Python FastMCP client to connect to your LiteLLM MCP server with MCP authentication:

Python FastMCP Example with MCP Auth
    
    
    import asyncio  
    import json  
      
    from fastmcp import Client  
    from fastmcp.client.transports import StreamableHttpTransport  
      
    # Create the transport with your LiteLLM MCP server URL and auth headers  
    server_url = "<your-litellm-proxy-base-url>/mcp"  
    transport = StreamableHttpTransport(  
        server_url,  
        headers={  
            "x-litellm-api-key": "Bearer YOUR_LITELLM_API_KEY",  
            "x-mcp-auth": "Bearer YOUR_MCP_AUTH_TOKEN"  
        }  
    )  
      
    # Initialize the client with the transport  
    client = Client(transport=transport)  
      
      
    async def main():  
        # Connection is established here  
        print("Connecting to LiteLLM MCP server with authentication...")  
        async with client:  
            print(f"Client connected: {client.is_connected()}")  
      
            # Make MCP calls within the context  
            print("Fetching available tools...")  
            tools = await client.list_tools()  
      
            print(f"Available tools: {json.dumps([t.name for t in tools], indent=2)}")  
              
            # Example: Call a tool (replace 'tool_name' with an actual tool name)  
            if tools:  
                tool_name = tools[0].name  
                print(f"Calling tool: {tool_name}")  
                  
                # Call the tool with appropriate arguments  
                result = await client.call_tool(tool_name, arguments={})  
                print(f"Tool result: {result}")  
      
      
    # Run the example  
    if __name__ == "__main__":  
        asyncio.run(main())  
    

## ✨ MCP Permission Management​

LiteLLM supports managing permissions for MCP Servers by Keys, Teams, Organizations (entities) on LiteLLM. When a MCP client attempts to list tools, LiteLLM will only return the tools the entity has permissions to access.

When Creating a Key, Team, or Organization, you can select the allowed MCP Servers that the entity has access to.

## LiteLLM Proxy - Walk through MCP Gateway​

LiteLLM exposes an MCP Gateway for admins to add all their MCP servers to LiteLLM. The key benefits of using LiteLLM Proxy with MCP are:

  1. Use a fixed endpoint for all MCP tools
  2. MCP Permission management by Key, Team, or User

This video demonstrates how you can onboard an MCP server to LiteLLM Proxy, use it and set access controls.

## LiteLLM Python SDK MCP Bridge​

LiteLLM Python SDK acts as a MCP bridge to utilize MCP tools with all LiteLLM supported models. LiteLLM offers the following features for using MCP

  * **List** Available MCP Tools: OpenAI clients can view all available MCP tools
    * `litellm.experimental_mcp_client.load_mcp_tools` to list all available MCP tools
  * **Call** MCP Tools: OpenAI clients can call MCP tools
    * `litellm.experimental_mcp_client.call_openai_tool` to call an OpenAI tool on an MCP server

### 1\. List Available MCP Tools​

In this example we'll use `litellm.experimental_mcp_client.load_mcp_tools` to list all available MCP tools on any MCP server. This method can be used in two ways:

  * `format="mcp"` \- (default) Return MCP tools
    * Returns: `mcp.types.Tool`
  * `format="openai"` \- Return MCP tools converted to OpenAI API compatible tools. Allows using with OpenAI endpoints.
    * Returns: `openai.types.chat.ChatCompletionToolParam`

  * LiteLLM Python SDK
  * OpenAI SDK + LiteLLM Proxy

MCP Client List Tools
    
    
    # Create server parameters for stdio connection  
    from mcp import ClientSession, StdioServerParameters  
    from mcp.client.stdio import stdio_client  
    import os  
    import litellm  
    from litellm import experimental_mcp_client  
      
      
    server_params = StdioServerParameters(  
        command="python3",  
        # Make sure to update to the full absolute path to your mcp_server.py file  
        args=["./mcp_server.py"],  
    )  
      
    async with stdio_client(server_params) as (read, write):  
        async with ClientSession(read, write) as session:  
            # Initialize the connection  
            await session.initialize()  
      
            # Get tools  
            tools = await experimental_mcp_client.load_mcp_tools(session=session, format="openai")  
            print("MCP TOOLS: ", tools)  
      
            messages = [{"role": "user", "content": "what's (3 + 5)"}]  
            llm_response = await litellm.acompletion(  
                model="gpt-4o",  
                api_key=os.getenv("OPENAI_API_KEY"),  
                messages=messages,  
                tools=tools,  
            )  
            print("LLM RESPONSE: ", json.dumps(llm_response, indent=4, default=str))  
    

In this example we'll walk through how you can use the OpenAI SDK pointed to the LiteLLM proxy to call MCP tools. The key difference here is we use the OpenAI SDK to make the LLM API request

MCP Client List Tools
    
    
    # Create server parameters for stdio connection  
    from mcp import ClientSession, StdioServerParameters  
    from mcp.client.stdio import stdio_client  
    import os  
    from openai import OpenAI  
    from litellm import experimental_mcp_client  
      
    server_params = StdioServerParameters(  
        command="python3",  
        # Make sure to update to the full absolute path to your mcp_server.py file  
        args=["./mcp_server.py"],  
    )  
      
    async with stdio_client(server_params) as (read, write):  
        async with ClientSession(read, write) as session:  
            # Initialize the connection  
            await session.initialize()  
      
            # Get tools using litellm mcp client  
            tools = await experimental_mcp_client.load_mcp_tools(session=session, format="openai")  
            print("MCP TOOLS: ", tools)  
      
            # Use OpenAI SDK pointed to LiteLLM proxy  
            client = OpenAI(  
                api_key="your-api-key",  # Your LiteLLM proxy API key  
                base_url="http://localhost:4000"  # Your LiteLLM proxy URL  
            )  
      
            messages = [{"role": "user", "content": "what's (3 + 5)"}]  
            llm_response = client.chat.completions.create(  
                model="gpt-4",  
                messages=messages,  
                tools=tools  
            )  
            print("LLM RESPONSE: ", llm_response)  
    

### 2\. List and Call MCP Tools​

In this example we'll use

  * `litellm.experimental_mcp_client.load_mcp_tools` to list all available MCP tools on any MCP server
  * `litellm.experimental_mcp_client.call_openai_tool` to call an OpenAI tool on an MCP server

The first llm response returns a list of OpenAI tools. We take the first tool call from the LLM response and pass it to `litellm.experimental_mcp_client.call_openai_tool` to call the tool on the MCP server.

#### How `litellm.experimental_mcp_client.call_openai_tool` works​

  * Accepts an OpenAI Tool Call from the LLM response
  * Converts the OpenAI Tool Call to an MCP Tool
  * Calls the MCP Tool on the MCP server
  * Returns the result of the MCP Tool call

  * LiteLLM Python SDK
  * OpenAI SDK + LiteLLM Proxy

MCP Client List and Call Tools
    
    
    # Create server parameters for stdio connection  
    from mcp import ClientSession, StdioServerParameters  
    from mcp.client.stdio import stdio_client  
    import os  
    import litellm  
    from litellm import experimental_mcp_client  
      
      
    server_params = StdioServerParameters(  
        command="python3",  
        # Make sure to update to the full absolute path to your mcp_server.py file  
        args=["./mcp_server.py"],  
    )  
      
    async with stdio_client(server_params) as (read, write):  
        async with ClientSession(read, write) as session:  
            # Initialize the connection  
            await session.initialize()  
      
            # Get tools  
            tools = await experimental_mcp_client.load_mcp_tools(session=session, format="openai")  
            print("MCP TOOLS: ", tools)  
      
            messages = [{"role": "user", "content": "what's (3 + 5)"}]  
            llm_response = await litellm.acompletion(  
                model="gpt-4o",  
                api_key=os.getenv("OPENAI_API_KEY"),  
                messages=messages,  
                tools=tools,  
            )  
            print("LLM RESPONSE: ", json.dumps(llm_response, indent=4, default=str))  
      
            openai_tool = llm_response["choices"][0]["message"]["tool_calls"][0]  
            # Call the tool using MCP client  
            call_result = await experimental_mcp_client.call_openai_tool(  
                session=session,  
                openai_tool=openai_tool,  
            )  
            print("MCP TOOL CALL RESULT: ", call_result)  
      
            # send the tool result to the LLM  
            messages.append(llm_response["choices"][0]["message"])  
            messages.append(  
                {  
                    "role": "tool",  
                    "content": str(call_result.content[0].text),  
                    "tool_call_id": openai_tool["id"],  
                }  
            )  
            print("final messages with tool result: ", messages)  
            llm_response = await litellm.acompletion(  
                model="gpt-4o",  
                api_key=os.getenv("OPENAI_API_KEY"),  
                messages=messages,  
                tools=tools,  
            )  
            print(  
                "FINAL LLM RESPONSE: ", json.dumps(llm_response, indent=4, default=str)  
            )  
    

In this example we'll walk through how you can use the OpenAI SDK pointed to the LiteLLM proxy to call MCP tools. The key difference here is we use the OpenAI SDK to make the LLM API request

MCP Client with OpenAI SDK
    
    
    # Create server parameters for stdio connection  
    from mcp import ClientSession, StdioServerParameters  
    from mcp.client.stdio import stdio_client  
    import os  
    from openai import OpenAI  
    from litellm import experimental_mcp_client  
      
    server_params = StdioServerParameters(  
        command="python3",  
        # Make sure to update to the full absolute path to your mcp_server.py file  
        args=["./mcp_server.py"],  
    )  
      
    async with stdio_client(server_params) as (read, write):  
        async with ClientSession(read, write) as session:  
            # Initialize the connection  
            await session.initialize()  
      
            # Get tools using litellm mcp client  
            tools = await experimental_mcp_client.load_mcp_tools(session=session, format="openai")  
            print("MCP TOOLS: ", tools)  
      
            # Use OpenAI SDK pointed to LiteLLM proxy  
            client = OpenAI(  
                api_key="your-api-key",  # Your LiteLLM proxy API key  
                base_url="http://localhost:8000"  # Your LiteLLM proxy URL  
            )  
      
            messages = [{"role": "user", "content": "what's (3 + 5)"}]  
            llm_response = client.chat.completions.create(  
                model="gpt-4",  
                messages=messages,  
                tools=tools  
            )  
            print("LLM RESPONSE: ", llm_response)  
      
            # Get the first tool call  
            tool_call = llm_response.choices[0].message.tool_calls[0]  
              
            # Call the tool using MCP client  
            call_result = await experimental_mcp_client.call_openai_tool(  
                session=session,  
                openai_tool=tool_call.model_dump(),  
            )  
            print("MCP TOOL CALL RESULT: ", call_result)  
      
            # Send the tool result back to the LLM  
            messages.append(llm_response.choices[0].message.model_dump())  
            messages.append({  
                "role": "tool",  
                "content": str(call_result.content[0].text),  
                "tool_call_id": tool_call.id,  
            })  
      
            final_response = client.chat.completions.create(  
                model="gpt-4",  
                messages=messages,  
                tools=tools  
            )  
            print("FINAL RESPONSE: ", final_response)  
    

  * Overview
  * Adding your MCP
  * Using your MCP
  * Using your MCP with client side credentials
  * ✨ MCP Permission Management
  * LiteLLM Proxy - Walk through MCP Gateway
  * LiteLLM Python SDK MCP Bridge
    * 1\. List Available MCP Tools
    * 2\. List and Call MCP Tools