# Set up threads | 🦜️🛠️ LangSmith

On this page

Recommended Reading

Before diving into this content, it might be helpful to read the following:

  * [Add metadata and tags to traces](/observability/how_to_guides/add_metadata_tags)

Many LLM applications have a chatbot-like interface in which the user and the LLM application engage in a multi-turn conversation. In order to track these conversations, you can use the `Threads` feature in LangSmith.

## Group traces into threads​

A `Thread` is a sequence of traces representing a single conversation. Each response is represented as its own trace, but these traces are linked together by being part of the same thread.

To associate traces together, you need to pass in a special `metadata` key where the value is the unique identifier for that thread.

The key value is the unique identifier for that conversation. The key name should be one of:

  * `session_id`
  * `thread_id`
  * `conversation_id`.

The value can be any string you want, but we recommend using UUIDs, such as `f47ac10b-58cc-4372-a567-0e02b2c3d479`.

### Code example​

This example demonstrates how to log and retrieve conversation history from LangSmith to maintain long-running chats.

You can [add metadata to your traces](/observability/how_to_guides/add_metadata_tags) in LangSmith in a variety of ways, this code will show how to do so dynamically, but read the previously linked guide to learn about all the ways you can add thread identifier metadata to your traces.

  * Python
  * TypeScript

    
    
    import openai  
    from langsmith import traceable  
    from langsmith import Client  
    import langsmith as ls  
    from langsmith.wrappers import wrap_openai  
      
    client = wrap_openai(openai.Client())  
    langsmith_client = Client()  
      
    # Config used for this example  
      
    langsmith_project = "project-with-threads"  
      
      
    session_id = "thread-id-1"  
      
      
    langsmith_extra={"project_name": langsmith_project, "metadata":{"session_id": session_id}}  
      
    # gets a history of all LLM calls in the thread to construct conversation history  
      
    def get_thread_history(thread_id: str, project_name: str): # Filter runs by the specific thread and project  
      filter_string = f'and(in(metadata_key, ["session_id","conversation_id","thread_id"]), eq(metadata_value, "{thread_id}"))' # Only grab the LLM runs  
      runs = [r for r in langsmith_client.list_runs(project_name=project_name, filter=filter_string, run_type="llm")]  
      
      # Sort by start time to get the most recent interaction  
      runs = sorted(runs, key=lambda run: run.start_time, reverse=True)  
      # The current state of the conversation  
      return runs[0].inputs['messages'] + [runs[0].outputs['choices'][0]['message']]  
      
    # if an existing conversation is continued, this function looks up the current run’s metadata to get the session_id, calls get_thread_history, and appends the new user question before making a call to the chat model  
      
    @traceable(name="Chat Bot")  
    def chat_pipeline(question: str, get_chat_history: bool = False): # Whether to continue an existing thread or start a new one  
      if get_chat_history:  
          run_tree = ls.get_current_run_tree()  
          messages = get_thread_history(run_tree.extra["metadata"]["session_id"],run_tree.session_name) + [{"role": "user", "content": question}]  
      else:  
          messages = [{"role": "user", "content": question}]  
      
      # Invoke the model  
      chat_completion = client.chat.completions.create(  
          model="gpt-4o-mini", messages=messages  
      )  
      return chat_completion.choices[0].message.content  
      
    # Start the conversation  
      
    chat_pipeline("Hi, my name is Bob", langsmith_extra=langsmith_extra)  
    
    
    
    import OpenAI from "openai";  
    import { traceable, getCurrentRunTree } from "langsmith/traceable";  
    import { Client } from "langsmith";  
    import { wrapOpenAI } from "langsmith/wrappers";  
      
    // Config used for this example  
    const langsmithProject = "project-with-threads";  
    const threadId = "thread-id-1";  
      
    const client = wrapOpenAI(new OpenAI(), {  
    project_name: langsmithProject,  
    metadata: { session_id: threadId }    
    });  
    const langsmithClient = new Client();  
      
    async function getThreadHistory(threadId: string, projectName: string) {  
    // Filter runs by the specific thread and project  
    const filterString = `and(in(metadata_key, ["session_id","conversation_id","thread_id"]), eq(metadata_value, "${threadId}"))`;  
      
    // Only grab the LLM runs  
    const runs = langsmithClient.listRuns({  
    projectName: projectName,  
    filter: filterString,  
    runType: "llm"  
    });  
      
    // Sort by start time to get the most recent interaction  
    const runsArray = [];  
    for await (const run of runs) {  
    runsArray.push(run);  
    }  
    const sortedRuns = runsArray.sort((a, b) =>  
    new Date(b.start_time).getTime() - new Date(a.start_time).getTime()  
    );  
      
    // The current state of the conversation  
    return [  
    ...sortedRuns[0].inputs.messages,  
    sortedRuns[0].outputs.choices[0].message  
    ];  
    }  
      
    const chatPipeline = traceable(  
    async (  
    question: string,  
    options: {  
    getChatHistory?: boolean;  
    } = {}  
    ) => {  
    const {  
    getChatHistory = false,  
    } = options;  
      
      let messages = [];  
      // Whether to continue an existing thread or start a new one  
      if (getChatHistory) {  
        const runTree = await getCurrentRunTree();  
        const historicalMessages = await getThreadHistory(  
          runTree.extra.metadata.session_id,  
          runTree.project_name  
        );  
        messages = [  
          ...historicalMessages,  
          { role:"user", content: question }  
        ];  
      } else {  
        messages = [{ role:"user", content: question }];  
      }  
      
      // Invoke the model  
      const chatCompletion = await client.chat.completions.create({  
        model: "gpt-4o-mini",  
        messages: messages  
      });  
      return chatCompletion.choices[0].message.content;  
      
    },  
    {  
    name: "Chat Bot",  
    project_name: langsmithProject,  
    metadata: { session_id: threadId }    
    }  
    );  
      
    // Start the conversation  
    await chatPipeline("Hi, my name is Bob");  
    

