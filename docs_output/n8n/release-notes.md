# Release notes | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/release-notes.md "Edit this page")

# Release notes#

New features and bug fixes for n8n.

You can also view the [Releases](https://github.com/n8n-io/n8n/releases) in the GitHub repository.

Latest and Next versions

n8n releases a new minor version most weeks. The `latest` version is for production use. `next` is the most recent release. You should treat `next` as a beta: it may be unstable. To report issues, use the [forum](https://community.n8n.io/c/questions/12).

Current `latest`: 1.95.3  
Current `next`: 1.97.1

## How to update n8n#

The steps to update your n8n depend on which n8n platform you use. Refer to the documentation for your n8n:

  * [Cloud](../manage-cloud/update-cloud-version/)
  * Self-hosted options:
    * [npm](../hosting/installation/npm/)
    * [Docker](../hosting/installation/docker/)

## Semantic versioning in n8n#

n8n uses [semantic versioning](https://semver.org/). All version numbers are in the format `MAJOR.MINOR.PATCH`. Version numbers increment as follows:

  * MAJOR version when making incompatible changes which can require user action.
  * MINOR version when adding functionality in a backward-compatible manner.
  * PATCH version when making backward-compatible bug fixes.

Older versions

You can find the release notes for older versions of n8n [here](0-x/)

## n8n@1.97.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.97.0...n8n@1.97.1) for this version.  
**Release date:** 2025-06-04

Next version

This is the `next` version. n8n recommends using the `latest` version. The `next` version may be unstable. To report issues, use the [forum](https://community.n8n.io/c/questions/12).

This release contains backports.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.95.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.95.2...n8n@1.95.3) for this version.  
**Release date:** 2025-06-03

Latest version

This is the `latest` version. n8n recommends using the `latest` version. The `next` version may be unstable. To report issues, use the [forum](https://community.n8n.io/c/questions/12).

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.97.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.96.0...n8n@1.97.0) for this version.  
**Release date:** 2025-06-02

This release contains new features, performance improvements and bug fixes.

### Convert to sub-workflow#

Large, monolithic workflows can slow things down. They’re harder to maintain, tougher to debug, and more difficult to scale. With sub-workflows, you can take a more modular approach, breaking up big workflows into smaller, manageable parts that are easier to reuse, test, understand, and explain.

Until now, creating sub-workflows required copying and pasting nodes manually, setting up a new workflow from scratch, and reconnecting everything by hand. **Convert to sub-workflow** allows you to simplify this process into a single action, so you can spend more time building and less time restructuring.

  

  

**How it works**

  1. Highlight the nodes you want to convert to a sub-workflow. These must:
     * Be fully connected, meaning no missing steps in between them
     * Start from a single starting node
     * End with a single node
  2. Right-click to open the context menu and select **Convert to sub-workflow**
     * Or use the shortcut: `Alt + X`
  3. n8n will:
     * Open a new tab containing the selected nodes
     * Preserve all node parameters as-is
     * Replace the selected nodes in the original workflow with a **Call My Sub-workflow** node

_Note_ : You will need to manually adjust the field types in the Start and Return nodes in the new sub-workflow.

This makes it easier to keep workflows modular, performant, and easier to maintain.

Learn more about [sub-workflows](../flow-logic/subworkflows/).

This release contains performance improvements and bug fixes.

### Contributors#

[maatthc](https://github.com/maatthc)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.96.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.95.0...n8n@1.96.0) for this version.  
**Release date:** 2025-06-02

Build failure

This release failed to build. Please use `1.97.0` instead.

This release contains API updates, core changes, editor improvements, node updates, and bug fixes.

### API support for assigning users to projects#

You can now use the API to add and update users within projects. This includes:

  * Assigning existing or pending users to a project with a specific role
  * Updating a user’s role within a project
  * Removing users from one or more projects

This update now allows you to use the API to add users to both the instance and specific projects, removing the need to manually assign them in the UI. 

### Add pending users to project member assignment#

You can now add **pending users,** those who have been invited but haven't completed sign-up, to projects as members.

This change lets you configure a user's project access upfront, without waiting for them to finish setting up their account. It eliminates the back-and-forth of managing access post-sign-up, ensuring users have the right project roles immediately upon joining.

### Contributors#

[matthabermehl](https://github.com/matthabermehl)  
[Stamsy](https://github.com/Stamsy)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.95.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.95.1...n8n@1.95.2) for this version.  
**Release date:** 2025-05-29

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.95.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.95.0...n8n@1.95.1) for this version.  
**Release date:** 2025-05-27

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.94.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.94.0...n8n@1.94.1) for this version.  
**Release date:** 2025-05-27

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.95.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.94.0...n8n@1.95.0) for this version.  
**Release date:** 2025-05-26

This release contains core updates, editor improvements, node updates, and bug fixes.

### Evaluations for AI workflows#

We’ve added a feature to help you iterate, test, and compare changes to your AI automations before pushing them to production so you can achieve more predictability and make better decisions.  
  

When you're building with AI, a small prompt tweak or model swap might improve results with some inputs, while quietly degrading performance with others. But without a way to evaluate performance across many inputs, you’re left guessing whether your AI is actually getting better when you make a change.   
  

By implementing **Evaluations for AI workflows** in n8n, you can assess how your AI performs across a range of inputs by adding a dedicated path in your workflow for running test cases and applying custom metrics to track results. This helps you build viable proof-of-concepts quickly, iterate more effectively, catch regressions early, and make more confident decisions when your AI is in production.  
  

  
  

#### Evaluation node and tab#

The **Evaluation node** includes several operations that, when used together, enable end-to-end AI evaluation.

  

![Evaluation node](../_images/release-notes/Evaluations_node.png) Evaluation node

  

Use this node to:

  * Run your AI logic against a wide range of test cases in the same execution
  * Capture the outputs of those test cases
  * Score the results using your own metrics or LLM-as-judge logic
  * Isolate a testing path to only include the nodes and logic you want to evaluate   

The **Evaluations tab** enables you to review test results in the n8n UI, perfect for comparing runs, spotting regressions, and viewing performance over time.   
  

#### 🛠 How evaluations work#

The evaluation path runs alongside your normal execution logic and only activates when you want—making it ideal for testing and iteration.   
  

Get started by selecting an AI workflow you want to evaluate that includes one or more LLM or Agent nodes.   

  1. Add an **Evaluation** node with the **On new Evaluation event** operation. This node will act as an additional trigger you’ll run only when testing. Configure it to read your dataset from Google Sheets, with each row representing a test input.  

> 💡 Better datasets mean better evaluations. Craft your dataset from a variety of test cases, including edge cases and typical inputs, to get meaningful feedback on how your AI performs. Learn more and access sample datasets [here](../advanced-ai/evaluations/light-evaluations/#1-create-a-dataset.md).

  2. Add a second **Evaluation** node using the **Set Outputs** operation after the part of the workflow you're testing—typically after an LLM or Agent node. This captures the response and writes it back to your dataset in Google Sheets.

  3. To evaluate output quality, add a third **Evaluation** node with the **Set Metrics** operation at a point after you’ve generated the outputs. You can develop workflow logic, custom calculations, or add an LLM-as-Judge to score the outputs. Map these metrics to your dataset in the node’s parameters.   

> 💡 Well-defined metrics = smarter decisions. Scoring your outputs based on similarity, correctness, or categorization can help you track whether changes are actually improving performance. Learn more and get links to example templates [here](../advanced-ai/evaluations/metric-based-evaluations/#2-calculate-metrics.md). 

  

![Evaluation workflow](../_images/release-notes/Evaluations_workflow.png) Evaluation workflow

  

When the Evaluation trigger node is executed, it runs each input in our dataset through your AI logic. This continues until all test cases are processed, a limit is reached, or you manually stop the execution. Once your evaluation path is set up, you can update your prompt, model, or workflow logic—and re-run the Evaluation trigger node to compare results. If you’ve added metrics, they’ll appear in the Evaluations tab.   
  

In some instances, you may want to isolate your testing path to make iteration faster or to avoid executing downstream logic. In this case, you can add an Evaluation node with the `Check If Evaluating` operation to ensure only the expected nodes run when performing evaluations.   
  

#### Things to keep in mind#

Evaluations for AI Workflows are designed to fit into your development flow, with more enhancements on the way. For now, here are a few things to note:

  * Test datasets are currently managed through Google Sheets. You’ll need a Google Sheets credential to run evaluations.
  * Each workflow supports one evaluation at a time. If you’d like to test multiple segments, consider splitting them into sub-workflows for more flexibility.
  * Community Edition supports one single evaluation. Pro and Enterprise plans allow unlimited evaluations.
  * AI Evaluations are not enabled for instances in scaling mode at this time.   

You can find details, tips, and common troubleshooting info [here](https://docs.n8n.io/advanced-ai/evaluations/tips-and-common-issues/).   
  

👉 Learn more about the AI evaluation strategies and practical implementation techniques during a **livestream on July 2nd, 2025 at 5:00 p.m GMT+2**. [Sign up](https://lu.ma/rfniiq2c). 

### Contributors#

[Phiph](https://github.com/Phiph)  
[cesars-gh](https://github.com/cesars-gh)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.94.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.93.0...n8n@1.94.0) for this version.  
**Release date:** 2025-05-19

This release contains editor improvements, an API update, node updates, new nodes, and bug fixes.

### Verified community nodes on Cloud#

We’ve expanded the n8n ecosystem and unlocked a new level of flexibility for all users including those on n8n Cloud! Now you can access a select set of community nodes and partner integrations without leaving the canvas. This means you install and automate with a wider range of integrations without leaving your workspace. The power of the community is now built-in.

This update focuses on three major improvements:

  * **Cloud availability** : Community nodes are no longer just for self-hosted users. A select set of nodes is now available on n8n Cloud.
  * **Built-in discovery** : You can find and explore these nodes right from the Nodes panel without leaving the editor or searching on npm.
  * **Trust and verification** : Nodes that appear in the editor have been manually vetted for quality and security. These verified nodes are marked with a checkmark.

We’re starting with a selection of around 25 nodes, including some of the most-used community-built packages and partner-supported integrations. For this phase, we focused on nodes that don’t include external package dependencies - helping streamline the review process and ensure a smooth rollout.   
  

This is just the start. We plan to expand the library gradually, bringing even more verified nodes into the editor along with the powerful and creative use cases they unlock. In time, our criteria will evolve, opening the door to a wider range of contributions while keeping quality and security in focus.   
  

Learn more about this update and find out which nodes are already installable from the editor in our [blog](https://blog.n8n.io/community-nodes-available-on-n8n-cloud/) post. 

  

💻 **Use a verified node**

Make sure you're on **n8n version 1.94.0** or later and the instance Owner has enabled verified community nodes. On Cloud, this can be done from the Admin Panel. For self-hosted instances, please refer to [documentation](../hosting/configuration/environment-variables/nodes/). In both cases, verified nodes are enabled by default.

  * Open the **Nodes panel** from the editor
  * Search for the Node. Verified nodes are indicated by a shield 🛡️
  * Select the node and click **Install**

  

  

Once an Owner installs a node, everyone on the instance can start using it—just drag, drop, and connect like any other node in your workflow.

  

🛠️ **Build a node and get it verified**

Want your node to be verified and discoverable from the editor? Here’s how to get involved:

  1. Review the [community node verification guidelines](../integrations/creating-nodes/build/reference/verification-guidelines/).
  2. If you’re building something new, follow the recommendations for [creating nodes](../integrations/creating-nodes/overview/).
  3. Check your design against the [UX guidelines](../integrations/creating-nodes/build/reference/ux-guidelines/).
  4. [Submit your node](../integrations/creating-nodes/deploy/submit-community-nodes/) to npm.
  5. Request verification by filling out [this form](https://internal.users.n8n.cloud/form/f0ff9304-f34a-420e-99da-6103a2f8ac5b).

  

**Already built a node? Raise your hand!**

If you’ve already published a community node and want it considered for verification, make sure it meets the requirements noted above, then let us know by submitting the interest [form](https://internal.users.n8n.cloud/form/f0ff9304-f34a-420e-99da-6103a2f8ac5b). We’re actively curating the next batch and would love to include your work.

### Extended logs view#

When workflows get complex, debugging can get... clicky. That’s where an extended **Logs View** comes in. Now you can get a clearer path to trace executions, troubleshoot issues, and understand the behavior of a complete workflow — without bouncing between node detail views. 

This update brings a unified, always-accessible panel to the bottom of the canvas, showing you each step of the execution as it happens. Whether you're working with loops, sub-workflows, or AI agents, you’ll see a structured view of everything that ran, in the order it ran—with input, output, and status info right where you need it.

You can jump into node details when you want to dig deeper, or follow a single item through every step it touched. Real-time highlighting shows you which nodes are currently running or have failed, and you’ll see total execution time for any workflow—plus token usage for AI workflows to help monitor performance. And if you're debugging across multiple screens? Just pop the logs out and drag them wherever you’d like.

⚙️**What it does**

  * Adds a **Logs view** to the bottom of the canvas that can be opened or collapsed. (Chat also appears here if your workflow uses it).
  * Displays a **hierarchical list of nodes** in the order they were executed—including expanded views of sub-workflows.
  * Allows you to **click a node in hierarchy** to preview inputs and outputs directly, or jump into the full Node Details view with a link.
  * Provides ability to **toggle** input and output data on and off.
  * Highlights each node **live as it runs** , showing when it starts, completes, or fails.
  * Includes **execution history** view to explore past execution data in a similar way.
  * Shows **roll-up stats** like total execution time and total AI tokens used (for AI-enabled workflows).
  * Includes a **“pop out”** button to open the logs as a floating window—perfect for dragging to another screen while debugging.

🛠️**How to**

To access the expanded logs view, click on the Logs bar at the bottom of the canvas. The view is also opens up when you open the chat window on the bottom of the page.

### Contributors#

[Stamsy](https://github.com/Stamsy)  
[feelgood-interface](https://github.com/feelgood-interface)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.93.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.92.0...n8n@1.93.0) for this version.  
**Release date:** 2025-05-12

This release contains core updates, editor improvements, new nodes, node updates, and bug fixes.

### Faster ways to open sub-workflows#

We’ve added several new ways to navigate your multi-workflow automations faster.

From any workflow with a sub-workflow node:

🖱️ Right-click on a sub-workflow node and select `Open sub-workflow` from the context menu

⌨️ Keyboard shortcuts

  * **Windows:** `CTRL + SHIFT + O` or `CTRL + Double Click`
  * **Mac:** `CMD + SHIFT + O` or `CMD + Double Click`

These options will bring your sub-workflow up in a new tab.

### Archive workflows#

If you’ve ever accidentally removed a workflow, you’ll appreciate the new archiving feature. Instead of permanently deleting workflows with the Remove action, workflows are now archived by default. This allows you to recover them if needed.

**How to:**

  * **Archive a workflow** \- Select **Archive** from the Editor UI menu. It has replaced the **Remove** action.
  * **Find archived workflows** \- Archived workflows are hidden by default. To find your archived workflows, select the option for **Show archived workflows** in the workflow filter menu.
  * **Permanently delete a workflow** \- Once a workflow is archived, you can **Delete** it from the options menu.
  * **Recover a workflow** \- Select **Unarchive** from the options menu.

**Keep in mind:**

  * Workflows archival requires the same permissions as required previously for removal.
  * You cannot select archived workflows as sub-workflows to execute
  * Active workflows are deactivated when they are archived
  * Archived workflows can not be edited

### Contributors#

[LeaDevelop](https://github.com/LeaDevelop)  
[ayhandoslu](https://github.com/ayhandoslu)  
[valentina98](https://github.com/valentina98)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.92.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.92.1...n8n@1.92.2) for this version.  
**Release date:** 2025-05-08

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.91.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.91.2...n8n@1.91.3) for this version.  
**Release date:** 2025-05-08

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.92.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.92.0...n8n@1.92.1) for this version.  
**Release date:** 2025-05-06

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.92.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.91.0...n8n@1.92.0) for this version.  
**Release date:** 2025-05-05

This release contains core updates, editor improvements, node updates, and bug fixes.

### Partial Execution for AI Tools#

We’ve made it easier to build and iterate on AI agents in n8n. You can now run and test specific tools without having to execute the entire agent workflow.

Partial execution is especially useful when refining or troubleshooting parts of your agent logic. It allows you to test changes incrementally, without triggering full agent runs, reducing unnecessary AI calls, token usage, and downstream activity. This makes iteration faster, more cost-efficient, and more precise when working with complex or multi-step AI workflows.

Partial execution for AI tools is available now for all tools - making it even easier to build, test, and fine-tune AI agents in n8n.

  

  

**How to:**

To use this feature you can either:

  * Click the **Play** button on the tool you want to execute directly from the canvas view.
  * Open the tool’s **Node Details View** and select **"Test step"** to run it from there.

If you have previously run the workflow, the input and output will be prefilled with data from the last execution. A pop-up form will open where you can manually fill in the parameters before executing your test.

### Extended logs view#

When workflows get complex, debugging can get... clicky. That’s where an extended **Logs View** comes in. Now you can get a clearer path to trace executions, troubleshoot issues, and understand the behavior of a complete workflow — without bouncing between node detail views. 

This update brings a unified, always-accessible panel to the bottom of the canvas, showing you each step of the execution as it happens. Whether you're working with loops, sub-workflows, or AI agents, you’ll see a structured view of everything that ran, in the order it ran—with input, output, and status info right where you need it.

You can jump into node details when you want to dig deeper, or follow a single item through every step it touched. Real-time highlighting shows you which nodes are currently running or have failed, and you’ll see total execution time for any workflow—plus token usage for AI workflows to help monitor performance. And if you're debugging across multiple screens? Just pop the logs out and drag them wherever you’d like.

⚙️**What it does**

  * Adds a **Logs view** to the bottom of the canvas that can be opened or collapsed. (Chat also appears here if your workflow uses it).
  * Displays a **hierarchical list of nodes** in the order they were executed—including expanded views of sub-workflows.
  * Allows you to **click a node in hierarchy** to preview inputs and outputs directly, or jump into the full Node Details view with a link.
  * Provides ability to **toggle** input and output data on and off.
  * Highlights each node **live as it runs** , showing when it starts, completes, or fails.
  * Includes **execution history** view to explore past execution data in a similar way.
  * Shows **roll-up stats** like total execution time and total AI tokens used (for AI-enabled workflows).
  * Includes a **“pop out”** button to open the logs as a floating window—perfect for dragging to another screen while debugging.

🛠️**How to**

To access the expanded logs view, click on the Logs bar at the bottom of the canvas. The view is also opens up when you open the chat window on the bottom of the page.

### Insights enhancements for Enterprise#

Two weeks after the launch of [Insights](../insights/), we’re releasing some enhancements designed for enterprise users.

  * **Expanded time ranges**. You can now filter insights over a variety of time periods, from the last 24 hours up to 1 year. Pro users are limited to 7 day and 14 day views. 
  * **Hourly granularity**. Drill down into the last 24 hours of production executions with hourly granularity, making it easier to analyze workflows and quickly identify issues. 

These updates provide deeper visibility into workflow history, helping you uncover trends over longer periods and detect problems sooner with more precise reporting.

  

![Filter insights](../_images/release-notes/Insights-drill-down.png) Filter insights

  

### Contributors#

[Stamsy](https://github.com/Stamsy)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.91.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.91.1...n8n@1.91.2) for this version.  
**Release date:** 2025-05-05

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.90.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.90.2...n8n@1.90.3) for this version.  
**Release date:** 2025-05-05

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.91.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.91.0...n8n@1.91.1) for this version.  
**Release date:** 2025-05-01

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.91.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.90.0...n8n@1.91.0) for this version.  
**Release date:** 2025-04-28

This release contains core updates, editor improvements, node updates, and bug fixes.

### Breadcrumb view from the canvas#

We’ve added **breadcrumb navigation directly on the canvas** , so you can quickly navigate to any of a workflow’s parent folders right from the canvas.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.90.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.90.1...n8n@1.90.2) for this version.  
**Release date:** 2025-04-25

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.90.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.90.0...n8n@1.90.1) for this version.  
**Release date:** 2025-04-22

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.90.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.89.0...n8n@1.90.0) for this version.  
**Release date:** 2025-04-22

This release contains core updates, editor updates, node updates, performance improvements, and bug fixes.

### Extended HTTP Request tool functionality#

We’ve brought the full power of the HTTP Request node to the HTTP Request tool in AI workflows. That means your AI Agents now have access to all the advanced configuration options—like Pagination, Batching, Timeout, Redirects, Proxy support, and even cURL import.

  

  

This update also includes support for the `$fromAI` function to dynamically generate the right parameters based on the context of your prompt — making API calls smarter, faster, and more flexible than ever.

**How to:**

  * Open your AI Agent node in the canvas.
  * Click the **‘+’ icon** to add a new tool connection.
  * In the **Tools panel** , select HTTP **Request Tool.**
  * Configure it just like you would a regular **HTTP Request node** — including advanced options

👉 Learn more about configuring the [HTTP Request tool](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolhttprequest/).

### Scoped API keys#

Users on the Enterprise plan can now create API keys with specific scopes to control exactly what each key can access.

![Scoped API keys](../_images/release-notes/scoped-API-keys.png) Scoped API keys

Previously, API keys had full read/write access across all endpoints. While sometimes necessary, this level of access can be excessive and too powerful for most use cases. Scoped API keys allow you to limit access to only the resources and actions a service or user actually needs.

**What’s new**

When creating a new API key, you can now:

  * Select whether the key has read, write, or both types of access. 
  * Specify which resources the key can interact with. 

Supported scopes include:

  * Variables — list, create, delete 
  * Security audit — generate reports 
  * Projects — list, create, update, delete 
  * Executions — list, read, delete 
  * Credentials — list, create, update, delete, move 
  * Workflows — list, create, update, delete, move, add/remove tags 

Scoped API keys give you more control and security. You can limit access to only what’s needed, making it safer to work with third parties and easier to manage internal API usage.

### Drag and Drop in Folders#

Folders just got friendlier. With this release, you can now **drag and drop workflows and folders** — making it even easier to keep things tidy.

Need to reorganize? Just select a workflow or folder and drag it into another folder or breadcrumb location. It’s a small change that makes a big difference when managing a growing collection of workflows.

  

  

📁 Folders are available to all [registered](../hosting/community-edition-features/#registered-community-edition) users—jump in and get your workspace in order!

### Contributors#

[Zordrak](https://github.com/Zordrak)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.89.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.89.1...n8n@1.89.2) for this version.  
**Release date:** 2025-04-16

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.89.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.89.0...n8n@1.89.1) for this version.  
**Release date:** 2025-04-15

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.89.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.88.0...n8n@1.89.0) for this version.  
**Release date:** 2025-04-14

This release contains API updates, core updates, editor updates, a new node, node updates, and bug fixes.

### Insights#

We're rolling out [Insights](../insights/), a new dashboard to monitor how your workflows are performing over time. It's designed to give admins (and owners) better visibility of their most important workflow metrics and help troubleshoot potential issues and improvements.   
  

In this first release, we’re introducing a summary banner, the insights dashboard, and time saved per execution.   
  

#### 1\. Summary banner#

A new banner on the overview page that gives instance admins and owners a birds eye view of key metrics over the last 7 days.

![Summary banner](../_images/release-notes/Insights-summary-banner.png) Insights summary banner

Available metrics:

  * Total production executions
  * Total failed executions
  * Failure rate
  * Average runtime of all workflows
  * Estimated time saved

This overview is designed to help you stay on top of workflow activity at a glance. It is available for all plans and editions.   
  

#### 2\. Insights dashboard#

On Pro and Enterprise plans, a new dashboard offers a deeper view into workflow performance and activity. 

![Insights dashboard](../_images/release-notes/Insights-dashboard.png) Insights dashboard

The dashboard includes:

  * Total production executions over time, including a comparison of successful and failed executions
  * Per-workflow breakdowns of key metrics
  * Comparisons with previous periods to help spot changes in usage or behavior
  * Runtime average and failure rate over time

#### 3\. Time saved per execution#

Within workflow settings, you can now assign a “time saved per execution” value to any workflow. This makes it possible to track the impact of your workflows and make it easier to share this visually with other teams and stakeholders.  
  

This is just the beginning for Insights: the next phase will introduce more advanced filtering and comparisons, custom date ranges, and additional monitoring capabilities. 

### Node updates#

  * We added a credential check for the Salesforce node
  * We added SearXNG as a tool for AI agents

You can now search within subfolders, making it easier to find workflows across all folder levels. Just type in the search bar and go. 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.88.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.87.0...n8n@1.88.0) for this version.  
**Release date:** 2025-04-10

This release contains new features, new nodes, performance improvements, and bug fixes.

### Model Context Protocol (MCP) nodes#

MCP aims to standardise how LLMs like Claude, ChatGPT, or Cursor can interact with tools or integrate data for their agents. Many providers - both established or new - are adopting MCP as a standard way to build agentic systems. It is an easy way to either expose your own app as a server, making capabilities available to a model as tools, or as a client that can call on tools outside of your own system.   

While it’s still early in the development process, we want to give you access to our new MCP nodes. This will help us understand your requirements better and will also let us converge on a great general solution quicker.   

We are adding two new nodes: 

  * a MCP [Server Trigger](../integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/) for any workflow 
  * a MCP [Client Tool](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp/) for the AI Agent 

The MCP Server Trigger turns n8n into an MCP server, providing n8n tools to models running outside of n8n. You can run multiple MCP servers from your n8n instance. The MCP Client Tool connects LLMs - and other intelligent agents - to any MCP-enabled service through a single interface.   

Max from our DevRel team created an official walkthrough for you to get started: 

  

[![Studio](../_images/release-notes/MCP-YouTube-thumb.jpg)](https://youtu.be/45WPU7P-1QQ?feature=shared)

[Studio Update #04](https://youtu.be/45WPU7P-1QQ?feature=shared)

### MCP Server Trigger#

The MCP Server Trigger turns n8n into an MCP server, providing n8n tools to models running outside of n8n. The node acts as an entry point into n8n for MCP clients. It operates by exposing a URL that MCP clients can interact with to access n8n tools. This means your n8n workflows and integrations are now available to models run elsewhere. Pretty neat. 

![MCP Server Trigger](../_images/release-notes/MCP-Server-Trigger.png) MCP Server Trigger

[Explore the MCP Server Trigger docs](../integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/)

### MCP Client Tool#

The MCP Client Tool node is a MCP client, allowing you to use the tools exposed by an external MCP server. You can connect the MCP Client Tool node to your models to call external tools with n8n agents. In this regard it is similar to using a n8n tool with your AI agent. One advantage is that the MCP Client Tool can access multiple tools on the MCP server at once, keeping your canvas cleaner and easier to understand. 

![MCP Client Tool](../_images/release-notes/MCP-Client-Tool.png) MCP Client Tools

[Explore the MCP Client Tool docs](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp/)

### Node updates#

  * Added a node for Azure Cosmos DB 
  * Added a node for Milvus Vector Store 
  * Updated the Email Trigger (IMAP) node 

### Contributors#

[adina-hub](https://github.com/adina-hub)  
[umanamente](https://github.com/umanamente)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.87.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.87.1...n8n@1.87.2) for this version.  
**Release date:** 2025-04-09

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.86.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.86.0...n8n@1.86.1) for this version.  
**Release date:** 2025-04-09

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.87.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.87.0...n8n@1.87.1) for this version.  
**Release date:** 2025-04-08

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.87.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.86.0...n8n@1.87.0) for this version.  
**Release date:** 2025-04-07

This release contains new nodes, node updates, API updates, core updates, editor updates, and bug fixes.

### Contributors#

[cesars-gh](https://github.com/cesars-gh)  
[Stamsy](https://github.com/Stamsy)  
[Pash10g](https://github.com/Pash10g)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.86.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.85.0...n8n@1.86.0) for this version.  
**Release date:** 2025-03-31

This release contains API updates, core updates, editor improvements, node updates, and bug fixes.

### Contributors#

[Aijeyomah](https://github.com/Aijeyomah)  
[ownerer](https://github.com/ownerer)  
[ulevitsky](https://github.com/ulevitsky)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.85.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.85.3...n8n@1.85.4) for this version.  
**Release date:** 2025-03-27

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.84.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.84.2...n8n@1.84.3) for this version.  
**Release date:** 2025-03-27

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.84.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.84.1...n8n@1.84.2) for this version.  
**Release date:** 2025-03-26

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.85.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.85.2...n8n@1.85.3) for this version.  
**Release date:** 2025-03-26

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.85.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.85.1...n8n@1.85.2) for this version.  
**Release date:** 2025-03-25

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.85.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.85.0...n8n@1.85.1) for this version.  
**Release date:** 2025-03-25

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.85.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.84.0...n8n@1.85.0) for this version.  
**Release date:** 2025-03-24

This release contains a new node, a new credential, core updates, editor updates, node updates, and bug fixes.

### Folders#

What can we say about folders? Well, they’re super handy for categorizing just about everything and they’re finally available for your n8n workflows. Tidy up your workspace with unlimited folders and nested folders. Search for workflows within folders. It’s one of the ways we’re making it easier to organize your n8n instances more effectively. 

**How to use it:**

Create and manage folders within your personal space or within projects. You can also create workflows from within a folder. You may need to restart your instance in order to activate folders.

![Folders](../_images/release-notes/Folders.png) It's a folder alright

  

Folders are available for all [registered](../hosting/community-edition-features/#registered-community-edition) users so get started with decluttering your workspace now and look for more features (like drag and drop) to organize your instances soon.

### Enhancements to Form Trigger Node#

Recent updates to the Form Trigger node have made it a more powerful tool for building business solutions. These enhancements provide more flexibility and customization, enabling teams to create visually engaging and highly functional workflows with forms.

  * **HTML customization:** Add custom HTML to forms, including embedded images and videos, for richer user experiences. 
  * **Custom CSS support** : Apply custom styles to user-facing components to align forms with your brand’s look and feel. Adjust fonts, colors, and spacing for a seamless visual identity.
  * **Form previews:** Your form’s description and title will pull into previews of your form when sharing on social media or messaging apps, providing a more polished look. 
  * **Hidden fields:** Use query parameters to add hidden fields, allowing you to pass data—such as a referral source—without exposing it to the user. 
  * **New responses options:** Respond to user submissions in multiple ways including text, HTML, or a downloadable file (binary format). This enables forms to display rich webpages or deliver digital assets such as dynamically generated invoices or personalized certificates. 

![Form with custom CSS applied](../_images/release-notes/Forms_with_custom_CSS_and_HTML.png) Form with custom CSS applied

  

These improvements elevate the Form Trigger node beyond a simple workflow trigger, transforming it into a powerful tool for addressing use cases from data collection and order processing to custom content creation.

### Contributors#

[Fank](https://github.com/Fank)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.84.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.84.0...n8n@1.84.1) for this version.  
**Release date:** 2025-03-18

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.84.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.83.0...n8n@1.84.0) for this version.  
**Release date:** 2025-03-17

This release contains a new node, node updates, editor updates, and bug fixes.

### Contributors#

[Pash10g](https://github.com/Pash10g)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.83.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.83.1...n8n@1.83.2) for this version.  
**Release date:** 2025-03-14

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.82.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.82.3...n8n@1.82.4) for this version.  
**Release date:** 2025-03-14

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.82.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.82.2...n8n@1.82.3) for this version.  
**Release date:** 2025-03-13

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.83.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.83.0...n8n@1.83.1) for this version.  
**Release date:** 2025-03-12

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.83.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.82.0...n8n@1.83.0) for this version.  
**Release date:** 2025-03-12

This release contains bug fixes and an editor update.

### Schema Preview#

Schema Preview lets you view and work with a node’s expected output without executing it or adding credentials, keeping you in flow while building.

  * **See expected node outputs instantly.** View schemas for over 100+ nodes to help you design workflows efficiently without extra steps. 
  * **Define workflow logic first, take care of credentials later.** Build your end-to-end workflow without getting sidetracked by credential setup. 
  * **Avoid unwanted executions when building.** Prevent unnecessary API calls, unwanted data changes, or potential third-party service costs by viewing outputs without executing nodes. 

**How to use it:**

  * Add a node with Schema Preview support to your workflow.
  * Open the next node in the sequence - Schema Preview data appears in the Node Editor where you would typically find it in the Schema View.
  * Use Schema Preview fields just like other schema data - drag and drop them into parameters and settings as needed.

  

  

Don’t forget to add the required credentials before putting your workflow into production.

### Contributors#

[pemontto](https://github.com/pemontto)  
[Haru922](https://github.com/Haru922)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.82.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.82.1...n8n@1.82.2) for this version.  
**Release date:** 2025-03-12

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.82.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.82.0...n8n@1.82.1) for this version.  
**Release date:** 2025-03-04

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.82.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.81.0...n8n@1.82.0) for this version.  
**Release date:** 2025-03-03

This release contains core updates, editor updates, new nodes, node updates, new credentials, credential updates, and bug fixes.

### Tidy up#

Tidy up instantly aligns nodes, centers stickies, untangles connections, and brings structure to your workflows. Whether you're preparing to share a workflow or just want to improve readability, this feature saves you time and makes your logic easier to follow. Clean, well-organized workflows aren't just nicer to look at—they’re also quicker to understand.

**How to:**

Open the workflow you want to tidy, then choose one of these options:

  * Click the **Tidy up** button in the bottom-left corner of the canvas (it looks like a broom 🧹)
  * Press **Shift + Alt + T** on your keyboard
  * Right-click anywhere on the canvas and select **Tidy up workflow**

Want to tidy up just part of your workflow? Select the specific nodes you want to clean up first - Tidy up will only adjust those, along with any stickies behind them.

  

  

### Multiple API keys#

n8n now supports multiple API keys, allowing users to generate and manage separate keys for different workflows or integrations. This improves security by enabling easier key rotation and isolation of credentials. Future updates will introduce more granular controls.   

![Multiple API keys](../_images/release-notes/Multiple-API-keys.png) Multiple API keys

  

### Contributors#

[Rostammahabadi](https://github.com/Rostammahabadi)  
[Lanhild](https://github.com/Lanhild)  
[matthiez](https://github.com/matthiez)  
[feelgood-interface](https://github.com/feelgood-interface)  
[adina-hub](https://github.com/adina-hub)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.81.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.81.3...n8n@1.81.4) for this version.  
**Release date:** 2025-03-03

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.81.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.81.2...n8n@1.81.3) for this version.  
**Release date:** 2025-03-03

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.81.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.81.1...n8n@1.81.2) for this version.  
**Release date:** 2025-02-28

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.80.5#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.80.4...n8n@1.80.5) for this version.  
**Release date:** 2025-02-28

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.80.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.80.3...n8n@1.80.4) for this version.  
**Release date:** 2025-02-27

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.81.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.81.0...n8n@1.81.1) for this version.  
**Release date:** 2025-02-27

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.81.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.80.0...n8n@1.81.0) for this version.  
**Release date:** 2025-02-24

This release contains bug fixes, a core update, editor improvements, and a node update.

### Improved partial executions#

The new execution engine for partial executions ensures that testing parts of a workflow in the builder closely mirrors production behaviour. This makes iterating with updated run-data faster and more reliable, particularly for complex workflows.

Before, user would test parts of a workflow in the builder that didn't consistently reflect production behaviour, leading to unexpected results during development.

This update aligns workflow execution in the builder with production behavior.

Here is an example for loops:

Before   

  
After   

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.80.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.80.2...n8n@1.80.3) for this version.  
**Release date:** 2025-02-21

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.79.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.79.3...n8n@1.79.4) for this version.  
**Release date:** 2025-02-21

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.80.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.80.1...n8n@1.80.2) for this version.  
**Release date:** 2025-02-21

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.79.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.79.2...n8n@1.79.3) for this version.  
**Release date:** 2025-02-21

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.80.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.80.0...n8n@1.80.1) for this version.  
**Release date:** 2025-02-20

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.79.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.79.1...n8n@1.79.2) for this version.  
**Release date:** 2025-02-20

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.80.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.79.0...n8n@1.80.0) for this version.  
**Release date:** 2025-02-17

