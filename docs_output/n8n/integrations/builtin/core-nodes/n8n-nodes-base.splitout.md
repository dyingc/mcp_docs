# Split Out | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/core-nodes/n8n-nodes-base.splitout.md "Edit this page")

# Split Out#

Use the Split Out node to separate a single data item containing a list into multiple items. For example, a list of customers, and you want to split them so that you have an item for each customer.

## Node parameters#

Configure this node using the following parameters.

### Field to Split Out#

Enter the field containing the list you want to separate out into individual items.

If you're working with binary data inputs, use `$binary` in an expression to set the field to split out.

### Include#

Select whether and how you want n8n to keep any other fields from the input data with each new individual item.

You can select:

  * **No Other Fields** : No other fields will be included.
  * **All Other Fields** : All other fields will be included.
  * **Selected Other Fields** : Only the selected fields will be included.
    * **Fields to Include** : Enter a comma separated list of the fields you want to include.

## Node options#

### Disable Dot Notation#

By default, n8n enables dot notation to reference child fields in the format `parent.child`. Use this option to disable dot notation (turned on) or to continue using dot (turned off).

### Destination Field Name#

Enter the field in the output where the split field contents should go.

### Include Binary#

Choose whether to include binary data from the input in the new output (turned on) or not (turned off).

## Templates and examples#

**Scrape and summarize webpages with AI**

by n8n Team

[View template details](https://n8n.io/workflows/1951-scrape-and-summarize-webpages-with-ai/)

**Scrape business emails from Google Maps without the use of any third party APIs**

by Akram Kadri

[View template details](https://n8n.io/workflows/2567-scrape-business-emails-from-google-maps-without-the-use-of-any-third-party-apis/)

**Automated Web Scraping: email a CSV, save to Google Sheets & Microsoft Excel**

by Mihai Farcas

[View template details](https://n8n.io/workflows/2275-automated-web-scraping-email-a-csv-save-to-google-sheets-and-microsoft-excel/)

[Browse Split Out integration templates](https://n8n.io/integrations/split-out/), or [search all templates](https://n8n.io/workflows/)

## Related resources#

Learn more about [data structure and data flow](../../../../data/) in n8n workflows.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top