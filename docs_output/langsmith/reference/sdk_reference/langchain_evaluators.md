# LangChain off-the-shelf evaluators | 🦜️🛠️ LangSmith

LangChain's evaluation module provides evaluators you can use as-is for common evaluation scenarios. To learn how to use these evaluators, please refer to the [following guide](/evaluation/how_to_guides/use_langchain_off_the_shelf_evaluators_old).

note

We currently support off-the-shelf evaluators in LangChain for Python only.

note

Most of these evaluators are useful but imperfect! We recommend against blind trust of any single automated metric and to always incorporate them as a part of a holistic testing and evaluation strategy. Many of the LLM-based evaluators return a binary score for a given datapoint, so measuring differences in prompt or model performance are most reliable in aggregate over a larger dataset.

The following table enumerates the off-the-shelf evaluators available in LangSmith, along with their output keys and a simple code sample.

Evaluator name| Output Key| Simple Code Example  
---|---|---  
Q&A| `correctness`| `LangChainStringEvaluator("qa")`  
Contextual Q&A| `contextual accuracy`| `LangChainStringEvaluator("context_qa")`  
Chain of Thought Q&A| `cot contextual accuracy`| `LangChainStringEvaluator("cot_qa")`  
Criteria| Depends on criteria key| `LangChainStringEvaluator("criteria", config={ "criteria": <criterion> })`  
  
`criterion` may be one of the default implemented criteria: `conciseness`, `relevance`, `correctness`, `coherence`, `harmfulness`, `maliciousness`, `helpfulness`, `controversiality`, `misogyny`, and `criminality`.  
  
Or, you may define your own criteria in a custom dict as follows:  
`{ "criterion_key": "criterion description" }`  
Labeled Criteria| Depends on criteria key| `LangChainStringEvaluator("labeled_criteria", config={ "criteria": <criterion> })`  
  
`criterion` may be one of the default implemented criteria: `conciseness`, `relevance`, `correctness`, `coherence`, `harmfulness`, `maliciousness`, `helpfulness`, `controversiality`, `misogyny`, and `criminality`.  
  
Or, you may define your own criteria in a custom dict as follows:  
`{ "criterion_key": "criterion description" }`  
Score| Depends on criteria key| `LangChainStringEvaluator("score_string", config={ "criteria": <criterion>, "normalize_by": 10 })`  
  
`criterion` may be one of the default implemented criteria: `conciseness`, `relevance`, `correctness`, `coherence`, `harmfulness`, `maliciousness`, `helpfulness`, `controversiality`, `misogyny`, and `criminality`.  
  
Or, you may define your own criteria in a custom dict as follows:  
`{ "criterion_key": "criterion description" }`. Scores are out of 10, so normalize_by will cast this to a score from 0 to 1.  
Labeled Score| Depends on criteria key| `LangChainStringEvaluator("labeled_score_string", config={ "criteria": <criterion>, "normalize_by": 10 })`  
  
`criterion` may be one of the default implemented criteria: `conciseness`, `relevance`, `correctness`, `coherence`, `harmfulness`, `maliciousness`, `helpfulness`, `controversiality`, `misogyny`, and `criminality`.  
  
Or, you may define your own criteria in a custom dict as follows:  
`{ "criterion_key": "criterion description" }`. Scores are out of 10, so normalize_by will cast this to a score from 0 to 1.  
Embedding distance| `embedding_cosine_distance`| `LangChainStringEvaluator("embedding_distance")`  
String Distance| `string_distance`| `LangChainStringEvaluator("string_distance", config={"distance": "damerau_levenshtein" })`   
  
`distance` defines the string difference metric to be applied, such as `levenshtein` or `jaro_winkler`.  
Exact Match| `exact_match`| `LangChainStringEvaluator("exact_match")`  
Regex Match| `regex_match`| `LangChainStringEvaluator("regex_match")`  
Json Validity| `json_validity`| `LangChainStringEvaluator("json_validity")`  
Json Equality| `json_equality`| `LangChainStringEvaluator("json_equality")`  
Json Edit Distance| `json_edit_distance`| `LangChainStringEvaluator("json_edit_distance")`  
Json Schema| `json_schema`| `LangChainStringEvaluator("json_schema")`  
  
* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).