# Gmail node common issues | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues.md "Edit this page")

# Gmail node common issues#

Here are some common errors and issues with the [Gmail node](../) and steps to resolve or troubleshoot them.

## Remove the n8n attribution from sent messages#

If you're using the node to [send a message](../message-operations/#send-a-message) or [reply to a message](../message-operations/#reply-to-a-message), the node appends this statement to the end of the email:

> This email was sent automatically with n8n

To remove this attribution:

  1. In the node's **Options** section, select **Add option**.
  2. Select **Append n8n attribution**.
  3. Turn the toggle off.

Refer to [Send options](../message-operations/#send-options) and [Reply options](../message-operations/#reply-options) for more information.

## Forbidden - perhaps check your credentials#

This error displays next to certain dropdowns in the node, like the **Label Names or IDs** dropdown. The full text looks something like this:
    
    
    1

| 
    
    
    There was a problem loading the parameter options from server: "Forbidden - perhaps check your credentials?"
      
  
---|---  
  
The error most often displays when you're using a Google Service Account as the credential and the credential doesn't have **Impersonate a User** turned on.

Refer to [Google Service Account: Finish your n8n credential](../../../credentials/google/service-account/#finish-your-n8n-credential) for more information.

## 401 unauthorized error#

The full text of the error looks like this:
    
    
    1

| 
    
    
    401 - {"error":"unauthorized_client","error_description":"Client is unauthorized to retrieve access tokens using this method, or client not authorized for any of the scopes requested."}
      
  
---|---  
  
This error occurs when there's an issue with the credential you're using and its scopes or permissions.

To resolve:

  1. For [OAuth2](../../../credentials/google/oauth-single-service/) credentials, make sure you've enabled the Gmail API in **APIs & Services > Library**. Refer to [Google OAuth2 Single Service - Enable APIs](../../../credentials/google/oauth-single-service/#enable-apis) for more information.
  2. For [Service Account](../../../credentials/google/service-account/) credentials:
     1. [Enable domain-wide delegation](../../../credentials/google/service-account/#enable-domain-wide-delegation).
     2. Make sure you add the Gmail API as part of the domain-wide delegation configuration.

## Bad request - please check your parameters#

This error most often occurs if you enter a Message ID, Thread ID, or Label ID that doesn't exist.

Try a **Get** operation with the ID to confirm it exists.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top