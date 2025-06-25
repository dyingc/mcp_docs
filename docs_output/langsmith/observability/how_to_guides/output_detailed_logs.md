# How to print detailed logs (Python SDK) | 🦜️🛠️ LangSmith

On this page

The LangSmith package uses Python's built in [`logging`](https://docs.python.org/3/library/logging.html) mechanism to output logs about its behavior to standard output.

## Ensure logging is configured​

note

By default, Jupyter notebooks send logs to standard error instead of standard output, which means your logs will not show up in your notebook cell output unless you configure logging as we do below.

If logging is not currently configured to send logs to standard output for your Python environment, you'll need to explicitly turn it on as follows:

  * Python

    
    
      
    import logging  
    # Note: this will affect _all_ packages that use python's built-in logging mechanism,   
    #       so may increase your log volume. Pick the right log level for your use case.  
    logging.basicConfig(level=logging.WARNING)  
    

## Increase the logger's verbosity​

When debugging an issue, it's helpful to increase logs to a higher level verbosity so more info is outputted to standard output. Python loggers default to using `WARNING` log level, but you can choose different values to get different levels of verbosity. The values, from least verbose to most, are `ERROR`, `WARNING`, `INFO`, and `DEBUG`. You can set this as follows:

  * Python

    
    
      
    import langsmith  
    import logging  
      
    # Loggers are hierarchical, so setting the log level on "langsmith" will  
    # set it on all modules inside the "langsmith" package  
    langsmith_logger = logging.getLogger("langsmith")  
    langsmith_logger.setLevel(level=logging.DEBUG)  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Ensure logging is configured
  * Increase the logger's verbosity