This release contains bug fixes and an editor improvement.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.75.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.75.2...n8n@1.75.3) for this version.  
**Release date:** 2025-02-17

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.74.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.74.3...n8n@1.74.4) for this version.  
**Release date:** 2025-02-17

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.79.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.79.0...n8n@1.79.1) for this version.  
**Release date:** 2025-02-15

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.78.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.78.0...n8n@1.78.1) for this version.  
**Release date:** 2025-02-15

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.77.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.77.3...n8n@1.77.4) for this version.  
**Release date:** 2025-02-15

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.76.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.76.3...n8n@1.76.4) for this version.  
**Release date:** 2025-02-15

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.79.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.77.0...n8n@1.78.0) for this version.  
**Release date:** 2025-02-12

This release contains new features, node updates, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.77.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.77.2...n8n@1.77.3) for this version.  
**Release date:** 2025-02-06

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.78.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.77.0...n8n@1.78.0) for this version.  
**Release date:** 2025-02-05

This release contains new features, node updates, and bug fixes.

### Contributors#

[mocanew](https://github.com/mocanew)  
[Timtendo12](https://github.com/Timtendo12)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.77.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.77.1...n8n@1.77.2) for this version.  
**Release date:** 2025-02-04

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.76.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.76.2...n8n@1.76.3) for this version.  
**Release date:** 2025-02-04

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.77.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.77.0...n8n@1.77.1) for this version.  
**Release date:** 2025-02-03

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.76.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.76.1...n8n@1.76.2) for this version.  
**Release date:** 2025-02-03

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.77.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.76.0...n8n@1.77.0) for this version.  
**Release date:** 2025-01-29

