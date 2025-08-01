# Internal User Self-Serve | liteLLM

On this page

## Allow users to create their own keys on [Proxy UI](/docs/proxy/ui).​

  1. Add user with permissions to a team on proxy

  * UI
  * API

Go to `Internal Users` -> `+New User`

Create a new Internal User on LiteLLM and assign them the role `internal_user`.
    
    
    curl -X POST '<PROXY_BASE_URL>/user/new' \  
    -H 'Authorization: Bearer <PROXY_MASTER_KEY>' \  
    -H 'Content-Type: application/json' \  
    -D '{  
        "user_email": "krrishdholakia@gmail.com",  
        "user_role": "internal_user" # 👈 THIS ALLOWS USER TO CREATE/VIEW/DELETE THEIR OWN KEYS + SEE THEIR SPEND  
    }'  
    

Expected Response
    
    
    {  
        "user_id": "e9d45c7c-b20b-4ff8-ae76-3f479a7b1d7d", 👈 USE IN STEP 2  
        "user_email": "<YOUR_USERS_EMAIL>",  
        "user_role": "internal_user",  
        ...  
    }  
    

Here's the available UI roles for a LiteLLM Internal User:

Admin Roles:

  * `proxy_admin`: admin over the platform
  * `proxy_admin_viewer`: can login, view all keys, view all spend. **Cannot** create/delete keys, add new users.

Internal User Roles:

  * `internal_user`: can login, view/create/delete their own keys, view their spend. **Cannot** add new users.
  * `internal_user_viewer`: can login, view their own keys, view their own spend. **Cannot** create/delete keys, add new users.

  2. Share invitation link with user

  * UI
  * API

Copy the invitation link with the user
    
    
    curl -X POST '<PROXY_BASE_URL>/invitation/new' \  
    -H 'Authorization: Bearer <PROXY_MASTER_KEY>' \  
    -H 'Content-Type: application/json' \  
    -D '{  
        "user_id": "e9d45c7c-b20b..." # 👈 USER ID FROM STEP 1  
    }'  
    

Expected Response
    
    
    {  
        "id": "a2f0918f-43b0-4770-a664-96ddd192966e",  
        "user_id": "e9d45c7c-b20b..",  
        "is_accepted": false,  
        "accepted_at": null,  
        "expires_at": "2024-06-13T00:02:16.454000Z", # 👈 VALID FOR 7d  
        "created_at": "2024-06-06T00:02:16.454000Z",  
        "created_by": "116544810872468347480",  
        "updated_at": "2024-06-06T00:02:16.454000Z",  
        "updated_by": "116544810872468347480"  
    }  
    

Invitation Link:
    
    
    http://0.0.0.0:4000/ui/onboarding?id=a2f0918f-43b0-4770-a664-96ddd192966e  
      
    # <YOUR_PROXY_BASE_URL>/ui/onboarding?id=<id>  
    

info

Use [Email Notifications](/docs/proxy/email) to email users onboarding links

  3. User logs in via email + password auth

info

