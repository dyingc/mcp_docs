# SCIM with LiteLLM | liteLLM

On this page

✨ **Enterprise** : SCIM support requires a premium license.

Enables identity providers (Okta, Azure AD, OneLogin, etc.) to automate user and team (group) provisioning, updates, and deprovisioning on LiteLLM.

This tutorial will walk you through the steps to connect your IDP to LiteLLM SCIM Endpoints.

### Supported SSO Providers for SCIM​

Below is a list of supported SSO providers for connecting to LiteLLM SCIM Endpoints.

  * Microsoft Entra ID (Azure AD)
  * Okta
  * Google Workspace
  * OneLogin
  * Keycloak
  * Auth0

## 1\. Get your SCIM Tenant URL and Bearer Token​

On LiteLLM, navigate to the Settings > Admin Settings > SCIM. On this page you will create a SCIM Token, this allows your IDP to authenticate to litellm `/scim` endpoints.

## 2\. Connect your IDP to LiteLLM SCIM Endpoints​

On your IDP provider, navigate to your SSO application and select `Provisioning` > `New provisioning configuration`.

On this page, paste in your litellm scim tenant url and bearer token.

Once this is pasted in, click on `Test Connection` to ensure your IDP can authenticate to the LiteLLM SCIM endpoints.

## 3\. Test SCIM Connection​

### 3.1 Assign the group to your LiteLLM Enterprise App​

On your IDP Portal, navigate to `Enterprise Applications` > Select your litellm app

  
  

Once you've selected your litellm app, click on `Users and Groups` > `Add user/group`

  

Now select the group you created in step 1.1. And add it to the LiteLLM Enterprise App. At this point we have added `Production LLM Evals Group` to the LiteLLM Enterprise App. The next step is having LiteLLM automatically create the `Production LLM Evals Group` on the LiteLLM DB when a new user signs in.

### 3.2 Sign in to LiteLLM UI via SSO​

Sign into the LiteLLM UI via SSO. You should be redirected to the Entra ID SSO page. This SSO sign in flow will trigger LiteLLM to fetch the latest Groups and Members from Azure Entra ID.

### 3.3 Check the new team on LiteLLM UI​

On the LiteLLM UI, Navigate to `Teams`, You should see the new team `Production LLM Evals Group` auto-created on LiteLLM.

  * Supported SSO Providers for SCIM
  * 1\. Get your SCIM Tenant URL and Bearer Token
  * 2\. Connect your IDP to LiteLLM SCIM Endpoints
  * 3\. Test SCIM Connection
    * 3.1 Assign the group to your LiteLLM Enterprise App
    * 3.2 Sign in to LiteLLM UI via SSO
    * 3.3 Check the new team on LiteLLM UI