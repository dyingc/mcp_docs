# Data pinning | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/data-pinning.md "Edit this page")

# Data pinning#

You can 'pin' data during workflow development. Data pinning means saving the output data of a node, and using the saved data instead of fetching fresh data in future workflow executions. 

You can use this when working with data from external sources to avoid having to repeat requests to the external system. This can save time and resources:

  * If your workflow relies on an external system to trigger it, such as a webhook call, being able to pin data means you don't need to use the external system every time you test the workflow.
  * If the external resource has data or usage limits, pinning data during tests avoids consuming your resource limits.
  * You can fetch and pin the data you want to test, then have confidence that the data is consistent in all your workflow tests.

You can only pin data for nodes that have a single main output ("error" outputs don't count for this purpose).

For development only

Data pinning isn't available for production workflow executions. It's a feature to help test workflows during development.

## Pin data#

To pin data in a node:

  1. Run the node to load data.
  2. In the **OUTPUT** view, select **Pin data** ![Pin data icon](../../_images/data/data-pinning/data-pinning-button.png). When data pinning is active, the button is disabled and a "This data is pinned" banner is displayed in the **OUTPUT** view.

Nodes that output binary data

You can't pin data if the output data includes binary data.

## Unpin data#

When data pinning is active, a banner appears at the top of the node's output panel indicating that n8n has pinned the data. To unpin data and fetch fresh data on the next execution, select the **Unpin** link in the banner.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top