This release contains new features, editor updates, new nodes, new credentials, node updates, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.76.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.76.0...n8n@1.76.1) for this version.  
**Release date:** 2025-01-23

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.76.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.75.0...n8n@1.76.0) for this version.  
**Release date:** 2025-01-22

This release contains new features, editor updates, new credentials, node improvements, and bug fixes.

### Contributors#

[Stamsy](https://github.com/Stamsy)  
[GKdeVries](https://github.com/GKdeVries)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.75.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.75.1...n8n@1.75.2) for this version.  
**Release date:** 2025-01-17

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.74.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.74.2...n8n@1.74.3) for this version.  
**Release date:** 2025-01-17

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.75.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.75.0...n8n@1.75.1) for this version.  
**Release date:** 2025-01-17

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.74.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.74.1...n8n@1.74.2) for this version.  
**Release date:** 2025-01-17

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.75.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.74.0...n8n@1.75.0) for this version.  
**Release date:** 2025-01-15

This release contains bug fixes and editor updates.

### Improved consistency across environments#

We added new UX and automatic changes improvements resulting in a better consistency between your staging and production instances.

Previously, users faced issues like: 

  * Lack of visibility into required credential updates when pulling changes 
  * Incomplete synchronization, where changes — such as deletions — weren’t always applied across environments 
  * Confusing commit process, making it unclear what was being pushed or pulled 

We addressed these by:

  * Clearly indicating required credential updates when pulling changes 
  * Ensuring deletions and other modifications sync correctly across environments 
  * Improving commit selection to provide better visibility into what’s being pushed  
  

![Commit modal](../_images/release-notes/Commit-modal.png) Commit modal

  

![Pull notification](../_images/release-notes/Pull-notification.png) Pull notification

  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.74.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.74.0...n8n@1.74.1) for this version.  
**Release date:** 2025-01-09

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.74.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.73.0...n8n@1.74.0) for this version.  
**Release date:** 2025-01-08

This release contains new features, a new node, node updates, performance improvements and bug fixes.

### Overhauled Code node editing experience#

We added a ton of new helpers to the Code node, making edits of your code much faster and more comfortable. You get:

  * TypeScript autocomplete 
  * TypeScript linting 
  * TypeScript hover tips 
  * Search and replace 
  * New keyboard shortcuts based on the VSCode keymap 
  * Auto-formatting using prettier (Alt+Shift+F) 
  * Remember folded regions and history after refresh 
  * Multi cursor 
  * Type function in the Code node using JSDoc types 
  * Drag and drop for all Code node modes 
  * Indentation markers 

We build this on a web worker architecture so you won't have to suffer from performance degradation while typing.   
  
To get the full picture, check out our Studio update with Max and Elias, where they discuss and demo the new editing experience. 👇   