After waiting a few seconds, you can make the following calls to contineu the conversation. By passing `getChatHistory: true`, you can continue the conversation from where it left off. This means that the LLM will receive the entire message history and respond to it, instead of just responding to the latest message.

  * Python
  * TypeScript

    
    
    # Continue the conversation (WAIT A FEW SECONDS BEFORE RUNNING THIS SO THE FRIST TRACE CAN BE INGESTED)  
    chat_pipeline("What is my name?", get_chat_history=True, langsmith_extra=langsmith_extra)  
      
    # Keep the conversation going (WAIT A FEW SECONDS BEFORE RUNNING THIS SO THE PREVIOUS TRACE CAN BE INGESTED)  
      
    chat_pipeline("What was the first message I sent you", get_chat_history=True, langsmith_extra=langsmith_extra)  
    
    
    
    // Continue the conversation (WAIT A FEW SECONDS BEFORE RUNNING THIS SO THE FRIST TRACE CAN BE INGESTED)  
    await chatPipeline("What is my name?", { getChatHistory: true });  
      
    // Keep the conversation going (WAIT A FEW SECONDS BEFORE RUNNING THIS SO THE PREVIOUS TRACE CAN BE INGESTED)  
    await chatPipeline("What was the first message I sent you", { getChatHistory: true });  
    

## View threads​

You can view threads by clicking on the `Threads` tab in any project details page. You will then see a list of all threads, sorted by the most recent activity.

![Thread Tab](/assets/images/convo_tab-c8ef1ebd2b8b6987bb00204c8fac2b45.png)

You can then click into a particular thread. This will open the history for a particular thread. If your threads are formatted as chat messages, you will a chatbot-like UI where you can see a history of inputs and outputs.

![Conversation](/assets/images/convo-b6f7b5ed3df4aaf3e1ec0908ea8e929e.png)

You can open up the trace or annotate the trace in a side panel by clicking on `Annotate` and `Open trace`, respectively.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Group traces into threads
    * Code example
  * View threads

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)