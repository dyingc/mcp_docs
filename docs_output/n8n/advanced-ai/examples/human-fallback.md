# Set a human fallback for AI workflows | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/advanced-ai/examples/human-fallback.md "Edit this page")

# Have a human fallback for AI workflows#

This is a workflow that tries to answer user queries using the standard GPT-4 model. If it can't answer, it sends a message to Slack to ask for human help. It prompts the user to supply an email address.

This workflow uses the [Chat Trigger](../../../integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/) to provide the chat interface, and the [Call n8n Workflow Tool](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow/) to call a second workflow that handles checking for email addresses and sending the Slack message. 

[View workflow file](/_workflows/advanced-ai/examples/ask_a_human.json)

## Key features#

This workflow uses:

  * [Chat Trigger](../../../integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/): start your workflow and respond to user chat interactions. The node provides a customizable chat interface.
  * [Agent](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/): the key piece of the AI workflow. The Agent interacts with other components of the workflow and makes decisions about what tools to use.
  * [Call n8n Workflow Tool](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow/): plug in n8n workflows as custom tools. In AI, a tool is an interface the AI can use to interact with the world (in this case, the data provided by your workflow). It allows the AI model to access information beyond its built-in dataset.

## Using the example#

To load the template into your n8n instance:

  1. Download the workflow JSON file.
  2. Open a new workflow in your n8n instance.
  3. Copy in the JSON, or select **Workflow menu** ![Workflow menu icon](../../../_images/common-icons/three-dots-horizontal.png) > **Import from file...**.

The example workflows use Sticky Notes to guide you:

  * Yellow: notes and information.
  * Green: instructions to run the workflow.
  * Orange: you need to change something to make the workflow work.
  * Blue: draws attention to a key feature of the example.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top