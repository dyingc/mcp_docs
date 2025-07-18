# Set up automation rules | 🦜️🛠️ LangSmith

On this page

While you can manually sift through and process production logs from our LLM application, it often becomes difficult as your application scales to more users. LangSmith provides a powerful feature called automations that allow you to trigger certain actions on your trace data. At a high level, automations are defined by a **filter** , **sampling rate** , and **action**.

Automation rules can trigger actions such as online evaluation, adding inputs/outputs of traces to a dataset, adding to an annotation queue, and triggering a webhook.

An example of an automation you can set up can be _"trigger an online evaluation that grades on vagueness for all of my downvoted traces."_

## Create a rule​

We will outline the steps for creating an automation rule in LangSmith below.

### Step 1: Navigate to rule creation​

To create a rule, head click on **Rules** in the top right corner of any project details page, then scroll to the bottom and click on **\+ Add Rule**.

![](/assets/images/add_automation_rule-0c0ef9b379005d13684634332636e758.png)

_Alternatively_ , you can access rules in settings by navigating to [this link](https://smith.langchain.com/settings/workspaces/rules), click on **\+ Add Rule** , then **Project Rule**.

note

There are currently two types of rules you can create: **Project Rule** and **Dataset Rule**.

  * **Project Rule** : This rule will apply to traces in the specified project. Actions allowed are adding to a dataset, adding to an annotation queue, running online evaluation, and triggering a webhook.
  * **Dataset Rule** : This rule will apply to traces that are part of an experiment in the specified dataset. Actions allowed are only running an evaluator on the experiment results. To see this in action, you can follow [this guide](/evaluation/how_to_guides/run_evaluation_from_prompt_playground).

Give your rule a name, for example "my_rule":

![](/assets/images/give_rule_name-b4dd6615be519422d890b7f4834ca438.png)

### Step 2: Define the filter​

You can create a filter as you normally would to filter traces in the project. For more information on filters, you can refer to [this guide](/observability/how_to_guides/filter_traces_in_application).

![](/assets/images/rules_filter-3450cda01142e59c5b6ac5ea2080bcea.png)

### (Optional) Step 3: Apply Rule to Past Runs​

When creating a new rule, you can apply the rule to past runs as well. To do this, select **Apply to Past Runs** checkbox and enter **Backfill From** date as the start date to apply the rule.

This will start from the **Backfill From** date and apply the run rules until it is caught up with the latest runs.

![](/assets/images/rules_past_runs-304ff5e82bcc8f8825393aa73aaba491.png)

Note that you will have to expand the date range for logs if you wanted to look at the progress of the backfill, see [View logs for your automations](/observability/how_to_guides/rules#view-logs-for-your-automations) for details.

### Step 4: Define the sampling rate​

You can specify a sampling rate (between 0 and 1) for automations. This will control the percent of the filtered runs that are sent to an automation action. For example, if you set the sampling rate to 0.5, then 50% of the traces that pass the filter will be sent to the action.

### Step 5: Define the action​

There are four actions you can take with an automation rule:

  * **Add to dataset** : Add the inputs and outputs of the trace to a dataset.
  * **Add to annotation queue** : Add the trace to an annotation queue.
  * **Run online evaluation** : Run an online evaluation on the trace. For more information on online evaluations, you can refer to [this guide](/observability/how_to_guides/online_evaluations).
  * **Trigger webhook** : Trigger a webhook with the trace data. For more information on webhooks, you can refer to [this guide](/observability/how_to_guides/webhooks).
  * **Extend data retention** : Extends the data retention period on matching traces that use base retention [(see data retention docs for more details)](/administration/concepts#data-retention). Note that all other rules will also extend data retention on matching traces through the auto-upgrade mechanism described in the aforementioned data retention docs, but this rule takes no additional action.

## View logs for your automations​

You can view logs for your automations by going to `Settings` -> `Rules` and click on the `Logs` button in any row.

You can also get to logs by clicking on `Rules` in the top right hand corner of any project details page, then clicking on `See Logs` for any rule.

Logs allow you to gain confidence that your rules are working as expected. You can now view logs that list all runs processed by a given rule for the past day. For rules that apply online evaluation scores, you can easily see the output score and navigate to the run. For rules that add runs as examples to datasets, you can view the example produced. If a particular rule execution has triggered an error, you can view the error message by hovering over the error icon.

![Logs_Gif](/assets/images/rules_logs-f007f2fcb6fdcee543ede0179d998340.gif)

![Logs](/assets/images/rules_logs-185421b78d6946142d5f44def24ef41e.png)

By default, rule logs only show results for runs that occurred in the last day. To see results for older runs, you can select **Last 1 day** and enter the desired date range. When applying a rule to past runs, the processing will start from the start date and go forward, so this would be needed to view logs while the backfill is proceeding.

![](/assets/images/rules_past_runs_logs-15a932828e71d3b0e47221a10a1169f8.png)

If you prefer a video tutorial, check out the [Automations video](https://academy.langchain.com/pages/intro-to-langsmith-preview) from the Introduction to LangSmith Course.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Create a rule
    * Step 1: Navigate to rule creation
    * Step 2: Define the filter
    * (Optional) Step 3: Apply Rule to Past Runs
    * Step 4: Define the sampling rate
    * Step 5: Define the action
  * View logs for your automations

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)