# User management | 🦜️🛠️ LangSmith

On this page

note

This guide assumes you have read the [admin guide](/administration/concepts) and [organization setup guide](/administration/how_to_guides/organization_management/set_up_organization).

LangSmith offers additional customization features for user management using feature flags.

## Features​

### Workspace level invites to an organization​

The default behavior in LangSmith requires a user to be an Organization Admin in order to invite new users to an organization, as this operation can increase cost by adding seats. For self-hosted customers that would like to delegate this responsibility to workspace Admins, a feature flag may be set that enables workspace Admins to invite new users to the organization as well as their specific workspace **at the workspace level**.

Once this feature is enabled via the configuration option below, workspace Admins may add new users in the `Workspace members` tab under `Settings` > `Workspaces`. Both of the following cases are supported when inviting at the workspace level, while the organization level invite functions the same as before.

  1. Invite users who are NOT already active in the organization: this will add the users as pending to the organization and specific workspace
  2. Invite users who ARE already active in the organization: adds the users directly to the workspace as an active member (no pending state).

Admins may invite users for both cases at the same time.

#### Configuration​

  * Helm
  * Docker

    
    
    config:  
      workspaceScopeOrgInvitesEnabled: true  
    
    
    
    # In your .env file  
    WORKSPACE_SCOPE_ORG_INVITES_ENABLED="true"  
    

### Disabling Organization Creating​

By default, any user can create an organization in LangSmith. For self-hosted customers, an admin may want to restrict this ability after setting up initial organizations. This feature flag allows an admin to disable the ability for users to create new organizations.

#### Configuration​

  * Helm
  * Docker

    
    
    config:  
      orgCreationDisabled: true  
    
    
    
    # In your .env file  
    ORG_CREATION_DISABLED="true"  
    

### Disabling Personal Organizations​

By default, any user who logs in to LangSmith will have a personal organization created for them. For self-hosted customers, an admin may want to restrict this ability. This feature flag allows an admin to disable the ability for users to create personal organizations.

#### Configuration​

  * Helm
  * Docker

    
    
    config:  
      personalOrgsDisabled: true  
    
    
    
    # In your .env file  
    PERSONAL_ORGS_DISABLED="true"  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Features
    * Workspace level invites to an organization
    * Disabling Organization Creating
    * Disabling Personal Organizations

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)