# Use annotation queues | 🦜️🛠️ LangSmith

On this page

Annotation queues are a powerful LangSmith feature that provide a streamlined, directed view for human annotators to attach feedback to specific runs. While you can always [annotate runs inline](/evaluation/how_to_guides/annotate_traces_inline), annotation queues provide another option to group runs together, then have annotators review and provide feedback on them.

## Create an annotation queue​

![](/assets/images/create_annotation_queue-6fcbcf31308cfa8297287f7d7cb5fa7c.png)

To create an annotation queue, navigate to the **Annotation queues** section through the homepage or left-hand navigation bar. Then click **\+ New annotation queue** in the top right corner.

![](/assets/images/create_annotation_queue_new-4ef470bd39073c0b24a047583d9989f1.png)

### Basic Details​

Fill in the form with the **name** and **description** of the queue. You can also assign a **default dataset** to queue, which will streamline the process of sending the inputs and outputs of certain runs to datasets in your LangSmith workspace.

### Annotation Rubric​

Begin by drafting some high-level instructions for your annotators, which will be shown in the sidebar on every run.

Next, click "+ Desired Feedback" to add feedback keys to your annotation queue. Annotators will be presented with these feedback keys on each run. Add a description for each, as well as a short description of each category if the feedback is categorical.

![annotation queue rubric](/assets/images/create_annotation_rubric-cd88030818ddf6f7e2cef2f38eb95f4a.png)

Reviewers will see this:

![rubric for annotators](/assets/images/rubric_for_annotators-1a7b3e09a1dfa4504a0f468ae96124e7.png)

### Collaborator Settings​

There are a few settings related to multiple annotators:

  * **Number of reviewers per run** : This determines the number of reviewers that must mark a run as "Done" for it to be removed from the queue. If you check "All workspace members review each run," then a run will remain in the queue until all workspace members have marked it "Done".
  * **Enable reservations on runs** : We recommend enabling reservations. This will prevent multiple annotators from reviewing the same run at the same time.

  1. **How do reservations work?**

When a reviewer views a run, the run is reserved for that reviewer for the specified "reservation length". If there are multiple reviewers per run as specified above, the run can be reserved by multiple reviewers (up to the number of reviewers per run) at the same time.

  2. **What happens if time runs out?**

If a reviewer has viewed a run and then leaves the run without marking it "Done", the reservation will expire after the specified "reservation length". The run is then released back into the queue and can be reserved by another reviewer.

note

Clicking "Requeue at end" will only move the current run to the end of the current user's queue; it won't affect the queue order of any other user. It will also release the reservation that the current user has on that run.

Because of these settings, it's possible (and likely) that the number of runs visible to an individual in an annotation queue differs from the total number of runs in the queue as well as anyone else's queue size.

You can update these settings at any time by clicking on the pencil icon in the **Annotation Queues** section.

![](/assets/images/annotation_queue_edit-24378216c29bef3569544238feef0b55.png)

## Assign runs to an annotation queue​

To assign runs to an annotation queue, either:

  1. Click on **Add to Annotation Queue** in top right corner of any trace view. You can add ANY intermediate run (span) of the trace to an annotation queue, not just the root span. ![](/assets/images/add_to_annotation_queue-a536d57618587d8cd8b7d7e56f2465cf.png)

  2. Select multiple runs in the runs table then click **Add to Annotation Queue** at the bottom of the page. ![](/assets/images/multi_select_annotation_queue-efeab98023dccbd3f8dc6da86f138f87.png)

  3. [Set up an automation rule](/observability/how_to_guides/rules) that automatically assigns runs which pass a certain filter and sampling condition to an annotation queue.

  4. Select one or multiple experiments from the dataset page and click **Annotate**. From the resulting popup, you may either create a new queue or add the runs to an existing one: ![](/assets/images/annotate_experiment-8911b495c3ba92db1660af23cb314097.png)

tip

It is often a very good idea to assign runs that have a certain user feedback score (eg thumbs up, thumbs down) from the application to an annotation queue. This way, you can identify and address issues that are causing user dissatisfaction. To learn more about how to capture user feedback from your LLM application, follow [this guide](/evaluation/how_to_guides/attach_user_feedback).

## Review runs in an annotation queue​

To review runs in an annotation queue, navigate to the **Annotation Queues** section through the homepage or left-hand navigation bar. Then click on the queue you want to review. This will take you to a focused, cyclical view of the runs in the queue that require review.

You can attach a comment, attach a score for a particular feedback criteria, add the run a dataset and/or mark the run as reviewed. You can also remove the run from the queue for all users, despite any current reservations or settings for the queue, by clicking the **Trash** icon next to "View run".

The keyboard shortcuts shown can help streamline the review process.

![](/assets/images/review_runs-6ee82b92d6a07141bd2fcf0fc0638ba2.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Create an annotation queue
    * Basic Details
    * Annotation Rubric
    * Collaborator Settings
  * Assign runs to an annotation queue
  * Review runs in an annotation queue

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)