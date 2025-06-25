# Annotate traces and runs inline | 🦜️🛠️ LangSmith

LangSmith allows you to manually annotate traces with feedback within the application. This can be useful for adding context to a trace, such as a user's comment or a note about a specific issue. You can annotate a trace either inline or by sending the trace to an annotation queue, which allows you closely inspect and log feedbacks to runs one at a time. Feedback tags are associated with your [workspace](/administration/concepts#workspaces).

note

You can attach user feedback to ANY intermediate run (span) of the trace, not just the root span. This is useful for critiquing specific parts of the LLM application, such as the retrieval step or generation step of the RAG pipeline.

To annotate a trace inline, click on the `Annotate` in the upper right corner of trace view for any particular run that is part of the trace.

![](/assets/images/annotate_trace_inline-632a5b3e248e1838a384afb0256d446c.png)

This will open up a pane that allows you to choose from feedback tags associated with your workspace and add a score for particular tags. You can also add a standalone comment. Follow [this guide](/evaluation/how_to_guides/set_up_feedback_criteria) to set up feedback tags for your workspace. You can also set up new feedback criteria from within the pane itself.

![](/assets/images/annotation_sidebar-f2d92eeed575f79637b3ad5562016118.png)

You can use the labeled keyboard shortcuts to streamline the annotation process.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)