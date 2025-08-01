# Reddit credentials | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/credentials/reddit.md "Edit this page")

# Reddit credentials#

You can use these credentials to authenticate the following nodes:

  * [Reddit](../../app-nodes/n8n-nodes-base.reddit/)

## Prerequisites#

Create a [Reddit](https://reddit.com/) account.

## Supported authentication methods#

  * OAuth2

## Related resources#

Refer to [Reddit's developer documentation](https://support.reddithelp.com/hc/en-us/articles/14945211791892-Developer-Platform-Accessing-Reddit-Data) for more information about the service.

## Using OAuth2#

To configure this credential, you'll need:

  * A **Client ID**
  * A **Client Secret**

Developer program

Reddit's developer program is in a closed beta. The instructions below are for regular Reddit users, not members of the developer platform.

Generate both by creating a [third-party app](https://www.reddit.com/prefs/apps). Visit the previous link or go to your **profile > Settings > Safety & Privacy > Manage third-party app authorization > are you a developer? create an app**.

Use these settings for your app:

  * Copy the **OAuth Callback URL** from n8n and use it as your app's **redirect uri**.
  * The app's client ID displays underneath your app name. Copy that and add it as your n8n **Client ID**.
  * Copy the app's **secret** and add it as your n8n **Client Secret**.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top