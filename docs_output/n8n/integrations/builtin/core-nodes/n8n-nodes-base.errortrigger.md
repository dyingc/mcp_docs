# Error Trigger node documentation | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md "Edit this page")

# Error Trigger node#

You can use the Error Trigger node to create error workflows. When another linked workflow fails, this node gets details about the failed workflow and the errors, and runs the error workflow.

## Usage#

  1. Create a new workflow, with the Error Trigger as the first node. 
  2. Give the workflow a name, for example `Error Handler`. 
  3. Select **Save**.
  4. In the workflow where you want to use this error workflow:
     1. Select **Options** ![Options menu icon](../../../../_images/common-icons/three-dot-options-menu.png) > **Settings**.
     2. In **Error workflow** , select the workflow you just created. For example, if you used the name Error Handler, select **Error handler**.
     3. Select **Save**. Now, when this workflow errors, the related error workflow runs.

Note the following:

  * If a workflow uses the Error Trigger node, you don't have to activate the workflow.
  * If a workflow contains the Error Trigger node, by default, the workflow uses itself as the error workflow.
  * You can't test error workflows when running workflows manually. The Error Trigger only runs when an automatic workflow errors.

## Templates and examples#

[Browse Error Trigger integration templates](https://n8n.io/integrations/error-trigger/), or [search all templates](https://n8n.io/workflows/)

## Related resources#

You can use the [Stop And Error](../n8n-nodes-base.stopanderror/) node to send custom messages to the Error Trigger.

Read more about [Error workflows](../../../../flow-logic/error-handling/) in n8n workflows. 

## Error data#

The default error data received by the Error Trigger is:
    
    
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19

| 
    
    
    [
    	{
    		"execution": {
    			"id": "231",
    			"url": "https://n8n.example.com/execution/231",
    			"retryOf": "34",
    			"error": {
    				"message": "Example Error Message",
    				"stack": "Stacktrace"
    			},
    			"lastNodeExecuted": "Node With Error",
    			"mode": "manual"
    		},
    		"workflow": {
    			"id": "1",
    			"name": "Example Workflow"
    		}
    	}
    ]
      
  
---|---  
  
All information is always present, except:

  * `execution.id`: requires the execution to be saved in the database. Not present if the error is in the trigger node of the main workflow, as the workflow doesn't execute.
  * `execution.url`: requires the execution to be saved in the database. Not present if the error is in the trigger node of the main workflow, as the workflow doesn't execute.
  * `execution.retryOf`: only present when the execution is a retry of a failed execution.

If the error is caused by the trigger node of the main workflow, rather than a later stage, the data sent to the error workflow is different. There's less information in `execution{}` and more in `trigger{}`:
    
    
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22

| 
    
    
    {
      "trigger": {
        "error": {
          "context": {},
          "name": "WorkflowActivationError",
          "cause": {
            "message": "",
            "stack": ""
          },
          "timestamp": 1654609328787,
          "message": "",
          "node": {
            . . . 
          }
        },
        "mode": "trigger"
      },
      "workflow": {
        "id": "",
        "name": ""
      }
    }
      
  
---|---  
  
Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top