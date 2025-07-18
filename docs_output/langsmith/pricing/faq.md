# Frequently Asked Questions | 🦜️🛠️ LangSmith

On this page

## Questions and Answers​

### I’ve been using LangSmith since before pricing took effect for new users. When will pricing go into effect for my account?​

If you’ve been using LangSmith already, your usage will be billable starting in July 2024. At that point if you want to add seats or use more than the monthly allotment of free traces, you will need to add a credit card to LangSmith or contact sales. If you are interested in the Enterprise plan with higher rate limits and special deployment options, you can learn more or make a purchase by reaching out to [sales@langchain.dev](mailto:sales@langchain.dev).

### Which plan is right for me?​

If you’re an individual developer, the Developer plan is a great choice for small projects.

For teams that want to collaborate in LangSmith, check out the Plus plan. **If you are an early-stage startup building an AI application** , you may be eligible for our Startup plan with discounted prices and a generous free monthly trace allotment. Please reach out via our [Startup Contact Form](https://airtable.com/app8ZrGLtHAtFVO1o/pagfLAmdTz4ep7TGu/form) for more details.

If you need more advanced administration, authentication and authorization, deployment options, support, or annual invoicing, the Enterprise plan is right for you. Please reach out via our [Sales Contact Form](https://www.langchain.com/contact-sales) for more details.

### What is a seat?​

A seat is a distinct user inside your organization. We consider the total number of users (including invited users) to determine the number of seats to bill.

### What is a trace?​

A trace is one complete invocation of your application chain or agent, evaluator run, or playground run. Here is an [example](https://smith.langchain.com/public/17c24270-9f74-47e7-b70c-d508afc448fa/r) of a single trace.

### What is an ingested event?​

An ingested event is any distinct, trace-related data sent to LangSmith. This includes:

  * Inputs, outputs and metadata sent at the start of a run step within a trace
  * Inputs, outputs and metadata sent at the end of a run step within a trace
  * Feedback on run steps or traces

### I’ve hit my rate or usage limits. What can I do?​

When you first sign up for a LangSmith account, you get a Personal organization that is limited to 5000 monthly traces. To continue sending traces after reaching this limit, upgrade to the Developer or Plus plans by adding a credit card. Head to [Plans and Billing](https://smith.langchain.com/settings/payments) to upgrade.

Simialrly, if you’ve hit the rate limits on your currnt plan, you can upgrade to a higher plan to get higher limits, or reach out to [support@langchain.dev](mailto:support@langchain.dev) with questions.

### I have a developer account, can I upgrade my account to the Plus or Enterprise plan?​

Yes, Developer plan users can easily upgrade to the Plus plan on the [Plans and Billing](https://smith.langchain.com/settings/payments) page. For the Enterprise plan, please [contact our sales team](https://www.langchain.com/contact-sales) to discuss your needs.

### How does billing work?​

**Seats**   

Seats are billed monthly on the first of the month. Additional seats purchased mid-month are pro-rated and billed within one day of the purchase. Seats removed mid-month will not be credited.

  
**Traces**   

As long as you have a card on file in your account, we’ll service your traces and bill you on the first of the month for traces that you submitted in the previous month. You will be able to set usage limits if you so choose to limit the maximum charges you could incur in any given month.

### Can I limit how much I spend on tracing?​

You can set limits on the number of traces that can be sent to LangSmith per month on the [Usage configuration](https://smith.langchain.com/settings/payments) page.

note

While we do show you the dollar value of your usage limit for convenience, this limit evaluated in terms of number of traces instead of dollar amount. For example, if you are approved for our startup plan tier where you are given a generous allotment of free traces, your usage limit will not automatically change.

You are not currently able to set a spend limit in the product.

### How can my track my usage so far this month?​

Under the Settings section for your Organization you will see subsection for **Usage**. There, you will able to see a graph of the daily number of billable LangSmith traces from the last 30, 60, or 90 days. Note that this data is delayed by 1-2 hours and so may trail your actual number of runs slightly for the current day.

### I have a question about my bill...​

Customers on the Developer and Plus plan tiers should email [support@langchain.dev](mailto:support@langchain.dev). Customers on the Enterprise plan should contact their sales representative directly.

Enterprise plan customers are billed annually by invoice.

### What can I expect from Support?​

On the Developer plan, community-based support is available on [LangChain community Slack](https://www.langchain.com/join-community).

On the Plus plan, you will also receive preferential, email support at [support@langchain.dev](mailto:support@langchain.dev) for LangSmith-related questions only and we'll do our best to respond within the next business day.

On the Enterprise plan, you’ll get white-glove support with a Slack channel, a dedicated customer success manager, and monthly check-ins to go over LangSmith and LangChain questions. We can help with anything from debugging, agent and RAG techniques, evaluation approaches, and cognitive architecture reviews. If you purchase the add-on to run LangSmith in your environment, we’ll also support deployments and new releases with our infra engineering team on-call.

### Where is my data stored?​

You may choose to sign up in either the US or EU region. See the [cloud architecture reference](/reference/cloud_architecture_and_scalability) for more details. If you’re on the Enterprise plan, we can deliver LangSmith to run on your kubernetes cluster in AWS, GCP, or Azure so that data never leaves your environment.

### Which security frameworks is LangSmith compliant with?​

We are SOC 2 Type II, GDPR, and HIPAA compliant.

You can request more information about our security policies and posture at [trust.langchain.com](https://trust.langchain.com). Please note we only enter into BAAs with customers on our Enterprise plan.

### Will you train on the data that I send LangSmith?​

We will not train on your data, and you own all rights to your data. See [LangSmith Terms of Service](https://langchain.dev/terms-of-service) for more information.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Questions and Answers
    * I’ve been using LangSmith since before pricing took effect for new users. When will pricing go into effect for my account?
    * Which plan is right for me?
    * What is a seat?
    * What is a trace?
    * What is an ingested event?
    * I’ve hit my rate or usage limits. What can I do?
    * I have a developer account, can I upgrade my account to the Plus or Enterprise plan?
    * How does billing work?
    * Can I limit how much I spend on tracing?
    * How can my track my usage so far this month?
    * I have a question about my bill...
    * What can I expect from Support?
    * Where is my data stored?
    * Which security frameworks is LangSmith compliant with?
    * Will you train on the data that I send LangSmith?

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)