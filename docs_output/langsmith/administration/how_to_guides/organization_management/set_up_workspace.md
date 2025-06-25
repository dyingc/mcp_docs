# Set up a workspace | 🦜️🛠️ LangSmith

On this page

Recommended Reading

Before diving into this content, it might be helpful to read the following:

  * [Conceptual guide on organizations and workspaces](/administration/concepts)

When you log in for the first time, a default [workspace](/administration/concepts#workspaces) will be created for you automatically in your [personal organization](/administration/how_to_guides/organization_management/set_up_organization#personal-vs-shared-organizations).  
Workspaces are often used to separate resources between different teams or business units, ensuring clear trust boundaries between them. Within each workspace, Role-Based Access Control (RBAC) is implemented to manage permissions and access levels, ensuring that users only have access to the resources and settings necessary for their role. Most LangSmith activity happens in the context of a workspace, each of which has its own settings and access controls.

To organize resources _within_ a workspace, you can use [resource tags](/administration/how_to_guides/organization_management/set_up_resource_tags).

## Create a workspace​

To create a new workspace, head to the [Settings page](https://smith.langchain.com/settings) `Workspaces` tab in your shared organization and click **Add Workspace**. Once your workspace has been created, you can manage its members and other configuration by selecting it on this page.

![](/assets/images/create_workspace-8acf7883bef46bd556eea8c5a83584dc.png)

note

Different plans have different limits placed on the number of workspaces that can be used in an organization. Please see the [pricing page](https://www.langchain.com/pricing-langsmith) for more information.

## Manage users​

info

Only workspace `Admins` may manage workspace membership and, if RBAC is enabled, change a user's workspace role.

For users that are already members of an organization, a workspace admin may add them to a workspace in the `Workspace members` tab under [workspace settings page](https://smith.langchain.com/settings/workspaces).  
Users may also be invited directly to one or more workspaces when they are [invited to an organization](/administration/how_to_guides/organization_management/set_up_organization#manage-users).

## Configure workspace settings​

Workspace configuration exists in the [workspace settings page](https://smith.langchain.com/settings/workspaces) tab. Select the workspace to configure and then the desired configuration sub-tab. The example below shows the `API keys`, and other configuration options including secrets, models, and shared URLs are available here as well.

![](/assets/images/workspace_settings-0dc7f4a80b3620ca403d04d97978b513.png)

## Delete a workspace​

warning

Deleting a workspace will permanently delete the workspace and all associated data. This action cannot be undone.

Workspaces can be deleted through the LangSmith UI or via [API](https://api.smith.langchain.com/redoc?#tag/workspaces/operation/delete_workspace_api_v1_workspaces__workspace_id__delete). You must be a workspace admin in order to delete a workspace.

#### Deleting a workspace via the UI​

  1. Navigate to **Settings**.
  2. Select the workspace you want to delete.
  3. Click **Delete** in the top-right corner of the screen.

![Delete a workspace](/assets/images/delete_workspace-cd1edc05b2f81b1c18c3613157c7d194.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Create a workspace
  * Manage users
  * Configure workspace settings
  * Delete a workspace

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)