# Code node common issues | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/core-nodes/n8n-nodes-base.code/common-issues.md "Edit this page")

# Code node common issues#

Here are some common errors and issues with the [Code node](../) and steps to resolve or troubleshoot them.

## Code doesn't return items properly#

This error occurs when the code in your Code node doesn't return data in the expected format.

In n8n, all data passed between nodes is an array of objects. Each of these objects wraps another object with the `json` key:
    
    
    1
    2
    3
    4
    5
    6
    7

| 
    
    
    [
      {
        "json": {
    	  // your data goes here
    	}
      }
    ]
      
  
---|---  
  
To troubleshoot this error, check the following:

  * Read the [data structure](../../../../../data/data-structure/) to understand the data you receive in the Code node and the requirements for outputting data from the node.
  * Understand how data items work and how to connect data items from previous nodes with [item linking](../../../../../data/data-mapping/data-item-linking/).

## A 'json' property isn't an object#

This error occurs when the Code node returns data where the `json` key isn't pointing to an object.

This may happen if you set `json` to a different data structure, like an array:
    
    
    1
    2
    3
    4
    5
    6
    7

| 
    
    
    [
      {
        "json": [
    	  // Setting `json` to an array like this will produce an error
    	]
      }
    ]
      
  
---|---  
  
To resolve this, ensure that the `json` key references an object in your return data:
    
    
    1
    2
    3
    4
    5
    6
    7

| 
    
    
    [
      {
        "json": {
    	  // Setting `json` to an object as expected
    	}
      }
    ]
      
  
---|---  
  
## Code doesn't return an object#

This error may occur when your Code node doesn't return anything or if it returns an unexpected result.

To resolve this, ensure that your Code node returns the [expected data structure](../../../../../data/data-structure/):
    
    
    1
    2
    3
    4
    5
    6
    7

| 
    
    
    [
      {
        "json": {
    	  // your data goes here
    	}
      }
    ]
      
  
---|---  
  
This error may also occur if the code you provided returns `'undefined'` instead of the expected result. In that case, ensure that the data you are referencing in your Code node exists in each execution and that it has the structure your code expects.

## 'import' and 'export' may only appear at the top level#

This error occurs if you try to use `import` or `export` in the Code node. These aren't supported by n8n's JavaScript sandbox. Instead, use the `require` function to load modules.

To resolve this issue, try changing your `import` statements to use `require`:
    
    
    1
    2
    3
    4

| 
    
    
    // Original code:
    // import express from "express";
    // New code:
    const express = require("express");
      
  
---|---  
  
## Cannot find module '<module>'#

This error occurs if you try to use `require` in the Code node and n8n can't find the module.

Only for self-hosted

n8n doesn't support importing modules in the [Cloud](../../../../../manage-cloud/overview/) version.

If you're [self-hosting](../../../../../hosting/) n8n, follow these steps:

  * Install the module into your n8n environment.
    * If you are running n8n with [npm](../../../../../hosting/installation/npm/), install the module in the same environment as n8n.
    * If you are running n8n with [Docker](../../../../../hosting/installation/docker/), you need to extend the official n8n image with a [custom image](https://docs.docker.com/build/building/base-images/) that includes your module.
  * Set the `NODE_FUNCTION_ALLOW_BUILTIN` and `NODE_FUNCTION_ALLOW_EXTERNAL` [environment variables](../../../../../hosting/configuration/configuration-examples/modules-in-code-node/) to allow importing modules.

## Using global variables#

Sometimes you may wish to set and retrieve simple global data related to a workflow across and within executions. For example, you may wish to include the date of the previous report when compiling a report with a list of project updates.

To set, update, and retrieve data directly to a workflow, use the [static data](../../../../../code/cookbook/builtin/get-workflow-static-data/) functions within your code. You can manage data either globally or tied to specific nodes.

Use Remove Duplicates when possible

If you're interested in using variables to avoid processing the same data items more than once, consider using the [Remove Duplicates node](../../n8n-nodes-base.removeduplicates/) instead. The Remove Duplicates node can save information across executions to avoid processing the same items multiple times.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top