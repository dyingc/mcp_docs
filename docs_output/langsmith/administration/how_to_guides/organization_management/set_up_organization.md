# Set up an organization | 🦜️🛠️ LangSmith

On this page

Recommended Reading

Before diving into this content, it might be helpful to read the following:

  * [Conceptual guide on organizations and workspaces](/administration/concepts)

note

If you're interested in managing your organization and workspaces programmatically, see [this how-to guide](/administration/how_to_guides/organization_management/manage_organization_by_api).

## Create an organization​

When you log in for the first time, a personal organization will be created for you automatically. If you'd like to collaborate with others, you can create a separate organization and invite your team members to join.

To do this, open the Organizations drawer by clicking your profile icon in the bottom left and click **\+ New**. Shared organizations require a credit card before they can be used. You will need to [set up billing](/administration/how_to_guides/organization_management/set_up_billing) to proceed.

## Manage and navigate workspaces​

Once you've subscribed to a plan that allows for multiple users per organization, you can [set up workspaces](/administration/how_to_guides/organization_management/set_up_workspace) to collaborate more effectively and isolate LangSmith resources between different groups of users. To navigate between workspaces and access the resources within each workspace (trace projects, annotation queues, etc.), select the desired workspace from the picker in the top left:

![](/assets/images/select_workspace-b56235ac87fae4b49a46f161cfa5d887.png)

## Manage users​

Manage membership in your shared organization in the [Settings page](https://smith.langchain.com/settings) `Members and roles` tab. Here you can

  * Invite new users to your organization, selecting workspace membership and (if RBAC is enabled) workspace role
  * Edit a user's organization role
  * Remove users from your organization

![](/assets/images/organization_members_and_roles-52964d637277b463665a15c2cb3bb8c9.png)

Organizations on the Enterprise plan may set up custom workspace roles in the `Roles` tab here. See the [access control setup guide](/administration/how_to_guides/organization_management/set_up_access_control) for more details.

### Organization roles​

These are organization-scoped roles that are used to determine access to organization settings. The role selected also impacts workspace membership as described here:

  * `Organization Admin` grants full access to manage all organization configuration, users, billing, and workspaces. **Any`Organization Admin` has `Admin` access to all workspaces in an organization**
  * `Organization User` may read organization information but cannot execute any write actions at the organization level. **An`Organization User` can be added to a subset of workspaces and assigned workspace roles as usual (if RBAC is enabled), which specify permissions at the workspace level.**

info

The `Organization User` role is only available in organizations on plans with multiple workspaces. In organizations limited to a single workspace, all users are `Organization Admins`. Custom organization-scoped roles are not available yet.

See [this conceptual guide](/administration/concepts#organization-roles) for a full list of permissions associated with each role.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Create an organization
  * Manage and navigate workspaces
  * Manage users
    * Organization roles

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)