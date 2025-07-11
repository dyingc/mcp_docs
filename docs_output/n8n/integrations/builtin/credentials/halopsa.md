# HaloPSA credentials | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/credentials/halopsa.md "Edit this page")

# HaloPSA credentials#

You can use these credentials to authenticate the following nodes:

  * [HaloPSA](../../app-nodes/n8n-nodes-base.halopsa/)

## Prerequisites#

Create a [HaloPSA](https://halopsa.com/) account.

## Supported authentication methods#

  * API key

## Related resources#

Refer to [HaloPSA's API documentation](https://halopsa.com/apidoc/info) for more information about the service.

## Using API key#

To configure this credential, you'll need:

  * To select your **Hosting Type** :
    * **On Premise Solution** : Choose this option if you're hosting the Halo application on your own server
    * **Hosted Solution Of Halo** : Choose this option if your application is hosted by Halo. If this option is selected, you'll need to provide your **Tenant**.
  * The **HaloPSA Authorisation Server URL** : Your Authorisation Server URL is displayed within HaloPSA in **Configuration > Integrations > Halo API** in [API Details](https://halopsa.com/guides/article/?kbid=1737).
  * The **Resource Server** URL: Your Resource Server is displayed within HaloPSA in **Configuration > Integrations > Halo API** in [API Details](https://halopsa.com/guides/article/?kbid=1737).
  * A **Client ID** : Obtained by registering the application in the Halo API settings. Refer to [HaloPSA's Authorisation documentation](https://halopsa.com/apidoc/authorisation) for detailed instructions. n8n recommends using these settings:
    * Choose `Client Credentials` as your **Authentication Method**.
    * Use the `all` permission.
  * A **Client Secret** : Obtained by registering the application in the Halo API settings.
  * Your **Tenant** name: If **Hosted Solution of Halo** is selected as the **Hosting Type** , you must provide your tenant name. Your tenant name is displayed within HaloPSA in **Configuration > Integrations > Halo API** in [API Details](https://halopsa.com/guides/article/?kbid=1737).

HaloPSA uses both the application permissions and the agent's permissions to determine API access.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top