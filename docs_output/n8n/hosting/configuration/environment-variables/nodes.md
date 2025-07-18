# Nodes environment variables | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/environment-variables/nodes.md "Edit this page")

# Nodes environment variables#

File-based configuration

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](../../configuration-methods/#keeping-sensitive-data-in-separate-files) for more details.

This page lists the environment variables configuration options for managing [nodes](../../../../glossary/#node-n8n) in n8n, including specifying which nodes to load or exclude, importing built-in or external modules in the Code node, and enabling community nodes.

Variable | Type | Default | Description  
---|---|---|---  
`NODES_INCLUDE` | Array of strings | - | Specify which nodes to load.  
`NODES_EXCLUDE` | Array of strings | - | Specify which nodes not to load. For example, to block nodes that can be a security risk if users aren't trustworthy: `NODES_EXCLUDE: "[\"n8n-nodes-base.executeCommand\", \"n8n-nodes-base.readWriteFile\"]"`  
`NODE_FUNCTION_ALLOW_BUILTIN` | String | - | Permit users to import specific built-in modules in the Code node. Use * to allow all. n8n disables importing modules by default.  
`NODE_FUNCTION_ALLOW_EXTERNAL` | String | - | Permit users to import specific external modules (from `n8n/node_modules`) in the Code node. n8n disables importing modules by default.  
`NODES_ERROR_TRIGGER_TYPE` | String | `n8n-nodes-base.errorTrigger` | Specify which node type to use as Error Trigger.  
`N8N_CUSTOM_EXTENSIONS` | String | - | Specify the path to directories containing your custom nodes.  
`N8N_COMMUNITY_PACKAGES_ENABLED` | Boolean | `true` | Enables (true) or disables (false) the functionality to install and load community nodes. If set to false, neither verified nor unverified community packages will be available, regardless of their individual settings.  
`N8N_COMMUNITY_PACKAGES_REGISTRY` | String | `https://registry.npmjs.org` | NPM registry URL to pull community packages from (license required).  
`N8N_VERIFIED_PACKAGES_ENABLED` | Boolean | `true` | When `N8N_COMMUNITY_PACKAGES_ENABLED` is true, this variable controls whether to show verified community nodes in the nodes panel for installation and use (true) or to hide them (false).  
`N8N_UNVERIFIED_PACKAGES_ENABLED` | Boolean | `true` | When `N8N_COMMUNITY_PACKAGES_ENABLED` is true, this variable controls whether to enable the installation and use of unverified community nodes from an NPM registry (true) or not (false).  
`N8N_COMMUNITY_PACKAGES_PREVENT_LOADING` | Boolean | `false` | Prevents (true) or allows (false) loading installed community nodes on instance startup. Use this if a faulty node prevents the instance from starting.  
Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top