LiteLLM Enterprise: Enable [SSO login](/docs/proxy/ui#setup-ssoauth-for-ui)

  4. User can now create their own keys

## Allow users to View Usage, Caching Analytics​

  1. Go to Internal Users -> +Invite User

Set their role to `Admin Viewer` \- this means they can only view usage, caching analytics

  

  2. Share invitation link with user

  

  3. User logs in via email + password auth

  

  4. User can now view Usage, Caching Analytics

## Available Roles​

Here's the available UI roles for a LiteLLM Internal User:

**Admin Roles:**

  * `proxy_admin`: admin over the platform
  * `proxy_admin_viewer`: can login, view all keys, view all spend. **Cannot** create/delete keys, add new users.

**Internal User Roles:**

  * `internal_user`: can login, view/create/delete their own keys, view their spend. **Cannot** add new users.
  * `internal_user_viewer`: can login, view their own keys, view their own spend. **Cannot** create/delete keys, add new users.

**Team Roles:**

  * `admin`: can add new members to the team, can control Team Permissions, can add team-only models (useful for onboarding a team's finetuned models).
  * `user`: can login, view their own keys, view their own spend. **Cannot** create/delete keys (controllable via Team Permissions), add new users.

## Auto-add SSO users to teams​

This walks through setting up sso auto-add for **Okta, Google SSO**

### Okta, Google SSO​

  1. Specify the JWT field that contains the team ids, that the user belongs to.

    
    
    general_settings:  
      master_key: sk-1234  
      litellm_jwtauth:  
        team_ids_jwt_field: "groups" # 👈 CAN BE ANY FIELD  
    

This is assuming your SSO token looks like this. **If you need to inspect the JWT fields received from your SSO provider by LiteLLM, follow these instructionshere**
    
    
    {  
      ...,  
      "groups": ["team_id_1", "team_id_2"]  
    }  
    

  2. Create the teams on LiteLLM

    
    
    curl -X POST '<PROXY_BASE_URL>/team/new' \  
    -H 'Authorization: Bearer <PROXY_MASTER_KEY>' \  
    -H 'Content-Type: application/json' \  
    -D '{  
        "team_alias": "team_1",  
        "team_id": "team_id_1" # 👈 MUST BE THE SAME AS THE SSO GROUP ID  
    }'  
    

  3. Test the SSO flow

Here's a walkthrough of [how it works](https://www.loom.com/share/8959be458edf41fd85937452c29a33f3?sid=7ebd6d37-569a-4023-866e-e0cde67cb23e)

### Microsoft Entra ID SSO group assignment​

Follow this [tutorial for auto-adding sso users to teams with Microsoft Entra ID](https://docs.litellm.ai/docs/tutorials/msft_sso)

### Debugging SSO JWT fields​

If you need to inspect the JWT fields received from your SSO provider by LiteLLM, follow these instructions. This guide walks you through setting up a debug callback to view the JWT data during the SSO process.

  

  1. Add `/sso/debug/callback` as a redirect URL in your SSO provider

In your SSO provider's settings, add the following URL as a new redirect (callback) URL:

Redirect URL
    
    
    http://<proxy_base_url>/sso/debug/callback  
    

  2. Navigate to the debug login page on your browser

Navigate to the following URL on your browser:

URL to navigate to
         
         https://<proxy_base_url>/sso/debug/login  
         

This will initiate the standard SSO flow. You will be redirected to your SSO provider's login screen, and after successful authentication, you will be redirected back to LiteLLM's debug callback route.

  3. View the JWT fields

Once redirected, you should see a page called "SSO Debug Information". This page displays the JWT fields received from your SSO provider (as shown in the image above)

## Advanced​

### Setting custom logout URLs​

Set `PROXY_LOGOUT_URL` in your .env if you want users to get redirected to a specific URL when they click logout
    
    
    export PROXY_LOGOUT_URL="https://www.google.com"  
    

### Set max budget for internal users​

Automatically apply budget per internal user when they sign up. By default the table will be checked every 10 minutes, for users to reset. To modify this, [see this](/docs/proxy/users#reset-budgets)
    
    
    litellm_settings:  
      max_internal_user_budget: 10  
      internal_user_budget_duration: "1mo" # reset every month  
    

This sets a max budget of $10 USD for internal users when they sign up.

This budget only applies to personal keys created by that user - seen under `Default Team` on the UI.

This budget does not apply to keys created under non-default teams.

### Set max budget for teams​

[**Go Here**](/docs/proxy/team_budgets)

### Default Team​

  * UI
  * YAML

Go to `Internal Users` -> `Default User Settings` and set the default team to the team you just created.

Let's also set the default models to `no-default-models`. This means a user can only create keys within a team.

info

Team must be created before setting it as the default team.
    
    
    litellm_settings:  
      default_internal_user_params:    # Default Params used when a new user signs in Via SSO  
          user_role: "internal_user"     # one of "internal_user", "internal_user_viewer",   
          models: ["no-default-models"] # Optional[List[str]], optional): models to be used by the user  
          teams: # Optional[List[NewUserRequestTeam]], optional): teams to be used by the user  
            - team_id: "team_id_1" # Required[str]: team_id to be used by the user  
              user_role: "user" # Optional[str], optional): Default role in the team. Values: "user" or "admin". Defaults to "user"  
    

### Team Member Budgets​

Set a max budget for a team member.

You can do this when creating a new team, or by updating an existing team.

  * UI
  * API

    
    
    curl -X POST '<PROXY_BASE_URL>/team/new' \  
    -H 'Authorization: Bearer <PROXY_MASTER_KEY>' \  
    -H 'Content-Type: application/json' \  
    -D '{  
        "team_alias": "team_1",  
        "budget_duration": "10d",  
        "team_member_budget": 10  
    }'  
    

### Set default params for new teams​

When you connect litellm to your SSO provider, litellm can auto-create teams. Use this to set the default `models`, `max_budget`, `budget_duration` for these auto-created teams.

**How it works**

  1. When litellm fetches `groups` from your SSO provider, it will check if the corresponding group_id exists as a `team_id` in litellm.
  2. If the team_id does not exist, litellm will auto-create a team with the default params you've set.
  3. If the team_id already exist, litellm will not apply any settings on the team.

**Usage**

Default Params for new teams
    
    
    litellm_settings:  
      default_team_params:             # Default Params to apply when litellm auto creates a team from SSO IDP provider  
        max_budget: 100                # Optional[float], optional): $100 budget for the team  
        budget_duration: 30d           # Optional[str], optional): 30 days budget_duration for the team  
        models: ["gpt-3.5-turbo"]      # Optional[List[str]], optional): models to be used by the team  
    

### Restrict Users from creating personal keys​

This is useful if you only want users to create keys under a specific team.

This will also prevent users from using their session tokens on the test keys chat pane.

👉 [**See this**](/docs/proxy/virtual_keys#restricting-key-generation)

## **All Settings for Self Serve / SSO Flow**​

All Settings for Self Serve / SSO Flow
    
    
    litellm_settings:  
      max_internal_user_budget: 10        # max budget for internal users  
      internal_user_budget_duration: "1mo" # reset every month  
      
      default_internal_user_params:    # Default Params used when a new user signs in Via SSO  
        user_role: "internal_user"     # one of "internal_user", "internal_user_viewer", "proxy_admin", "proxy_admin_viewer". New SSO users not in litellm will be created as this user  
        max_budget: 100                # Optional[float], optional): $100 budget for a new SSO sign in user  
        budget_duration: 30d           # Optional[str], optional): 30 days budget_duration for a new SSO sign in user  
        models: ["gpt-3.5-turbo"]      # Optional[List[str]], optional): models to be used by a new SSO sign in user  
        teams: # Optional[List[NewUserRequestTeam]], optional): teams to be used by the user  
          - team_id: "team_id_1" # Required[str]: team_id to be used by the user  
            max_budget_in_team: 100 # Optional[float], optional): $100 budget for the team. Defaults to None.  
            user_role: "user" # Optional[str], optional): "user" or "admin". Defaults to "user"  
        
      default_team_params:             # Default Params to apply when litellm auto creates a team from SSO IDP provider  
        max_budget: 100                # Optional[float], optional): $100 budget for the team  
        budget_duration: 30d           # Optional[str], optional): 30 days budget_duration for the team  
        models: ["gpt-3.5-turbo"]      # Optional[List[str]], optional): models to be used by the team  
      
      
      upperbound_key_generate_params:    # Upperbound for /key/generate requests when self-serve flow is on  
        max_budget: 100 # Optional[float], optional): upperbound of $100, for all /key/generate requests  
        budget_duration: "10d" # Optional[str], optional): upperbound of 10 days for budget_duration values  
        duration: "30d" # Optional[str], optional): upperbound of 30 days for all /key/generate requests  
        max_parallel_requests: 1000 # (Optional[int], optional): Max number of requests that can be made in parallel. Defaults to None.  
        tpm_limit: 1000 #(Optional[int], optional): Tpm limit. Defaults to None.  
        rpm_limit: 1000 #(Optional[int], optional): Rpm limit. Defaults to None.  
      
      key_generation_settings: # Restricts who can generate keys. [Further docs](./virtual_keys.md#restricting-key-generation)  
        team_key_generation:  
          allowed_team_member_roles: ["admin"]  
        personal_key_generation: # maps to 'Default Team' on UI   
          allowed_user_roles: ["proxy_admin"]  
    

## Further Reading​

  * [Onboard Users for AI Exploration](/docs/tutorials/default_team_self_serve)

  * Allow users to create their own keys on Proxy UI.
  * Allow users to View Usage, Caching Analytics
  * Available Roles
  * Auto-add SSO users to teams
    * Okta, Google SSO
    * Microsoft Entra ID SSO group assignment
    * Debugging SSO JWT fields
  * Advanced
    * Setting custom logout URLs
    * Set max budget for internal users
    * Set max budget for teams
    * Default Team
    * Team Member Budgets
    * Set default params for new teams
    * Restrict Users from creating personal keys
  * **All Settings for Self Serve / SSO Flow**
  * Further Reading