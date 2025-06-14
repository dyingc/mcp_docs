# Zoom credentials | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/credentials/zoom.md "Edit this page")

# Zoom credentials#

You can use these credentials to authenticate the following nodes:

  * [Zoom](../../app-nodes/n8n-nodes-base.zoom/)

## Prerequisites#

Create a [Zoom](https://zoom.us/) account. Your account must have one of the following permissions:

  * Account owner
  * Account admin
  * Zoom for developers role

## Supported authentication methods#

  * API JWT token
  * OAuth2

API JWT token deprecation

Zoom removed support for JWT access tokens in June 2023. You must use OAuth2 for all new credentials.

## Related resources#

Refer to [Zoom's API documentation](https://developers.zoom.us/docs/api/) for more information about the service.

## Using API JWT token#

This authentication method has been fully deprecated by Zoom. Don't create new credentials with it.

To configure this credential, you'll need:

  * A **JWT token** : To create a JWT token, create a new JWT app in the [Zoom App Marketplace](https://marketplace.zoom.us/).

## Using OAuth2#

To configure this credential, you'll need:

  * A **Client ID** : Generated when you create an OAuth app on the Zoom App Marketplace.
  * A **Client Secret** : Generated when you create an OAuth app.

To generate your **Client ID** and **Client Secret** , [create an OAuth app](https://developers.zoom.us/docs/integrations/create/).

Use these settings for your OAuth app:

  * Select **User-managed app** for **Select how the app is managed**.
  * Copy the **OAuth Callback URL** from n8n and enter it as an **OAuth Redirect URL** in Zoom.
  * If your n8n credential displays a **Whitelist URL** , also enter that URL as a an **OAuth Redirect URL**.
  * Enter **Scopes** for the scopes you plan to use. For all functionality in the [Zoom](../../app-nodes/n8n-nodes-base.zoom/) node, select:
    * `meeting:read`
    * `meeting:write`
    * Refer to [OAuth scopes | Meeting scopes](https://developers.zoom.us/docs/integrations/oauth-scopes/#meeting-scopes) for more information on meeting scopes.
  * Copy the **Client ID** and **Client Secret** provided in the Zoom app and enter them in your n8n credential.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top