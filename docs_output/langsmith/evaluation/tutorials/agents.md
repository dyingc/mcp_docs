# Evaluate a complex agent | 🦜️🛠️ LangSmith

On this page

Key concepts

[Agent evaluation](/evaluation/concepts#agents) | [Evaluators](/evaluation/concepts#evaluators) | [LLM-as-judge evaluators](/evaluation/concepts#llm-as-judge)

In this tutorial, we'll build a customer support bot that helps users navigate a digital music store. Then, we'll go through the three most effective types of evaluations to run on chat bots:

  * [Final response](/evaluation/concepts#evaluating-an-agents-final-response): Evaluate the agent's final response.
  * [Trajectory](/evaluation/concepts#evaluating-an-agents-trajectory): Evaluate whether the agent took the expected path (e.g., of tool calls) to arrive at the final answer.
  * [Single step](/evaluation/concepts#evaluating-a-single-step-of-an-agent): Evaluate any agent step in isolation (e.g., whether it selects the appropriate first tool for a given step).

We'll build our agent using [LangGraph](https://github.com/langchain-ai/langgraph), but the techniques and LangSmith functionality shown here are framework-agnostic.

## Setup​

### Configure the environment​

Let's install the required dependencies:
    
    
    pip install -U langgraph langchain[openai]  
    

Let's set up environment variables for OpenAI and [LangSmith](https://smith.langchain.com):

⌵
    
    
    import getpass  
    import os  
      
    def _set_env(var: str) -> None:  
        if not os.environ.get(var):  
            os.environ[var] = getpass.getpass(f"Set {var}: ")  
      
    os.environ["LANGSMITH_TRACING"] = "true"  
    _set_env("LANGSMITH_API_KEY")  
    _set_env("OPENAI_API_KEY")  
    

### Download the database​

We will create a SQLite database for this tutorial. SQLite is a lightweight database that is easy to set up and use. We will load the `chinook` database, which is a sample database that represents a digital media store. Find more information about the database [here](https://www.sqlitetutorial.net/sqlite-sample-database/).

For convenience, we have hosted the database in a public GCS bucket:

⌵
    
    
    import requests  
      
    url = "https://storage.googleapis.com/benchmarks-artifacts/chinook/Chinook.db"  
      
    response = requests.get(url)  
      
    if response.status_code == 200:  
        # Open a local file in binary write mode  
        with open("chinook.db", "wb") as file:  
            # Write the content of the response (the file) to the local file  
            file.write(response.content)  
        print("File downloaded and saved as Chinook.db")  
    else:  
        print(f"Failed to download the file. Status code: {response.status_code}")  
    

Here's a sample of the data in the db:

⌵
    
    
    import sqlite3 ...  
    
    
    
    [(1, 'AC/DC'), (2, 'Accept'), (3, 'Aerosmith'), (4, 'Alanis Morissette'), (5, 'Alice In Chains'), (6, 'Antônio Carlos Jobim'), (7, 'Apocalyptica'), (8, 'Audioslave'), (9, 'BackBeat'), (10, 'Billy Cobham')]  
    

And here's the database schema (image from <https://github.com/lerocha/chinook-database>):

![Chinook DB](/assets/images/chinook-diagram-1e507a47313c15ffd706a785175b2c14.png)

### Define the customer support agent​

We'll create a [LangGraph](https://langchain-ai.github.io/langgraph/) agent with limited access to our database. For demo purposes, our agent will support two basic types of requests:

  * Lookup: The customer can look up song titles, artist names, and albums based on other identifying information. For example: "What songs do you have by Jimi Hendrix?"
  * Refund: The customer can request a refund on their past purchases. For example: "My name is Claude Shannon and I'd like a refund on a purchase I made last week, could you help me?"

For simplicity in this demo, we'll implement refunds by deleting the corresponding database records. We'll skip implementing user authentication and other production security measures.

The agent's logic will be structured as two separate subgraphs (one for lookups and one for refunds), with a parent graph that routes requests to the appropriate subgraph.

#### Refund agent​

Let's build the refund processing agent. This agent needs to:

  1. Find the customer's purchase records in the database
  2. Delete the relevant Invoice and InvoiceLine records to process the refund

We'll create two SQL helper functions:

  1. A function to execute the refund by deleting records
  2. A function to look up a customer's purchase history

To make testing easier, we'll add a "mock" mode to these functions. When mock mode is enabled, the functions will simulate database operations without actually modifying any data.

⌵

⌵
    
    
    import sqlite3  
      
    def _refund(invoice_id: int | None, invoice_line_ids: list[int] | None, mock: bool = False) -> float: ...  
      
    def _lookup( ...  
    

Now let's define our graph. We'll use a simple architecture with three main paths:

  1. Extract customer and purchase information from the conversation
  2. Route the request to one of three paths:
     * Refund path: If we have sufficient purchase details (Invoice ID or Invoice Line IDs) to process a refund
     * Lookup path: If we have enough customer information (name and phone) to search their purchase history
     * Response path: If we need more information, respond to the user requesting the specific details needed

The graph's state will track:

  * The conversation history (messages between user and agent)
  * All customer and purchase information extracted from the conversation
  * The next message to send to the user (followup text)

⌵

⌵

⌵

⌵

⌵

⌵

⌵
    
    
    from typing import Literal  
    import json  
      
    from langchain.chat_models import init_chat_model  
    from langchain_core.runnables import RunnableConfig  
    from langgraph.graph import END, StateGraph  
    from langgraph.graph.message import AnyMessage, add_messages  
    from langgraph.types import Command, interrupt  
    from tabulate import tabulate  
    from typing_extensions import Annotated, TypedDict  
      
    # Graph state.  
    class State(TypedDict):  
        """Agent state."""  
        messages: Annotated[list[AnyMessage], add_messages]  
        followup: str | None  
      
        invoice_id: int | None  
        invoice_line_ids: list[int] | None  
        customer_first_name: str | None  
        customer_last_name: str | None  
        customer_phone: str | None  
        track_name: str | None  
        album_title: str | None  
        artist_name: str | None  
        purchase_date_iso_8601: str | None  
      
    # Instructions for extracting the user/purchase info from the conversation.  
    gather_info_instructions = """You are managing an online music store that sells song tracks. \  
    Customers can buy multiple tracks at a time and these purchases are recorded in a database as \  
    an Invoice per purchase and an associated set of Invoice Lines for each purchased track.  
      
    Your task is to help customers who would like a refund for one or more of the tracks they've \  
    purchased. In order for you to be able refund them, the customer must specify the Invoice ID \  
    to get a refund on all the tracks they bought in a single transaction, or one or more Invoice \  
    Line IDs if they would like refunds on individual tracks.  
      
    Often a user will not know the specific Invoice ID(s) or Invoice Line ID(s) for which they \  
    would like a refund. In this case you can help them look up their invoices by asking them to \  
    specify:  
    - Required: Their first name, last name, and phone number.  
    - Optionally: The track name, artist name, album name, or purchase date.  
      
    If the customer has not specified the required information (either Invoice/Invoice Line IDs \  
    or first name, last name, phone) then please ask them to specify it."""  
      
    # Extraction schema, mirrors the graph state.  
    class PurchaseInformation(TypedDict):  
        """All of the known information about the invoice / invoice lines the customer would like refunded. Do not make up values, leave fields as null if you don't know their value."""  
      
        invoice_id: int | None  
        invoice_line_ids: list[int] | None  
        customer_first_name: str | None  
        customer_last_name: str | None  
        customer_phone: str | None  
        track_name: str | None  
        album_title: str | None  
        artist_name: str | None  
        purchase_date_iso_8601: str | None  
        followup: Annotated[  
            str | None,  
            ...,  
            "If the user hasn't enough identifying information, please tell them what the required information is and ask them to specify it.",  
        ]  
      
    # Model for performing extraction.  
    info_llm = init_chat_model("gpt-4o-mini").with_structured_output(  
        PurchaseInformation, method="json_schema", include_raw=True  
    )  
      
    # Graph node for extracting user info and routing to lookup/refund/END.  
    async def gather_info(state: State) -> Command[Literal["lookup", "refund", END]]:  
        info = await info_llm.ainvoke(  
            [  
                {"role": "system", "content": gather_info_instructions},  
                *state["messages"],  
            ]  
        )  
        parsed = info["parsed"]  
        if any(parsed[k] for k in ("invoice_id", "invoice_line_ids")):  
            goto = "refund"  
        elif all(  
            parsed[k]  
            for k in ("customer_first_name", "customer_last_name", "customer_phone")  
        ):  
            goto = "lookup"  
        else:  
            goto = END  
        update = {"messages": [info["raw"]], **parsed}  
        return Command(update=update, goto=goto)  
      
    # Graph node for executing the refund.  
    # Note that here we inspect the runtime config for an "env" variable.  
    # If "env" is set to "test", then we don't actually delete any rows from our database.  
    # This will become important when we're running our evaluations.  
    def refund(state: State, config: RunnableConfig) -> dict:  
        # Whether to mock the deletion. True if the configurable var 'env' is set to 'test'.  
        mock = config.get("configurable", {}).get("env", "prod") == "test"  
        refunded = _refund(  
            invoice_id=state["invoice_id"], invoice_line_ids=state["invoice_line_ids"], mock=mock  
        )  
        response = f"You have been refunded a total of: ${refunded:.2f}. Is there anything else I can help with?"  
        return {  
            "messages": [{"role": "assistant", "content": response}],  
            "followup": response,  
        }  
      
    # Graph node for looking up the users purchases  
    def lookup(state: State) -> dict:  
        args = (  
            state[k]  
            for k in (  
                "customer_first_name",  
                "customer_last_name",  
                "customer_phone",  
                "track_name",  
                "album_title",  
                "artist_name",  
                "purchase_date_iso_8601",  
            )  
        )  
        results = _lookup(*args)  
        if not results:  
            response = "We did not find any purchases associated with the information you've provided. Are you sure you've entered all of your information correctly?"  
            followup = response  
        else:  
            response = f"Which of the following purchases would you like to be refunded for?\n\n```json{json.dumps(results, indent=2)}\n```"  
            followup = f"Which of the following purchases would you like to be refunded for?\n\n{tabulate(results, headers='keys')}"  
        return {  
            "messages": [{"role": "assistant", "content": response}],  
            "followup": followup,  
            "invoice_line_ids": [res["invoice_line_id"] for res in results],  
        }  
      
    # Building our graph  
    graph_builder = StateGraph(State)  
      
    graph_builder.add_node(gather_info)  
    graph_builder.add_node(refund)  
    graph_builder.add_node(lookup)  
      
    graph_builder.set_entry_point("gather_info")  
    graph_builder.add_edge("lookup", END)  
    graph_builder.add_edge("refund", END)  
      
    refund_graph = graph_builder.compile()  
    

We can visualize our refund graph:

⌵
    
    
    # Assumes you're in an interactive Python environment  
    from IPython.display import Image, display ...  
    

![Refund graph](/assets/images/refund_graph-787b57e15d5eec1642ee69a47b3c3d0c.png)

#### Lookup agent​

For the lookup (i.e. question-answering) agent, we'll use a simple ReACT architecture and give the agent tools for looking up track names, artist names, and album names based on various filters. For example, you can look up albums by a particular artist, artists who released songs with a specific name, etc.

⌵

⌵

⌵

⌵

⌵

⌵
    
    
    from langchain.embeddings import init_embeddings  
    from langchain_core.tools import tool  
    from langchain_core.vectorstores import InMemoryVectorStore  
    from langgraph.prebuilt import create_react_agent  
      
    # Our SQL queries will only work if we filter on the exact string values that are in the DB.  
    # To ensure this, we'll create vectorstore indexes for all of the artists, tracks and albums  
    # ahead of time and use those to disambiguate the user input. E.g. if a user searches for  
    # songs by "prince" and our DB records the artist as "Prince", ideally when we query our  
    # artist vectorstore for "prince" we'll get back the value "Prince", which we can then  
    # use in our SQL queries.  
    def index_fields() -> tuple[InMemoryVectorStore, InMemoryVectorStore, InMemoryVectorStore]: ...  
      
    track_store, artist_store, album_store = index_fields()  
      
    # Agent tools  
    @tool  
    def lookup_track( ...  
      
    @tool  
    def lookup_album( ...  
      
    @tool  
    def lookup_artist( ...  
      
    # Agent model  
    qa_llm = init_chat_model("claude-3-5-sonnet-latest")  
    # The prebuilt ReACT agent only expects State to have a 'messages' key, so the  
    # state we defined for the refund agent can also be passed to our lookup agent.  
    qa_graph = create_react_agent(qa_llm, [lookup_track, lookup_artist, lookup_album])  
    
    
    
    display(Image(qa_graph.get_graph(xray=True).draw_mermaid_png()))  
    

![QA Graph](data:image/png;base64,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)

#### Parent agent​

Now let's define a parent agent that combines our two task-specific agents. The only job of the parent agent is to route to one of the sub-agents by classifying the user's current intent, and to compile the output into a followup message.

⌵

⌵

⌵

⌵
    
    
    # Schema for routing user intent.  
    # We'll use structured outputs to enforce that the model returns only  
    # the desired output.  
    class UserIntent(TypedDict):  
        """The user's current intent in the conversation"""  
      
        intent: Literal["refund", "question_answering"]  
      
    # Routing model with structured output  
    router_llm = init_chat_model("gpt-4o-mini").with_structured_output(  
        UserIntent, method="json_schema", strict=True  
    )  
      
    # Instructions for routing.  
    route_instructions = """You are managing an online music store that sells song tracks. \  
    You can help customers in two types of ways: (1) answering general questions about \  
    tracks sold at your store, (2) helping them get a refund on a purhcase they made at your store.  
      
    Based on the following conversation, determine if the user is currently seeking general \  
    information about song tracks or if they are trying to refund a specific purchase.  
      
    Return 'refund' if they are trying to get a refund and 'question_answering' if they are \  
    asking a general music question. Do NOT return anything else. Do NOT try to respond to \  
    the user.  
    """  
      
    # Node for routing.  
    async def intent_classifier(  
        state: State,  
    ) -> Command[Literal["refund_agent", "question_answering_agent"]]:  
        response = router_llm.invoke(  
            [{"role": "system", "content": route_instructions}, *state["messages"]]  
        )  
        return Command(goto=response["intent"] + "_agent")  
      
    # Node for making sure the 'followup' key is set before our agent run completes.  
    def compile_followup(state: State) -> dict:  
        """Set the followup to be the last message if it hasn't explicitly been set."""  
        if not state.get("followup"):  
            return {"followup": state["messages"][-1].content}  
        return {}  
      
    # Agent definition  
    graph_builder = StateGraph(State)  
    graph_builder.add_node(intent_classifier)  
    # Since all of our subagents have compatible state,  
    # we can add them as nodes directly.  
    graph_builder.add_node("refund_agent", refund_graph)  
    graph_builder.add_node("question_answering_agent", qa_graph)  
    graph_builder.add_node(compile_followup)  
      
    graph_builder.set_entry_point("intent_classifier")  
    graph_builder.add_edge("refund_agent", "compile_followup")  
    graph_builder.add_edge("question_answering_agent", "compile_followup")  
    graph_builder.add_edge("compile_followup", END)  
      
    graph = graph_builder.compile()  
    

We can visualize our compiled parent graph including all of its subgraphs:
    
    
    display(Image(graph.get_graph().draw_mermaid_png()))  
    

![graph](/assets/images/agent_tutorial_graph-a1f868518e2642d1fdbb3ecfc7606a5c.png)

#### Try it out​

Let's give our custom support agent a whirl!

⌵
    
    
    state = await graph.ainvoke(  
        {"messages": [{"role": "user", "content": "what james brown songs do you have"}]}  
    )  
    print(state["followup"])  
    

⌵
    
    
    I found 20 James Brown songs in the database, all from the album "Sex Machine". Here they are: ...  
    

⌵
    
    
    state = await graph.ainvoke({"messages": [  
        {  
            "role": "user",  
            "content": "my name is Aaron Mitchell and my number is +1 (204) 452-6452. I bought some songs by Led Zeppelin that i'd like refunded",  
        }  
    ]})  
    print(state["followup"])  
    

⌵
    
    
    Which of the following purchases would you like to be refunded for? ...  
    

## Evaluations​

Now that we've got a testable version of our agent, let's run some evaluations. Agent evaluation can focus on at least 3 things:

  * [Final response](/evaluation/concepts#evaluating-an-agents-final-response): The inputs are a prompt and an optional list of tools. The output is the final agent response.
  * [Trajectory](/evaluation/concepts#evaluating-an-agents-trajectory): As before, the inputs are a prompt and an optional list of tools. The output is the list of tool calls
  * [Single step](/evaluation/concepts#evaluating-a-single-step-of-an-agent): As before, the inputs are a prompt and an optional list of tools. The output is the tool call.

Let's run each type of evaluation:

### Final response evaluator​

First, let's create a [dataset](/evaluation/concepts#datasets) that evaluates end-to-end performance of the agent. For simplicity we'll use the same dataset for final response and trajectory evaluation, so we'll add both ground-truth responses and trajectories for each example question. We'll cover the trajectories in the next section.

⌵

⌵
    
    
    from langsmith import Client  
      
    client = Client()  
      
    # Create a dataset  
    examples = [  
        {  
            "inputs": {  
                "question": "How many songs do you have by James Brown",  
            },  
            "outputs": {  
                "response": "We have 20 songs by James Brown",  
                "trajectory": ["question_answering_agent", "lookup_track"]  
            }  
        },  
        {  
            "inputs": {  
                "question": "My name is Aaron Mitchell and I'd like a refund.",  
            },  
            "outputs": {  
                "response": "I need some more information to help you with the refund. Please specify your phone number, the invoice ID, or the line item IDs for the purchase you'd like refunded.",  
                "trajectory": ["refund_agent"],  
            }  
        },  
        {  
            "inputs": {  
                "question": "My name is Aaron Mitchell and I'd like a refund on my Led Zeppelin purchases. My number is +1 (204) 452-6452",  
            },  
            "outputs": {  
                "response": 'Which of the following purchases would you like to be refunded for?\n\n  invoice_line_id  track_name                        artist_name    purchase_date          quantity_purchased    price_per_unit\n-----------------  --------------------------------  -------------  -------------------  --------------------  ----------------\n              267  How Many More Times               Led Zeppelin   2009-08-06 00:00:00                     1              0.99\n              268  What Is And What Should Never Be  Led Zeppelin   2009-08-06 00:00:00                     1              0.99',  
                "trajectory": ["refund_agent", "lookup"],  
            },  
        },  
        {  
            "inputs": {  
                "question": "Who recorded Wish You Were Here again? What other albums of there's do you have?",  
            },  
            "outputs": {  
                "response": "Wish You Were Here is an album by Pink Floyd",  
                "trajectory": ["question_answering_agent", "lookup_album"],  
            },  
        },  
        {  
            "inputs": {  
                "question": "I want a full refund for invoice 237",  
            },  
            "outputs": {  
                "response": "You have been refunded $0.99.",  
                "trajectory": ["refund_agent", "refund"],  
            }  
        },  
    ]  
      
    dataset_name = "Chinook Customer Service Bot: E2E"  
      
    if not client.has_dataset(dataset_name=dataset_name):  
        dataset = client.create_dataset(dataset_name=dataset_name)  
        client.create_examples(  
            dataset_id=dataset.id,  
            examples=examples  
        )  
    

We'll create a custom [LLM-as-judge](/evaluation/concepts#llm-as-judge) evaluator that uses another model to compare our agent's output on each example to the reference response, and judge if they're equivalent or not:

⌵

⌵

⌵
    
    
    # LLM-as-judge instructions  
    grader_instructions = """You are a teacher grading a quiz.  
      
    You will be given a QUESTION, the GROUND TRUTH (correct) RESPONSE, and the STUDENT RESPONSE.  
      
    Here is the grade criteria to follow:  
    (1) Grade the student responses based ONLY on their factual accuracy relative to the ground truth answer.  
    (2) Ensure that the student response does not contain any conflicting statements.  
    (3) It is OK if the student response contains more information than the ground truth response, as long as it is factually accurate relative to the  ground truth response.  
      
    Correctness:  
    True means that the student's response meets all of the criteria.  
    False means that the student's response does not meet all of the criteria.  
      
    Explain your reasoning in a step-by-step manner to ensure your reasoning and conclusion are correct."""  
      
    # LLM-as-judge output schema  
    class Grade(TypedDict):  
        """Compare the expected and actual answers and grade the actual answer."""  
        reasoning: Annotated[str, ..., "Explain your reasoning for whether the actual response is correct or not."]  
        is_correct: Annotated[bool, ..., "True if the student response is mostly or exactly correct, otherwise False."]  
      
    # Judge LLM  
    grader_llm = init_chat_model("gpt-4o-mini", temperature=0).with_structured_output(Grade, method="json_schema", strict=True)  
      
    # Evaluator function  
    async def final_answer_correct(inputs: dict, outputs: dict, reference_outputs: dict) -> bool:  
        """Evaluate if the final response is equivalent to reference response."""  
      
        # Note that we assume the outputs has a 'response' dictionary. We'll need to make sure  
        # that the target function we define includes this key.  
        user = f"""QUESTION: {inputs['question']}  
        GROUND TRUTH RESPONSE: {reference_outputs['response']}  
        STUDENT RESPONSE: {outputs['response']}"""  
      
        grade = await grader_llm.ainvoke([{"role": "system", "content": grader_instructions}, {"role": "user", "content": user}])  
        return grade["is_correct"]  
    

Now we can run our evaluation. Our evaluator assumes that our target function returns a 'response' key, so lets define a target function that does so.

Also remember that in our refund graph we made the refund node configurable, so that if we specified `config={"env": "test"}`, we would mock out the refunds without actually updating the DB. We'll use this configurable variable in our target `run_graph` method when invoking our graph:

⌵
    
    
    # Target function  
    async def run_graph(inputs: dict) -> dict:  
        """Run graph and track the trajectory it takes along with the final response."""  
        result = await graph.ainvoke({"messages": [  
            { "role": "user", "content": inputs['question']},  
        ]}, config={"env": "test"})  
        return {"response": result["followup"]}  
      
    # Evaluation job and results  
    experiment_results = await client.aevaluate(  
        run_graph,  
        data=dataset_name,  
        evaluators=[final_answer_correct],  
        experiment_prefix="sql-agent-gpt4o-e2e",  
        num_repetitions=1,  
        max_concurrency=4,  
    )  
    experiment_results.to_pandas()  
    

You can see what these results look like here: [LangSmith link](https://smith.langchain.com/public/708d08f4-300e-4c75-9677-c6b71b0d28c9/d).

### Trajectory evaluator​

As agents become more complex, they have more potential points of failure. Rather than using simple pass/fail evaluations, it's often better to use evaluations that can give partial credit when an agent takes some correct steps, even if it doesn't reach the right final answer.

This is where trajectory evaluations come in. A trajectory evaluation:

  1. Compares the actual sequence of steps the agent took against an expected sequence
  2. Calculates a score based on how many of the expected steps were completed correctly

For this example, our end-to-end dataset contains an ordered list of steps that we expect the agent to take. Let's create an evaluator that checks the agent's actual trajectory against these expected steps and calculates what percentage were completed:

⌵
    
    
    def trajectory_subsequence(outputs: dict, reference_outputs: dict) -> float:  
        """Check how many of the desired steps the agent took."""  
        if len(reference_outputs['trajectory']) > len(outputs['trajectory']):  
            return False  
      
        i = j = 0  
        while i < len(reference_outputs['trajectory']) and j < len(outputs['trajectory']):  
            if reference_outputs['trajectory'][i] == outputs['trajectory'][j]:  
                i += 1  
            j += 1  
      
        return i / len(reference_outputs['trajectory'])  
    

Now we can run our evaluation. Our evaluator assumes that our target function returns a 'trajectory' key, so lets define a target function that does so. We'll need to usage [LangGraph's streaming capabilities](https://langchain-ai.github.io/langgraph/concepts/streaming/) to record the trajectory.

Note that we are reusing the same dataset as for our final response evaluation, so we could have run both evaluators together and defined a target function that returns both "response" and "trajectory". In practice it's often useful to have separate datasets for each type of evaluation, which is why we show them separately here:

⌵
    
    
    async def run_graph(inputs: dict) -> dict:  
        """Run graph and track the trajectory it takes along with the final response."""  
        trajectory = []  
        # Set subgraph=True to stream events from subgraphs of the main graph: https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/  
        # Set stream_mode="debug" to stream all possible events: https://langchain-ai.github.io/langgraph/concepts/streaming  
        async for namespace, chunk in graph.astream({"messages": [  
                {  
                    "role": "user",  
                    "content": inputs['question'],  
                }  
            ]}, subgraphs=True, stream_mode="debug"):  
            # Event type for entering a node  
            if chunk['type'] == 'task':  
                # Record the node name  
                trajectory.append(chunk['payload']['name'])  
                # Given how we defined our dataset, we also need to track when specific tools are  
                # called by our question answering ReACT agent. These tool calls can be found  
                # when the ToolsNode (named "tools") is invoked by looking at the AIMessage.tool_calls  
                # of the latest input message.  
                if chunk['payload']['name'] == 'tools' and chunk['type'] == 'task':  
                    for tc in chunk['payload']['input']['messages'][-1].tool_calls:  
                        trajectory.append(tc['name'])  
      
        return {"trajectory": trajectory}  
      
    experiment_results = await client.aevaluate(  
        run_graph,  
        data=dataset_name,  
        evaluators=[trajectory_subsequence],  
        experiment_prefix="sql-agent-gpt4o-trajectory",  
        num_repetitions=1,  
        max_concurrency=4,  
    )  
    experiment_results.to_pandas()  
    

You can see what these results look like here: [LangSmith link](https://smith.langchain.com/public/708d08f4-300e-4c75-9677-c6b71b0d28c9/d).

### Single step evaluators​

While end-to-end tests give you the most signal about your agents performance, for the sake of debugging and iterating on your agent it can be helpful to pinpoint specific steps that are difficult and evaluate them directly.

In our case, a crucial part of our agent is that it routes the user's intention correctly into either the "refund" path or the "question answering" path. Let's create a dataset and run some evaluations to directly stress test this one component.

⌵

⌵
    
    
    # Create dataset  
    examples = [  
        {  
            "inputs": {"messages": [{"role": "user", "content": "i bought some tracks recently and i dont like them"}]},   
            "outputs": {"route": "refund_agent"},  
        },  
        {  
            "inputs": {"messages": [{"role": "user", "content": "I was thinking of purchasing some Rolling Stones tunes, any recommendations?"}]},   
            "outputs": {"route": "question_answering_agent"},  
        },  
        {  
            "inputs": {"messages": [{"role": "user", "content": "i want a refund on purchase 237"}, {"role": "assistant", "content": "I've refunded you a total of $1.98. How else can I help you today?"}, {"role": "user", "content": "did prince release any albums in 2000?"}]},   
            "outputs": {"route": "question_answering_agent"},  
        },  
        {  
            "inputs": {"messages": [{"role": "user", "content": "i purchased a cover of Yesterday recently but can't remember who it was by, which versions of it do you have?"}]},   
            "outputs": {"route": "question_answering_agent"},  
        },  
    ]  
      
    dataset_name = "Chinook Customer Service Bot: Intent Classifier"  
    if not client.has_dataset(dataset_name=dataset_name):  
        dataset = client.create_dataset(dataset_name=dataset_name)  
        client.create_examples(  
            dataset_id=dataset.id,  
            examples=examples  
        )  
      
    # Evaluator  
    def correct(outputs: dict, reference_outputs: dict) -> bool:  
        """Check if the agent chose the correct route."""  
        return outputs["route"] == reference_outputs["route"]  
      
    # Target function for running the relevant step  
    async def run_intent_classifier(inputs: dict) -> dict:  
        # Note that we can access and run the intent_classifier node of our graph directly.  
        command = await graph.nodes['intent_classifier'].ainvoke(inputs)  
        return {"route": command.goto}  
      
    # Run evaluation  
    experiment_results = await client.aevaluate(  
        run_intent_classifier,  
        data=dataset_name,  
        evaluators=[correct],  
        experiment_prefix="sql-agent-gpt4o-intent-classifier",  
        max_concurrency=4,  
    )  
    

You can see what these results look like here: [LangSmith link](https://smith.langchain.com/public/f133dae2-8a88-43a0-9bfd-ab45bfa3920b/d).

## Reference code​

Here's a consolidated script with all the above code:

⌵
    
    
    import json ...  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Setup
    * Configure the environment
    * Download the database
    * Define the customer support agent
  * Evaluations
    * Final response evaluator
    * Trajectory evaluator
    * Single step evaluators
  * Reference code

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)