[![Studio](../_images/release-notes/The_Studio_thumbnail_Code_node.jpg)](https://youtu.be/De1E58MPaMQ?t=645)

[Studio Update #04](https://youtu.be/De1E58MPaMQ?t=645)

### New node: Microsoft Entra ID#

Microsoft Entra ID (formerly known as Microsoft Azure Active Directory or Azure AD) is used for cloud-based identity and access management. [The new node](../integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra/) supports a wide range of Microsoft Entra ID features, which includes creating, getting, updating, and deleting users and groups, as well as adding users to and removing them from groups. 

### Node updates#

  * [AI Agent](../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/): Vector stores can now be directly used as tools for the agent
  * [Code](../code/builtin/overview/): Tons of new speed and convenience features, see above for details 
  * [Google Vertex Chat](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex/): Added option to specify the GCP region for the Google API credentials 
  * [HighLevel](../integrations/builtin/app-nodes/n8n-nodes-base.highlevel/): Added support for calendar items 

We also added a custom [projects](../user-management/rbac/projects/) icon selector on top of the available emojis. Pretty!

### Contributors#

[igatanasov](https://github.com/igatanasov)  
[Stamsy](https://github.com/Stamsy)  
[feelgood-interface](https://github.com/feelgood-interface)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.73.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.73.0...n8n@1.73.1) for this version.  
**Release date:** 2024-12-19

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.73.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.72.0...n8n@1.73.0) for this version.  
**Release date:** 2024-12-19

This release contains node updates, performance improvements, and bug fixes.

### Node updates#

  * [AI Agent](../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/): Updated descriptions for Chat Trigger options
  * [Facebook Graph API](../integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi/): Updated for API v21.0
  * [Gmail](../integrations/builtin/app-nodes/n8n-nodes-base.gmail/): Added two new options for the `Send and wait` operation, free text and custom form 
  * [Linear Trigger](../integrations/builtin/trigger-nodes/n8n-nodes-base.lineartrigger/): Added support for admin scope 
  * [MailerLite](../integrations/builtin/app-nodes/n8n-nodes-base.mailerlite/): Now supports the new API 
  * [Slack](../integrations/builtin/app-nodes/n8n-nodes-base.slack/): Added two new options for the `Send and wait` operation, free text and custom form 

We also added credential support for [SolarWinds IPAM](../integrations/builtin/credentials/solarwindsipam/) and [SolarWinds Observability](../integrations/builtin/credentials/solarwindsobservability/). 

Last, but not least, we [improved the schema view performance in the node details view by 90%](https://github.com/n8n-io/n8n/pull/12180) and added drag and drop re-ordering to parameters. This comes in very handy in the [If](../integrations/builtin/core-nodes/n8n-nodes-base.if/) or [Edit Fields](../integrations/builtin/core-nodes/n8n-nodes-base.set/) nodes. 

### Contributors#

[CodeShakingSheep](https://github.com/CodeShakingSheep)  
[mickaelandrieu](https://github.com/mickaelandrieu)  
[Stamsy](https://github.com/Stamsy)  
[pbdco](https://github.com/pbdco)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.72.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.72.0...n8n@1.72.1) for this version.  
**Release date:** 2024-12-12

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.71.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.71.2...n8n@1.71.3) for this version.  
**Release date:** 2024-12-12

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.72.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.71.0...n8n@1.72.0) for this version.  
**Release date:** 2024-12-11

This release contains node updates, usability improvements, and bug fixes.

### Node updates#

  * [AI Transform](../integrations/builtin/core-nodes/n8n-nodes-base.aitransform/): The `maximum context length` error now retries with reduced payload size
  * [Redis](../integrations/builtin/app-nodes/n8n-nodes-base.redis/): Added support for `continue on fail`

### Improved commit modal#

We added filters and text search to the commit modal when working with [Environments](../source-control-environments/). This will make committing easier as we provide more information and better visibility. Environments are available on the Enterprise plan. 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.71.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.71.1...n8n@1.71.2) for this version.  
**Release date:** 2024-12-10

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.70.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.70.3...n8n@1.70.4) for this version.  
**Release date:** 2024-12-10

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.71.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.71.0...n8n@1.71.1) for this version.  
**Release date:** 2024-12-06

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.70.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.70.2...n8n@1.70.3) for this version.  
**Release date:** 2024-12-05

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.71.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.70.2...n8n@1.71.0) for this version.  
**Release date:** 2024-12-04

This release contains node updates, performance improvements, and bug fixes.

### Task runners for the Code node in public beta#

We're introducing a significant performance upgrade to the Code node with our new Task runner system. This enhancement moves JavaScript code execution to a separate process, improving your workflow execution speed while adding better isolation.

![Task runners overview](../_images/hosting/configuration/task-runner-concept.png) Task runners overview

Our benchmarks show up to 6x improvement in workflow executions using Code nodes - from approximately 6 to 35 executions per second. All these improvements happen under the hood, keeping your Code node experience exactly the same.

The Task runner comes in two modes:

  * Internal mode (default): Perfect for getting started, automatically managing task runners as child processes 
  * External mode: For advanced hosting scenarios requiring maximum isolation and security

Currently, this feature is opt-in and can be enabled using [environment variables](../hosting/configuration/environment-variables/task-runners/). Once stable, it will become the default execution method for Code nodes.

To start using Task runners today, [check out the docs](../hosting/configuration/task-runners/).

### Node updates#

  * [AI Transform node](../integrations/builtin/core-nodes/n8n-nodes-base.aitransform/): We improved the prompt for code generation to transform data
  * [Code node](../integrations/builtin/core-nodes/n8n-nodes-base.code/): We added a warning if `pairedItem` is absent or could not be auto mapped 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.70.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.70.1...n8n@1.70.2) for this version.  
**Release date:** 2024-12-04

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.70.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.70.0...n8n@1.70.1) for this version.  
**Release date:** 2024-11-29

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.70.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.69.0...n8n@1.70.0) for this version.  
**Release date:** 2024-11-27

This release contains node updates, performance improvements and bug fixes.

### New canvas in beta#

The new canvas is now the default setting for all users. It should bring significant performance improvements and adds a handy minimap. As it is still a beta version you can still revert to the previous version with the three dot menu. 

We're looking forward to your feedback. Should you encounter a bug, you will find a handy button to create an issue at the bottom of the new canvas as well. 

### Node updates#

  * We added credential support for [Zabbix](../integrations/builtin/credentials/zabbix/) to the HTTP request node 
  * We added new OAuth2 credentials for [Microsoft SharePoint](../integrations/builtin/credentials/microsoft/)
  * The [Slack node](../integrations/builtin/app-nodes/n8n-nodes-base.slack/#operations) now uses markdown for the approval message when using the `Send and Wait for Approval` operation

### Contributors#

[feelgood-interface](https://github.com/feelgood-interface)  
[adina-hub](https://github.com/adina-hub)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.68.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.68.0...n8n@1.68.1) for this version.  
**Release date:** 2024-11-26

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.69.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.69.1...n8n@1.69.2) for this version.  
**Release date:** 2024-11-26

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.69.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.69.0...n8n@1.69.1) for this version.  
**Release date:** 2024-11-25

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.69.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.68.0...n8n@1.69.0) for this version.  
**Release date:** 2024-11-20

This release contains a new feature, node improvements and bug fixes.

### Sub-workflow debugging#

We made it much easier to debug sub-workflows by improving their accessibility from the parent workflow. 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.68.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.67.1...n8n@1.68.0) for this version.  
**Release date:** 2024-11-13

This release contains node updates, performance improvements and many bug fixes.

#### New AI agent canvas chat#

We revamped the chat experience for AI agents on the canvas. A neatly organized view instead of a modal hiding the nodes. You can now see the canvas, chat and logs at the same time when testing your workflow.   
  

  
  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.67.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.67.0...n8n@1.67.1) for this version.  
**Release date:** 2024-11-07

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.67.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.66.0...n8n@1.67.0) for this version.  
**Release date:** 2024-11-06

This release contains node updates and bug fixes.

### Node updates#

  * [AI Transform](../integrations/builtin/core-nodes/n8n-nodes-base.aitransform/): Improved usability 
  * [Anthropic Chat Model Node](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic/): Added Haiku 3.5 support 
  * [Convert to File](../integrations/builtin/core-nodes/n8n-nodes-base.converttofile/): Added delimiter option for writing to CSV 
  * [Gmail Trigger](../integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/): Added option to filter for draft messages 
  * [Intercom](../integrations/builtin/app-nodes/n8n-nodes-base.intercom/): Credential can now be used in the HTTP Request node 
  * [Rapid7 InsightVM](../integrations/builtin/credentials/rapid7insightvm/): Added credential support 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.66.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.65.2...n8n@1.66.0) for this version.  
**Release date:** 2024-10-31

This release contains performance improvements, a node update and bug fixes.

### Node update#

  * [Anthropic Chat Model](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic/): Added support for claude-3-5-sonnet-20241022 

We made updates to how projects and workflow ownership are displayed making them easier to understand and navigate. 

We further improved the performance logic of partial executions, leading to a smoother and more enjoyable building experience. 

### New n8n canvas alpha#

We have enabled the alpha version of our new canvas. The canvas is the ‘drawing board’ of the n8n editor, and we’re working on a full rewrite. Your feedback and testing will help us improve it. [Read all about it on our community forum](https://community.n8n.io/t/help-us-test-the-new-n8n-canvas-alpha/60070). 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.65.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.65.1...n8n@1.65.2) for this version.  
**Release date:** 2024-10-28

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.64.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.64.2...n8n@1.64.3) for this version.  
**Release date:** 2024-10-25

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.65.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.65.0...n8n@1.65.1) for this version.  
**Release date:** 2024-10-25

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.65.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.64.1...n8n@1.65.0) for this version.  
**Release date:** 2024-10-24

[Breaking change](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md)

What changed? Queue polling via the environment variable `QUEUE_RECOVERY_INTERVAL` has been removed.

When is action necessary? If you have set `QUEUE_RECOVERY_INTERVAL`, you can remove it as it no longer has any effect.

This release contains a new features, new nodes, node enhancements, and bug fixes.

### New node: n8n Form#

Use the [n8n Form node](../integrations/builtin/core-nodes/n8n-nodes-base.form/) to create user-facing forms with multiple pages. You can add other nodes with custom logic between to process user input. Start the workflow with a [n8n Form Trigger](../integrations/builtin/core-nodes/n8n-nodes-base.formtrigger/). 

![A multi-page form with branching](../_images/integrations/builtin/core-nodes/n8n-nodes-base.form/example_image.png) A multi-page form with branching

Additionally you can: 

  * Set default selections with query parameters 
  * Define the form with a JSON array of objects
  * Show a completion screen and redirect to another URL

### Node updates#

New nodes: 

  * [Google Business Profile](../integrations/builtin/app-nodes/n8n-nodes-base.googlebusinessprofile/) and [Google Business Profile Trigger](../integrations/builtin/trigger-nodes/n8n-nodes-base.googlebusinessprofiletrigger/): Use these to integrate Google Business Profile reviews and posts with your workflows 

Enhanced nodes:

  * [AI Agent](../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/): Removed the requirement to add at least one tool 
  * [GitHub](../integrations/builtin/app-nodes/n8n-nodes-base.github/): Added workflows as a resource operation 
  * [Structured Output Parser](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/): Added more user-friendly error messages

For additional security, we improved how we handle multi-factor authentication, hardened config file permissions and introduced JWT for the public API. 

For better performance, we improved how partial executions are handled in loops. 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

  * [Idan Fishman](https://github.com/idanfishman)

## n8n@1.64.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.64.1...n8n@1.64.2) for this version.  
**Release date:** 2024-10-24

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.64.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.64.0...n8n@1.64.1) for this version.  
**Release date:** 2024-10-21

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.64.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.63.4...n8n@1.64.0) for this version.  
**Release date:** 2024-10-16

This release contains a new node, node enhancements, performance improvements and bug fixes.

### Enhanced node: Remove Duplicates#

The [Remove Duplicates node](../integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/) got a major makeover with the addition of two new operations: 

  * Remove Items Processed in Previous Executions: Compare items in the current input to items from previous executions and remove duplicates 
  * Clear Deduplication History: Wipe the memory of items from previous executions.

This makes it easier to only process new items from any data source. For example, you can now more easily poll a Google sheet for new entries by `id` or remove duplicate orders from the same customer by comparing their `order date`. The great thing is, you can now do this within **and across** workflow runs. 

### New node: Gong#

The new node for [Gong](../integrations/builtin/app-nodes/n8n-nodes-base.gong/) allows you to get users and calls to process them further in n8n. Very useful for sales related workflows. 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

  * [Sören Uhrbach](https://github.com/soerenuhrbach)

## n8n@1.63.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.63.3...n8n@1.63.4) for this version.  
**Release date:** 2024-10-15

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.62.6#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.62.5...n8n@1.62.6) for this version.  
**Release date:** 2024-10-15

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.63.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.63.2...n8n@1.63.3) for this version.  
**Release date:** 2024-10-15

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.63.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.63.1...n8n@1.63.2) for this version.  
**Release date:** 2024-10-11

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.62.5#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.62.4...n8n@1.62.5) for this version.  
**Release date:** 2024-10-11

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.63.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.63.0...n8n@1.63.1) for this version.  
**Release date:** 2024-10-11

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.62.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.62.3...n8n@1.62.4) for this version.  
**Release date:** 2024-10-11

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.63.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.62.3...n8n@1.63.0) for this version.  
**Release date:** 2024-10-09

[Breaking change](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md)

What changed?

  * The worker server used to bind to IPv6 by default. It now binds to IPv4 by default. 
  * The worker server's `/healthz` used to report healthy status based on database and Redis checks. It now reports healthy status regardless of database and Redis status, and the database and Redis checks are part of `/healthz/readiness`. 

When is action necessary?

  * If you experience a port conflict error when starting a worker server using its default port, set a different port for the worker server with `QUEUE_HEALTH_CHECK_PORT`. 
  * If you are relying on database and Redis checks for worker health status, switch to checking `/healthz/readiness` instead of `/healthz`. 

This release contains new features, node enhancements and bug fixes.

### Node updates#

  * [OpenAI](../integrations/builtin/app-nodes/n8n-nodes-langchain.openai/): Added the option to choose between the default memory connector to provide memory to the assistant or to specify a thread ID 
  * [Gmail](../integrations/builtin/app-nodes/n8n-nodes-base.gmail/) and [Slack](../integrations/builtin/app-nodes/n8n-nodes-base.slack/): Added custom approval operations to have a human in the loop of a workflow 

We have also optimized the [worker health checks](../hosting/logging-monitoring/monitoring/) (see breaking change above). 

Each credential now has a seperate url you can link to. This makes sharing much easier. 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Pemontto](https://github.com/pemontto)

## n8n@1.62.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.62.2...n8n@1.62.3) for this version.  
**Release date:** 2024-10-08

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.62.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.62.1...n8n@1.62.2) for this version.  
**Release date:** 2024-10-07

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.62.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.61.0...n8n@1.62.1) for this version.  
**Release date:** 2024-10-02

This release contains new features, node enhancements and bug fixes.

Skipped 1.62.0

