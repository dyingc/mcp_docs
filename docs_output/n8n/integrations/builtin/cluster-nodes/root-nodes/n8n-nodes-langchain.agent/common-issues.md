# AI Agent node common issues | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues.md "Edit this page")

# AI Agent node common issues#

Here are some common errors and issues with the [AI Agent node](../) and steps to resolve or troubleshoot them.

## Internal error: 400 Invalid value for 'content'#

A full error message might look like this:
    
    
    1
    2
    3

| 
    
    
    Internal error
    Error: 400 Invalid value for 'content': expected a string, got null.
    <stack-trace>
      
  
---|---  
  
This error can occur if the **Prompt** input contains a null value.

You might see this in one of two scenarios:

  1. When you've set the **Prompt** to **Define below** and have an expression in your **Text** that isn't generating a value.
     * To resolve, make sure your expressions reference valid fields and that they resolve to valid input rather than null.
  2. When you've set the **Prompt** to **Connected Chat Trigger Node** and the incoming data has null values.
     * To resolve, remove any null values from the `chatInput` field of the input node.

## Error in sub-node Simple Memory#

This error displays when n8n runs into an issue with the [Simple Memory](../../../sub-nodes/n8n-nodes-langchain.memorybufferwindow/) sub-node.

It most often occurs when your workflow or the workflow template you copied uses an older version of the Simple memory node (previously known as "Window Buffer Memory").

Try removing the Simple Memory node from your workflow and re-adding it, which will guarantee you're using the latest version of the node.

## A Chat Model sub-node must be connected error#

This error displays when n8n tries to execute the node without having a Chat Model connected.

To resolve this, click the + Chat Model button at the bottom of your screen when the node is open, or click the Chat Model + connector when the node is closed. n8n will then open a selection of possible Chat Models to pick from.

## No prompt specified error#

This error occurs when the agent expects to get the prompt from the previous node automatically. Typically, this happens when you're using the [Chat Trigger Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/). 

To resolve this issue, find the **Prompt** parameter of the AI Agent node and change it from **Connected Chat Trigger Node** to **Define below**. This allows you to manually build your prompt by referencing output data from other nodes or by adding static text.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top