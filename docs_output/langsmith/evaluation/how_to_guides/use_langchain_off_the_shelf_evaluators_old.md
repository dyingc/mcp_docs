# How to use off-the-shelf evaluators (Python only) | 🦜️🛠️ LangSmith

On this page

Recommended Reading

Before diving into this content, it might be helpful to read the following:

  * [LangChain evaluator reference](/reference/sdk_reference/langchain_evaluators)

LangChain provides a suite of off-the-shelf evaluators you can use right away to evaluate your application performance without writing any custom code. These evaluators are meant to be used more as a starting point for evaluation.

Prerequisites

Create a dataset and set up the LangSmith client in Python to follow along
    
    
    from langsmith import Client  
      
    client = Client()  
      
     Create a dataset  
    examples = [  
        {  
            "inputs": {"input": "Ankush"},  
            "outputs": {"expected": "Hello Ankush"},  
        },  
        {  
            "inputs": {"input": "Harrison"},  
            "outputs": {"expected": "Hello Harrison"},  
        },  
    ]  
      
    dataset_name = "Hello Set"  
    dataset = client.create_dataset(dataset_name=dataset_name)  
    client.create_examples(dataset_id=dataset.id, examples=examples)  
    

## Use question and answer (correctness) evaluators​

Question and answer (QA) evaluators help to measure the correctness of a response to a user query or question. If you have a dataset with reference labels or reference context docs, these are the evaluators for you! Three QA evaluators you can load are: `"qa"`, `"context_qa"`, `"cot_qa"`. Based on our meta-evals, we recommend using `"cot_qa"`, or Chain of Thought QA.

Here is a trivial example that uses a `"cot_qa"` evaluator to evaluate a simple pipeline that prefixes the input with "Hello":
    
    
    from langsmith import Client  
    from langsmith.evaluation import LangChainStringEvaluator, evaluate  
      
    cot_qa_evaluator = LangChainStringEvaluator("cot_qa")  
      
    client = Client()  
    evaluate(  
        lambda input: "Hello " + input["input"],  
        data=dataset_name,  
        evaluators=[cot_qa_evaluator],  
    )  
    

## Use criteria evaluators​

If you don't have ground truth reference labels, you can evaluate your run against a custom set of criteria using the `"criteria"` evaluators. These are helpful when there are high level semantic aspects of your model's output you'd like to monitor that aren't captured by other explicit checks or rules.

  * The `"criteria"` evaluator instructs an LLM to assess if a prediction satisfies the given criteria, outputting a binary score (0 or 1) for each criterion

    
    
    from langsmith import Client  
    from langsmith.evaluation import LangChainStringEvaluator, evaluate  
      
    criteria_evaluator = LangChainStringEvaluator(  
        "criteria",  
        config={  
            "criteria": {  
                "says_hello": "Does the submission say hello?",  
            }  
        }  
    )  
      
    client = Client()  
    evaluate(  
        lambda input: "Hello " + input["input"],  
        data=dataset_name,  
        evaluators=[  
            criteria_evaluator,  
        ],  
    )  
    

Supported Criteria

Default criteria are implemented for the following aspects: conciseness, relevance, correctness, coherence, harmfulness, maliciousness, helpfulness, controversiality, misogyny, and criminality. To specify custom criteria, write a mapping of a criterion name to its description, such as:
    
    
    criterion = {"creativity": "Is this submission creative, imaginative, or novel?"}  
    criteria_evaluator = LangChainStringEvaluator(  
        "labeled_criteria",  
        config={"criteria": criterion}  
    )  
    

Interpreting the Score

Evaluation scores don't have an inherent "direction" (i.e., higher is not necessarily better). The direction of the score depends on the criteria being evaluated. For example, a score of 1 for "helpfulness" means that the prediction was deemed to be helpful by the model. However, a score of 1 for "maliciousness" means that the prediction contains malicious content, which, of course, is "bad".

## Use labeled criteria evaluators​

