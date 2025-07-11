# Create and run | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/workflows/create.md "Edit this page")

# Create a workflow#

A [workflow](../../glossary/#workflow-n8n) is a collection of nodes connected together to automate a process. You build workflows on the [workflow canvas](../../glossary/#canvas-n8n).

## Create a workflow#

  1. Select the ![universal create resource icon](../../_images/common-icons/universal-resource-button.png) **button** in the upper-left corner of the side menu. Select workflow.
  2. If your n8n instance supports projects, you'll also need to choose whether to create the workflow inside your **personal space** or a specific **project** you have access to. If you're using the community version, you'll always create workflows inside your personal space.
  3. Get started by adding a trigger node: select **Add first step...**

Or:

  1. Select the ![universal create resource icon](../../_images/common-icons/universal-resource-button.png) **create** button in the upper-right corner from either the **Overview** page or a specific **project**. Select workflow.
  2. If you're doing this from the **Overview** page, you'll create the workflow inside your personal space. If you're doing this from inside a project, you'll create the workflow inside that specific project.
  3. Get started by adding a trigger node: select **Add first step...**

If it's your first time building a workflow, you may want to use the [quickstart guides](../../try-it-out/) to quickly try out n8n features.

## Run workflows manually#

You may need to run your workflow manually when building and testing, or if your workflow doesn't have a trigger node. 

To run manually, select **Test Workflow**.

## Run workflows automatically#

All new workflows are inactive by default.

You need to activate workflows that start with a trigger node or Webhook node so that they can run automatically. When a workflow is inactive, you must run it manually.

To activate or deactivate your workflow, open your workflow and toggle **Inactive** / **Active**.

Once a workflow is active, it runs whenever its trigger conditions are met.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top