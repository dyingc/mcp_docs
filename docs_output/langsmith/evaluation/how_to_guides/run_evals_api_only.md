# How to use the REST API | 🦜️🛠️ LangSmith

On this page

Recommended Reading

Before diving into this content, it might be helpful to read the following:

  * [Evaluate LLM applications](/evaluation/how_to_guides/evaluate_llm_application)
  * [LangSmith API Reference](https://api.smith.langchain.com/redoc)

It is highly recommended to run evals with either the Python or TypeScript SDKs. The SDKs have many optimizations and features that enhance the performance and reliability of your evals. However, if you are unable to use the SDKs, either because you are using a different language or because you are running in a restricted environment, you can use the REST API directly.

This guide will show you how to run evals using the REST API, using the `requests` library in Python as an example. However, the same principles apply to any language.

## Create a dataset​

Here, we are using the python SDK for convenience. You can also use the API directly use the UI, see [this guide](/evaluation/how_to_guides/manage_datasets_in_application) for more information.
    
    
    import openai  
    import os  
    import requests  
      
    from datetime import datetime  
    from langsmith import Client  
    from uuid import uuid4  
      
      
    client = Client()  
      
    #  Create a dataset  
    examples = [  
        {  
            "inputs": {"text": "Shut up, idiot"},  
            "outputs": {"label": "Toxic"},  
        },  
        {  
            "inputs": {"text": "You're a wonderful person"},  
            "outputs": {"label": "Not toxic"},  
        },  
        {  
            "inputs": {"text": "This is the worst thing ever"},  
            "outputs": {"label": "Toxic"},  
        },  
        {  
            "inputs": {"text": "I had a great day today"},  
            "outputs": {"label": "Not toxic"},  
        },  
        {  
            "inputs": {"text": "Nobody likes you"},  
            "outputs": {"label": "Toxic"},  
        },  
        {  
            "inputs": {"text": "This is unacceptable. I want to speak to the manager."},  
            "outputs": {"label": "Not toxic"},  
        },  
    ]  
      
    dataset_name = "Toxic Queries - API Example"  
    dataset = client.create_dataset(dataset_name=dataset_name)  
    client.create_examples(dataset_id=dataset.id, examples=examples)  
    

## Run a single experiment​

First, pull all of the examples you'd want to use in your experiment.
    
    
    #  Pick a dataset id. In this case, we are using the dataset we created above.  
    #  Spec: https://api.smith.langchain.com/redoc#tag/examples/operation/delete_example_api_v1_examples__example_id__delete  
    dataset_id = dataset.id  
    params = { "dataset": dataset_id }  
      
    resp = requests.get(  
        "https://api.smith.langchain.com/api/v1/examples",  
        params=params,  
        headers={"x-api-key": os.environ["LANGSMITH_API_KEY"]}  
    )  
      
    examples = resp.json()  
    

Next, we'll define a method that will create a run for a single example.
    
    
    os.environ["OPENAI_API_KEY"] = "sk-..."  
      
    def run_completion_on_example(example, model_name, experiment_id):  
        """Run completions on a list of examples."""  
        # We are using the OpenAI API here, but you can use any model you like  
      
        def _post_run(run_id, name, run_type, inputs, parent_id=None):  
            """Function to post a new run to the API."""  
            data = {  
                "id": run_id.hex,  
                "name": name,  
                "run_type": run_type,  
                "inputs": inputs,  
                "start_time": datetime.utcnow().isoformat(),  
                "reference_example_id": example["id"],  
                "session_id": experiment_id,  
            }  
            if parent_id:  
                data["parent_run_id"] = parent_id.hex  
            resp = requests.post(  
                "https://api.smith.langchain.com/api/v1/runs", # Update appropriately for self-hosted installations or the EU region  
                json=data,  
                headers=headers  
            )  
            resp.raise_for_status()  
      
        def _patch_run(run_id, outputs):  
            """Function to patch a run with outputs."""  
            resp = requests.patch(  
                f"https://api.smith.langchain.com/api/v1/runs/{run_id}",  
                json={  
                    "outputs": outputs,  
                    "end_time": datetime.utcnow().isoformat(),  
                },  
                headers=headers,  
            )  
            resp.raise_for_status()  
      
        # Send your API Key in the request headers  
        headers = {"x-api-key": os.environ["LANGSMITH_API_KEY"]}  
      
        text = example["inputs"]["text"]  
      
        messages = [  
            {  
                "role": "system",  
                "content": "Please review the user query below and determine if it contains any form of toxic behavior, such as insults, threats, or highly negative comments. Respond with 'Toxic' if it does, and 'Not toxic' if it doesn't.",  
            },  
            {"role": "user", "content": text},  
        ]  
      
      
        # Create parent run  
        parent_run_id = uuid4()  
        _post_run(parent_run_id, "LLM Pipeline", "chain", {"text": text})  
      
        # Create child run  
        child_run_id = uuid4()  
        _post_run(child_run_id, "OpenAI Call", "llm", {"messages": messages}, parent_run_id)  
      
        # Generate a completion  
        client = openai.Client()  
        chat_completion = client.chat.completions.create(model=model_name, messages=messages)  
      
        # End runs  
        _patch_run(child_run_id, chat_completion.dict())  
        _patch_run(parent_run_id, {"label": chat_completion.choices[0].message.content})  
    

We are going to run completions on all examples using two models: gpt-3.5-turbo and gpt-4o-mini.
    
    
    #  Create a new experiment using the /sessions endpoint  
    #  An experiment is a collection of runs with a reference to the dataset used  
    #  Spec: https://api.smith.langchain.com/redoc#tag/tracer-sessions/operation/create_tracer_session_api_v1_sessions_post  
      
    model_names = ("gpt-3.5-turbo", "gpt-4o-mini")  
    experiment_ids = []  
    for model_name in model_names:  
        resp = requests.post(  
            "https://api.smith.langchain.com/api/v1/sessions",  
            json={  
                "start_time": datetime.utcnow().isoformat(),  
                "reference_dataset_id": str(dataset_id),  
                "description": "An optional description for the experiment",  
                "name": f"Toxicity detection - API Example - {model_name} - {str(uuid4())[0:8]}",  # A name for the experiment  
                "extra": {  
                    "metadata": {"foo": "bar"},  # Optional metadata  
                },  
            },  
            headers={"x-api-key": os.environ["LANGSMITH_API_KEY"]}  
        )  
      
        experiment = resp.json()  
        experiment_ids.append(experiment["id"])  
      
        # Run completions on all examples  
        for example in examples:  
            run_completion_on_example(example, model_name, experiment["id"])  
      
        # Issue a patch request to "end" the experiment by updating the end_time  
        requests.patch(  
            f"https://api.smith.langchain.com/api/v1/sessions/{experiment['id']}",  
            json={"end_time": datetime.utcnow().isoformat()},  
            headers={"x-api-key": os.environ["LANGSMITH_API_KEY"]}  
        )  
    

## Run a pairwise experiment​

Next, we'll demonstrate how to run a pairwise experiment. In a pairwise experiment, you compare two examples against each other. For more information, check out [this guide](/evaluation/how_to_guides/evaluate_pairwise).
    
    
    #  A comparative experiment allows you to provide a preferential ranking on the outputs of two or more experiments  
    #  Spec: https://api.smith.langchain.com/redoc#tag/datasets/operation/create_comparative_experiment_api_v1_datasets_comparative_post  
    resp = requests.post(  
        "https://api.smith.langchain.com/api/v1/datasets/comparative",  
        json={  
            "experiment_ids": experiment_ids,  
            "name": "Toxicity detection - API Example - Comparative - " + str(uuid4())[0:8],  
            "description": "An optional description for the comparative experiment",  
            "extra": {  
                "metadata": {"foo": "bar"},  # Optional metadata  
            },  
            "reference_dataset_id": str(dataset_id),  
        },  
        headers={"x-api-key": os.environ["LANGSMITH_API_KEY"]}  
    )  
      
    comparative_experiment = resp.json()  
    comparative_experiment_id = comparative_experiment["id"]  
      
    #  You can iterate over the runs in the experiments belonging to the comparative experiment and preferentially rank the outputs  
      
    #  Fetch the comparative experiment  
    resp = requests.get(  
        f"https://api.smith.langchain.com/api/v1/datasets/{str(dataset_id)}/comparative",  
        params={"id": comparative_experiment_id},  
        headers={"x-api-key": os.environ["LANGSMITH_API_KEY"]}  
    )  
      
    comparative_experiment = resp.json()[0]  
    experiment_ids = [info["id"] for info in comparative_experiment["experiments_info"]]  
      
    from collections import defaultdict  
    example_id_to_runs_map = defaultdict(list)  
      
    #  Spec: https://api.smith.langchain.com/redoc#tag/run/operation/query_runs_api_v1_runs_query_post  
    runs = requests.post(  
        f"https://api.smith.langchain.com/api/v1/runs/query",  
        headers={"x-api-key": os.environ["LANGSMITH_API_KEY"]},  
        json={  
            "session": experiment_ids,  
            "is_root": True, # Only fetch root runs (spans) which contain the end outputs  
            "select": ["id", "reference_example_id", "outputs"],  
        }  
    ).json()  
    runs = runs["runs"]  
    for run in runs:  
        example_id = run["reference_example_id"]  
        example_id_to_runs_map[example_id].append(run)  
      
    for example_id, runs in example_id_to_runs_map.items():  
        print(f"Example ID: {example_id}")  
        # Preferentially rank the outputs, in this case we will always prefer the first output  
        # In reality, you can use an LLM to rank the outputs  
        feedback_group_id = uuid4()  
      
        # Post a feedback score for each run, with the first run being the preferred one  
        # Spec: https://api.smith.langchain.com/redoc#tag/feedback/operation/create_feedback_api_v1_feedback_post  
        # We'll use the feedback group ID to associate the feedback scores with the same group  
        for i, run in enumerate(runs):  
            print(f"Run ID: {run['id']}")  
            feedback = {  
                "score": 1 if i == 0 else 0,  
                "run_id": str(run["id"]),  
                "key": "ranked_preference",  
                "feedback_group_id": str(feedback_group_id),  
                "comparative_experiment_id": comparative_experiment_id,  
            }  
            resp = requests.post(  
                "https://api.smith.langchain.com/api/v1/feedback",  
                json=feedback,  
                headers={"x-api-key": os.environ["LANGSMITH_API_KEY"]}  
            )  
            resp.raise_for_status()  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Create a dataset
  * Run a single experiment
  * Run a pairwise experiment

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)