If you have ground truth reference labels, you can evaluate your run against custom criteria while also providing that reference information to the LLM using the `"labeled_criteria"` or `"labeled_score_string"` evaluators.

  * The `"labeled_criteria"` evaluator instructs an LLM to assess if a prediction satisfies the criteria, taking into account the reference label
  * The `"labeled_score_string"` evaluator instructs an LLM to assess the prediction against a reference label on a specified scale

    
    
    from langsmith import Client  
    from langsmith.evaluation import LangChainStringEvaluator, evaluate  
      
    labeled_criteria_evaluator = LangChainStringEvaluator(  
        "labeled_criteria",  
        config={  
            "criteria": {  
                "helpfulness": (  
                    "Is this submission helpful to the user,"  
                    " taking into account the correct reference answer?"  
                )  
            }  
        }  
    )  
      
    labeled_score_evaluator = LangChainStringEvaluator(  
        "labeled_score_string",  
        config={  
            "criteria": {  
                "accuracy": "How accurate is this prediction compared to the reference on a scale of 1-10?"  
            },  
            "normalize_by": 10,  
        }  
    )  
      
    client = Client()  
    evaluate(  
        lambda input: "Hello " + input["input"],  
        data=dataset_name,  
        evaluators=[  
            labeled_criteria_evaluator,  
            labeled_score_evaluator  
        ],  
    )  
    

## Use string or embedding distance metrics​

To measure the similarity between a predicted string and a reference, you can use string distance metrics:

  * The `"string_distance"` evaluator computes a normalized string edit distance between the prediction and reference
  * The `"embedding_distance"` evaluator computes the distance between the text embeddings of the prediction and reference

    
    
     !pip install rapidfuzz  
    from langsmith.evaluation import LangChainStringEvaluator, evaluate  
      
    string_distance_evaluator = LangChainStringEvaluator(  
        "string_distance",  
        config={"distance": "levenshtein", "normalize_score": True}  
    )  
      
    embedding_distance_evaluator = LangChainStringEvaluator(  
        "embedding_distance",  
        config={  
          # Defaults to OpenAI, but you can customize which embedding provider to use:  
          # "embeddings": HuggingFaceEmbeddings(model="distilbert-base-uncased"),  
          # Can also choose "euclidean", "chebyshev", "hamming", and "manhattan"  
            "distance_metric": "cosine",  
          }  
    )  
      
    evaluate(  
        lambda input: "Hello " + input["input"],  
        data=dataset_name,  
        evaluators=[  
            string_distance_evaluator,  
            embedding_distance_evaluator,  
        ],  
    )  
    

## Use a custom LLM in off-the-shelf evaluators​

You can customize the model used for any LLM-based evaluator (criteria or QA). Note that this currently requires using LangChain libraries.
    
    
    from langchain_openai import ChatOpenAI  
    from langchain_core.prompts.prompt import PromptTemplate  
    from langsmith.evaluation import LangChainStringEvaluator  
      
    eval_llm = ChatOpenAI(temperature=0.0, model="gpt-4o-mini")  
    cot_qa_evaluator = LangChainStringEvaluator("cot_qa", config={"llm": eval_llm})  
      
    evaluate(  
        lambda input: "Hello " + input["input"],  
        data=dataset_name,  
        evaluators=[cot_qa_evaluator],  
    )  
    

## Handle multiple input or output fields​

LangChain off-the-shelf evaluators work seamlessly if your input dictionary, output dictionary, or example dictionary each have single fields. If you have multiple fields, you can use the `prepare_data` function to extract the relevant fields for evaluation. These map the keys `"prediction"`, `"reference"`, and `"input"` to the correct fields in the input and output dictionaries.

For the below example, we have a model that outputs two fields: `"greeting"` and `"foo"`. We want to evaluate the `"greeting"` field against the `"expected"` field in the output dictionary.
    
    
    from langsmith import Client  
    from langsmith.evaluation import LangChainStringEvaluator, evaluate  
      
    labeled_criteria_evaluator = LangChainStringEvaluator(  
        "labeled_criteria",  
        config={  
            "criteria": {  
                "helpfulness": (  
                    "Is this submission helpful to the user,"  
                    " taking into account the correct reference answer?"  
                )  
            }  
        },  
        prepare_data=lambda run, example: {  
            "prediction": run.outputs["greeting"],  
            "reference": example.outputs["expected"],  
            "input": example.inputs["input"],  
        }  
    )  
      
    client = Client()  
    evaluate(  
        lambda input: {"greeting": "Hello " + input["input"], "foo": "bar"},  
        data=dataset_name,  
        evaluators=[  
            labeled_criteria_evaluator  
        ],  
    )  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Use question and answer (correctness) evaluators
  * Use criteria evaluators
  * Use labeled criteria evaluators
  * Use string or embedding distance metrics
  * Use a custom LLM in off-the-shelf evaluators
  * Handle multiple input or output fields

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)