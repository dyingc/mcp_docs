# (node-name).all | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/cookbook/builtin/all.md "Edit this page")

# `("<node-name>").all(branchIndex?: number, runIndex?: number)`#

This gives access to all the items of the current or parent nodes. If you don't supply any parameters, it returns all the items of the current node.

## Getting items#

JavaScriptPython
    
    
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

| 
    
    
    // Returns all the items of the given node and current run
    let allItems = $("<node-name>").all();
    
    // Returns all items the node "IF" outputs (index: 0 which is Output "true" of its most recent run)
    let allItems = $("IF").all();
    
    // Returns all items the node "IF" outputs (index: 0 which is Output "true" of the same run as current node)
    let allItems = $("IF").all(0, $runIndex);
    
    // Returns all items the node "IF" outputs (index: 1 which is Output "false" of run 0 which is the first run)
    let allItems = $("IF").all(1, 0);
      
  
---|---  
      
    
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

| 
    
    
    # Returns all the items of the given node and current run
    allItems = _("<node-name>").all();
    
    # Returns all items the node "IF" outputs (index: 0 which is Output "true" of its most recent run)
    allItems = _("IF").all();
    
    # Returns all items the node "IF" outputs (index: 0 which is Output "true" of the same run as current node)
    allItems = _("IF").all(0, _runIndex);
    
    # Returns all items the node "IF" outputs (index: 1 which is Output "false" of run 0 which is the first run)
    allItems = _("IF").all(1, 0);
      
  
---|---  
  
## Accessing item data#

Get all items output by a previous node, and log out the data they contain:

JavaScriptPython
    
    
    1
    2
    3
    4

| 
    
    
    previousNodeData = $("<node-name>").all();
    for(let i=0; i<previousNodeData.length; i++) {
    	console.log(previousNodeData[i].json);
    }
      
  
---|---  
      
    
    1
    2
    3
    4
    5
    6

| 
    
    
    previousNodeData = _("<node-name>").all();
    for item in previousNodeData:
    	# item is of type <class 'pyodide.ffi.JsProxy'>
    	# You need to convert it to a Dict
    	itemDict = item.json.to_py()
    	print(itemDict)
      
  
---|---  
  
Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top