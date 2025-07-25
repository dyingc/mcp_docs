# Set up webhook notifications for rules | 🦜️🛠️ LangSmith

On this page

When you add a webhook URL on an automation action, we will make a POST request to your webhook endpoint any time the rules you defined match any new runs.

![](/assets/images/webhook-62ab900a1a3806c8513ce6ad3147b2aa.png)

## Webhook payload​

The payload we send to your webhook endpoint contains

  * `"rule_id"` this is the ID of the automation that sent this payload
  * `"start_time"` and `"end_time"` these are the time boundaries where we found matching runs
  * `"runs"` this is an array of runs, where each run is a dictionary. If you need more information about each run we suggest using our SDK in your endpoint to fetch it from our API.
  * `"feedback_stats"` this is a dictionary with the feedback statistics for the runs. An example payload for this field is shown below.

    
    
    "feedback_stats": {  
        "about_langchain": {  
            "n": 1,  
            "avg": 0.0,  
            "show_feedback_arrow": true,  
            "values": {}  
        },  
        "category": {  
            "n": 0,  
            "avg": null,  
            "show_feedback_arrow": true,  
            "values": {  
                "CONCEPTUAL": 1  
            }  
        },  
        "user_score": {  
            "n": 2,  
            "avg": 0.0,  
            "show_feedback_arrow": false,  
            "values": {}  
        },  
        "vagueness": {  
            "n": 1,  
            "avg": 0.0,  
            "show_feedback_arrow": true,  
            "values": {}  
        }  
    },  
    

fetching from S3 URLs

Depending on how recent your runs are, the `inputs_s3_urls` and `outputs_s3_urls` fields may contain S3 URLs to the actual data instead of the data itself.

The `inputs` and `outputs` can be fetched by the `ROOT.presigned_url` provided in `inputs_s3_urls` and `outputs_s3_urls` respectively.

This is an example of the entire payload we send to your webhook endpoint:
    
    
    {  
      "rule_id": "d75d7417-0c57-4655-88fe-1db3cda3a47a",  
      "start_time": "2024-04-05T01:28:54.734491+00:00",  
      "end_time": "2024-04-05T01:28:56.492563+00:00",  
      "runs": [  
        {  
          "status": "success",  
          "is_root": true,  
          "trace_id": "6ab80f10-d79c-4fa2-b441-922ed6feb630",  
          "dotted_order": "20230505T051324571809Z6ab80f10-d79c-4fa2-b441-922ed6feb630",  
          "run_type": "tool",  
          "modified_at": "2024-04-05T01:28:54.145062",  
          "tenant_id": "2ebda79f-2946-4491-a9ad-d642f49e0815",  
          "end_time": "2024-04-05T01:28:54.085649",  
          "name": "Search",  
          "start_time": "2024-04-05T01:28:54.085646",  
          "id": "6ab80f10-d79c-4fa2-b441-922ed6feb630",  
          "session_id": "6a3be6a2-9a8c-4fc8-b4c6-a8983b286cc5",  
          "parent_run_ids": [],  
          "child_run_ids": null,  
          "direct_child_run_ids": null,  
          "total_tokens": 0,  
          "completion_tokens": 0,  
          "prompt_tokens": 0,  
          "total_cost": null,  
          "completion_cost": null,  
          "prompt_cost": null,  
          "first_token_time": null,  
          "app_path": "/o/2ebda79f-2946-4491-a9ad-d642f49e0815/projects/p/6a3be6a2-9a8c-4fc8-b4c6-a8983b286cc5/r/6ab80f10-d79c-4fa2-b441-922ed6feb630?trace_id=6ab80f10-d79c-4fa2-b441-922ed6feb630&start_time=2023-05-05T05:13:24.571809",  
          "in_dataset": false,  
          "last_queued_at": null,  
          "inputs": null,  
          "inputs_s3_urls": null,  
          "outputs": null,  
          "outputs_s3_urls": null,  
          "extra": null,  
          "events": null,  
          "feedback_stats": null,  
          "serialized": null,  
          "share_token": null  
        }  
      ]  
    }  
    

### Webhook Security​

We strongly recommend you add a secret query string parameter to the webhook URL, and verify it on any incoming request. This ensures that if someone discovers your webhook URL you can distinguish those calls from authentic webhook notifications.

An example would be
    
    
    https://api.example.com/langsmith_webhook?secret=38ee77617c3a489ab6e871fbeb2ec87d  
    

### Webhook custom HTTP headers​

If you'd like to send any specific headers with your webhook, this can be configured per URL. To set this up, click on the `Headers` option next to the URL field and add your headers.

note

Headers are stored in encrypted format.

![](/assets/images/webhook_headers-7ce2425dfc9201bf7fd233eedf033526.png)

