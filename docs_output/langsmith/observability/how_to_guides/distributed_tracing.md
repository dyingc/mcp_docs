# Implement distributed tracing | 🦜️🛠️ LangSmith

On this page

Sometimes, you need to trace a request across multiple services.

LangSmith supports distributed tracing out of the box, linking runs within a trace across services using context propagation headers (`langsmith-trace` and optional `baggage` for metadata/tags).

Example client-server setup:

  * Trace starts on client
  * Continues on server

## Distributed tracing in Python​
    
    
    # client.py  
    from langsmith.run_helpers import get_current_run_tree, traceable  
    import httpx  
      
    @traceable  
    async def my_client_function():  
        headers = {}  
        async with httpx.AsyncClient(base_url="...") as client:  
            if run_tree := get_current_run_tree():  
                # add langsmith-id to headers  
                headers.update(run_tree.to_headers())  
            return await client.post("/my-route", headers=headers)  
    

Then the server (or other service) can continue the trace by handling the headers appropriately. If you are using an asgi app Starlette or FastAPI, you can connect the distributed trace using LangSmith's `TracingMiddleware`.

info

The `TracingMiddleware` class was added in `langsmith==0.1.133`.

Example using FastAPI:
    
    
    from langsmith import traceable  
    from langsmith.middleware import TracingMiddleware  
    from fastapi import FastAPI, Request  
      
      
    app = FastAPI()  # Or Flask, Django, or any other framework  
    app.add_middleware(TracingMiddleware)  
      
    @traceable  
    async def some_function():  
        ...  
      
    @app.post("/my-route")  
    async def fake_route(request: Request):  
      return await some_function()  
    

Or in Starlette:
    
    
    from starlette.applications import Starlette  
    from starlette.middleware import Middleware  
    from langsmith.middleware import TracingMiddleware  
      
    routes = ...  
      
    middleware = [  
        Middleware(TracingMiddleware),  
    ]  
      
    app = Starlette(..., middleware=middleware)  
    

If you are using other server frameworks, you can always "receive" the distributed trace by passing the headers in through `langsmith_extra`:
    
    
    # server.py  
    from langsmith import traceable  
    from langsmith.run_helpers import tracing_context  
    from fastapi import FastAPI, Request  
      
      
    @traceable  
    async def my_application():  
        ...  
      
      
    app = FastAPI()  # Or Flask, Django, or any other framework  
      
      
    @app.post("/my-route")  
    async def fake_route(request: Request):  
        # request.headers:  {"langsmith-trace": "..."}  
        # as well as optional metadata/tags in `baggage`  
        with tracing_context(parent=request.headers):  
            return await my_application()  
    

The example above uses the `tracing_context` context manager. You can also directly specify the parent run context in the `langsmith_extra` parameter of a method wrapped with `@traceable`.
    
    
    from langsmith.run_helpers import traceable, trace  
    # ... same as above  
    @app.post("/my-route")  
    async def fake_route(request: Request):  
        # request.headers:  {"langsmith-trace": "..."}  
        my_application(langsmith_extra={"parent": request.headers})  
    

## Distributed tracing in TypeScript​

note

Distributed tracing in TypeScript requires `langsmith` version `>=0.1.31`

First, we obtain the current run tree from the client and convert it to `langsmith-trace` and `baggage` header values, which we can pass to the server:
    
    
    // client.mts  
    import { getCurrentRunTree, traceable } from "langsmith/traceable";  
      
    const client = traceable(  
      async () => {  
        const runTree = getCurrentRunTree();  
        return await fetch("...", {  
          method: "POST",  
          headers: runTree.toHeaders(),  
        }).then((a) => a.text());  
      },  
      { name: "client" }  
    );  
      
    await client();  
    

Then, the server converts the headers back to a run tree, which it uses to further continue the tracing.

To pass the newly created run tree to a traceable function, we can use the `withRunTree` helper, which will ensure the run tree is propagated within traceable invocations.

  * Express.JS
  * Hono

    
    
    // server.mts  
    import { RunTree } from "langsmith";  
    import { traceable, withRunTree } from "langsmith/traceable";  
      
    import express from "express";  
    import bodyParser from "body-parser";  
      
    const server = traceable(  
      (text: string) => `Hello from the server! Received "${text}"`,  
      { name: "server" }  
    );  
      
    const app = express();  
      
    app.use(bodyParser.text());  
      
    app.post("/", async (req, res) => {  
      const runTree = RunTree.fromHeaders(req.headers);  
      const result = await withRunTree(runTree, () => server(req.body));  
      res.send(result);  
    });  
    
    
    
    // server.mts  
    import { RunTree } from "langsmith";  
    import { traceable, withRunTree } from "langsmith/traceable";  
      
    import { Hono } from "hono";  
      
    const server = traceable(  
      (text: string) => `Hello from the server! Received "${text}"`,  
      { name: "server" }  
    );  
      
    const app = new Hono();  
      
    app.post("/", async (c) => {  
      const body = await c.req.text();  
      const runTree = RunTree.fromHeaders(c.req.raw.headers);  
      const result = await withRunTree(runTree, () => server(body));  
      return c.body(result);  
    });  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Distributed tracing in Python
  * Distributed tracing in TypeScript

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)