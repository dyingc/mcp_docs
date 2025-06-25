# Set up online evaluations | 🦜️🛠️ LangSmith

On this page

Recommended Reading

Before diving into this content, it might be helpful to read the following:

  * [Set up automation rules](/observability/how_to_guides/rules)
  * Running [online evaluations](/evaluation/concepts#online-evaluation)

Online evaluations provide real-time feedback on your production traces. This is useful to continuously monitor the performance of your application - to identify issues, measure improvements, and ensure consistent quality over time.

There are two types of online evaluations supported in LangSmith:

  * **[LLM-as-a-judge](/evaluation/concepts#llm-as-judge)** : Use an LLM to evaluate your traces. Used as a scalable way to provide human-like judgement to your output (e.g. toxicity, hallucination, correctness, etc.).
  * **Custom Code** : Write an evaluator in Python directly in LangSmith. Often used for validating structure or statistical properties of your data.

Online evaluations are configured using [automation rules](/observability/how_to_guides/rules).

## Get started with online evaluators​

#### 1\. Open the [tracing project](/observability/concepts#projects) you want to configure the online evalautor on​

#### 2\. Select the Add Rules button (top right)​

#### 3\. Configure your rule​

  * Add an evaluator name
  * Optionally filter runs that you would like to apply your evaluator on or configure a sampling rate. For example, it is commmon to apply specific evaluators based on runs that a user indicated the response was unsatisfactory, runs with a specific model, etc.
  * Select **Apply Evaluator**

### Configure a LLM-as-a-judge online evaluator​

View this guide to configure on configuring an [LLM-as-a-judge evaluator](/evaluation/how_to_guides/llm_as_judge).

### Configure a custom code evaluator​

Select **custom code** evaluator.

#### Write your evaluation function​

Custom code evaluators restrictions.

**Allowed Libraries** : You can import all standard library functions, as well as the following public packages:
    
    
      numpy (v2.2.2): "numpy"  
      pandas (v1.5.2): "pandas"  
      jsonschema (v4.21.1): "jsonschema"  
      scipy (v1.14.1): "scipy"  
      sklearn (v1.26.4): "scikit-learn"  
    

**Network Access** : You cannot access the internet from a custom code evaluator.

Custom code evaluators must be written inline. We reccomend testing locally before setting up your custom code evaluator in LangSmith.

In the UI, you will see a panel that lets you write your code inline, with some starter code:

![](/assets/images/online-eval-custom-code-a4ebb57603069f5ff0a1e5941a150222.png)

Custom code evaluators take in one arguments:

  * A `Run` ([reference](/reference/data_formats/run_data_format)). This represents the sampled run to evaluate.

They return a single value:

  * Feedback(s) Dictionary: A dictionary whose keys are the type of feedback you want to return, and values are the score you will give for that feedback key. For example, `{"correctness": 1, "silliness": 0}` would create two types of feedback on the run, one saying it is correct, and the other saying it is not silly.

In the below screenshot, you can see an example of a simple function that validates that each run in the experiment has a known json field:
    
    
    import json  
      
    def perform_eval(run):  
      output_to_validate = run['outputs']  
      is_valid_json = 0  
      
      # assert you can serialize/deserialize as json  
      try:  
        json.loads(json.dumps(output_to_validate))  
      except Exception as e:  
        return { "formatted": False }  
      
      # assert output facts exist  
      if "facts" not in output_to_validate:  
        return { "formatted": False }  
      
      # assert required fields exist  
      if "years_mentioned" not in output_to_validate["facts"]:  
        return { "formatted": False }  
      
      return {"formatted": True}  
    

#### Test and save your evaluation function​

Before saving, you can test your evaluator function on a recent run by clicking **Test Code** to make sure that your code executes properly.

Once you **Save** , your online evaluator will run over newly sampled runs (or backfilled ones too if you chose the backfill option).

If you prefer a video tutorial, check out the [Online Evaluations video](https://academy.langchain.com/pages/intro-to-langsmith-preview) from the Introduction to LangSmith Course.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Get started with online evaluators
    * Configure a LLM-as-a-judge online evaluator
    * Configure a custom code evaluator

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)