# How to compare experiment results | 🦜️🛠️ LangSmith

On this page

Oftentimes, when you are iterating on your LLM application (such as changing the model or the prompt), you will want to compare the results of different experiments.

LangSmith supports a powerful comparison view that lets you hone in on key differences, regressions, and improvements between different experiments.

![](/assets/images/compare-92cf87a92a0592831d6b8ff89372020e.gif)

## Open the comparison view​

To open the experiment comparison view, click the **Dataset & Experiments** page, select the relevant Dataset, select two or more experiments on the Experiments tab and click compare.

![](/assets/images/compare_select-a65688e7942d0d4bf824473a8bd9bf18.png)

## Adjust the table display​

You can toggle between different views by clicking "Full" or "Compact" at the top of the page.

Toggling Full Text will show the full text of the input, output and reference output for each run. If the reference output is too long to display in the table, you can click on expand to view the full content.

You can also select and hide individual feedback keys or individual metrics in the display settings dropdown to isolate the information you want to see.

![](/assets/images/toggle_views-44fb854d566e54a2b5014601cf1f1353.gif)

## View regressions and improvements​

In the LangSmith comparison view, runs that _regressed_ on your specified feedback key against your baseline experiment will be highlighted in red, while runs that _improved_ will be highlighted in green. At the top of each column, you can see how many runs in that experiment did better and how many did worse than your baseline experiment.

![Regressions](/assets/images/regression_view-6445db75bfcaa79c88446da1429045dd.png)

## Filter on regressions or improvements​

Click on the regressions or improvements buttons on the top of each column to filter to the runs that regressed or improved in that specific experiment.

![Regressions Filter](/assets/images/filter_to_regressions-a40ec775f25c1c7179a3ec8a4df8f732.png)

## Update baseline experiment and metric​

In order to track regressions, you need to:

  1. Select a baseline experiment against which to compare and a metric to measure. By default, the newest experiment is selected as the baseline.
  2. Select feedback key (evaluation metric) you want to focus compare against. One will be assigned by default, but you can adjust as needed.
  3. Configure whether a higher score is better for the selected feedback key. This preference will be stored.

![Baseline](/assets/images/select_baseline-eb990d76f6ee4e5c76509e693a5e6227.png)

## Open a trace​

If the example you're evaluating is from an ingested [run](/observability/concepts#runs), you can hover over the output cell and click on the trace icon to open the trace view for that run. This will open up a trace in the side panel.

![](/assets/images/open_source_trace-426f75ecb6815cb9ab38ab55ee99d6cf.png)

## Expand detailed view​

From any cell, you can click on the expand icon in the hover state to open up a detailed view of all experiment results on that particular example input, along with feedback keys and scores.

![](/assets/images/expanded_view-73880f6556e9f2c4152fda9b269f0641.png)

## View summary charts​

You can also view summary charts by clicking on the "Charts" tab at the top of the page.

![](/assets/images/charts_tab-f9b42b53119df27d2c7b0b4fc07d325b.png)

## Use experiment metadata as chart labels​

You can configure the x-axis labels for the charts based on [experiment metadata](/evaluation/how_to_guides/filter_experiments_ui#background-add-metadata-to-your-experiments).

Select a metadata key to see change the x-axis labels of the charts.

![](/assets/images/metadata_in_charts-54244735eea874ca500038f71dd05153.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Open the comparison view
  * Adjust the table display
  * View regressions and improvements
  * Filter on regressions or improvements
  * Update baseline experiment and metric
  * Open a trace
  * Expand detailed view
  * View summary charts
  * Use experiment metadata as chart labels