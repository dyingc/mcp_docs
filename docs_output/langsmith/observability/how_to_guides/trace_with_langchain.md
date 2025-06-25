# Trace with LangChain (Python and JS/TS) | 🦜️🛠️ LangSmith

On this page

LangSmith integrates seamlessly with LangChain ([Python](https://python.langchain.com/) and [JS](https://js.langchain.com/docs/get_started/introduction)), the popular open-source framework for building LLM applications.

## Installation​

Install the core library and the OpenAI integration for Python and JS (we use the OpenAI integration for the code snippets below).

For a full list of packages available, see the [LangChain Python docs](https://python.langchain.com/docs/integrations/platforms/) and [LangChain JS docs](https://js.langchain.com/docs/integrations/platforms/).

  * pip
  * yarn
  * npm
  * pnpm

    
    
    pip install langchain_openai langchain_core  
    
    
    
    yarn add @langchain/openai @langchain/core  
    
    
    
    npm install @langchain/openai @langchain/core  
    
    
    
    pnpm add @langchain/openai @langchain/core  
    

## Quick start​

### 1\. Configure your environment​

  * Python
  * TypeScript

    
    
    export LANGSMITH_TRACING=true  
    export LANGSMITH_API_KEY=<your-api-key>  
    # This example uses OpenAI, but you can use any LLM provider of choice  
    export OPENAI_API_KEY=<your-openai-api-key>  
    
    
    
    export LANGSMITH_TRACING=true  
    export LANGSMITH_API_KEY=<your-api-key>  
    # This example uses OpenAI, but you can use any LLM provider of choice  
    export OPENAI_API_KEY=<your-openai-api-key>  
    

info

If you are using LangChain.js with LangSmith and are not in a serverless environment, we also recommend setting the following explicitly to reduce latency:

`export LANGCHAIN_CALLBACKS_BACKGROUND=true`

If you are in a serverless environment, we recommend setting the reverse to allow tracing to finish before your function ends:

`export LANGCHAIN_CALLBACKS_BACKGROUND=false`

See [this LangChain.js guide](https://js.langchain.com/docs/how_to/callbacks_serverless) for more information.

### 2\. Log a trace​

No extra code is needed to log a trace to LangSmith. Just run your LangChain code as you normally would.

  * Python
  * TypeScript

    
    
    from langchain_openai import ChatOpenAI  
    from langchain_core.prompts import ChatPromptTemplate  
    from langchain_core.output_parsers import StrOutputParser  
      
    prompt = ChatPromptTemplate.from_messages([  
        ("system", "You are a helpful assistant. Please respond to the user's request only based on the given context."),  
        ("user", "Question: {question}\nContext: {context}")  
    ])  
    model = ChatOpenAI(model="gpt-4o-mini")  
    output_parser = StrOutputParser()  
      
    chain = prompt | model | output_parser  
      
    question = "Can you summarize this morning's meetings?"  
    context = "During this morning's meeting, we solved all world conflict."  
    chain.invoke({"question": question, "context": context})  
    
    
    
    import { ChatOpenAI } from "@langchain/openai";  
    import { ChatPromptTemplate } from "@langchain/core/prompts";  
    import { StringOutputParser } from "@langchain/core/output_parsers";  
      
    const prompt = ChatPromptTemplate.fromMessages([  
      ["system", "You are a helpful assistant. Please respond to the user's request only based on the given context."],  
      ["user", "Question: {question}\nContext: {context}"],  
    ]);  
    const model = new ChatOpenAI({ modelName: "gpt-4o-mini" });  
    const outputParser = new StringOutputParser();  
      
    const chain = prompt.pipe(model).pipe(outputParser);  
      
    const question = "Can you summarize this morning's meetings?"  
    const context = "During this morning's meeting, we solved all world conflict."  
    await chain.invoke({ question: question, context: context });  
    

### 3\. View your trace​

By default, the trace will be logged to the project with the name `default`. An example of a trace logged using the above code is made public and can be viewed [here](https://smith.langchain.com/public/e6a46eb2-d785-4804-a1e3-23f167a04300/r).

![](/assets/images/langchain_trace-906c6783b28da0d523b2675ee0c02eef.png)

## Trace selectively​

The previous section showed how to trace all invocations of a LangChain runnables within your applications by setting a single environment variable. While this is a convenient way to get started, you may want to trace only specific invocations or parts of your application.

There are two ways to do this in Python: by manually passing in a `LangChainTracer` ([reference docs](https://api.python.langchain.com/en/latest/tracers/langchain_core.tracers.langchain.LangChainTracer.html#langchain_core.tracers.langchain.LangChainTracer)) instance as a callback, or by using the `tracing_v2_enabled` context manager ([reference docs](https://api.python.langchain.com/en/latest/tracers/langchain_core.tracers.context.tracing_v2_enabled.html)).

In JS/TS, you can pass a `LangChainTracer` ([reference docs](https://api.js.langchain.com/classes/langchain_core_tracers_tracer_langchain.LangChainTracer.html)) instance as a callback.

  * Python
  * TypeScript

    
    
    # You can configure a LangChainTracer instance to trace a specific invocation.  
    from langchain.callbacks.tracers import LangChainTracer  
      
    tracer = LangChainTracer()  
    chain.invoke({"question": "Am I using a callback?", "context": "I'm using a callback"}, config={"callbacks": [tracer]})  
      
    # LangChain Python also supports a context manager for tracing a specific block of code.  
    from langchain_core.tracers.context import tracing_v2_enabled  
    with tracing_v2_enabled():  
      chain.invoke({"question": "Am I using a context manager?", "context": "I'm using a context manager"})  
      
    # This will NOT be traced (assuming LANGSMITH_TRACING is not set)  
    chain.invoke({"question": "Am I being traced?", "context": "I'm not being traced"})  
    
    
    
    // You can configure a LangChainTracer instance to trace a specific invocation.  
    import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";  
      
    const tracer = new LangChainTracer();  
    await chain.invoke(  
    {  
      question: "Am I using a callback?",  
      context: "I'm using a callback"  
    },  
    { callbacks: [tracer] }  
    );  
    

## Log to a specific project​

### Statically​

As mentioned in the [tracing conceptual guide](/observability/concepts) LangSmith uses the concept of a Project to group traces. If left unspecified, the tracer project is set to default. You can set the `LANGSMITH_PROJECT` environment variable to configure a custom project name for an entire application run. This should be done before executing your application.
    
    
    export LANGSMITH_PROJECT=my-project  
    

SDK compatibility in JS

The `LANGSMITH_PROJECT` flag is only supported in JS SDK versions >= 0.2.16, use `LANGCHAIN_PROJECT` instead if you are using an older version.

### Dynamically​

This largely builds off of the previous section and allows you to set the project name for a specific `LangChainTracer` instance or as parameters to the `tracing_v2_enabled` context manager in Python.

  * Python
  * TypeScript

    
    
    # You can set the project name for a specific tracer instance:  
    from langchain.callbacks.tracers import LangChainTracer  
      
    tracer = LangChainTracer(project_name="My Project")  
    chain.invoke({"question": "Am I using a callback?", "context": "I'm using a callback"}, config={"callbacks": [tracer]})  
      
    # You can set the project name using the project_name parameter.  
    from langchain_core.tracers.context import tracing_v2_enabled  
    with tracing_v2_enabled(project_name="My Project"):  
      chain.invoke({"question": "Am I using a context manager?", "context": "I'm using a context manager"})  
    
    
    
    // You can set the project name for a specific tracer instance:  
    import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";  
      
    const tracer = new LangChainTracer({ projectName: "My Project" });  
    await chain.invoke(  
    {  
      question: "Am I using a callback?",  
      context: "I'm using a callback"  
    },  
    { callbacks: [tracer] }  
    );  
    

## Add metadata and tags to traces​

You can send annotate your traces with arbitrary metadata and tags by providing them in the [Config](https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain-core-runnables-config-runnableconfig). This is useful for associating additional information with a trace, such as the environment in which it was executed, or the user who initiated it. For information on how to query traces and runs by metadata and tags, see [this guide](/observability/how_to_guides/export_traces)

note

When you attach metadata or tags to a runnable (either through the RunnableConfig or at runtime with invocation params), they are inherited by all child runnables of that runnable.

  * Python
  * TypeScript

    
    
    from langchain_openai import ChatOpenAI  
    from langchain_core.prompts import ChatPromptTemplate  
    from langchain_core.output_parsers import StrOutputParser  
      
    prompt = ChatPromptTemplate.from_messages([  
    ("system", "You are a helpful AI."),  
    ("user", "{input}")  
    ])  
    # The tag "model-tag" and metadata {"model-key": "model-value"} will be attached to the ChatOpenAI run only  
    chat_model = ChatOpenAI().with_config({"tags": ["model-tag"], "metadata": {"model-key": "model-value"}})  
    output_parser = StrOutputParser()  
      
    # Tags and metadata can be configured with RunnableConfig  
    chain = (prompt | chat_model | output_parser).with_config({"tags": ["config-tag"], "metadata": {"config-key": "config-value"}})  
      
    # Tags and metadata can also be passed at runtime  
    chain.invoke({"input": "What is the meaning of life?"}, {"tags": ["invoke-tag"], "metadata": {"invoke-key": "invoke-value"}})  
    
    
    
    import { ChatOpenAI } from "@langchain/openai";  
    import { ChatPromptTemplate } from "@langchain/core/prompts";  
    import { StringOutputParser } from "@langchain/core/output_parsers";  
      
    const prompt = ChatPromptTemplate.fromMessages([  
    ["system", "You are a helpful AI."],  
    ["user", "{input}"]  
    ])  
    // The tag "model-tag" and metadata {"model-key": "model-value"} will be attached to the ChatOpenAI run only  
    const model = new ChatOpenAI().withConfig({ tags: ["model-tag"], metadata: { "model-key": "model-value" } });  
    const outputParser = new StringOutputParser();  
      
    // Tags and metadata can be configured with RunnableConfig  
    const chain = (prompt.pipe(model).pipe(outputParser)).withConfig({"tags": ["config-tag"], "metadata": {"config-key": "top-level-value"}});  
      
    // Tags and metadata can also be passed at runtime  
    await chain.invoke({input: "What is the meaning of life?"}, {tags: ["invoke-tag"], metadata: {"invoke-key": "invoke-value"}})  
    

## Customize run name​

You can customize the name of a given run when invoking or streaming your LangChain code by providing it in the [Config](https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain-core-runnables-config-runnableconfig). This name is used to identify the run in LangSmith and can be used to filter and group runs. The name is also used as the title of the run in the LangSmith UI. This can be done by setting a `run_name` in the `RunnableConfig` object at construction or by passing a `run_name` in the invocation parameters in JS/TS.

note

This feature is not currently supported directly for LLM objects.

  * Python
  * TypeScript

    
    
    # When tracing within LangChain, run names default to the class name of the traced object (e.g., 'ChatOpenAI').  
    configured_chain = chain.with_config({"run_name": "MyCustomChain"})  
    configured_chain.invoke({"input": "What is the meaning of life?"})  
      
    # You can also configure the run name at invocation time, like below  
    chain.invoke({"input": "What is the meaning of life?"}, {"run_name": "MyCustomChain"})  
    
    
    
    // When tracing within LangChain, run names default to the class name of the traced object (e.g., 'ChatOpenAI').  
    const configuredChain = chain.withConfig({ runName: "MyCustomChain" });  
    await configuredChain.invoke({ input: "What is the meaning of life?" });  
      
    // You can also configure the run name at invocation time, like below  
    await chain.invoke({ input: "What is the meaning of life?" }, {runName: "MyCustomChain"})  
    

## Customize run ID​

You can customize the ID of a given run when invoking or streaming your LangChain code by providing it in the [Config](https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain-core-runnables-config-runnableconfig). This ID is used to uniquely identify the run in LangSmith and can be used to query specific runs. The ID can be useful for linking runs across different systems or for implementing custom tracking logic. This can be done by setting a `run_id` in the `RunnableConfig` object at construction or by passing a `run_id` in the invocation parameters in JS/TS.

note

This feature is not currently supported directly for LLM objects.

  * Python
  * TypeScript

    
    
    import uuid  
      
    my_uuid = uuid.uuid4()  
    # You can configure the run ID at invocation time:  
    chain.invoke({"input": "What is the meaning of life?"}, {"run_id": my_uuid})  
    
    
    
    import { v4 as uuidv4 } from 'uuid';  
      
    const myUuid = uuidv4();  
      
    // You can configure the run ID at invocation time, like below  
    await chain.invoke({ input: "What is the meaning of life?" }, { runId: myUuid });  
    

Note that if you do this at the **root** of a trace (i.e., the top-level run, that run ID will be used as the `trace_id`).

## Access run (span) ID for LangChain invocations​

When you invoke a LangChain object, you can access the run ID of the invocation. This run ID can be used to query the run in LangSmith.

In Python, you can use the `collect_runs` context manager to access the run ID.

In JS/TS, you can use a `RunCollectorCallbackHandler` instance to access the run ID.

  * Python
  * TypeScript

    
    
    from langchain_openai import ChatOpenAI  
    from langchain_core.prompts import ChatPromptTemplate  
    from langchain_core.output_parsers import StrOutputParser  
    from langchain_core.tracers.context import collect_runs  
      
    prompt = ChatPromptTemplate.from_messages([  
      ("system", "You are a helpful assistant. Please respond to the user's request only based on the given context."),  
      ("user", "Question: {question}\n\nContext: {context}")  
    ])  
    model = ChatOpenAI(model="gpt-4o-mini")  
    output_parser = StrOutputParser()  
      
    chain = prompt | model | output_parser  
      
    question = "Can you summarize this morning's meetings?"  
    context = "During this morning's meeting, we solved all world conflict."  
    with collect_runs() as cb:  
    result = chain.invoke({"question": question, "context": context})  
    # Get the root run id  
    run_id = cb.traced_runs[0].id  
    print(run_id)  
    
    
    
    import { ChatOpenAI } from "@langchain/openai";  
    import { ChatPromptTemplate } from "@langchain/core/prompts";  
    import { StringOutputParser } from "@langchain/core/output_parsers";  
    import { RunCollectorCallbackHandler } from "@langchain/core/tracers/run_collector";  
      
    const prompt = ChatPromptTemplate.fromMessages([  
    ["system", "You are a helpful assistant. Please respond to the user's request only based on the given context."],  
    ["user", "Question: {question\n\nContext: {context}"],  
    ]);  
    const model = new ChatOpenAI({ modelName: "gpt-4o-mini" });  
    const outputParser = new StringOutputParser();  
      
    const chain = prompt.pipe(model).pipe(outputParser);  
    const runCollector = new RunCollectorCallbackHandler();  
      
    const question = "Can you summarize this morning's meetings?"  
    const context = "During this morning's meeting, we solved all world conflict."  
    await chain.invoke(  
      { question: question, context: context },  
      { callbacks: [runCollector] }  
    );  
    const runId = runCollector.tracedRuns[0].id;  
    console.log(runId);  
    

## Ensure all traces are submitted before exiting​

In LangChain Python, LangSmith's tracing is done in a background thread to avoid obstructing your production application. This means that your process may end before all traces are successfully posted to LangSmith. This is especially prevalent in a serverless environment, where your VM may be terminated immediately once your chain or agent completes.

You can make callbacks synchronous by setting the `LANGCHAIN_CALLBACKS_BACKGROUND` environment variable to `"false"`.

For both languages, LangChain exposes methods to wait for traces to be submitted before exiting your application. Below is an example:

  * Python
  * TypeScript

    
    
    from langchain_openai import ChatOpenAI  
    from langchain_core.tracers.langchain import wait_for_all_tracers  
      
    llm = ChatOpenAI()  
    try:  
      llm.invoke("Hello, World!")  
    finally:  
      wait_for_all_tracers()  
    
    
    
    import { ChatOpenAI } from "@langchain/openai";  
    import { awaitAllCallbacks } from "@langchain/core/callbacks/promises";  
      
    try {  
    const llm = new ChatOpenAI();  
    const response = await llm.invoke("Hello, World!");  
    } catch (e) {  
    // handle error  
    } finally {  
    await awaitAllCallbacks();  
    }  
    

## Trace without setting environment variables​

As mentioned in other guides, the following environment variables allow you to configure tracing enabled, the api endpoint, the api key, and the tracing project:

  * `LANGSMITH_TRACING`
  * `LANGSMITH_API_KEY`
  * `LANGSMITH_ENDPOINT`
  * `LANGSMITH_PROJECT`

However, in some environments, it is not possible to set environment variables. In these cases, you can set the tracing configuration programmatically.

This largely builds off of the previous section.

  * Python
  * TypeScript

    
    
    from langchain.callbacks.tracers import LangChainTracer  
    from langsmith import Client  
      
    # You can create a client instance with an api key and api url  
    client = Client(  
      api_key="YOUR_API_KEY",  # This can be retrieved from a secrets manager  
      api_url="https://api.smith.langchain.com",  # Update appropriately for self-hosted installations or the EU region  
    )  
      
    # You can pass the client and project_name to the LangChainTracer instance  
    tracer = LangChainTracer(client=client, project_name="test-no-env")  
    chain.invoke({"question": "Am I using a callback?", "context": "I'm using a callback"}, config={"callbacks": [tracer]})  
      
    # LangChain Python also supports a context manager which allows passing the client and project_name  
    from langchain_core.tracers.context import tracing_v2_enabled  
    with tracing_v2_enabled(client=client, project_name="test-no-env"):  
      chain.invoke({"question": "Am I using a context manager?", "context": "I'm using a context manager"})  
    
    
    
    import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";  
    import { Client } from "langsmith";  
      
    // You can create a client instance with an api key and api url  
    const client = new Client(  
      {  
          apiKey: "YOUR_API_KEY",  
          apiUrl: "https://api.smith.langchain.com", // Update appropriately for self-hosted installations or the EU region  
      }  
    );  
      
    // You can pass the client and project_name to the LangChainTracer instance  
    const tracer = new LangChainTracer({client, projectName: "test-no-env"});  
    await chain.invoke(  
    {  
      question: "Am I using a callback?",  
      context: "I'm using a callback",  
    },  
    { callbacks: [tracer] }  
    );  
    

## Distributed tracing with LangChain (Python)​

LangSmith supports distributed tracing with LangChain Python. This allows you to link runs (spans) across different services and applications. The principles are similar to the [distributed tracing guide](/observability/how_to_guides/distributed_tracing) for the LangSmith SDK.
    
    
    import langsmith  
    from langchain_core.runnables import chain  
    from langsmith.run_helpers import get_current_run_tree  
      
    # -- This code should be in a separate file or service --  
    @chain  
    def child_chain(inputs):  
        return inputs["test"] + 1  
      
    def child_wrapper(x, headers):  
        with langsmith.tracing_context(parent=headers):  
            child_chain.invoke({"test": x})  
      
    # -- This code should be in a separate file or service --  
    @chain  
    def parent_chain(inputs):  
      
        rt = get_current_run_tree()  
        headers = rt.to_headers()  
        # ... make a request to another service with the headers  
        # The headers should be passed to the other service, eventually to the child_wrapper function  
      
    parent_chain.invoke({"test": 1})  
    

## Interoperability between LangChain (Python) and LangSmith SDK​

If you are using LangChain for part of your application and the LangSmith SDK (see [this guide](/observability/how_to_guides/annotate_code)) for other parts, you can still trace the entire application seamlessly.

LangChain objects will be traced when invoked within a `traceable` function and be bound as a child run of the `traceable` function.
    
    
    from langchain_openai import ChatOpenAI  
    from langchain_core.prompts import ChatPromptTemplate  
    from langchain_core.output_parsers import StrOutputParser  
      
    from langsmith import traceable  
      
    prompt = ChatPromptTemplate.from_messages([  
        ("system", "You are a helpful assistant. Please respond to the user's request only based on the given context."),  
        ("user", "Question: {question}\nContext: {context}")  
    ])  
    model = ChatOpenAI(model="gpt-4o-mini")  
    output_parser = StrOutputParser()  
      
    chain = prompt | model | output_parser  
      
    # The above chain will be traced as a child run of the traceable function  
    @traceable(  
        tags=["openai", "chat"],  
        metadata={"foo": "bar"}  
    )  
    def invoke_runnnable(question, context):  
        result = chain.invoke({"question": question, "context": context})  
        return "The response is: " + result  
      
    invoke_runnnable("Can you summarize this morning's meetings?", "During this morning's meeting, we solved all world conflict.")  
    

This will produce the following trace tree: ![](/assets/images/trace_tree_python_interop-b5c85bda5c4610f4a6b131bd3b2492cd.png)

## Interoperability between LangChain.JS and LangSmith SDK​

### Tracing LangChain objects inside `traceable` (JS only)​

Starting with `langchain@0.2.x`, LangChain objects are traced automatically when used inside `@traceable` functions, inheriting the client, tags, metadata and project name of the traceable function.

For older versions of LangChain below `0.2.x`, you will need to manually pass an instance `LangChainTracer` created from the tracing context found in `@traceable`.
    
    
    import { ChatOpenAI } from "@langchain/openai";  
    import { ChatPromptTemplate } from "@langchain/core/prompts";  
    import { StringOutputParser } from "@langchain/core/output_parsers";  
    import { getLangchainCallbacks } from "langsmith/langchain";  
      
    const prompt = ChatPromptTemplate.fromMessages([  
      [  
        "system",  
        "You are a helpful assistant. Please respond to the user's request only based on the given context.",  
      ],  
      ["user", "Question: {question}\nContext: {context}"],  
    ]);  
    const model = new ChatOpenAI({ modelName: "gpt-4o-mini" });  
    const outputParser = new StringOutputParser();  
      
    const chain = prompt.pipe(model).pipe(outputParser);  
      
    const main = traceable(  
      async (input: { question: string; context: string }) => {  
        const callbacks = await getLangchainCallbacks();  
        const response = await chain.invoke(input, { callbacks });  
        return response;  
      },  
      { name: "main" }  
    );  
    

### Tracing LangChain child runs via `traceable` / RunTree API (JS only)​

note

We're working on improving the interoperability between `traceable` and LangChain. The following limitations are present when using combining LangChain with `traceable`:

  1. Mutating RunTree obtained from `getCurrentRunTree()` of the RunnableLambda context will result in a no-op.
  2. It's discouraged to traverse the RunTree obtained from RunnableLambda via `getCurrentRunTree()` as it may not contain all the RunTree nodes.
  3. Different child runs may have the same `execution_order` and `child_execution_order` value. Thus in extreme circumstances, some runs may end up in a different order, depending on the `start_time`.

In some uses cases, you might want to run `traceable` functions as part of the RunnableSequence or trace child runs of LangChain run imperatively via the `RunTree` API. Starting with LangSmith 0.1.39 and @langchain/core 0.2.18, you can directly invoke `traceable`-wrapped functions within RunnableLambda.
    
    
    import { traceable } from "langsmith/traceable";  
    import { RunnableLambda } from "@langchain/core/runnables";  
    import { RunnableConfig } from "@langchain/core/runnables";  
      
    const tracedChild = traceable((input: string) => `Child Run: ${input}`, {  
      name: "Child Run",  
    });  
      
    const parrot = new RunnableLambda({  
      func: async (input: { text: string }, config?: RunnableConfig) => {  
        return await tracedChild(input.text);  
      },  
    });  
    

![Trace Tree](/assets/images/trace_tree_manual_tracing-2d0109064a77410ad2321852e0f3f4af.png)

Alternatively, you can convert LangChain's `RunnableConfig` to a equivalent RunTree object by using `RunTree.fromRunnableConfig` or pass the `RunnableConfig` as the first argument of `traceable`-wrapped function.

  * Traceable
  * Run Tree

    
    
    import { traceable } from "langsmith/traceable";  
    import { RunnableLambda } from "@langchain/core/runnables";  
    import { RunnableConfig } from "@langchain/core/runnables";  
      
    const tracedChild = traceable((input: string) => `Child Run: ${input}`, {  
      name: "Child Run",  
    });  
      
    const parrot = new RunnableLambda({  
      func: async (input: { text: string }, config?: RunnableConfig) => {  
        // Pass the config to existing traceable function  
        await tracedChild(config, input.text);  
        return input.text;  
      },  
    });  
    
    
    
    import { RunTree } from "langsmith/run_trees";  
    import { RunnableLambda } from "@langchain/core/runnables";  
    import { RunnableConfig } from "@langchain/core/runnables";  
      
    const parrot = new RunnableLambda({  
      func: async (input: { text: string }, config?: RunnableConfig) => {  
        // create the RunTree from the RunnableConfig of the RunnableLambda  
        const childRunTree = RunTree.fromRunnableConfig(config, {  
          name: "Child Run",  
        });  
          
        childRunTree.inputs = { input: input.text };  
        await childRunTree.postRun();  
          
        childRunTree.outputs = { output: `Child Run: ${input.text}` };  
        await childRunTree.patchRun();  
          
        return input.text;  
      },  
    });  
    

If you prefer a video tutorial, check out the [Alternative Ways to Trace video](https://academy.langchain.com/pages/intro-to-langsmith-preview) from the Introduction to LangSmith Course.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Installation
  * Quick start
    * 1\. Configure your environment
    * 2\. Log a trace
    * 3\. View your trace
  * Trace selectively
  * Log to a specific project
    * Statically
    * Dynamically
  * Add metadata and tags to traces
  * Customize run name
  * Customize run ID
  * Access run (span) ID for LangChain invocations
  * Ensure all traces are submitted before exiting
  * Trace without setting environment variables
  * Distributed tracing with LangChain (Python)
  * Interoperability between LangChain (Python) and LangSmith SDK
  * Interoperability between LangChain.JS and LangSmith SDK
    * Tracing LangChain objects inside `traceable` (JS only)
    * Tracing LangChain child runs via `traceable` / RunTree API (JS only)