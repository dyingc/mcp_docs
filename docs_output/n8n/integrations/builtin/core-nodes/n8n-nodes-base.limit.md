# Limit | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/core-nodes/n8n-nodes-base.limit.md "Edit this page")

# Limit#

Use the Limit node to remove items beyond a defined maximum number. You can choose whether n8n takes the items from the beginning or end of the input data.

## Node parameters#

Configure this node using the following parameters.

### Max Items#

Enter the maximum number of items that n8n should keep. If the input data contains more than this value, n8n removes the items.

### Keep#

If the node has to remove items, select where it keeps the input items from:

  * **First Items** : Keeps the **Max Items** number of items from the beginning of the input data.
  * **Last Items** : Keeps the **Max Items** number of items from the end of the input data.

## Templates and examples#

**Scrape and summarize webpages with AI**

by n8n Team

[View template details](https://n8n.io/workflows/1951-scrape-and-summarize-webpages-with-ai/)

**Chat with OpenAI Assistant (by adding a memory)**

by David Roberts

[View template details](https://n8n.io/workflows/2098-chat-with-openai-assistant-by-adding-a-memory/)

**Hacker News to Video Content**

by Alex Kim

[View template details](https://n8n.io/workflows/2557-hacker-news-to-video-content/)

[Browse Limit integration templates](https://n8n.io/integrations/limit/), or [search all templates](https://n8n.io/workflows/)

## Related resources#

Learn more about [data structure and data flow](../../../../data/) in n8n workflows.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top