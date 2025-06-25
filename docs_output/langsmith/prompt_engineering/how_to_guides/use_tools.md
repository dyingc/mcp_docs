# Use tools in a prompt | 🦜️🛠️ LangSmith

On this page

Tools allow language models to interact with external systems and perform actions beyond just generating text. In the LangSmith playground, you can use two types of tools:

  1. **Built-in tools** : Pre-configured tools provided by model providers (like OpenAI and Anthropic) that are ready to use. These include capabilities like web search, code interpretation, and more.

  2. **Custom tools** : Functions you define to perform specific tasks. These are useful when you need to integrate with your own systems or create specialized functionality. When you define custom tools within the LangSmith Playground, you can verify that the model correctly identifies and calls these tools with the correct arguments. Soon we plan to support executing these custom tool calls directly.

## When to use tools​

  * Use **built-in tools** when you need common capabilities like web search or code interpretation. These are built and maintained by the model providers.
  * Use **custom tools** when you want to test and validate your own tool designs, including:
    * Validating which tools the model chooses to use and seeing the specific arguments it provides in tool calls
    * Simulating tool interactions

## Built-in tools​

The LangSmith Playground has native support for a variety of tools from OpenAI and Anthropic. If you want to use a tool that isn't explicitly listed in the Playground, you can still add it by manually specifying its `type` and any required arguments.

### OpenAI Tools​

  * **Web search** : [Search the web for real-time information](https://platform.openai.com/docs/guides/tools-web-search?api-mode=responses)
  * **Image generation** : [Generate images based on a text prompt](https://platform.openai.com/docs/guides/tools-image-generation)
  * **MCP** : [Gives the model access to tools hosted on a remote MCP server](https://platform.openai.com/docs/guides/tools-remote-mcp)
  * [View all OpenAI tools](https://platform.openai.com/docs/guides/tools?api-mode=responses)

### Anthropic Tools​

  * **Web search** : [Search the web for up-to-date information](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool)
  * [View all Anthropic tools](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)

## Adding and using tools​

### Add a tool​

To add a tool to your prompt, click the `+ Tool` button at the bottom of the prompt editor. ![](/assets/images/add_tool-81f83ab9df7e00f16ca7a44f51f8938c.png)

### Use a built-in tool​

  1. In the tool section, select the built-in tool you want to use. You'll only see the tools that are compatible with the provider and model you've chosen.
  2. When the model calls the tool, the playground will display the response

![](/assets/images/web_search_tool-512e57cc1a215c972836ee050d147e33.gif)

### Create a custom tool​

To create a custom tool, you'll need to provide:

  * Name: A descriptive name for your tool
  * Description: Clear explanation of what the tool does
  * Arguments: The inputs your tool requires

![](/assets/images/custom_tool-840229db77b829c12cdcc9498a36212d.gif)

Note: When running a custom tool in the playground, the model will respond with a JSON object containing the tool name and the tool call. Currently, there's no way to connect this to a hosted tool via MCP.

![](/assets/images/tool_call-9a1b3a56c3347646ba55a9e8a0fca62f.png)

## Tool choice settings​

Some models provide control over which tools are called. To configure this:

  1. Go to prompt settings
  2. Navigate to tool settings
  3. Select tool choice

To understand the available tool choice options, check the documentation for your specific provider. For example, [OpenAI's documentation on tool choice](https://platform.openai.com/docs/guides/function-calling/function-calling-behavior?api-mode=responses#tool-choice).

![](/assets/images/tool_choice-80c88b50d3087269d0fbbd200a91ff86.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * When to use tools
  * Built-in tools
    * OpenAI Tools
    * Anthropic Tools
  * Adding and using tools
    * Add a tool
    * Use a built-in tool
    * Create a custom tool
  * Tool choice settings

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)