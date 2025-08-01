# Prompt Engineering Quick Start (SDK) | 🦜️🛠️ LangSmith

On this page

This quick start will walk through how to create, test, and iterate on prompts using the SDK. In this tutorial we will use OpenAI, but you can use whichever LLM you want.

QuickStart

This tutorial uses the SDK for prompt engineering, if you are interested in using the UI instead, read [this guide](/prompt_engineering/quickstarts/quickstart_ui).

## 1\. Setup​

First, install the required packages:

  * Python
  * TypeScript

    
    
    pip install -qU langsmith openai langchain_core  
    
    
    
    yarn add langsmith @langchain/core langchain openai  
    

Next, make sure you have signed up for a [LangSmith](https://langsmith.com) account, then [create](/administration/how_to_guides/organization_management/create_account_api_key#create-an-api-key) and set your API key. You will also want to sign up for an OpenAI API key to run the code in this tutorial.
    
    
    LANGSMITH_API_KEY = '<your_api_key>'  
    OPENAI_API_KEY = '<your_api_key>'  
    

## 2\. Create a prompt​

To create a prompt in LangSmith, define the list of messages you want in your prompt and then wrap them using the `ChatPromptTemplate` function ([Python](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)) or [TypeScript](https://v03.api.js.langchain.com/classes/_langchain_core.prompts.ChatPromptTemplate.html) function. Then all you have to do is call [`push_prompt`](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client#langsmith.client.Client.push_prompt) (Python) or [`pushPrompt`](https://langsmith-docs-7jgx2bq8f-langchain.vercel.app/reference/js/classes/client.Client#pushprompt) (TypeScript) to send your prompt to LangSmith!

  * Python
  * TypeScript

    
    
    from langsmith import Client  
    from langchain_core.prompts import ChatPromptTemplate  
      
    # Connect to the LangSmith client  
      
    client = Client()  
      
    # Define the prompt  
      
    prompt = ChatPromptTemplate([  
    ("system", "You are a helpful chatbot."),  
    ("user", "{question}"),  
    ])  
      
    # Push the prompt  
      
    client.push_prompt("my-prompt", object=prompt)  
    
    
    
    import { Client } from "langsmith";  
    import { ChatPromptTemplate } from "@langchain/core/prompts";  
      
    // Connect to the LangSmith client  
    const client = new Client();  
      
    // Define the prompt  
    const prompt = ChatPromptTemplate.fromMessages([  
    ["system", "You are a helpful chatbot."],  
    ["user", "{question}"]  
    ]);  
      
    // Push the prompt  
    await client.pushPrompt("my-prompt", {  
    object: prompt  
    });  
    

## 3\. Test a prompt​

To test a prompt, you need to pull the prompt, invoke it with the input values you want to test and then call the model with those input values. your LLM or application expects.

  * Python
  * TypeScript

    
    
    from langsmith import Client  
    from openai import OpenAI  
    from langchain_core.messages import convert_to_openai_messages  
      
    # Connect to LangSmith and OpenAI  
      
    client = Client()  
    oai_client = OpenAI()  
      
    # Pull the prompt to use  
      
    # You can also specify a specific commit by passing the commit hash "my-prompt:<commit-hash>"  
      
    prompt = client.pull_prompt("my-prompt")  
      
    # Since our prompt only has one variable we could also pass in the value directly  
      
    # The code below is equivalent to formatted_prompt = prompt.invoke("What is the color of the sky?")  
      
    formatted_prompt = prompt.invoke({"question": "What is the color of the sky?"})  
      
    # Test the prompt  
      
    response = oai_client.chat.completions.create(  
    model="gpt-4o",  
    messages=convert_to_openai_messages(formatted_prompt.messages),  
    )  
    
    
    
    import { OpenAI } from "openai";  
    import { pull } from "langchain/hub"  
    import { convertPromptToOpenAI } from "@langchain/openai";  
      
    // Connect to LangSmith and OpenAI  
    const oaiClient = new OpenAI();  
      
    // Pull the prompt to use  
    // You can also specify a specific commit by passing the commit hash "my-prompt:<commit-hash>"  
    const prompt = await pull("my-prompt");  
      
    // Format the prompt with the question  
    const formattedPrompt = await prompt.invoke({ question: "What is the color of the sky?" });  
      
    // Test the prompt  
    const response = await oaiClient.chat.completions.create({  
    model: "gpt-4o",  
    messages: convertPromptToOpenAI(formattedPrompt).messages,  
    });  
    

## 4\. Iterate on a prompt​

LangSmith makes it easy to iterate on prompts with your entire team. Members of your workspace can select a prompt to iterate on, and once they are happy with their changes, they can simply save it as a new commit.

To improve your prompts:

  * We recommend referencing the documentation provided by your model provider for best practices in prompt creation, such as [Best practices for prompt engineering with the OpenAI API](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api) and [Gemini’s Introduction to prompt design](https://ai.google.dev/gemini-api/docs/prompting-intro).

  * To help with iterating on your prompts in LangSmith, we've created Prompt Canvas — an interactive tool to build and optimize your prompts. Learn about how to use [Prompt Canvas](/prompt_engineering/concepts#prompt-canvas).

To add a new commit to a prompt, you can use the same [`push_prompt`](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client#langsmith.client.Client.push_prompt) (Python) or [`pushPrompt`](https://langsmith-docs-7jgx2bq8f-langchain.vercel.app/reference/js/classes/client.Client#pushprompt) (TypeScript) methods as when you first created the prompt.

  * Python
  * TypeScript

    
    
    from langsmith import Client  
    from langchain_core.prompts import ChatPromptTemplate  
      
    # Connect to the LangSmith client  
      
    client = Client()  
      
    # Define the prompt to update  
      
    new_prompt = ChatPromptTemplate([  
    ("system", "You are a helpful chatbot. Respond in Spanish."),  
    ("user", "{question}"),  
    ])  
      
    # Push the updated prompt making sure to use the correct prompt name  
      
    # Tags can help you remember specific versions in your commit history  
      
    client.push_prompt("my-prompt", object=new_prompt, tags=["Spanish"])  
    
    
    
    import { Client } from "langsmith";  
    import { ChatPromptTemplate } from "@langchain/core/prompts";  
      
    // Connect to the LangSmith client  
    const client = new Client();  
      
    // Define the prompt  
    const newPrompt = ChatPromptTemplate.fromMessages([  
    ["system", "You are a helpful chatbot. Speak in Spanish."],  
    ["user", "{question}"]  
    ]);  
      
    // Push the updated prompt making sure to use the correct prompt name  
    // Tags can help you remember specific versions in your commit history  
    await client.pushPrompt("my-prompt", {  
    object: newPrompt,  
    tags: ["Spanish"]  
    });  
    

## 5\. Next steps​

  * Learn more about how to store and manage prompts using the Prompt Hub in [these how-to guides](/prompt_engineering/how_to_guides#prompt-hub)
  * Learn more about how to use the playground for prompt engineering in [these how-to guides](/prompt_engineering/how_to_guides#playground)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * 1\. Setup
  * 2\. Create a prompt
  * 3\. Test a prompt
  * 4\. Iterate on a prompt
  * 5\. Next steps

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)