We skipped 1.62.0 and went straight to 1.62.1 with an additional fix. 

#### Additional nodes as tools#

We have made additional nodes usable with the [Tools AI Agent node](../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent/).   
  

  
  
Additionally, we have added a `$fromAI()` placeholder function to use with tools, allowing you to dynamically pass information from the models to the connected tools. This function works similarly to placeholders used elsewhere in n8n.   
  
Both of these new features enable you to build even more powerful AI agents by drawing directly from the apps your business uses. This makes integrating LLMs into your business processes even easier than before. 

### Node updates#

  * [Google BigQuery](../integrations/builtin/app-nodes/n8n-nodes-base.googlebigquery/): Added option to return numeric values as integers and not strings 
  * [HTTP Request](../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/): Added credential support for Sysdig 
  * [Invoice Ninja](../integrations/builtin/app-nodes/n8n-nodes-base.invoiceninja/): Additional query params for getAll requests 
  * [Question and Answer Chain](../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/): Added the option to use a custom prompt 

Drag and drop insertion on cursor position from schema view is now also enabled for code, SQL and Html fields in nodes. 

Customers with an enterprise license can now rate, tag and highlight execution data in the executions view. To use highlighting, add an [Execution Data Node](../integrations/builtin/core-nodes/n8n-nodes-base.executiondata/) (or Code node) to the workflow to set [custom executions data](../workflows/executions/custom-executions-data/). 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Benjamin Roedell](https://github.com/benrobot)  
[CodeShakingSheep](https://github.com/CodeShakingSheep)  
[manuelbcd](https://github.com/manuelbcd)  
[Miguel Prytoluk](https://github.com/mprytoluk)

## n8n@1.61.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.60.1...n8n@1.61.0) for this version.  
**Release date:** 2024-09-25

This release contains new features, node enhancements and bug fixes.

### Node updates#

  * [Brandfetch](../integrations/builtin/app-nodes/n8n-nodes-base.brandfetch/): Updated to use the new API
  * [Slack](../integrations/builtin/app-nodes/n8n-nodes-base.slack/): Made adding or removing the workflow link to a message easier

Big datasets now render faster thanks to virtual scrolling and execution annotations are harder to delete.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.59.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.59.3...n8n@1.59.4) for this version.  
**Release date:** 2024-09-20

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.60.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.60.0...n8n@1.60.1) for this version.  
**Release date:** 2024-09-20

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.60.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.59.3...n8n@1.60.0) for this version.  
**Release date:** 2024-09-18

This release contains new features, node enhancements and bug fixes.

#### Queue metrics for workers#

You can now [expose and consume metrics from your workers](https://docs.n8n.io/hosting/configuration/configuration-examples/prometheus/). The worker instances have the same metrics available as the main instance(s) and can be configured with [environment variables](../hosting/configuration/environment-variables/endpoints/).

You can now customize the maximum file size when uploading files within forms to webhooks. The [environment variable to set](../hosting/configuration/environment-variables/endpoints/) for this is `N8N_FORMDATA_FILE_SIZE_MAX`. The default setting is 200MiB.

### Node updates#

Enhanced nodes:

  * [Invoice Ninja](../integrations/builtin/app-nodes/n8n-nodes-base.invoiceninja/): Added actions for bank transactions
  * [OpenAI](../integrations/builtin/app-nodes/n8n-nodes-langchain.openai/): Added O1 models to the model select

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[CodeShakingSheep](https://github.com/CodeShakingSheep)

## n8n@1.59.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.59.2...n8n@1.59.3) for this version.  
**Release date:** 2024-09-18

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.59.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.59.1...n8n@1.59.2) for this version.  
**Release date:** 2024-09-17

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.59.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.59.0...n8n@1.59.1) for this version.  
**Release date:** 2024-09-16

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.58.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.58.1...n8n@1.58.2) for this version.  
**Release date:** 2024-09-12

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.59.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.58.1...n8n@1.59.0) for this version.  
**Release date:** 2024-09-11

Chat Trigger

If you are using the Chat Trigger in "Embedded Chat" mode, with authentication turned on, you could see errors connecting to n8n if the authentication on the sending/embedded side is mis-configured.

This release contains bug fixes and feature enhancements.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[oscarpedrero](https://github.com/oscarpedrero)

## n8n@1.58.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.58.0...n8n@1.58.1) for this version.  
**Release date:** 2024-09-06

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.58.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.57.0...n8n@1.58.0) for this version.  
**Release date:** 2024-09-05

This release contains new features, bug fixes and feature enhancements.

#### New node: PGVector Vector Store#

This release adds the PGVector Vector Store node. Use this node to interact with the PGVector tables in your PostgreSQL database. You can insert, get, and retrieve documents from a vector table to provide them to a retriever connected to a chain.

#### See active collaborators on workflows#

We added collaborator avatars back to the workflow canvas. You will see other users who are active on the workflow, preventing you from overriding each other's work.

![Collaboration avatars](../_images/release-notes/Collaboration-avatar.png) Collaboration avatars

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.57.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.56.2...n8n@1.57.0) for this version.  
**Release date:** 2024-08-28

This release contains new features and bug fixes.

#### Improved execution queue handling#

We are [exposing new execution queue metrics](../hosting/configuration/configuration-examples/prometheus/) to give users more visibility of the queue length. This helps to inform decisions on horizontal scaling, based on queue status. We have also made querying executions faster.

#### New credentials for the HTTP Request node#

We added credential support for Datadog, Dynatrace, Elastic Security, Filescan, Iris, and Malcore to the HTTP Request node making it easier to use existing credentials.

We also made it easier to select workflows as tools when working with AI agents by implementing a new `workflow selector` parameter type.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Bram Kn](https://github.com/bramkn)

## n8n@1.56.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.56.1...n8n@1.56.2) for this version.  
**Release date:** 2024-08-26

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.56.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.56.0...n8n@1.56.1) for this version.  
**Release date:** 2024-08-23

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.56.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.55.3...n8n@1.56.0) for this version.  
**Release date:** 2024-08-21

This release contains node updates, security and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[CodeShakingSheep](https://github.com/CodeShakingSheep)  
[Oz Weiss](https://github.com/thewizarodofoz)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.55.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.55.2...n8n@1.55.3) for this version.  
**Release date:** 2024-08-16

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.55.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.55.1...n8n@1.55.2) for this version.  
**Release date:** 2024-08-16

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.55.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.55.0...n8n@1.55.1) for this version.  
**Release date:** 2024-08-15

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.54.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.54.3...n8n@1.54.4) for this version.  
**Release date:** 2024-08-15

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.54.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.54.2...n8n@1.54.3) for this version.  
**Release date:** 2024-08-15

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.54.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.54.1...n8n@1.54.2) for this version.  
**Release date:** 2024-08-14

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.55.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.54.1...n8n@1.55.0) for this version.  
**Release date:** 2024-08-14

[Breaking change](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md)

The N8N_BLOCK_FILE_ACCESS_TO_N8N_FILES environment variable now also blocks access to n8n's static cache directory at ~/.cache/n8n/public.

If you are writing to or reading from a file at n8n's static cache directory via a node, e.g. Read/Write Files from Disk, please update your node to use a different path.

This release contains a new feature, a new node, a node update and bug fixes.

#### Override the npm registry#

This release adds the option to override the npm registry for installing community packages. This is a paid feature.

We now also prevent npm downloading community packages from a compromised npm registry by explicitly using --registry in all npm install commands.

#### New node: AI Transform#

This release adds the [AI Transform node](../integrations/builtin/core-nodes/n8n-nodes-base.aitransform/). Use the AI Transform node to generate code snippets based on your prompt. The AI is context-aware, understanding the workflow’s nodes and their data types. The node is only available on [Cloud plans](../manage-cloud/overview/).

#### New node: Okta#

This release adds the [Okta node](../integrations/builtin/app-nodes/n8n-nodes-base.okta/). Use the Okta node to automate work in Okta and integrate Okta with other applications. n8n has built-in support for a wide range of Okta features, which includes creating, updating, and deleting users.

### Node updates#

Enhanced node:

  * [MySQL](../integrations/builtin/app-nodes/n8n-nodes-base.mysql/)

This release also adds the new schema view for the expression editor modal.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.54.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.54.0...n8n@1.54.1) for this version.  
**Release date:** 2024-08-13

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.53.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.53.1...n8n@1.53.2) for this version.  
**Release date:** 2024-08-08

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.54.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.53.1...n8n@1.54.0) for this version.  
**Release date:** 2024-08-07

This release contains new features, node enhancements, bug fixes and updates to our API.

### API update#

Our [public REST API](../api/) now supports additional operations:

  * Create, delete, and edit roles for users
  * Create, read, update and delete projects

Find the details in the [API reference](../api/api-reference/).

### Contributors#

[CodeShakingSheep](https://github.com/CodeShakingSheep)  
[Javier Ferrer González](https://github.com/JavierCane)  
[Mickaël Andrieu](https://github.com/mickaelandrieu)  
[Oz Weiss](https://github.com/thewizarodofoz)  
[Pemontto](https://github.com/pemontto)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.45.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.45.1...n8n@1.45.2) for this version.  
**Release date:** 2024-08-06

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.53.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.53.0...n8n@1.53.1) for this version.  
**Release date:** 2024-08-02

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.53.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.52.2...n8n@1.53.0) for this version.  
**Release date:** 2024-07-31

This release contains new features, new nodes, node enhancements, bug fixes and updates to our API.

#### Added Google Cloud Platform Secrets Manager support#

This release adds [Google Cloud Platform Secrets Manager](../external-secrets/) to the list of external secret stores. We already support AWS secrets, Azure Key Vault, Infisical and HashiCorp Vault. External secret stores are available under an enterprise license.

#### New node: Information Extractor#

This release adds the [Information Extractor node](../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor/). The node is specifically tailored for information extraction tasks. It uses Structured Output Parser under the hood, but provides a simpler way to extract information from text in a structured JSON form.

#### New node: Sentiment Analysis#

This release adds the [Sentiment Analysis node](../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis/). The node leverages LLMs to analyze and categorize the sentiment of input text. Users can easily integrate this node into their workflows to perform sentiment analysis on text data. The node is flexible enough to handle various use cases, from basic positive/negative classification to more nuanced sentiment categories.

### Node updates#

Enhanced nodes:

  * [Calendly Trigger](../integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger/)
  * [HTTP Request](../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)
  * [n8n Form Trigger](../integrations/builtin/core-nodes/n8n-nodes-base.formtrigger/)
  * [Shopify](../integrations/builtin/app-nodes/n8n-nodes-base.shopify/)

### API update#

Our [public REST API](../api/) now supports additional operations:

  * Create, read, and delete for variables
  * Filtering workflows by project
  * Transferring workflows

Find the details in the [API reference](../api/api-reference/).

### Contributors#

[feelgood-interface](https://github.com/feelgood-interface)  
[Oz Weiss](https://github.com/thewizarodofoz)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.52.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.52.1...n8n@1.52.2) for this version.  
**Release date:** 2024-07-31

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.52.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.52.0...n8n@1.52.1) for this version.  
**Release date:** 2024-07-26

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.51.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.51.1...n8n@1.51.2) for this version.  
**Release date:** 2024-07-26

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.52.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.51.1...n8n@1.52.0) for this version.  
**Release date:** 2024-07-25

[Breaking change](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md)

Prometheus metrics enabled via N8N_METRICS_INCLUDE_DEFAULT_METRICS and N8N_METRICS_INCLUDE_API_ENDPOINTS were fixed to include the default n8n_ prefix.

If you are using Prometheus metrics from these categories and are using a non-empty prefix, please update those metrics to match their new prefixed names.

This release contains new features, node enhancements and bug fixes.

#### Added Azure Key Vault support#

This release adds [Azure Key Vault](../external-secrets/) to the list of external secret stores. We already support AWS secrets, Infisical and HashiCorp Vault and are working on Google Secrets Manager. External secret stores are available under an enterprise license.

### Node updates#

Enhanced nodes:

  * [Pinecone Vector Store](../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone/)
  * [Supabase Vector Store](../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase/)
  * [Send Email](../integrations/builtin/core-nodes/n8n-nodes-base.sendemail/)

Deprecated nodes:

  * OpenAI Model: You can use the OpenAI Chat Model instead
  * Google Palm Chat Model: You can use Google Vertex or Gemini instead
  * Google Palm Model: You can use Google Vertex or Gemini instead

## n8n@1.51.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.51.0...n8n@1.51.1) for this version.  
**Release date:** 2024-07-23

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.50.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.50.1...n8n@1.50.2) for this version.  
**Release date:** 2024-07-23

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.51.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.50.1...n8n@1.51.0) for this version.  
**Release date:** 2024-07-18

This release contains new nodes, node enhancements and bug fixes.

#### New node: Text Classifier#

This release adds the [Text Classifier node](../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier/).

#### New node: Postgres Chat Memory#

This release adds the [Postgres Chat Memory node](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat/).

#### New node: Google Vertex Chat Model#

This release adds the [Google Vertex Chat Model node](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex/).

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Node updates#

  * Enhanced nodes: Asana

## n8n@1.50.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.50.0...n8n@1.50.1) for this version.  
**Release date:** 2024-07-16

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.50.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.49.0...n8n@1.50.0) for this version.  
**Release date:** 2024-07-10

This release contains node enhancements and bug fixes.

### Node updates#

  * Enhanced nodes: Chat Trigger, Google Cloud Firestore, Qdrant Vector Store, Splunk, Telegram
  * Deprecated node: Orbit (product shut down)

### Beta Feature Removal#

The Ask AI beta feature for the HTTP Request node has been removed from this version

### Contributors#

