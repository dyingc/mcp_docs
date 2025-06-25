# Prompt Tags | 🦜️🛠️ LangSmith

On this page

Prompt tags are labels that attached to specific commits in your prompt's version history. They help you mark significant versions and control which versions run in different environments. By referencing tags rather than commit IDs in your code, you can easily update which version is being used without modifying the code itself.

## Overview​

  * A tag is a named reference to a specific commit
  * Each tag points to exactly one commit at a time
  * Tags can be moved between commits
  * Common uses include marking commits for different environments (e.g., "production", "staging") or marking stable versions

## Managing Tags​

### Create a tag​

To create a tag, navigate to the commits tab of a prompt. Click on the tag icon next to the commit you want to tag. Click "New Tag" and enter the name of the tag.

![](/assets/images/commits_tab-6c39f66e5734451dbc7e614119a0e5c7.png) ![](/assets/images/create_new_prompt_tag-5c6a58ee5730d29b4b022cf011a2659c.png)

### Move a tag​

To point a tag to a different commit, click on the tag icon next to the destination commit, and select the tag you want to move. This will automatically update the tag to point to the new commit.

![](/assets/images/move_prompt_tag-62a99e58991405ba424653735eacf117.png)

## Delete a tag​

To delete a tag, click on the delete icon next to the tag you want to delete. Note that this will delete the tag altogether and it will no longer be associated with any commit.

## Using tags in code​

Tags provide a stable way to reference specific versions of your prompts in code. Instead of using commit hashes directly, you can reference tags which can be updated without changing your code.

See [managing prompts programatically](/prompt_engineering/how_to_guides/manage_prompts_programatically) for more information on how to use prompts in code.

Here is an example of pulling a prompt by tag in Python:
    
    
    prompt = client.pull_prompt("joke-generator:prod")  
      
    # If prod tag points to commit a1b2c3d4, this is equivalent to:  
    prompt = client.pull_prompt("joke-generator:a1b2c3d4")  
    

## Common use cases​

  1. **Environment-specific tags** : Use tags like "prod" or "staging" to mark versions for different environments. This makes it easy to switch between different versions without changing your code.
  2. **Version control** : Use tags to mark stable versions of your prompts (ex. v1, v2). This makes it easy to reference specific versions in your code and track changes over time.
  3. **Collaboration** : Use tags to mark versions ready for review. This makes it easy to share specific versions with collaborators and get feedback.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Overview
  * Managing Tags
    * Create a tag
    * Move a tag
  * Delete a tag
  * Using tags in code
  * Common use cases

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)