# Onboard Users for AI Exploration | liteLLM

On this page

v1.73.0 introduces the ability to assign new users to Default Teams. This makes it much easier to enable experimentation with LLMs within your company, by allowing users to sign in and create $10 keys for AI exploration.

### 1\. Create a team​

Create a team called `internal exploration` with:

  * `models`: access to specific models (e.g. `gpt-4o`, `claude-3-5-sonnet`)
  * `max budget`: The team max budget will ensure spend for the entire team never exceeds a certain amount.
  * `reset budget`: Set this to monthly. LiteLLM will reset the budget at the start of each month.
  * `team member max budget`: The team member max budget will ensure spend for an individual team member never exceeds a certain amount.

### 2\. Update team member permissions​

Click on the team you just created, and update the team member permissions under `Member Permissions`.

This will allow all team members, to create keys.

### 3\. Set team as default team​

Go to `Internal Users` -> `Default User Settings` and set the default team to the team you just created.

Let's also set the default models to `no-default-models`. This means a user can only create keys within a team.

### 4\. Test it!​

Let's create a new user and test it out.

#### a. Create a new user​

Create a new user with email `test_default_team_user@xyz.com`.

Once you click `Create User`, you will get an invitation link, save it for later.

#### b. Verify user is added to the team​

Click on the created user, and verify they are added to the team.

We can see the user is added to the team, and has no default models.

#### c. Login as user​

Now use the invitation link from 4a. to login as the user.

#### d. Verify you can't create keys without specifying a team​

You should see a message saying you need to select a team.

#### e. Verify you can create a key when specifying a team​

Success!

You should now see the created key

  * 1\. Create a team
  * 2\. Update team member permissions
  * 3\. Set team as default team
  * 4\. Test it!