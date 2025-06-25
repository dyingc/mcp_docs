# Alerts in LangSmith | 🦜️🛠️ LangSmith

On this page

Self-hosted Version Requirement

Access to alerts requires Helm chart version **0.10.3** or later.

## Overview​

Effective observability in LLM applications requires proactive detection of failures, performance degradations, and regressions. LangSmith's alerts feature helps identify critical issues such as:

  * API rate limit violations from model providers
  * Latency increases for your application
  * Application changes that affect feedback scores reflecting end-user experience

Alerts in LangSmith are project-scoped, requiring separate configuration for each monitored project.

## Configuring an alert​

### Step 1: Navigate To Create Alert​

First navigate to the Tracing project that you would like to configure alerts for. Click **\+ New Alert** in the top right hand corner of the page to set up an alert.

### Step 2: Select Metric Type​

  

![Alert Metrics](/assets/images/alert_metric-f77a74539657b9b00b45feacbdb5de24.png)

LangSmith offers threshold-based alerting on three core metrics:

Metric Type| Description| Use Case  
---|---|---  
**Errored Runs**|  Track runs with an error status| Monitors for failures in an application.  
**Feedback Score**|  Measures the average feedback score| Track [feedback from end users](/evaluation/how_to_guides/attach_user_feedback) or [online evaluation results](/observability/how_to_guides/online_evaluations) to alert on regressions.  
**Latency**|  Measures average run execution time| Tracks the latency of your application to alert on spikes and performance bottlenecks.  
  
Additionally, for **Errored Runs** and **Run Latency** , you can define filters to narrow down the runs that trigger alerts. For example, you might create an error alert filter for all `llm` runs tagged with `support_agent` that encounter a `RateLimitExceeded` error.

![Alert Metrics](/assets/images/alerts_filter-de964e6782d3f070535d126ae7f60d04.png)

### Step 2: Define Alert Conditions​

Alert conditions consist of several components:

  * **Aggregation Method** : Average, Percentage, or Count
  * **Comparison Operator** : `>=`, `<=`, or exceeds threshold
  * **Threshold Value** : Numerical value triggering the alert
  * **Aggregation Window** : Time period for metric calculation (currently choose between 5 or 15 minutes)
  * **Feedback Key** (Feedback Score alerts only): Specific feedback metric to monitor

  

![Alert Condition Configuration](/assets/images/define_conditions-c4c2d47c8b15a4634ca0f843130e3f94.png)

**Example:** The configuration shown above would generate an alert when more than 5% of runs within the past 5 minutes result in errors.

You can preview alert behavior over a historical time window to understand how many datapoints—and which ones—would have triggered an alert at a chosen threshold (indicated in red). For example, setting an average latency threshold of 60 seconds for a project lets you visualize potential alerts, as shown in the image below.

![Alert Metrics](/assets/images/alert_preview-eb5b4bb58c418f1ee6d3be17a00c39f1.png)

### Step 3: Configure Notification Channel​

LangSmith supports the following notification channels:

  1. [PagerDuty Integration](/observability/how_to_guides/alerts_pagerduty)
  2. [Webhook Notifications](/observability/how_to_guides/alerts_webhook)

Select the appropriate channel to ensure notifications reach the responsible team members.

## Best Practices​

  * Adjust sensitivity based on application criticality
  * Start with broader thresholds and refine based on observed patterns
  * Ensure alert routing reaches appropriate on-call personnel

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Overview
  * Configuring an alert
    * Step 1: Navigate To Create Alert
    * Step 2: Select Metric Type
    * Step 2: Define Alert Conditions
    * Step 3: Configure Notification Channel
  * Best Practices

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)