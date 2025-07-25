# How to evaluate a langchain runnable | 🦜️🛠️ LangSmith

On this page

Key concepts

  * `langchain`: [Python](https://python.langchain.com) and [JS/TS](https://js.langchain.com)
  * Runnable: [Python](https://python.langchain.com/docs/concepts/runnables/) and [JS/TS](https://js.langchain.com/docs/concepts/runnables/)

`langchain` [Runnable](https://python.langchain.com/docs/concepts/runnables/) objects (such as chat models, retrievers, chains, etc.) can be passed directly into `evaluate()` / `aevaluate()`.

## Setup​

Let's define a simple chain to evaluate. First, install all the required packages:

  * Python
  * TypeScript

    
    
    pip install -U langsmith langchain[openai]  
    
    
    
    yarn add langsmith @langchain/openai  
    

Now define a chain:

  * Python
  * TypeScript

    
    
    from langchain.chat_models import init_chat_model  
    from langchain_core.prompts import ChatPromptTemplate  
    from langchain_core.output_parsers import StrOutputParser  
      
    instructions = (  
        "Please review the user query below and determine if it contains any form "  
        "of toxic behavior, such as insults, threats, or highly negative comments. "  
        "Respond with 'Toxic' if it does, and 'Not toxic' if it doesn't."  
    )  
      
    prompt = ChatPromptTemplate(  
        [("system", instructions), ("user", "{text}")],  
    )  
    llm = init_chat_model("gpt-4o")  
      
    chain = prompt | llm | StrOutputParser()  
    
    
    
    import { ChatOpenAI } from "@langchain/openai";  
    import { ChatPromptTemplate } from "@langchain/core/prompts";  
    import { StringOutputParser } from "@langchain/core/output_parsers";  
      
    const prompt = ChatPromptTemplate.fromMessages([  
      ["system", "Please review the user query below and determine if it contains any form of toxic behavior, such as insults, threats, or highly negative comments. Respond with 'Toxic' if it does, and 'Not toxic' if it doesn't."],  
      ["user", "{text}"]  
    ]);  
    const chatModel = new ChatOpenAI();  
    const outputParser = new StringOutputParser();  
      
    const chain = prompt.pipe(chatModel).pipe(outputParser);  
    

## Evaluate​

To evaluate our chain we can pass it directly to the `evaluate()` / `aevaluate()` method. Note that the input variables of the chain must match the keys of the example inputs. In this case, the example inputs should have the form `{"text": "..."}`.

  * Python
  * TypeScript

Requires `langsmith>=0.2.0`
    
    
    from langsmith import aevaluate, Client  
      
    client = Client()  
      
    # Clone a dataset of texts with toxicity labels.  
    # Each example input has a "text" key and each output has a "label" key.  
    dataset = client.clone_public_dataset(  
        "https://smith.langchain.com/public/3d6831e6-1680-4c88-94df-618c8e01fc55/d"  
    )  
      
    def correct(outputs: dict, reference_outputs: dict) -> bool:  
        # Since our chain outputs a string not a dict, this string  
        # gets stored under the default "output" key in the outputs dict:  
        actual = outputs["output"]  
        expected = reference_outputs["label"]  
      
        return actual == expected  
      
    results = await aevaluate(  
        chain,  
        data=dataset,  
        evaluators=[correct],  
        experiment_prefix="gpt-4o, baseline",  
    )  
    
    
    
    import { evaluate } from "langsmith/evaluation";  
    import { Client } from "langsmith";  
      
    const langsmith = new Client();  
    const dataset = await client.clonePublicDataset(  
      "https://smith.langchain.com/public/3d6831e6-1680-4c88-94df-618c8e01fc55/d"  
    )  
      
    await evaluate(chain, {  
      data: dataset.name,  
      evaluators: [correct],  
      experimentPrefix: "gpt-4o, baseline",  
    });  
    

The runnable is traced appropriately for each output.

![](/assets/images/runnable_eval-4e36ece7ae7bfabf2ca97e6fa247de58.png)

## Related​

  * [How to evaluate a `langgraph` graph](/evaluation/how_to_guides/langgraph)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Setup
  * Evaluate
  * Related

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)