### Webhook Delivery​

When delivering events to your webhook endpoint we follow these guidelines

  * If we fail to connect to your endpoint, we retry the transport connection up to 2 times, before declaring the delivery failed.
  * If your endpoint takes longer than 5 seconds to reply we declare the delivery failed and do not .
  * If your endpoint returns a 5xx status code in less than 5 seconds we retry up to 2 times with exponential backoff.
  * If your endpoint returns a 4xx status code, we declare the delivery failed and do not retry.
  * Anything your endpoint returns in the body will be ignored

## Example with Modal​

### Setup​

For an example of how to set this up, we will use [Modal](https://modal.com/). Modal provides autoscaling GPUs for inference and fine-tuning, secure containerization for code agents, and serverless Python web endpoints. We'll focus on the web endpoints here.

First, create a Modal account. Then, locally install the Modal SDK:
    
    
    pip install modal  
    

To finish setting up your account, run the command:
    
    
    modal setup  
    

and follow the instructions

### Secrets​

Next, you will need to set up some secrets in Modal.

First, LangSmith will need to authenticate to Modal by passing in a secret. The easiest way to do this is to pass in a secret in the query parameters. To validate this secret, we will need to add a secret in _Modal_ to validate it. We will do that by creating a Modal secret. You can see instructions for secrets [here](https://modal.com/docs/guide/secrets). For this purpose, let's call our secret `ls-webhook` and have it set an environment variable with the name `LS_WEBHOOK`.

We can also set up a LangSmith secret - luckily there is already an integration template for this!

![LangSmith Modal Template](/assets/images/modal_langsmith_secret-423427ddebfb97eae4269687372b3b70.png)

### Service​

After that, you can create a Python file that will serve as your endpoint. An example is below, with comments explaining what is going on:
    
    
    from fastapi import HTTPException, status, Request, Query  
    from modal import Secret, Stub, web_endpoint, Image  
      
    stub = Stub("auth-example", image=Image.debian_slim().pip_install("langsmith"))  
      
      
    @stub.function(  
        secrets=[Secret.from_name("ls-webhook"), Secret.from_name("my-langsmith-secret")]  
    )  
    # We want this to be a `POST` endpoint since we will post data here  
    @web_endpoint(method="POST")  
    # We set up a `secret` query parameter  
    def f(data: dict, secret: str = Query(...)):  
        # You can import dependencies you don't have locally inside Modal functions  
        from langsmith import Client  
      
        # First, we validate the secret key we pass  
        import os  
      
        if secret != os.environ["LS_WEBHOOK"]:  
            raise HTTPException(  
                status_code=status.HTTP_401_UNAUTHORIZED,  
                detail="Incorrect bearer token",  
                headers={"WWW-Authenticate": "Bearer"},  
            )  
      
        # This is where we put the logic for what should happen inside this webhook  
        ls_client = Client()  
        runs = data["runs"]  
        ids = [r["id"] for r in runs]  
        feedback = list(ls_client.list_feedback(run_ids=ids))  
        for r, f in zip(runs, feedback):  
            try:  
                ls_client.create_example(  
                    inputs=r["inputs"],  
                    outputs={"output": f.correction},  
                    dataset_name="classifier-github-issues",  
                )  
            except Exception:  
                raise ValueError(f"{r} and {f}")  
        # Function body  
        return "success!"  
    

We can now deploy this easily with `modal deploy ...` (see docs [here](https://modal.com/docs/guide/managing-deployments)).

You should now get something like:
    
    
    ✓ Created objects.  
    ├── 🔨 Created mount /Users/harrisonchase/workplace/langsmith-docs/example-webhook.py  
    ├── 🔨 Created mount PythonPackage:langsmith  
    └── 🔨 Created f => https://hwchase17--auth-example-f.modal.run  
    ✓ App deployed! 🎉  
      
    View Deployment: https://modal.com/apps/hwchase17/auth-example  
    

The important thing to remember is `https://hwchase17--auth-example-f.modal.run` \- the function we created to run. NOTE: this is NOT the final deployment URL, make sure not to accidentally use that.

### Hooking it up​

We can now take the function URL we create above and add it as a webhook. We have to remember to also pass in the secret key as a query parameter. Putting it all together, it should look something like:
    
    
    https://hwchase17--auth-example-f-dev.modal.run?secret={SECRET}  
    

Replace `{SECRET}` with the secret key you created to access the Modal service.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Webhook payload
    * Webhook Security
    * Webhook custom HTTP headers
    * Webhook Delivery
  * Example with Modal
    * Setup
    * Secrets
    * Service
    * Hooking it up

  *[/]: Positional-only parameter separator (PEP 570)