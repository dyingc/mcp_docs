# Log retriever traces | 🦜️🛠️ LangSmith

note

Nothing will break if you don't log retriever traces in the correct format and data will still be logged. However, the data will not be rendered in a way that is specific to retriever steps.

Many LLM applications require looking up documents from vector databases, knowledge graphs, or other types of indexes. Retriever traces are a way to log the documents that are retrieved by the retriever. LangSmith provides special rendering for retrieval steps in traces to make it easier to understand and diagnose retrieval issues. In order for retrieval steps to be rendered correctly, a few small steps need to be taken.

  1. Annotate the retriever step with `run_type="retriever"`.
  2. Return a list of Python dictionaries or TypeScript objects from the retriever step. Each dictionary should contain the following keys:
     * `page_content`: The text of the document.
     * `type`: This should always be "Document".
     * `metadata`: A python dictionary or TypeScript object containing metadata about the document. This metadata will be displayed in the trace.

The following code snippets show how to log a retrieval steps in Python and TypeScript.

  * Python
  * TypeScript

    
    
    from langsmith import traceable  
      
    def _convert_docs(results):  
      return [  
          {  
              "page_content": r,  
              "type": "Document",  
              "metadata": {"foo": "bar"}  
          }  
          for r in results  
      ]  
      
    @traceable(run_type="retriever")  
    def retrieve_docs(query):  
      # Foo retriever returning hardcoded dummy documents.  
      # In production, this could be a real vector datatabase or other document index.  
      contents = ["Document contents 1", "Document contents 2", "Document contents 3"]  
      return _convert_docs(contents)  
      
    retrieve_docs("User query")  
    
    
    
    import { traceable } from "langsmith/traceable";  
      
    interface Document {  
    page_content: string;  
    type: string;  
    metadata: { foo: string };  
    }  
      
    function convertDocs(results: string[]): Document[] {  
    return results.map((r) => ({  
      page_content: r,  
      type: "Document",  
      metadata: { foo: "bar" }  
    }));  
    }  
      
    const retrieveDocs = traceable(  
    (query: string): Document[] => {  
      // Foo retriever returning hardcoded dummy documents.  
      // In production, this could be a real vector database or other document index.  
      const contents = ["Document contents 1", "Document contents 2", "Document contents 3"];  
      return convertDocs(contents);  
    },  
    { name: "retrieveDocs", run_type: "retriever" } // Configuration for traceable  
    );  
      
    await retrieveDocs("User query");  
    

The following image shows how a retriever step is rendered in a trace. The contents along with the metadata are displayed with each document.

![](/assets/images/retriever_trace-9ded87adb076749f7e76fbbe9a81fba5.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)