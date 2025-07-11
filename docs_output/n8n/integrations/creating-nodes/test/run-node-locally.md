# Run your node locally | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/creating-nodes/test/run-node-locally.md "Edit this page")

# Run your node locally#

You can test your node as you build it by running it in a local n8n instance.

  1. Install n8n using npm: 
         
         1

| 
         
         npm install n8n -g
           
  
---|---  
  
  2. When you are ready to test your node, publish it locally: 
         
         1
         2
         3

| 
         
         # In your node directory
         npm run build
         npm link
           
  
---|---  
  
  3. Install the node into your local n8n instance: 
         
         1
         2
         3

| 
         
         # In the nodes directory within your n8n installation
         # node-package-name is the name from the package.json
         npm link <node-package-name>
           
  
---|---  
  
Check your directory

Make sure you run `npm link <node-name>` in the nodes directory within your n8n installation. This can be: 

     * `~/.n8n/custom/`
     * `~/.n8n/<your-custom-name>`: if your n8n installation set a different name using `N8N_CUSTOM_EXTENSIONS`.

  4. Start n8n: 
         
         1

| 
         
         n8n start
           
  
---|---  
  
  5. Open n8n in your browser. You should see your nodes when you search for them in the nodes panel.

Node names

Make sure you search using the node name, not the package name. For example, if your npm package name is `n8n-nodes-weather-nodes`, and the package contains nodes named `rain`, `sun`, `snow`, you should search for `rain`, not `weather-nodes`. 

### Troubleshooting#

  * There's no `custom` directory in `~/.n8n` local installation.

You have to create `custom` directory manually and run `npm init`
    
    
    1
    2
    3
    4

| 
    
    
    # In ~/.n8n directory run
    mkdir custom 
    cd custom 
    npm init
      
  
---|---  
  
Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top