# Manage your organization using the API | 🦜️🛠️ LangSmith

On this page

LangSmith's API supports programmatic access via API key to all of the actions available in the UI, with only a few exceptions that are noted below.

Recommended Reading

Before diving into this content, it might be helpful to read the following:

  * [Conceptual guide on organizations and workspaces](/administration/concepts)
  * [Organization setup how-to guild](/administration/how_to_guides/organization_management/set_up_organization)

note

There are a few limitations that will be lifted soon:

  * The LangSmith SDKs do not support these organization management actions yet.
  * [Service Keys](/administration/concepts#api-keys) don't have access to newly-added workspaces yet (we're adding support soon). We recommend using a PAT of an Organization Admin for now, which by default has the required permissions for these actions.

Some commonly-used endpoints and use cases are listed below. For a complete list of available endpoints, see the [API docs](https://api.smith.langchain.com/redoc).  
**The`X-Organization-Id` header should be present on all requests, and `X-Tenant-Id` header should be present on requests that are scoped to a particular workspace.**

## Workspaces​

  * [List workspaces](https://api.smith.langchain.com/redoc#tag/workspaces/operation/list_workspaces_api_v1_workspaces_get)
  * [Create workspace](https://api.smith.langchain.com/redoc#tag/workspaces/operation/create_workspace_api_v1_workspaces_post)
  * [Update workspace name](https://api.smith.langchain.com/redoc#tag/workspaces/operation/patch_workspace_api_v1_workspaces__workspace_id__patch)

## User management​

### RBAC​

  * [List roles](https://api.smith.langchain.com/redoc#tag/orgs/operation/list_organization_roles_api_v1_orgs_current_roles_get)
  * [List permissions](https://api.smith.langchain.com/redoc#tag/orgs/operation/update_organization_roles_api_v1_orgs_current_roles__role_id__patch)
  * [Create role](https://api.smith.langchain.com/redoc#tag/orgs/operation/create_organization_roles_api_v1_orgs_current_roles_post)
  * [Update role](https://api.smith.langchain.com/redoc#tag/orgs/operation/update_organization_roles_api_v1_orgs_current_roles__role_id__patch)

### Membership management​

`List roles` under RBAC should be used for retrieving role IDs of these operations.  
`List [organization|workspace] members` endpoints (below) response `"id"`s should be used as `identity_id` in these operations.

Organization level:

  * [List organization members](https://api.smith.langchain.com/redoc#tag/orgs/operation/get_current_org_members_api_v1_orgs_current_members_get)
  * [Invite a user to the organization and one or more workspaces](https://api.smith.langchain.com/redoc#tag/workspaces/operation/add_member_to_current_workspace_api_v1_workspaces_current_members_post) . This should be used when the user is not already a member in the organization.
  * [Update a user’s organization role](https://api.smith.langchain.com/redoc#tag/workspaces/operation/add_member_to_current_workspace_api_v1_workspaces_current_members_post)
  * [Remove someone from the organization](https://api.smith.langchain.com/redoc#tag/orgs/operation/remove_member_from_current_org_api_v1_orgs_current_members__identity_id__delete)

Workspace level:

  * [List workspace members](https://api.smith.langchain.com/redoc#tag/workspaces/operation/get_current_workspace_members_api_v1_workspaces_current_members_get)
  * [Add a member to a workspace that is already part of the organization](https://api.smith.langchain.com/redoc#tag/workspaces/operation/add_member_to_current_workspace_api_v1_workspaces_current_members_post)
  * [Update a user’s workspace role](https://api.smith.langchain.com/redoc#tag/workspaces/operation/add_member_to_current_workspace_api_v1_workspaces_current_members_post)
  * [Remove someone from a workspace](https://api.smith.langchain.com/redoc#tag/workspaces/operation/delete_current_workspace_member_api_v1_workspaces_current_members__identity_id__delete)

note

These params should be omitted: `read_only` (deprecated), `password` and `full_name` ([basic auth](/reference/authentication_authorization/authentication_methods) only)

## API Keys​

note

Use the `X-Tenant-Id` header to specify which workspace to target.  
If the header is not present, operations will default to the workspace the API key was initially created in.

  * [Create a service key](https://api.smith.langchain.com/redoc#tag/api-key/operation/generate_api_key_api_v1_api_key_post)
  * [Delete a service key](https://api.smith.langchain.com/redoc#tag/api-key/operation/delete_api_key_api_v1_api_key__api_key_id__delete)

## Security Settings​

note

"Shared resources" in this context refer to [public prompts](/prompt_engineering/how_to_guides/create_a_prompt#save-your-prompt), [shared runs](/observability/how_to_guides/share_trace), and [shared datasets](/evaluation/how_to_guides/share_dataset).

  * [Update organization sharing settings](https://api.smith.langchain.com/redoc#tag/orgs/operation/update_current_organization_info_api_v1_orgs_current_info_patch)
    * use `unshare_all` to unshare **ALL** shared resources in the organization - use `disable_public_sharing` to prevent future sharing of resources

## User-Only Endpoints​

These endpoints are user-scoped and require a logged-in user's JWT, so they should only be executed through the UI.

  * `/api-key/current` endpoints: these are related a user's PATs
  * `/sso/email-verification/send` (Cloud-only): this endpoint is related to [SAML SSO](/administration/how_to_guides/organization_management/set_up_saml_sso)

## Sample Code​

The sample code below goes through a few common workflows related to organization management.  
Make sure to make necessary replacements wherever `<replace_me>` is in the code.
    
    
    import os  
      
    import requests  
      
      
    def main():  
        api_key = os.environ["LANGSMITH_API_KEY"]  
        # LANGSMITH_ORGANIZATION_ID is not a standard environment variable in the SDK, just used for this example  
        organization_id = os.environ["LANGSMITH_ORGANIZATION_ID"]  
        base_url = os.environ.get("LANGSMITH_ENDPOINT") # or "https://api.smith.langchain.com". Update appropriately for self-hosted installations or the EU region  
        headers = {  
            "Content-Type": "application/json",  
            "X-API-Key": api_key,  
            "X-Organization-Id": organization_id,  
        }  
      
        session = requests.Session()  
        session.headers.update(headers)  
        workspaces_path = f"{base_url}/api/v1/workspaces"  
        orgs_path = f"{base_url}/api/v1/orgs/current"  
        api_keys_path = f"{base_url}/api/v1/api-key"  
      
        # Create a workspace  
        workspace_res = session.post(workspaces_path, json={"display_name": "My Workspace"})  
        workspace_res.raise_for_status()  
        workspace = workspace_res.json()  
        workspace_id = workspace["id"]  
      
        new_workspace_headers = {  
            "X-Tenant-Id": workspace_id,  
        }  
      
        # Grab roles - this includes both organization and workspace roles  
        roles_res = session.get(f"{orgs_path}/roles")  
        roles_res.raise_for_status()  
        roles = roles_res.json()  
        # system org roles are 'Organization Admin', 'Organization User'  
        # system workspace roles are 'Admin', 'Editor', 'Viewer'  
        org_roles_by_name = {role["display_name"]: role for role in roles if role["access_scope"] == "organization"}  
        ws_roles_by_name = {role["display_name"]: role for role in roles if role["access_scope"] == "workspace"}  
      
        # Invite a user to the org and the new workspace, as an Editor.  
        # workspace_role_id is only allowed if RBAC is enabled (an enterprise feature).  
        new_user_email = "<replace_me>"  
        new_user_res = session.post(  
            f"{orgs_path}/members",  
            json={  
                "email": new_user_email,  
                "role_id": org_roles_by_name["Organization User"]["id"],  
                "workspace_ids": [workspace_id],  
                "workspace_role_id": ws_roles_by_name["Editor"]["id"],  
            },  
        )  
        new_user_res.raise_for_status()  
      
        # Add a user that already exists in the org to the new workspace, as a Viewer.  
        # workspace_role_id is only allowed if RBAC is enabled (an enterprise feature).  
        existing_user_email = "<replace_me>"  
        org_members_res = session.get(f"{orgs_path}/members")  
        org_members_res.raise_for_status()  
        org_members = org_members_res.json()  
        existing_org_member = next(  
            (member for member in org_members["members"] if member["email"] == existing_user_email), None  
        )  
        existing_user_res = session.post(  
            f"{workspaces_path}/current/members",  
            json={  
                "user_id": existing_org_member["user_id"],  
                "workspace_ids": [workspace_id],  
                "workspace_role_id": ws_roles_by_name["Viewer"]["id"],  
            },  
            headers=new_workspace_headers,  
        )  
        existing_user_res.raise_for_status()  
      
        # List all members of the workspace  
        members_res = session.get(f"{workspaces_path}/current/members", headers=new_workspace_headers)  
        members_res.raise_for_status()  
        members = members_res.json()  
        workspace_member = next(  
            (member for member in members["members"] if member["email"] == existing_user_email), None  
        )  
      
        # Update the user's workspace role to Admin (enterprise-only)  
        existing_user_id = workspace_member["id"]  
        update_res = session.patch(  
            f"{workspaces_path}/current/members/{existing_user_id}",  
            json={"role_id": ws_roles_by_name["Admin"]["id"]},  
            headers=new_workspace_headers,  
        )  
        update_res.raise_for_status()  
      
        # Update the user's organization role to Organization Admin  
        update_res = session.patch(  
            f"{orgs_path}/members/{existing_org_member['id']}",  
            json={"role_id": org_roles_by_name["Organization Admin"]["id"]},  
        )  
        update_res.raise_for_status()  
      
        # Create a new Service key  
        api_key_res = session.post(  
            api_keys_path,  
            json={"description": "my key"},  
            headers=new_workspace_headers,  
        )  
        api_key_res.raise_for_status()  
        api_key_json = api_key_res.json()  
        api_key = api_key_json["key"]  
      
      
    if __name__ == "__main__":  
        main()  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Workspaces
  * User management
    * RBAC
    * Membership management
  * API Keys
  * Security Settings
  * User-Only Endpoints
  * Sample Code

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)