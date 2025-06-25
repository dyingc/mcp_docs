# How to define a target function to evaluate | 🦜️🛠️ LangSmith

On this page

There are three main pieces need to run an evaluation:

  1. A [dataset](/evaluation/concepts#datasets) of test inputs and expected outputs.
  2. A target function which is what you're evaluating.
  3. [Evaluators](/evaluation/concepts#evaluators) that score your target function's outputs.

This guide shows you how to define the target function depending on the part of your application you are evaluating. See here for [how to create a dataset](/evaluation/how_to_guides/manage_datasets_programmatically) and [how to define evaluators](/evaluation/how_to_guides/custom_evaluator), and here for an [end-to-end example of running an evaluation](/evaluation/how_to_guides/evaluate_llm_application).

## Target function signature​

In order to evaluate an application in code, we need a way to run the application. When using `evaluate()` ([Python](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client#langsmith.client.Client.evaluate)/[TypeScript](https://docs.smith.langchain.com/reference/js/functions/evaluation.evaluate))we'll do this by passing in a _target function_ argument. This is a function that takes in a dataset [Example's](/evaluation/concepts#examples) inputs and returns the application output as a dict. Within this function we can call our application however we'd like. We can also format the output however we'd like. The key is that any evaluator functions we define should work with the output format we return in our target function.
    
    
    from langsmith import Client  
      
    # 'inputs' will come from your dataset.  
    def dummy_target(inputs: dict) -> dict:  
        return {"foo": 1, "bar": "two"}  
      
    # 'inputs' will come from your dataset.  
    # 'outputs' will come from your target function.  
    def evaluator_one(inputs: dict, outputs: dict) -> bool:  
        return outputs["foo"] == 2  
      
    def evaluator_two(inputs: dict, outputs: dict) -> bool:  
        return len(outputs["bar"]) < 3  
      
    client = Client()  
    results = client.evaluate(  
        dummy_target,  # <-- target function  
        data="your-dataset-name",  
        evaluators=[evaluator_one, evaluator_two],   
        ...  
    )  
    

Automatic tracing

`evaluate()` will automatically trace your target function. This means that if you run any traceable code within your target function, this will also be traced as child runs of the target trace.

## Example: Single LLM call​

When we're iterating on a prompt or comparing models it can be useful to evaluate a single LLM call:

  * Python
  * TypeScript
  * Python (LangChain)
  * TypeScript (LangChain)

Set env var `OPENAI_API_KEY` and install deps `pip install -U openai langsmith`.
    
    
    from langsmith import wrappers  
    from openai import OpenAI  
      
    # Optionally wrap the OpenAI client to automatically   
    # trace all model calls.  
    oai_client = wrappers.wrap_openai(OpenAI())  
      
    def target(inputs: dict) -> dict:  
      # This assumes your dataset has inputs with a 'messages' key.  
      # You can update to match your dataset schema.  
      messages = inputs["messages"]  
      response = oai_client.chat.completions.create(  
          messages=messages,  
          model="gpt-4o-mini",  
      )  
      return {"answer": response.choices[0].message.content}  
    

Set env var `OPENAI_API_KEY` and install `openai` and `langsmith`.
    
    
    import OpenAI from 'openai';  
    import { wrapOpenAI } from "langsmith/wrappers";  
      
    const client = wrapOpenAI(new OpenAI());  
      
    // This is the function you will evaluate.  
    const target = async(inputs) => {  
      // This assumes your dataset has inputs with a `messages` key  
      const messages = inputs.messages;  
      const response = await client.chat.completions.create({  
          messages: messages,  
          model: 'gpt-4o-mini',  
      });  
      return { answer: response.choices[0].message.content };  
    }  
    

Set env var `OPENAI_API_KEY` and install deps `pip install -U langchain[openai]`.
    
    
    from langchain.chat_models import init_chat_model  
      
    llm = init_chat_model("openai:gpt-4o-mini")  
      
    def target(inputs: dict) -> dict:  
      # This assumes your dataset has inputs with a `messages` key  
      messages = inputs["messages"]  
      response = llm.invoke(messages)  
      return {"answer": response.content}  
    

Set env var `OPENAI_API_KEY` and install `@langchain/openai`.
    
    
      
    import { ChatOpenAI } from '@langchain/openai';  
      
    // This is the function you will evaluate.  
    const target = async(inputs) => {  
      // This assumes your dataset has inputs with a `messages` key  
      const messages = inputs.messages;  
      const model = new ChatOpenAI({ model: "gpt-4o-mini" });  
      const response = await model.invoke(messages);  
      return {"answer": response.content};  
    }  
    

## Example: Non-LLM component​

Sometimes, you may want to evaluate a step of your application that doesn't involve an LLM. This includes but is not limited to:

  * A retrieval step in a RAG application
  * Execution of a tool

In this example we show how to test a simple calculator tool. In practice evaluations are useful for components that have more complex and hard-to-unit-test behavior, like a retriever or an online research tool.

  * Python
  * TypeScript

    
    
    from langsmith import traceable  
      
    # Optionally decorate with '@traceable' to trace all invocations of this function.  
    @traceable  
    def calculator_tool(operation: str, number1: float, number2: float) -> str:  
      if operation == "add":  
          return str(number1 + number2)  
      elif operation == "subtract":  
          return str(number1 - number2)  
      elif operation == "multiply":  
          return str(number1 * number2)  
      elif operation == "divide":  
          return str(number1 / number2)  
      else:  
          raise ValueError(f"Unrecognized operation: {operation}.")  
      
    # This is the function you will evaluate.  
    def target(inputs: dict) -> dict:  
      # This assumes your dataset has inputs with `operation`, `num1`, and `num2` keys.  
      operation = inputs["operation"]  
      number1 = inputs["num1"]  
      number2 = inputs["num2"]  
      result = calculator_tool(operation, number1, number2)  
      return {"result": result}  
    
    
    
    import { traceable } from "langsmith/traceable";  
      
    // Optionally wrap in 'traceable' to trace all invocations of this function.   
    const calculatorTool = traceable(async ({ operation, number1, number2 }) => {  
    // Functions must return strings  
    if (operation === "add") {  
      return (number1 + number2).toString();  
    } else if (operation === "subtract") {  
      return (number1 - number2).toString();  
    } else if (operation === "multiply") {  
      return (number1 * number2).toString();  
    } else if (operation === "divide") {  
      return (number1 / number2).toString();  
    } else {  
      throw new Error("Invalid operation.");  
    }  
    });  
      
    // This is the function you will evaluate.  
    const target = async (inputs) => {  
    // This assumes your dataset has inputs with `operation`, `num1`, and `num2` keys  
    const result = await calculatorTool.invoke({  
      operation: inputs.operation,  
      number1: inputs.num1,  
      number2: inputs.num2,  
    });  
    return { result };  
    }  
    

## Example: Application or agent​

Evaluating the complete output of your agentic application captures the interactions between multiple components, providing a more realistic picture of end-to-end performance. End-to-end evaluations may also uncover integration and error handling issues that might be missed when testing isolated functions or individual LLM calls.

  * Python
  * TypeScript

    
    
    from my_agent import agent  
            
    # This is the function you will evaluate.  
    def target(inputs: dict) -> dict:  
      # This assumes your dataset has inputs with a `messages` key  
      messages = inputs["messages"]  
      # Replace `invoke` with whatever you use to call your agent  
      response = agent.invoke({"messages": messages})  
      # This assumes your agent output is in the right format  
      return response  
    
    
    
      
    import { agent } from 'my_agent';  
      
    // This is the function you will evaluate.  
    const target = async(inputs) => {  
    // This assumes your dataset has inputs with a `messages` key  
    const messages = inputs.messages;  
    // Replace `invoke` with whatever you use to call your agent  
    const response = await agent.invoke({ messages });  
    // This assumes your agent output is in the right format  
    return response;  
    }  
    

LangGraph / LangChain targets

If you have a LangGraph/LangChain agent that accepts the inputs defined in your dataset and that returns the output format you want to use in your evaluators, you can pass that object in as the target directly:
    
    
    from my_agent import agent  
    from langsmith import Client  
      
    client = Client()  
    client.evaluate(agent, ...)  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Target function signature
  * Example: Single LLM call
  * Example: Non-LLM component
  * Example: Application or agent

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)