[Stanley Yoshinori Takamatsu](https://github.com/stanleytakamatsu)  
[CodeShakingSheep](https://github.com/CodeShakingSheep)  
[jeanpaul](https://github.com/jeanpaul)  
[adrian-martinez-onestic](https://github.com/adrian-martinez-onestic)  
[Malki Davis](https://github.com/mxdavis)

## n8n@1.49.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.48.3...n8n@1.49.0) for this version.  
**Release date:** 2024-07-03

This release contains a new node, node enhancements, and bug fixes.

### Node updates#

  * New node added: [Vector Store Tool](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore/) for the AI Agent
  * Enhanced nodes: Zep Cloud Memory, Copper, Embeddings Cohere, GitHub, Merge, Zammad

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Jochem](https://github.com/jvdweerthof)  
[KhDu](https://github.com/KhDu)  
[Nico Weichbrodt](https://github.com/envy)  
[Pavlo Paliychuk](https://github.com/paul-paliychuk)

## n8n@1.48.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.48.2...n8n@1.48.3) for this version.  
**Release date:** 2024-07-03

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.47.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.47.2...n8n@1.47.3) for this version.  
**Release date:** 2024-07-03

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.48.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.48.1...n8n@1.48.2) for this version.  
**Release date:** 2024-07-01

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.47.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.47.1...n8n@1.47.2) for this version.  
**Release date:** 2024-07-01

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.48.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.48.0...n8n@1.48.1) for this version.  
**Release date:** 2024-06-27

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.48.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.47.1...n8n@1.48.0) for this version.  
**Release date:** 2024-06-27

This release contains bug fixes and feature enhancements.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[KubeAl](https://github.com/KubeAl)

## n8n@1.47.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.47.0...n8n@1.47.1) for this version.  
**Release date:** 2024-06-26

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.47.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.46.0...n8n@1.47.0) for this version.  
**Release date:** 2024-06-20

Breaking change

Calling `$(...).last()` (or `(...).first()` or `$(...).all()`) without arguments now returns the last item (or first or all items) of the output that connects two nodes. Previously, it returned the item/items of the first output of that node. Refer to the [breaking changes log](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md#1470) for details.

This release contains bug fixes, feature enhancements, a new node, node enhancements and performance improvements.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

#### New node: HTTP request tool#

This release adds the HTTP request tool. You can use it with an AI agent as a tool to collect information from a website or API. Refer to the [HTTP request tool](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolhttprequest/) for details.

### Contributors#

[Daniel](https://github.com/daniel-alba17)  
[ekadin-mtc](https://github.com/ekadin-mtc)  
[Eric Francis](https://github.com/EricFrancis12)  
[Josh Sorenson](https://github.com/joshsorenson)  
Mohammad Alsmadi [Nikolai T. Jensen](https://github.com/ch0wm3in)  
[n8n-ninja](https://github.com/n8n-ninja)  
[pebosi](https://github.com/pebosi)  
[Taylor Hoffmann](https://github.com/TaylorHo)

## n8n@1.45.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.45.0...n8n@1.45.1) for this version.  
**Release date:** 2024-06-12

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.46.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.45.0...n8n@1.46.0) for this version.  
**Release date:** 2024-06-12

This release contains feature enhancements, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Jean Khawand](https://github.com/jeankhawand)  
[pemontto](https://github.com/pemontto)  
[Valentin Coppin](https://github.com/valimero)

## n8n@1.44.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.44.1...n8n@1.44.2) for this version.  
**Release date:** 2024-06-12

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.42.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.42.1...n8n@1.42.2) for this version.  
**Release date:** 2024-06-10

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.45.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.44.1...n8n@1.45.0) for this version.  
**Release date:** 2024-06-06

This release contains new features, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.44.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.44.0...n8n@1.44.1) for this version.  
**Release date:** 2024-06-03

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.44.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.43.1...n8n@1.44.0) for this version.  
**Release date:** 2024-05-30

This release contains new features, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.43.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.43.0...n8n@1.43.1) for this version.  
**Release date:** 2024-05-28

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.43.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.42.1...n8n@1.43.0) for this version.  
**Release date:** 2024-05-22

This release contains new features, node enhancements, and bug fixes.

Backup recommended

Although this release doesn't include a breaking change, it is a significant update including database migrations. n8n recommends backing up your data before updating to this version.

Credential sharing required for manual executions

Instance owners and admins: you will see changes if you try to manually execute a workflow where the credentials aren't shared with you. Manual workflow executions now use the same permissions checks as production executions, meaning you can't do a manual execution of a workflow if you don't have access to the credentials. Previously, owners and admins could do manual executions without credentials being shared with them. To resolve this, the credential creator needs to [share the credential](../credentials/credential-sharing/) with you.

#### New feature: Projects#

With projects and roles, you can give your team access to collections of workflows and credentials, rather than having to share each workflow and credential individually. Simultaneously, you tighten security by limiting access to people on the relevant team.   
  
Refer to the [RBAC](../user-management/rbac/) documentation for information on creating projects and using roles.   
  
The number of projects and role types vary depending on your plan. Refer to [Pricing](https://n8n.io/pricing/) for details.

#### New node: Slack Trigger#

This release adds a trigger node for Slack. Refer to the [Slack Trigger documentation](../integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger/) for details.

### Other highlights#

  * Improved [memory support for OpenAI assistants](../integrations/builtin/app-nodes/n8n-nodes-langchain.openai/).

### Rolling back to a previous version#

If you update to this version, then decide you need to role back:

Self-hosted n8n:

  1. Delete any RBAC projects you created.
  2. Revert the database migrations using `n8n db:revert`.

Cloud: contact [help@n8n.io](mailto:help@n8n.io).

### Contributors#

[Ayato Hayashi](https://github.com/hayashi-ay)  
[Daniil Zobov](https://github.com/ddzobov)  
[Guilherme Barile](https://github.com/GuilhermeBarile)  
[Romain MARTINEAU](https://github.com/RJiraya)

## n8n@1.42.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.42.0...n8n@1.42.1) for this version.  
**Release date:** 2024-05-20

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.41.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.41.0...n8n@1.41.1) for this version.  
**Release date:** 2024-05-16

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.42.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.41.0...n8n@1.42.0) for this version.  
**Release date:** 2024-05-15

This release contains new features, node enhancements, and bug fixes.

Note that this release removes the AI error debugger. We're working on a new and improved version.

#### New feature: Tools Agent#

This release adds a new option to the Agent node: the [Tools Agent](../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent/).

This agent has an enhanced ability to work with tools, and can ensure a standard output format. This is now the recommended default agent.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Mike Quinlan](https://github.com/mjquinlan2000)  
[guangwu](https://github.com/testwill)

## n8n@1.41.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.40.0...n8n@1.41.0) for this version.  
**Release date:** 2024-05-08

This release contains new features, node enhancements, and bug fixes.

Note that this release temporarily disables the AI error helper.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Florin Lungu](https://github.com/floryn90)

## n8n@1.40.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.39.1...n8n@1.40.0) for this version.  
**Release date:** 2024-05-02

Breaking change

Please note that this version contains a breaking change for instances using a Postgres database. The default value for the DB_POSTGRESDB_USER environment variable was switched from `root` to `postgres`. Refer to the [breaking changes log](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md#1400) for details.

This release contains new features, new nodes, node enhancements, and bug fixes.

#### New feature: Ask AI in the HTTP node#

You can now ask AI to help create API requests in the HTTP Request node:

  1. In the HTTP Request node, select **Ask AI**.
  2. Enter the **Service** and **Request** you want to use. For example, to use the NASA API to get their picture of the day, enter `NASA` in **Service** and `get picture of the day` in **Request**.
  3. Check the parameters: the AI tries to fill them out, but you may still need to adjust or correct the configuration.

Self-hosted users need to [enable AI features and provide their own API keys](../hosting/configuration/environment-variables/)

#### New node: Groq Chat Model#

This release adds the [Groq Chat Model node](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq/).

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Alberto Pasqualetto](https://github.com/albertopasqualetto)  
[Bram Kn](https://github.com/bramkn)  
[CodeShakingSheep](https://github.com/CodeShakingSheep)  
[Nicolas-nwb](https://github.com/Nicolas-nwb)  
[pemontto](https://github.com/pemontto)  
[pengqiseven](https://github.com/pengqiseven)  
[webk](https://github.com/webkp)  
[Yoshino-s](https://github.com/Yoshino-s)

## n8n@1.39.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.39.0...n8n@1.39.1) for this version.  
**Release date:** 2024-04-25

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.38.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.38.1...n8n@1.38.2) for this version.  
**Release date:** 2024-04-25

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.37.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.37.3...n8n@1.37.4) for this version.  
**Release date:** 2024-04-25

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.39.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.38.1...n8n@1.39.0) for this version.  
**Release date:** 2024-04-24

This release contains new nodes, node enhancements, and bug fixes.

#### New node: WhatsApp Trigger#

This release adds the [WhatsApp Trigger node](../integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger/).

#### Node enhancement: Multiple methods, one Webhook node#

The Webhook Trigger node can now handle calls to multiple HTTP methods. Refer to the [Webhook node documentation](../integrations/builtin/core-nodes/n8n-nodes-base.webhook/common-issues/#listen-for-multiple-http-methods) for information on enabling this.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Bram Kn](https://github.com/bramkn)

## n8n@1.38.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.38.0...n8n@1.38.1) for this version.  
**Release date:** 2024-04-18

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.37.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.37.2...n8n@1.37.3) for this version.  
**Release date:** 2024-04-18

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.38.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.37.2...n8n@1.38.0) for this version.  
**Release date:** 2024-04-17

This release contains new nodes, bug fixes, and node enhancements.

#### New node: Google Gemini Chat Model#

This release adds the [Google Gemini Chat Model sub-node](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini/).

#### New node: Embeddings Google Gemini#

This release adds the [Google Gemini Embeddings sub-node](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini/).

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Chengyou Liu](https://github.com/cyliu0)  
[Francesco Mannino](https://github.com/manninofrancesco)

## n8n@1.37.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.37.1...n8n@1.37.2) for this version.  
**Release date:** 2024-04-17

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.36.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.36.3...n8n@1.36.4) for this version.  
**Release date:** 2024-04-15

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.36.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.36.2...n8n@1.36.3) for this version.  
**Release date:** 2024-04-12

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.37.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.37.0...n8n@1.37.1) for this version.  
**Release date:** 2024-04-11

Breaking change

Please note that this version contains a breaking change for self-hosted n8n. It removes the `--file` flag for the `execute` CLI command. If you have scripts relying on the `--file` flag, update them to first import the workflow and then execute it using the `--id` flag. Refer to [CLI commands](../hosting/cli-commands/) for more information on CLI options.

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.36.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.36.1...n8n@1.36.2) for this version.  
**Release date:** 2024-04-11

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.37.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.36.1...n8n@1.37.0) for this version.  
**Release date:** 2024-04-10

Breaking change

Please note that this version contains a breaking change for self-hosted n8n. It removes the `--file` flag for the `execute` CLI command. If you have scripts relying on the `--file` flag, update them to first import the workflow and then execute it using the `--id` flag. Refer to [CLI commands](../hosting/cli-commands/) for more information on CLI options.

This release contains a new node, improvements to error handling and messaging, node enhancements, and bug fixes.

#### New node: JWT#

This release adds the [JWT core node](../integrations/builtin/core-nodes/n8n-nodes-base.jwt/).

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Miguel Prytoluk](https://github.com/mprytoluk)

## n8n@1.36.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.36.0...n8n@1.36.1) for this version.  
**Release date:** 2024-04-04

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.36.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.35.0...n8n@1.36.0) for this version.  
**Release date:** 2024-04-03

This release contains new nodes, enhancements and bug fixes.

#### New node: Salesforce Trigger node#

This release adds the [Salesforce Trigger node](../integrations/builtin/trigger-nodes/n8n-nodes-base.salesforcetrigger/).

#### New node: Twilio Trigger node#

This release adds the [Twilio Trigger node](../integrations/builtin/trigger-nodes/n8n-nodes-base.twiliotrigger/).

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.35.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.34.2...n8n@1.35.0) for this version.  
**Release date:** 2024-03-28

This release contains enhancements and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.34.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.34.1...n8n@1.34.2) for this version.  
**Release date:** 2024-03-26

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.34.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.34.0...n8n@1.34.1) for this version.  
**Release date:** 2024-03-25

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.34.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.33.1...n8n@1.34.0) for this version.  
**Release date:** 2024-03-20

This release contains new features, new nodes, and bug fixes.

#### New node: Microsoft OneDrive Trigger node#

This release adds the [Microsoft OneDrive Trigger node](../integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftonedrivetrigger/). You can now trigger workflows on file and folder creation and update events.

#### New data transformation functions#

This release introduces new [data transformation functions](../code/builtin/data-transformation-functions/):

**String**
    
    
    1
    2
    3
    4
    5
    6

| 
    
    
    toDateTime() //replaces toDate(). toDate() is retained for backwards compatability.
    parseJson()
    extractUrlPath()
    toBoolean()
    base64Encode()
    base64Decode()
      
  
---|---  
  
**Number**
    
    
    1
    2

| 
    
    
    toDateTime()
    toBoolean()
      
  
---|---  
  
**Object**
    
    
    1

| 
    
    
    toJsonString()
      
  
---|---  
  
**Array**
    
    
    1

| 
    
    
    toJsonString()
      
  
---|---  
  
**Date & DateTime**
    
    
    1
    2

| 
    
    
    toDateTime()
    toInt()
      
  
---|---  
  
**Boolean**
    
    
    1

| 
    
    
    toInt()
      
  
---|---  
  
### Contributors#

[Bram Kn](https://github.com/bramkn)  
[pemontto](https://github.com/pemontto)

## n8n@1.33.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.33.0...n8n@1.33.1) for this version.  
**Release date:** 2024-03-15

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.32.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.32.1...n8n@1.32.2) for this version.  
**Release date:** 2024-03-15

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.33.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.32.1...n8n@1.33.0) for this version.  
**Release date:** 2024-03-13

This release contains new features, node enhancements, and bug fixes.

#### Support for Claude 3#

This release adds support for Claude 3 to the [Anthropic Chat Model](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic/) node.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[gumida](https://github.com/gumida)  
[Ayato Hayashi](https://github.com/hayashi-ay)  
[Jordan](https://github.com/jordanburke)  
[MC Naveen](https://github.com/mcnaveen)

## n8n@1.32.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.32.0...n8n@1.32.1) for this version.  
**Release date:** 2024-03-07

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.31.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.31.1...n8n@1.31.2) for this version.  
**Release date:** 2024-03-07

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.32.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.31.1...n8n@1.32.0) for this version.  
**Release date:** 2024-03-06

This release contains new features, node enhancements, performance improvements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.31.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.31.0...n8n@1.31.1) for this version.  
**Release date:** 2024-03-06

Breaking changes

Please note that this version contains a breaking change. HTTP connections to the editor will fail on domains other than localhost. You can read more about it [here](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md#1320).

This is a bug fix release and it contains a breaking change.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.31.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.30.0...n8n@1.31.0) for this version.  
**Release date:** 2024-02-28

This release contains new features, new nodes, node enhancements and bug fixes.

#### New nodes: Microsoft Outlook trigger and Ollama embeddings#

This release adds two new nodes.

  * [Microsoft Outlook Trigger](../integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger/)
  * [Ollama Embeddings](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama/)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.30.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.30.0...n8n@1.30.1) for this version.  
**Release date:** 2024-02-23

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.30.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.29.1...n8n@1.30.0) for this version.  
**Release date:** 2024-02-21

This release contains new features, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.29.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.29.0...n8n@1.29.1) for this version.  
**Release date:** 2024-02-16

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.29.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.28.0...n8n@1.29.0) for this version.  
**Release date:** 2024-02-15

This release contains new features, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### New features#

#### OpenAI node overhaul#

This release includes a new version of the [OpenAI node](../integrations/builtin/app-nodes/n8n-nodes-langchain.openai/), adding more operations, including support for working with assistants.

Other highlights:

  * Support for AI events in [log streaming](../log-streaming/).
  * Added support for workflow tags in the [public API](../api/).

### Contributors#

[Bruno Inec](https://github.com/sweenu)  
[Jesús Burgers](https://github.com/jburgers-chakray)

## n8n@1.27.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.27.2...n8n@1.27.3) for this version.  
**Release date:** 2024-02-15

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.28.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.27.2...n8n@1.28.0) for this version.  
**Release date:** 2024-02-07

This release contains new features, new nodes, node enhancements and bug fixes.

#### New nodes: Azure OpenAI chat model and embeddings#

This release adds two new nodes to work with [Azure OpenAI](https://azure.microsoft.com/en-gb/products/ai-services/openai-service/) in your advanced AI workflows:

  * [Embeddings Azure OpenAI](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai/)
  * [Azure OpenAI Chat Model](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai/)

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Andrea Ascari](https://github.com/ascariandrea)

## n8n@1.27.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.27.1...n8n@1.27.2) for this version.  
**Release date:** 2024-02-02

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.27.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.26.0...n8n@1.27.1) for this version.  
**Release date:** 2024-01-31

This release contains new features, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.27.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.26.0...n8n@1.27.0) for this version.  
**Release date:** 2024-01-31

Breaking change

This release removes `own` mode for self-hosted n8n. You must now use `EXECUTIONS_MODE` and set to either `regular` or `queue`. Refer to [Queue mode](../hosting/scaling/queue-mode/) for information on configuring queue mode.

Skip this release

Please upgrade directly to 1.27.1.

This release contains node enhancements and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.26.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.25.1...n8n@1.26.0) for this version.  
**Release date:** 2024-01-24

This release contains new features, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Daniel Schröder](https://github.com/schroedan)  
[Nihaal Sangha](https://github.com/nihaals)

## n8n@1.25.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.25.0...n8n@1.25.1) for this version.  
**Release date:** 2024-01-22

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Nihaal Sangha](https://github.com/nihaals)

## n8n@1.25.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.24.1...n8n@1.25.0) for this version.  
**Release date:** 2024-01-17

This release contains a new node, feature improvements, and bug fixes.

#### New node: Chat Memory Manager#

The [Chat Memory Manager](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager/) node replaces the Chat Messages Retriever node. It manages chat message memories within your AI workflows.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.24.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.24.0...n8n@1.24.1) for this version.  
**Release date:** 2024-01-16

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.22.6#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.22.5...n8n@1.22.6) for this version.  
**Release date:** 2024-01-10

This is a bug fix release. It includes important fixes for the HTTP Request and monday.com nodes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.24.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.23.0...n8n@1.24.0) for this version.  
**Release date:** 2024-01-10

This release contains new nodes for advanced AI, node enhancements, new features, performance enhancements, and bug fixes.

#### Chat trigger#

n8n has created a new [Chat Trigger node](../integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/). The new node provides a chat interface that you can make publicly available, with customization and authentication options.

#### Mistral Cloud Chat and Embeddings#

This release introduces two new nodes to support [Mistral AI](https://mistral.ai/):

  * [Mistral Cloud Chat Model](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud/)
  * [Embeddings Mistral Cloud](../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud/)

### Contributors#

[Anush](https://github.com/Anush008)  
[Eric Koleda](https://github.com/ekoleda-codaio)  
[Mason Geloso](https://github.com/MasonGeloso)  
[vacitbaydarman](https://github.com/vacitbaydarman)

## n8n@1.22.5#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.22.4...n8n@1.22.5) for this version.  
**Release date:** 2024-01-09

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.23.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.22.4...n8n@1.23.0) for this version.  
**Release date:** 2024-01-03

This release contains new nodes, node enhancements, new features, and bug fixes.

#### New nodes and improved experience for working with files#

This release includes a major overhaul of nodes relating to files (binary data).

There are now three key nodes dedicated to handling binary data files:

  * [Read/Write Files from Disk](../integrations/builtin/core-nodes/n8n-nodes-base.readwritefile/) to read and write files from/to the machine where n8n is running.
  * [Convert to File](../integrations/builtin/core-nodes/n8n-nodes-base.converttofile/) to take input data and output it as a file.
  * [Extract From File](../integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile/) to get data from a binary format and convert it to JSON.

n8n has moved support for iCalendar, PDF, and spreadsheet formats into these nodes, and removed the iCalendar, Read PDF, and Spreadsheet File nodes. There are still standalone nodes for [HTML](../integrations/builtin/core-nodes/n8n-nodes-base.html/) and [XML](../integrations/builtin/core-nodes/n8n-nodes-base.xml/).

#### New node: Qdrant vector store#

This release adds support for [Qdrant](https://qdrant.tech/) with the Qdrant vector store node.

Read n8n's [Qdrant vector store node documentation](../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant/)

### Contributors#

[Aaron Gutierrez](https://github.com/aarongut)  
[Advaith Gundu](https://github.com/geodic)  
[Anush](https://github.com/Anush008)  
[Bin](https://github.com/soulhat)  
[Nihaal Sangha](https://github.com/nihaals)

## n8n@1.22.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.22.3...n8n@1.22.4) for this version.  
**Release date:** 2024-01-03

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.22.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.22.2...n8n@1.22.3) for this version.  
**Release date:** 2023-12-27

Upgrade directly to 1.22.4

Due to issues with this release, upgrade directly to 1.22.4.

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.22.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.22.1...n8n@1.22.2) for this version.  
**Release date:** 2023-12-27

Upgrade directly to 1.22.4

Due to issues with this release, upgrade directly to 1.22.4.

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.22.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.22.0...n8n@1.22.1) for this version.  
**Release date:** 2023-12-21

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.22.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.21.1...n8n@1.22.0) for this version.  
**Release date:** 2023-12-21

This release contains node enhancements, new features, performance improvements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.18.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.18.3...n8n@1.18.4) for this version.  
**Release date:** 2023-12-19

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.21.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.20.0...n8n@1.21.1) for this version.  
**Release date:** 2023-12-15

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.18.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.18.2...n8n@1.18.3) for this version.  
**Release date:** 2023-12-15

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.21.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.20.0...n8n@1.21.0) for this version.  
**Release date:** 2023-12-13

This release contains new features and nodes, node enhancements, and bug fixes.

#### New user role: Admin#

This release introduces a third account type: admin. This role is available on pro and enterprise plans. Admins have similar permissions to instance owners.

[Read more about user roles](../user-management/account-types/)

#### New data transformation nodes#

This release replaces the Item Lists node with a collection of nodes for data transformation tasks:

  * [Aggregate](../integrations/builtin/core-nodes/n8n-nodes-base.aggregate/): take separate items, or portions of them, and group them together into individual items.
  * [Limit](../integrations/builtin/core-nodes/n8n-nodes-base.aggregate/): remove items beyond a defined maximum number.
  * [Remove Duplicates](../integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/): identify and delete items that are identical across all fields or a subset of fields.
  * [Sort](../integrations/builtin/core-nodes/n8n-nodes-base.sort/): organize lists of in a desired ordering, or generate a random selection.
  * [Split Out](../integrations/builtin/core-nodes/n8n-nodes-base.splitout/): separate a single data item containing a list into multiple items.
  * [Summarize](../integrations/builtin/core-nodes/n8n-nodes-base.summarize/): aggregate items together, in a manner similar to Excel pivot tables.

#### Increased sharing permissions for owners and admins#

Instance owners and users with the admin role can now see and share all workflows and credentials. They can't view sensitive credential information.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.20.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.19.5...n8n@1.20.0) for this version.  
**Release date:** 2023-12-06

This release contains bug fixes, node enhancements, and ongoing new feature work.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Andrey Starostin](https://github.com/mayorandrew)

## n8n@1.19.5#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.19.4...n8n@1.19.5) for this version.  
**Release date:** 2023-12-05

This is a bug fix release.

Breaking change

This release removes the TensorFlow Embeddings node.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.18.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.18.1...n8n@1.18.2) for this version.  
**Release date:** 2023-12-05

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.19.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.19.0...n8n@1.19.4) for this version.  
**Release date:** 2023-12-01

Missing ARM v7 support

This version doesn't support ARM v7. n8n is working on fixing this in future releases.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.19.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.18.0...n8n@1.19.0) for this version.  
**Release date:** 2023-11-29

Upgrade directly to 1.19.4

Due to issues with this release, upgrade directly to 1.19.4.

This release contains new features, node enhancements, and bug fixes.

#### LangChain general availability#

This release adds LangChain support to the main n8n version. Refer to [LangChain](../advanced-ai/langchain/overview/) for more information on how to build AI tools in n8n, the new nodes n8n has introduced, and related learning resources.

#### Show avatars of users working on the same workflow#

This release improves the experience of users collaborating on workflows. You can now see who else is editing at the same time as you.

## n8n@1.18.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.18.0...n8n@1.18.1) for this version.  
**Release date:** 2023-11-30

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.18.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.17.1...n8n@1.18.0) for this version.  
**Release date:** 2023-11-22

