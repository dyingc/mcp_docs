# Observability Quick Start | 🦜️🛠️ LangSmith

On this page

This tutorial will get you up and running with our observability SDK by showing you how to trace your application to LangSmith.

If you're already familiar with the observability SDK, or are interested in tracing more than just LLM calls you can skip to the next steps section, or check out the [how-to guides](/observability/how_to_guides).

Trace LangChain or LangGraph Applications

If you are using [LangChain](https://python.langchain.com/docs/introduction/) or [LangGraph](https://langchain-ai.github.io/langgraph/), which both integrate seamlessly with LangSmith, you can get started by reading the guides for tracing with [LangChain](/observability/how_to_guides/trace_with_langchain) or tracing with [LangGraph](/observability/how_to_guides/trace_with_langgraph).

## 1\. Install Dependencies​

  * Python
  * TypeScript

    
    
    pip install -U langsmith openai  
    
    
    
    yarn add langsmith openai  
    

## 2\. Create an API key​

To create an API key head to the [LangSmith settings page](https://smith.langchain.com/settings). Then click **Create API Key.**

## 3\. Set up your environment​

  * Shell

    
    
    export LANGSMITH_TRACING=true  
    export LANGSMITH_API_KEY="<your-langsmith-api-key>"  
    # The example uses OpenAI, but it's not necessary if your code uses another LLM provider  
    export OPENAI_API_KEY="<your-openai-api-key>"  
    

## 4\. Define your application​

We will instrument a simple [RAG](https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-retrieval-augmented-generation-rag) application for this tutorial, but feel free to use your own code if you'd like - just make sure it has an LLM call!

Application Code

  * Python
  * TypeScript

    
    
    from openai import OpenAI  
      
    openai_client = OpenAI()  
      
    # This is the retriever we will use in RAG  
    # This is mocked out, but it could be anything we want  
    def retriever(query: str):  
        results = ["Harrison worked at Kensho"]  
        return results  
      
    # This is the end-to-end RAG chain.  
    # It does a retrieval step then calls OpenAI  
    def rag(question):  
        docs = retriever(question)  
        system_message = """Answer the users question using only the provided information below:  
          
        {docs}""".format(docs="\n".join(docs))  
          
        return openai_client.chat.completions.create(  
            messages=[  
                {"role": "system", "content": system_message},  
                {"role": "user", "content": question},  
            ],  
            model="gpt-4o-mini",  
        )  
    
    
    
    import { OpenAI } from "openai";  
      
    const openAIClient = new OpenAI();  
      
    // This is the retriever we will use in RAG  
    // This is mocked out, but it could be anything we want  
    async function retriever(query: string) {  
      return ["This is a document"];  
    }  
      
    // This is the end-to-end RAG chain.  
    // It does a retrieval step then calls OpenAI  
    async function rag(question: string) {  
      const docs = await retriever(question);  
        
      const systemMessage =  
        "Answer the users question using only the provided information below:\n\n" +  
        docs.join("\n");  
          
      return await openAIClient.chat.completions.create({  
        messages: [  
          { role: "system", content: systemMessage },  
          { role: "user", content: question },  
        ],  
        model: "gpt-4o-mini",  
      });  
    }  
    

## 5\. Trace OpenAI calls  ​

The first thing you might want to trace is all your OpenAI calls. LangSmith makes this easy with the [`wrap_openai`](https://docs.smith.langchain.com/reference/python/wrappers/langsmith.wrappers._openai.wrap_openai) (Python) or [`wrapOpenAI`](https://docs.smith.langchain.com/reference/js/functions/wrappers_openai.wrapOpenAI) (TypeScript) wrappers. All you have to do is modify your code to use the wrapped client instead of using the `OpenAI` client directly.

  * Python
  * TypeScript

    
    
    from openai import OpenAI  
    from langsmith.wrappers import wrap_openai  
      
    openai_client = wrap_openai(OpenAI())  
      
    # This is the retriever we will use in RAG  
    # This is mocked out, but it could be anything we want  
    def retriever(query: str):  
        results = ["Harrison worked at Kensho"]  
        return results  
      
    # This is the end-to-end RAG chain.  
    # It does a retrieval step then calls OpenAI  
    def rag(question):  
        docs = retriever(question)  
        system_message = """Answer the users question using only the provided information below:  
          
        {docs}""".format(docs="\n".join(docs))  
          
        return openai_client.chat.completions.create(  
            messages=[  
                {"role": "system", "content": system_message},  
                {"role": "user", "content": question},  
            ],  
            model="gpt-4o-mini",  
        )  
    
    
    
    import { OpenAI } from "openai";  
    import { wrapOpenAI } from "langsmith/wrappers";  
      
    const openAIClient = wrapOpenAI(new OpenAI());  
      
    // This is the retriever we will use in RAG  
    // This is mocked out, but it could be anything we want  
    async function retriever(query: string) {  
      return ["This is a document"];  
    }  
      
    // This is the end-to-end RAG chain.  
    // It does a retrieval step then calls OpenAI  
    async function rag(question: string) {  
      const docs = await retriever(question);  
        
      const systemMessage =  
        "Answer the users question using only the provided information below:\n\n" +  
        docs.join("\n");  
          
      return await openAIClient.chat.completions.create({  
        messages: [  
          { role: "system", content: systemMessage },  
          { role: "user", content: question },  
        ],  
        model: "gpt-4o-mini",  
      });  
    }  
    

Now when you call your application as follows:
    
    
    rag("where did harrison work")  
    

This will produce a trace of just the OpenAI call in LangSmith's default tracing project. It should look something like [this](https://smith.langchain.com/public/e7b7d256-10fe-4d49-a8d5-36ca8e5af0d2/r).

![](/assets/images/tracing_tutorial_openai-667b87c0df7e5bd45538c165314d7e22.png)

## 6\. Trace entire application​

You can also use the `traceable` decorator ([Python](https://docs.smith.langchain.com/reference/python/run_helpers/langsmith.run_helpers.traceable) or [TypeScript](https://langsmith-docs-bdk0fivr6-langchain.vercel.app/reference/js/functions/traceable.traceable)) to trace your entire application instead of just the LLM calls.

  * Python
  * TypeScript

    
    
    from openai import OpenAI  
    from langsmith import traceable  
    from langsmith.wrappers import wrap_openai  
      
    openai_client = wrap_openai(OpenAI())  
      
    def retriever(query: str):  
        results = ["Harrison worked at Kensho"]  
        return results  
      
    @traceable  
    def rag(question):  
        docs = retriever(question)  
        system_message = """Answer the users question using only the provided information below:  
          
        {docs}""".format(docs="\n".join(docs))  
          
        return openai_client.chat.completions.create(  
            messages=[  
                {"role": "system", "content": system_message},  
                {"role": "user", "content": question},  
            ],  
            model="gpt-4o-mini",  
        )  
    
    
    
    import { OpenAI } from "openai";  
    import { traceable } from "langsmith/traceable";  
    import { wrapOpenAI } from "langsmith/wrappers";  
      
    const openAIClient = wrapOpenAI(new OpenAI());  
      
    async function retriever(query: string) {  
      return ["This is a document"];  
    }  
      
    const rag = traceable(async function rag(question: string) {  
      const docs = await retriever(question);  
        
      const systemMessage =  
        "Answer the users question using only the provided information below:\n\n" +  
        docs.join("\n");  
          
      return await openAIClient.chat.completions.create({  
        messages: [  
          { role: "system", content: systemMessage },  
          { role: "user", content: question },  
        ],  
        model: "gpt-4o-mini",  
      });  
    });  
    

Now if you call your application as follows:
    
    
    rag("where did harrison work")  
    

This will produce a trace of just the entire pipeline (with the OpenAI call as a child run) - it should look something like [this](https://smith.langchain.com/public/2174f4e9-48ab-4f9e-a8c4-470372d976f1/r)

![](/assets/images/tracing_tutorial_chain-5023f6584725ddccf4052f7fc050977c.png)

## Next steps​

Congratulations! If you've made it this far, you're well on your way to being an expert in observability with LangSmith. Here are some topics you might want to explore next:

  * [Trace multiturn conversations](/observability/how_to_guides/threads)
  * [Send traces to a specific project](/observability/how_to_guides/log_traces_to_project)
  * [Filter traces in a project](/observability/how_to_guides/filter_traces_in_application)

Or you can visit the [how-to guides page](/observability/how_to_guides) to find out about all the things you can do with LangSmith observability.

If you prefer a video tutorial, check out the [Tracing Basics video](https://academy.langchain.com/pages/intro-to-langsmith-preview) from the Introduction to LangSmith Course.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * 1\. Install Dependencies
  * 2\. Create an API key
  * 3\. Set up your environment
  * 4\. Define your application
  * 5\. Trace OpenAI calls
  * 6\. Trace entire application
  * Next steps

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)