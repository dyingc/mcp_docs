# Gmail Trigger node common issues | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/common-issues.md "Edit this page")

# Gmail Trigger node common issues#

Here are some common errors and issues with the [Gmail Trigger node](../) and steps to resolve or troubleshoot them.

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

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top