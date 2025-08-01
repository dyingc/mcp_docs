# GraphQL | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/core-nodes/n8n-nodes-base.graphql.md "Edit this page")

# GraphQL#

[GraphQL](https://graphql.org/) is an open-source data query and manipulation language for APIs, and a runtime for fulfilling queries with existing data. Use the GraphQL node to query a GraphQL endpoint.

## Node parameters#

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](../../../../advanced-ai/examples/using-the-fromai-function/).

### Authentication#

Select the type of authentication to use.

If you select anything other than **None** , the **Credential for** parameter appears for you to select an existing or create a new authentication credential for that authentication type.

### HTTP Request Method#

Select the underlying HTTP Request method the node should use. Choose from:

  * **GET**
  * **POST** : If you select this method, you'll also need to select the **Request Format** the node should use for the query payload. Choose from:
    * **GraphQL (Raw)**
    * **JSON**

### Endpoint#

Enter the GraphQL Endpoint you'd like to hit.

### Ignore SSL Issues#

When you turn on this control, n8n ignores SSL certificate validation failure.

### Query#

Enter the GraphQL query you want to execute.

Refer to Related Resources for information on writing your query.

### Response Format#

Select the format you'd like to receive query results in. Choose between:

  * **JSON**
  * **String** : If you select this format, enter a **Response Data Property Name** to define the property the string is written to.

## Headers#

Enter any **Headers** you want to pass as part of the query as **Name** / **Value** pairs.

## Templates and examples#

**Get top 5 products on Product Hunt every hour**

by Harshil Agrawal

[View template details](https://n8n.io/workflows/1298-get-top-5-products-on-product-hunt-every-hour/)

**API queries data from GraphQL**

by Jan Oberhauser

[View template details](https://n8n.io/workflows/216-api-queries-data-from-graphql/)

**Sentiment Analysis Tracking on Support Issues with Linear and Slack**

by Jimleuk

[View template details](https://n8n.io/workflows/2647-sentiment-analysis-tracking-on-support-issues-with-linear-and-slack/)

[Browse GraphQL integration templates](https://n8n.io/integrations/graphql/), or [search all templates](https://n8n.io/workflows/)

## Related resources#

To use the GraphQL node, you need to understand GraphQL query language. GraphQL have their own [Introduction to GraphQL](https://graphql.org/learn/) tutorial.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top