This release contains new features and bug fixes.

#### Template creator hub#

Built a template you want to share? This release introduces the n8n Creator hub. Refer to the [creator hub Notion doc](https://www.notion.so/n8n-Creator-hub-7bd2cbe0fce0449198ecb23ff4a2f76f) for more information on this project.

#### Node input and output search filter#

Cloud Pro and Enterprise users can now search and filter the input and output data in nodes. Refer to [Data filtering](../data/data-filtering/) for more information.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.17.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.17.0...n8n@1.17.1) for this version.  
**Release date:** 2023-11-17

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.17.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.16.0...n8n@1.17.0) for this version.  
**Release date:** 2023-11-15

This release contains node enhancements and bug fixes.

#### Sticky Note Colors#

You can now select background colors for sticky notes.

#### Discord Node Overhaul#

An overhaul of the Discord node, improving the UI making it easier to configure, improving error handling, and fixing issues.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[antondollmaier](https://github.com/antondollmaier)  
[teomane](https://github.com/teomane)

## n8n@1.16.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.15.2...n8n@1.16.0) for this version.  
**Release date:** 2023-11-08

This release contains node enhancements and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.15.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.15.1...n8n@1.15.2) for this version.  
**Release date:** 2023-11-07

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.15.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.14.2...n8n@1.15.1) for this version.  
**Release date:** 2023-11-02

This release contains new features, node enhancements, and bug fixes.

#### Workflow history#

This release introduces workflow history: view and load previous versions of your workflows.

Workflow history is available in Enterprise n8n, and with limited history for Cloud Pro.

Learn more in the [Workflow history](../workflows/history/) documentation.

#### Dark mode#

_Almost_ in time for Halloween: this release introduces dark mode.

To enable dark mode:

  1. Select **Settings** > **Personal**.
  2. Under **Personalisation** , change **Theme** to **Dark theme**.

#### Optional error output for nodes#

All nodes apart from sub-nodes and trigger nodes have a new optional output: **Error**. Use this to add steps to handle node errors.

#### Pagination support added to HTTP Request node#

The HTTP Request node now supports an pagination. Read the [node docs](../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) for information and examples.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Yoshino-s](https://github.com/Yoshino-s)

## n8n@1.14.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.14.1...n8n@1.14.2) for this version.  
**Release date:** 2023-10-26

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.14.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.14.0...n8n@1.14.1) for this version.  
**Release date:** 2023-10-26

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.14.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.13.0...n8n@1.14.0) for this version.  
**Release date:** 2023-10-25

This release contains node enhancements and bug fixes.

#### Switch node supports more outputs#

The [Switch node](../integrations/builtin/core-nodes/n8n-nodes-base.switch/) now supports an unlimited number of outputs.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.13.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.12.2...n8n@1.13.0) for this version.  
**Release date:** 2023-10-25

This release contains new features, feature enhancements, and bug fixes.

Upgrade directly to 1.14.0

This release failed to publish to npm. Upgrade directly to 1.14.0.

#### RSS Feed Trigger node#

This releases introduces a new node, the [RSS Feed Trigger](../integrations/builtin/core-nodes/n8n-nodes-base.rssfeedreadtrigger/). Use this node to start a workflow when a new RSS feed item is published.

#### Facebook Lead Ads Trigger node#

