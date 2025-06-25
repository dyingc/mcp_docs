# Analyze a single experiment | 🦜️🛠️ LangSmith

On this page

After running an experiment, you can use LangSmith's experiment view to analyze the results and draw insights about how your experiment performed.

This guide will walk you through viewing the results of an experiment and highlights the features available in the experiments view.

## Open the experiment view​

To open the experiment view, select the relevant Dataset from the Dataset & Experiments page and then select the experiment you want to view.

![Open experiment view](/assets/images/select_experiment-8c8ba7c4fe01ad5c9c8e5e14eb9ee1ad.png)

## View experiment results​

This table displays your experiment results. This includes the input, output, and reference output for each [example](/evaluation/concepts#examples) in the dataset. It also shows each configured feedback key in separate columns alongside its corresponding feedback score.

Out of the box metrics (latency, status, cost, and token count) will also be displayed in individual columns.

In the columns dropdown, you can choose which columns to hide and which to show.

![Experiment view](/assets/images/experiment_view-876562a9613e8ba4044aebe107b03a4a.png)

## Heatmap view​

The experiment view defaults to a heatmap view, where feedback scores for each run are highlighted in a color. Red indicates a lower score, while green indicates a higher score. The heatmap visualization makes it easy to identify patterns, spot outliers, and understand score distributions across your dataset at a glance.

![Heatmap view](/assets/images/heatmap-788c827412f373adf1128c44ebce1c6d.png)

## Sort and filter​

To sort or filter feedback scores, you can use the actions in the column headers.

![Sort and filter](/assets/images/sort_filter-53db36c12a84ec02cf807480a1010998.png)

## Table views​

Depending on the view most useful for your analysis, you can change the formatting of the table by toggling between a compact view, a full, view, and a diff view.

  * The `Compact` view shows each run as a one-line row, for ease of comparing scores at a glance.
  * The `Full` view shows the full output for each run for digging into the details of individual runs.
  * The `Diff` view shows the text difference between the reference output and the output for each run.

![Diff view](/assets/images/diff_mode-211ab56443819b6e8d41d0c78ee794fe.png)

## View the traces​

Hover over any of the output cells, and click on the trace icon to view the trace for that run. This will open up a trace in the side panel.

To view the entire tracing project, click on the "View Project" button in the top right of the header.

![View trace](/assets/images/view_trace-5ca69528c296cf6a802fa5a004b67ada.png)

## View evaluator runs​

For evaluator scores, you can view the source run by hovering over the evaluator score cell and clicking on the arrow icon. This will open up a trace in the side panel. If you're running a LLM-as-a-judge evaluator, you can view the prompt used for the evaluator in this run. If your experiment has [repetitions](/evaluation/concepts#repetitions), you can click on the aggregate average score to find links to all of the individual runs.

![View evaluator runs](/assets/images/evaluator_run-beeb1702c25c4e07577812a8b0cfe904.png)

## Group results by metadata​

You can add metadata to examples to categorize and organize them. For example, if you're evaluating factual accuracy on a question answering dataset, the metadata might include which subject area each question belongs to. Metadata can be added either [via the UI](/evaluation/how_to_guides/manage_datasets_in_application#edit-example-metadata) or [via the SDK](/evaluation/how_to_guides/manage_datasets_programmatically#update-single-example).

To analyze results by metadata, use the "Group by" dropdown in the top right corner of the experiment view and select your desired metadata key. This displays average feedback scores, latency, total tokens, and cost for each metadata group.

info

You will only be able to group by example metadata on experiments created after February 20th, 2025. Any experiments before that date can still be grouped by metadata, but only if the metadata is on the experiment traces themselves.

![Group by](/assets/images/group_by-dd6672f38d782df98d8c66bdb307c63e.gif)

## Repetitions​

If you've run your experiment with [repetitions](/evaluation/concepts#repetitions), there will be arrows in the output results column so you can view outputs in the table. To view each run from the repetition, hover over the output cell and click the expanded view.

When you run an experiment with repetitions, LangSmith displays the average for each feedback score in the table. Click on the feedback score to view the feedback scores from individual runs, or to view the standard deviation across repetitions.

![Repetitions](/assets/images/repetitions-5ed8e2031f73454e46c64ecce1ecb166.png)

## Compare to another experiment​

In the top right of the experiment view, you can select another experiment to compare to. This will open up a comparison view, where you can see how the two experiments compare. To learn more about the comparison view, see [how to compare experiment results](/evaluation/how_to_guides/compare_experiment_results).

![Compare](/assets/images/compare_to_another-7fbee3c23adbc9e0fb8f43029972ddfb.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Open the experiment view
  * View experiment results
  * Heatmap view
  * Sort and filter
  * Table views
  * View the traces
  * View evaluator runs
  * Group results by metadata
  * Repetitions
  * Compare to another experiment

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)