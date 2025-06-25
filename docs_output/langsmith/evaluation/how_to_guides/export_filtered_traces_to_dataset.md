# How to export filtered traces from experiment to dataset | 🦜️🛠️ LangSmith

On this page

After running an offline evaluation in LangSmith, you may want to export traces that met some evaluation criteria to a dataset.

## View experiment traces​

![Export filtered traces](/assets/images/export-filtered-trace-to-dataset-d37b79d8aaaf286e32d870d8d282baba.png)

To do so, first click on the arrow next to your experiment name. This will direct you to a project that contains the traces generated from your experiment.

![Export filtered traces](/assets/images/experiment-tracing-project-9ab7812833896611732a5a125e0074b6.png)

From there, you can filter the traces based on your evaluation criteria. In this example, I want to filter for all traces that received an accuracy score greater than 0.5.

![Export filtered traces](/assets/images/filtered-traces-from-experiment-5d406cea3c104f91000192cd1963c1ba.png)

Afte applying the filter on my project, I can multi-select runs I'd like to add to my dataset, and click the 'Add to Dataset' at the bottom of my screen.

![Export filtered traces](/assets/images/add-filtered-traces-to-dataset-072a2a52719330955023d5de72030508.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * View experiment traces

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)