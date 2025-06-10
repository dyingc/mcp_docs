# Azure Storage node documentation | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.azurestorage.md "Edit this page")

# Azure Storage node#

The Azure Storage node has built-in support for a wide range of features, which includes creating, getting, and deleting blobs and containers. Use this node to automate work within the Azure Storage service or integrate it with other services in your workflow.

On this page, you'll find a list of operations the Azure Storage node supports, and links to more resources.

Credentials

You can find authentication information for this node [here](../../credentials/azurestorage/).

## Operations#

  * **Blob**
    * **Create blob** : Create a new blob or replace an existing one.
    * **Delete blob** : Delete an existing blob.
    * **Get blob** : Retrieve data for a specific blob.
    * **Get many blobs** : Retrieve a list of blobs.
  * **Container**
    * **Create container** : Create a new container.
    * **Delete container** : Delete an existing container.
    * **Get container** : Retrieve data for a specific container.
    * **Get many containers** : Retrieve a list of containers.

## Templates and examples#

**🤖 AI content generation for Auto Service 🚘 Automate your social media📲!**

by N8ner

[View template details](https://n8n.io/workflows/4600-ai-content-generation-for-auto-service-automate-your-social-media/)

**Build Your Own Counseling Chatbot on LINE to Support Mental Health Conversations**

by lin@davoy.tech

[View template details](https://n8n.io/workflows/2975-build-your-own-counseling-chatbot-on-line-to-support-mental-health-conversations/)

**CallForge - 05 - Gong.io Call Analysis with Azure AI & CRM Sync**

by Angel Menendez

[View template details](https://n8n.io/workflows/3035-callforge-05-gongio-call-analysis-with-azure-ai-and-crm-sync/)

[Browse Azure Storage integration templates](https://n8n.io/integrations/azure-storage/), or [search all templates](https://n8n.io/workflows/)

## Related resources#

Refer to [Microsoft's Azure Storage documentation](https://learn.microsoft.com/en-us/rest/api/storageservices/) for more information about the service.

## What to do if your operation isn't supported#

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node: 

  1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
  2. Select the service you want to connect to.
  3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top