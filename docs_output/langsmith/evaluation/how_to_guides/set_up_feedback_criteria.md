# Set up feedback criteria | 🦜️🛠️ LangSmith

On this page

Recommended Reading

Before diving into this content, it might be helpful to read the following:

  * [Conceptual guide on tracing and feedback](/observability/concepts)
  * [Reference guide on feedback data format](/reference/data_formats/feedback_data_format)

Feedback criteria are represented in the application as feedback tags. For human feedback, you can set up new feedback criteria as continuous feedback or categorical feedback.

To set up a new feedback criteria, follow [this link](https://smith.langchain.com/settings/workspaces/feedbacks) to view all existing tags for your workspace, then click **New Tag**.

## Continuous feedback​

For continuous feedback, you can enter a feedback tag name, then select a minimum and maximum value. Every value, including floating-point numbers, within this range will be accepted as feedback scores.

![](/assets/images/cont_feedback-6f21c75b4c0a296d3d7acc936a7c3776.png)

## Categorical feedback​

For categorical feedback, you can enter a feedback tag name, then add a list of categories, each category mapping to a score. When you provide feedback, you can select one of these categories as the feedback score. Both the category label and the score will be logged as feedback in `value` and `score` fields, respectively.

![](/assets/images/cat_feedback-095c88b03d912ac15bff9c917f30790c.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Continuous feedback
  * Categorical feedback

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)