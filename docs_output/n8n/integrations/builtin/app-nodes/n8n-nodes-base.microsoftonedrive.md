# Microsoft OneDrive node documentation | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.microsoftonedrive.md "Edit this page")

# Microsoft OneDrive node#

Use the Microsoft OneDrive node to automate work in Microsoft OneDrive, and integrate Microsoft OneDrive with other applications. n8n has built-in support for a wide range of Microsoft OneDrive features, including creating, updating, deleting, and getting files, and folders.

On this page, you'll find a list of operations the Microsoft OneDrive node supports and links to more resources.

Credentials

Refer to [Microsoft credentials](../../credentials/microsoft/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](../../../../advanced-ai/examples/using-the-fromai-function/).

## Operations#

  * File
    * Copy a file
    * Delete a file
    * Download a file
    * Get a file
    * Rename a file
    * Search a file
    * Share a file
    * Upload a file up to 4MB in size
  * Folder
    * Create a folder
    * Delete a folder
    * Get Children (get items inside a folder)
    * Rename a folder
    * Search a folder
    * Share a folder

## Templates and examples#

**Hacker News to Video Content**

by Alex Kim

[View template details](https://n8n.io/workflows/2557-hacker-news-to-video-content/)

**Working with Excel spreadsheet files (xls & xlsx)**

by n8n Team

[View template details](https://n8n.io/workflows/1826-working-with-excel-spreadsheet-files-xls-and-xlsx/)

**📂 Automatically Update Stock Portfolio from OneDrive to Excel**

by Louis

[View template details](https://n8n.io/workflows/2507-automatically-update-stock-portfolio-from-onedrive-to-excel/)

[Browse Microsoft OneDrive integration templates](https://n8n.io/integrations/microsoft-onedrive/), or [search all templates](https://n8n.io/workflows/)

## Related resources#

Refer to [Microsoft's OneDrive API documentation](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/) for more information about the service.

## Find the folder ID#

To perform operations on folders, you need to supply the ID. You can find this:

  * In the URL of the folder
  * By searching for it using the node. You need to do this if using MS 365 (where OneDrive uses SharePoint behind the scenes):
    1. Select **Resource** > **Folder**.
    2. Select **Operation** > **Search**.
    3. In **Query** , enter the folder name.
    4. Select **Execute step**. n8n runs the query and returns data about the folder, including an `id` field containing the folder ID.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top