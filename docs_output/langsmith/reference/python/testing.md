# testing — 🦜️🛠️ LangSmith  documentation

# `testing`#  
  
LangSmith pytest testing module.

**Classes**

[`testing._internal.SkipException`](testing/langsmith.testing._internal.SkipException.html#langsmith.testing._internal.SkipException "langsmith.testing._internal.SkipException") |   
---|---  
  
**Functions**

[`testing._internal.log_feedback`](testing/langsmith.testing._internal.log_feedback.html#langsmith.testing._internal.log_feedback "langsmith.testing._internal.log_feedback")([feedback, ...]) | Log run feedback from within a pytest test run.  
---|---  
[`testing._internal.log_inputs`](testing/langsmith.testing._internal.log_inputs.html#langsmith.testing._internal.log_inputs "langsmith.testing._internal.log_inputs")(inputs, /) | Log run inputs from within a pytest test run.  
[`testing._internal.log_outputs`](testing/langsmith.testing._internal.log_outputs.html#langsmith.testing._internal.log_outputs "langsmith.testing._internal.log_outputs")(outputs, /) | Log run outputs from within a pytest test run.  
[`testing._internal.log_reference_outputs`](testing/langsmith.testing._internal.log_reference_outputs.html#langsmith.testing._internal.log_reference_outputs "langsmith.testing._internal.log_reference_outputs")(...) | Log example reference outputs from within a pytest test run.  
[`testing._internal.test`](testing/langsmith.testing._internal.test.html#langsmith.testing._internal.test "langsmith.testing._internal.test")() | Trace a pytest test case in LangSmith.  
[`testing._internal.trace_feedback`](testing/langsmith.testing._internal.trace_feedback.html#langsmith.testing._internal.trace_feedback "langsmith.testing._internal.trace_feedback")(*[, name]) | Trace the computation of a pytest run feedback as its own run.  
[`testing._internal.unit`](testing/langsmith.testing._internal.unit.html#langsmith.testing._internal.unit "langsmith.testing._internal.unit")(*args, **kwargs) | Trace a pytest test case in LangSmith.
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)