# Infinity | liteLLM

On this page

Property| Details  
---|---  
Description| Infinity is a high-throughput, low-latency REST API for serving text-embeddings, reranking models and clip  
Provider Route on LiteLLM| `infinity/`  
Supported Operations| `/rerank`, `/embeddings`  
Link to Provider Doc| [Infinity ↗](https://github.com/michaelfeil/infinity)  
  
## **Usage - LiteLLM Python SDK**​
    
    
    from litellm import rerank, embedding  
    import os  
      
    os.environ["INFINITY_API_BASE"] = "http://localhost:8080"  
      
    response = rerank(  
        model="infinity/rerank",  
        query="What is the capital of France?",  
        documents=["Paris", "London", "Berlin", "Madrid"],  
    )  
    

## **Usage - LiteLLM Proxy**​

LiteLLM provides an cohere api compatible `/rerank` endpoint for Rerank calls.

**Setup**

Add this to your litellm proxy config.yaml
    
    
    model_list:  
      - model_name: custom-infinity-rerank  
        litellm_params:  
          model: infinity/rerank  
          api_base: https://localhost:8080  
          api_key: os.environ/INFINITY_API_KEY  
    

Start litellm
    
    
    litellm --config /path/to/config.yaml  
      
    # RUNNING on http://0.0.0.0:4000  
    

## Test request:​

### Rerank​
    
    
    curl http://0.0.0.0:4000/rerank \  
      -H "Authorization: Bearer sk-1234" \  
      -H "Content-Type: application/json" \  
      -d '{  
        "model": "custom-infinity-rerank",  
        "query": "What is the capital of the United States?",  
        "documents": [  
            "Carson City is the capital city of the American state of Nevada.",  
            "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",  
            "Washington, D.C. is the capital of the United States.",  
            "Capital punishment has existed in the United States since before it was a country."  
        ],  
        "top_n": 3  
      }'  
    

#### Supported Cohere Rerank API Params​

Param| Type| Description  
---|---|---  
`query`| `str`| The query to rerank the documents against  
`documents`| `list[str]`| The documents to rerank  
`top_n`| `int`| The number of documents to return  
`return_documents`| `bool`| Whether to return the documents in the response  
  
### Usage - Return Documents​

  * SDK
  * PROXY

    
    
    response = rerank(  
        model="infinity/rerank",  
        query="What is the capital of France?",  
        documents=["Paris", "London", "Berlin", "Madrid"],  
        return_documents=True,  
    )  
    
    
    
    curl http://0.0.0.0:4000/rerank \  
      -H "Authorization: Bearer sk-1234" \  
      -H "Content-Type: application/json" \  
      -d '{  
        "model": "custom-infinity-rerank",  
        "query": "What is the capital of France?",  
        "documents": [  
            "Paris",  
            "London",  
            "Berlin",  
            "Madrid"  
        ],  
        "return_documents": True,  
      }'  
    

## Pass Provider-specific Params​

Any unmapped params will be passed to the provider as-is.

  * SDK
  * PROXY

    
    
    from litellm import rerank  
    import os  
      
    os.environ["INFINITY_API_BASE"] = "http://localhost:8080"  
      
    response = rerank(  
        model="infinity/rerank",  
        query="What is the capital of France?",  
        documents=["Paris", "London", "Berlin", "Madrid"],  
        raw_scores=True, # 👈 PROVIDER-SPECIFIC PARAM  
    )  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: custom-infinity-rerank  
        litellm_params:  
          model: infinity/rerank  
          api_base: https://localhost:8080  
          raw_scores: True # 👈 EITHER SET PROVIDER-SPECIFIC PARAMS HERE OR IN REQUEST BODY  
    

  2. Start litellm

    
    
    litellm --config /path/to/config.yaml  
      
    # RUNNING on http://0.0.0.0:4000  
    

  3. Test it!

    
    
    curl http://0.0.0.0:4000/rerank \  
      -H "Authorization: Bearer sk-1234" \  
      -H "Content-Type: application/json" \  
      -d '{  
        "model": "custom-infinity-rerank",  
        "query": "What is the capital of the United States?",  
        "documents": [  
            "Carson City is the capital city of the American state of Nevada.",  
            "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",  
            "Washington, D.C. is the capital of the United States.",  
            "Capital punishment has existed in the United States since before it was a country."  
        ],  
        "raw_scores": True # 👈 PROVIDER-SPECIFIC PARAM  
      }'  
    

## Embeddings​

LiteLLM provides an OpenAI api compatible `/embeddings` endpoint for embedding calls.

**Setup**

Add this to your litellm proxy config.yaml
    
    
    model_list:  
      - model_name: custom-infinity-embedding  
        litellm_params:  
          model: infinity/provider/custom-embedding-v1  
          api_base: http://localhost:8080  
          api_key: os.environ/INFINITY_API_KEY  
    

### Test request:​
    
    
    curl http://0.0.0.0:4000/embeddings \  
      -H "Authorization: Bearer sk-1234" \  
      -H "Content-Type: application/json" \  
      -d '{  
        "model": "custom-infinity-embedding",  
        "input": ["hello"]  
      }'  
    

#### Supported Embedding API Params​

Param| Type| Description  
---|---|---  
`model`| `str`| The embedding model to use  
`input`| `list[str]`| The text inputs to generate embeddings for  
`encoding_format`| `str`| The format to return embeddings in (e.g. "float", "base64")  
`modality`| `str`| The type of input (e.g. "text", "image", "audio")  
  
### Usage - Basic Examples​

  * SDK
  * PROXY

    
    
    from litellm import embedding  
    import os  
      
    os.environ["INFINITY_API_BASE"] = "http://localhost:8080"  
      
    response = embedding(  
        model="infinity/bge-small",  
        input=["good morning from litellm"]  
    )  
      
    print(response.data[0]['embedding'])  
    
    
    
    curl http://0.0.0.0:4000/embeddings \  
      -H "Authorization: Bearer sk-1234" \  
      -H "Content-Type: application/json" \  
      -d '{  
        "model": "custom-infinity-embedding",  
        "input": ["hello"]  
      }'  
    

### Usage - OpenAI Client​

  * SDK
  * PROXY

    
    
    from openai import OpenAI  
      
    client = OpenAI(  
      api_key="<LITELLM_MASTER_KEY>",  
      base_url="<LITELLM_URL>"  
    )  
      
    response = client.embeddings.create(  
      model="bge-small",  
      input=["The food was delicious and the waiter..."],  
      encoding_format="float"  
    )  
      
    print(response.data[0].embedding)  
    
    
    
    curl http://0.0.0.0:4000/embeddings \  
      -H "Authorization: Bearer sk-1234" \  
      -H "Content-Type: application/json" \  
      -d '{  
        "model": "bge-small",  
        "input": ["The food was delicious and the waiter..."],  
        "encoding_format": "float"  
      }'  
    

  * **Usage - LiteLLM Python SDK**
  * **Usage - LiteLLM Proxy**
  * Test request:
    * Rerank
    * Usage - Return Documents
  * Pass Provider-specific Params
  * Embeddings
    * Test request:
    * Usage - Basic Examples
    * Usage - OpenAI Client