This releases add another new node, the [Facebook Lead Ads Trigger](../integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger/). Use this node to trigger a workflow when you get a new lead.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.12.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.12.1...n8n@1.12.2) for this version.  
**Release date:** 2023-10-24

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Burak Akgün](https://github.com/mbakgun)

## n8n@1.12.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.12.0...n8n@1.12.1) for this version.  
**Release date:** 2023-10-23

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Léo Martinez](https://github.com/martinezleoml)

## n8n@1.11.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.11.1...n8n@1.11.2) for this version.  
**Release date:** 2023-10-23

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Inga](https://github.com/inga-lovinde)  
[pemontto](https://github.com/pemontto)

## n8n@1.12.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.11.1...n8n@1.12.0) for this version.  
**Release date:** 2023-10-18

This release contains new features, node enhancements, and bug fixes.

#### Form Trigger node#

This releases introduces a new node, the [n8n Form Trigger](../integrations/builtin/core-nodes/n8n-nodes-base.formtrigger/). Use this node to start a workflow based on a user submitting a form. It provides a configurable form interface.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Damian Karzon](https://github.com/dkarzon)  
[Inga](https://github.com/inga-lovinde)  
[pemontto](https://github.com/pemontto)

## n8n@1.11.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.11.0...n8n@1.11.1) for this version.  
**Release date:** 2023-10-13

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.11.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.10.1...n8n@1.11.0) for this version.  
**Release date:** 2023-10-11

This release contains new features and bug fixes.

#### External storage for binary files#

Self-hosted users can now use an external service to store binary data. Learn more in [External storage](../hosting/scaling/external-storage/).

If you're using n8n Cloud and are interested in this feature, please [contact n8n](https://n8n-community.typeform.com/to/y9X2YuGa).

#### Item Lists node supports binary data#

The Item Lists node now supports splitting and concatenating binary data inputs. This means you no longer need to use code to split a collection of files into multiple items.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.10.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.10.0...n8n@1.10.1) for this version.  
**Release date:** 2023-10-11

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.9.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.9.2...n8n@1.9.3) for this version.  
**Release date:** 2023-10-10

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.9.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.9.1...n8n@1.9.2) for this version.  
**Release date:** 2023-10-09

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.10.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.9.1...n8n@1.10.0) for this version.  
**Release date:** 2023-10-05

This release contains bug fixes and preparatory work for new features.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.9.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.9.0...n8n@1.9.1) for this version.  
**Release date:** 2023-10-04

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## LangChain in n8n (beta)#

**Release date:** 2023-10-04

This release introduces support for building with LangChain in n8n.

With n8n's LangChain nodes you can build AI-powered functionality within your workflows. The LangChain nodes are configurable, meaning you can choose your preferred agent, LLM, memory, and other components. Alongside the LangChain nodes, you can connect any n8n node as normal: this means you can integrate your LangChain logic with other data sources and services.

Read more:

  * This is a beta release, and not yet available in the main product. Follow the instructions in [Access LangChain in n8n](../advanced-ai/langchain/overview/) to try it out. Self-hosted and Cloud options are available.
  * Learn how LangChain concepts map to n8n nodes in [LangChain concepts in n8n](../advanced-ai/langchain/langchain-n8n/).
  * Browse n8n's new [Cluster nodes](../integrations/builtin/cluster-nodes/). This is a new set of node types that allows for multiple nodes to work together to configure each other.

## n8n@1.9.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.8.2...n8n@1.9.0) for this version.  
**Release date:** 2023-09-28

This release contains new features, performance improvements, and bug fixes.

#### Tournament#

This releases replaces RiotTmpl, the templating language used in expressions, with n8n's own templating language, [Tournament](https://github.com/n8n-io/tournament). You can now use arrow functions in expressions.  

#### `N8N_BINARY_DATA_TTL` and `EXECUTIONS_DATA_PRUNE_TIMEOUT` removed#

The environment variables `N8N_BINARY_DATA_TTL` and `EXECUTIONS_DATA_PRUNE_TIMEOUT` no longer have any effect and can be removed. Instead of relying on a TTL system for binary data, n8n cleans up binary data together with executions during pruning.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.8.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.8.1...n8n@1.8.2) for this version.  
**Release date:** 2023-09-25

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.8.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.8.0...n8n@1.8.1) for this version.  
**Release date:** 2023-09-21

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.8.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.7.1...n8n@1.8.0) for this version.  
**Release date:** 2023-09-20

This release contains node enhancements and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.7.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.7.0...n8n@1.7.1) for this version.  
**Release date:** 2023-09-14

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.7.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.6.1...n8n@1.7.0) for this version.  
**Release date:** 2023-09-13

This release contains node enhancements and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Quang-Linh LE](https://github.com/linktohack)  
[MC Naveen](https://github.com/mcnaveen)

## n8n@1.6.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.6.0...n8n@1.6.1) for this version.  
**Release date:** 2023-09-06

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.6.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.5.1...n8n@1.6.0) for this version.  
**Release date:** 2023-09-06

This release contains bug fixes, new features, and node enhancements.

Upgrade directly to 1.6.1

Skip this version and upgrade directly to 1.6.1, which contains essential bug fixes.

#### TheHive 5#

This release introduces support for TheHive API version 5. This uses a new node and credentials:

  * [TheHive 5 node](../integrations/builtin/app-nodes/n8n-nodes-base.thehive5/)
  * [TheHive 5 Trigger node](../integrations/builtin/trigger-nodes/n8n-nodes-base.thehive5trigger/)
  * [TheHive 5 credentials](../integrations/builtin/credentials/thehive5/)

#### `N8N_PERSISTED_BINARY_DATA_TTL` removed#

The environment variables `N8N_PERSISTED_BINARY_DATA_TTL` no longer has any effect and can be removed. This legacy flag was originally introduced to support ephemeral executions (see [details](https://github.com/n8n-io/n8n/pull/7046)), which are no longer supported.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.5.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.5.0...n8n@1.5.1) for this version.  
**Release date:** 2023-08-31

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.5.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.4.1...n8n@1.5.0) for this version.  
**Release date:** 2023-08-31

This release contains new features, node enhancements, and bug fixes.

Upgrade directly to 1.5.1

Skip this version and upgrade directly to 1.5.1, which contains essential bug fixes.

### Highlights#

#### External secrets storage for credentials#

Enterprise-tier accounts can now use external secrets vaults to manage credentials in n8n. This allows you to store credential information securely outside your n8n instance. n8n supports Infisical and HashiCorp Vault.

Refer to [External secrets](../external-secrets/) for guidance on enabling and using this feature.

#### Two-factor authentication#

n8n now supports two-factor authentication (2FA) for self-hosted instances. n8n is working on bringing support to Cloud. Refer to [Two-factor authentication](../user-management/two-factor-auth/) for guidance on enabling and using it.

#### Debug executions#

Users on a paid n8n plan can now load data from previous executions into their current workflow. This is useful when debugging a failed execution.

Refer to [Debug executions](../workflows/executions/debug/) for guidance on using this feature.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.4.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.4.0...n8n@1.4.1) for this version.  
**Release date:** 2023-08-29

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.4.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.3.1...n8n@1.4.0) for this version.  
**Release date:** 2023-08-23

This release contains new features, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[pemontto](https://github.com/pemontto)

## n8n@1.3.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.3.0...n8n@1.3.1) for this version.  
**Release date:** 2023-08-18

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.3.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.2.2...n8n@1.3.0) for this version.  
**Release date:** 2023-08-16

This release contains new features and bug fixes.

### Highlights#

#### Trial feature: AI support in the Code node#

This release introduces limited support for using AI to generate code in the Code node. Initially this feature is only available on Cloud, and will gradually be rolled out, starting with about 20% of users.

Learn how to use the feature, including guidance on writing prompts, in [Generate code with ChatGPT](../code/ai-code/).

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Ian Gallagher](https://github.com/craSH)  
[Xavier Calland](https://github.com/xavier-calland)

## n8n@1.2.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.2.1...n8n@1.2.2) for this version.  
**Release date:** 2023-08-14

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.2.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.2.0...n8n@1.2.1) for this version.  
**Release date:** 2023-08-09

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.2.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.1.1...n8n@1.2.0) for this version.  
**Release date:** 2023-08-09

This release contains new features, node enhancements, bug fixes, and performance improvements.

Upgrade directly to 1.2.1

When upgrading, skip this release and go directly to 1.2.1.

### Highlights#

#### Credential support for SecOps services#

This release introduces support for setting up credentials in n8n for the following services:

  * [AlienVault](../integrations/builtin/credentials/alienvault/)
  * [Auth0 Management](../integrations/builtin/credentials/auth0management/)
  * [Carbon Black API](../integrations/builtin/credentials/carbonblack/)
  * [Cisco Meraki API](../integrations/builtin/credentials/ciscomeraki/)
  * [Cisco Secure Endpoint](../integrations/builtin/credentials/ciscosecureendpoint/)
  * [Cisco Umbrella API](../integrations/builtin/credentials/ciscoumbrella/)
  * [CrowdStrike](../integrations/builtin/credentials/crowdstrike/)
  * [F5 Big-IP](../integrations/builtin/credentials/f5bigip/)
  * [Fortinet FortiGate](../integrations/builtin/credentials/fortigate/)
  * [Hybrid Analysis](../integrations/builtin/credentials/hybridanalysis/)
  * [Imperva WAF](../integrations/builtin/credentials/impervawaf/)
  * [Kibana](../integrations/builtin/credentials/kibana/)
  * [Microsoft Entra ID](../integrations/builtin/credentials/microsoftentra/)
  * [Mist](../integrations/builtin/credentials/mist/)
  * [Okta](../integrations/builtin/credentials/okta/)
  * [OpenCTI](../integrations/builtin/credentials/opencti/)
  * [QRadar](../integrations/builtin/credentials/qradar/)
  * [Qualys](../integrations/builtin/credentials/qualys/)
  * [Recorded Future](../integrations/builtin/credentials/recordedfuture/)
  * [Sekoia](../integrations/builtin/credentials/sekoia/)
  * [Shuffler](../integrations/builtin/credentials/shuffler/)
  * [Trellix ePO](../integrations/builtin/credentials/trellixepo/)
  * [VirusTotal](../integrations/builtin/credentials/virustotal/)
  * [Zscaler ZIA](../integrations/builtin/credentials/zscalerzia/)

This makes it easier to do [Custom operations](../integrations/custom-operations/) with these services, using the [HTTP Request](../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) node.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.1.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.1.0...n8n@1.1.1) for this version.  
**Release date:** 2023-07-27

This is a bug fix release.

Breaking changes

Please note that this version contains breaking changes if upgrading from a `0.x.x` version. For full details, refer to the [n8n v1.0 migration guide](../1-0-migration-checklist/).

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.1.0#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.0.5...n8n@1.1.0) for this version.  
**Release date:** 2023-07-26

This release contains new features, bug fixes, and node enhancements.

Breaking changes

Please note that this version contains breaking changes if upgrading from a `0.x.x` version. For full details, refer to the [n8n v1.0 migration guide](../1-0-migration-checklist/).

### Highlights#

#### Source control and environments#

This release introduces source control and environments for enterprise users.

n8n uses Git-based source control to support environments. Linking your n8n instances to a Git repository lets you create multiple n8n environments, backed by Git branches.

Refer to [Source control and environments](../source-control-environments/) to learn more about the features and set up your environments.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Adrián Martínez](https://github.com/adrian-martinez-vdshop)  
[Alberto Pasqualetto](https://github.com/albertopasqualetto)  
[Marten Steketee](https://github.com/Marten-S)  
[perseus-algol](https://github.com/perseus-algol)  
[Sandra Ashipala](https://github.com/sandramsc)  
[ZergRael](https://github.com/ZergRael)

## n8n@1.0.5#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.0.4...n8n@1.0.5) for this version.  
**Release date:** 2023-07-24

This is a bug fix release.

Breaking changes

Please note that this version contains breaking changes if upgrading from a `0.x.x` version. For full details, refer to the [n8n v1.0 migration guide](../1-0-migration-checklist/).

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

## n8n@1.0.4#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.0.3...n8n@1.0.4) for this version.  
**Release date:** 2023-07-19

This is a bug fix release.

Breaking changes

Please note that this version contains breaking changes if upgrading from a `0.x.x` version. For full details, refer to the [n8n v1.0 migration guide](../1-0-migration-checklist/).

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Romain Dunand](https://github.com/airmoi)  
[noctarius aka Christoph Engelbert](https://github.com/noctarius)

## n8n@1.0.3#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.0.2...n8n@1.0.3) for this version.  
**Release date:** 2023-07-13

This release contains API enhancements and adds support for sending messages to forum threads in the Telegram node.

Breaking changes

Please note that this version contains breaking changes if upgrading from a `0.x.x` version. For full details, refer to the [n8n v1.0 migration guide](../1-0-migration-checklist/).

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases) on GitHub.

### Contributors#

[Kirill](https://github.com/chrtkv)

## n8n@1.0.2#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.0.1...n8n@1.0.2) for this version.  
**Release date:** 2023-07-05

This is a bug fix release.

Breaking changes

Please note that this version contains breaking changes if upgrading from a `0.x.x` version. For full details, refer to the [n8n v1.0 migration guide](../1-0-migration-checklist/).

### Contributors#

[Romain Dunand](https://github.com/airmoi)

## n8n@1.0.1#

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.0.0...n8n@1.0.1) for this version.  
**Release date:** 2023-07-05

Breaking changes

Please note that this version contains breaking changes. For full details, refer to the [n8n v1.0 migration guide](../1-0-migration-checklist/).

This is n8n's version one release.

For full details, refer to the [n8n v1.0 migration guide](../1-0-migration-checklist/).

### Highlights#

#### Python support#

Although JavaScript remains the default language, you can now also select Python as an option in the [Code node](../code/code-node/) and even make use of [many Python modules](https://pyodide.org/en/stable/usage/packages-in-pyodide.html#packages-in-pyodide). Note that Python is unavailable in Code nodes added to a workflow before v1.0.

### Contributors#

[Marten Steketee](https://github.com/Marten-S)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top