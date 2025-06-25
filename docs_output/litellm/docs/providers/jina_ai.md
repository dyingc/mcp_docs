# Jina AI | liteLLM

On this page

<https://jina.ai/embeddings/>

Supported endpoints:

  * /embeddings
  * /rerank

## API Key​
    
    
    # env variable  
    os.environ['JINA_AI_API_KEY']  
    

## Sample Usage - Embedding​

  * SDK
  * PROXY

    
    
    from litellm import embedding  
    import os  
      
    os.environ['JINA_AI_API_KEY'] = ""  
    response = embedding(  
        model="jina_ai/jina-embeddings-v3",  
        input=["good morning from litellm"],  
    )  
    print(response)  
    

  1. Add to config.yaml

    
    
    model_list:  
      - model_name: embedding-model  
        litellm_params:  
          model: jina_ai/jina-embeddings-v3  
          api_key: os.environ/JINA_AI_API_KEY  
    

  2. Start proxy

    
    
    litellm --config /path/to/config.yaml  
      
    # RUNNING on http://0.0.0.0:4000/  
    

  3. Test it!

    
    
    curl -L -X POST 'http://0.0.0.0:4000/embeddings' \  
    -H 'Authorization: Bearer sk-1234' \  
    -H 'Content-Type: application/json' \  
    -d '{"input": ["hello world"], "model": "embedding-model"}'  
    

## Sample Usage - Rerank​

  * SDK
  * PROXY

    
    
    from litellm import rerank  
    import os  
      
    os.environ["JINA_AI_API_KEY"] = "sk-..."  
      
    query = "What is the capital of the United States?"  
    documents = [  
        "Carson City is the capital city of the American state of Nevada.",  
        "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",  
        "Washington, D.C. is the capital of the United States.",  
        "Capital punishment has existed in the United States since before it was a country.",  
    ]  
      
    response = rerank(  
        model="jina_ai/jina-reranker-v2-base-multilingual",  
        query=query,  
        documents=documents,  
        top_n=3,  
    )  
    print(response)  
    

  1. Add to config.yaml

    
    
    model_list:  
      - model_name: rerank-model  
        litellm_params:  
          model: jina_ai/jina-reranker-v2-base-multilingual  
          api_key: os.environ/JINA_AI_API_KEY  
    

  2. Start proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
    curl -L -X POST 'http://0.0.0.0:4000/rerank' \  
    -H 'Authorization: Bearer sk-1234' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "model": "rerank-model",  
        "query": "What is the capital of the United States?",  
        "documents": [  
            "Carson City is the capital city of the American state of Nevada.",  
            "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",  
            "Washington, D.C. is the capital of the United States.",  
            "Capital punishment has existed in the United States since before it was a country."  
        ],  
        "top_n": 3  
    }'  
    

## Supported Models​

All models listed here <https://jina.ai/embeddings/> are supported

## Supported Optional Rerank Parameters​

All cohere rerank parameters are supported.

## Supported Optional Embeddings Parameters​
    
    
    dimensions  
    

## Provider-specific parameters​

Pass any jina ai specific parameters as a keyword argument to the `embedding` or `rerank` function, e.g.

  * SDK
  * PROXY

    
    
    response = embedding(  
        model="jina_ai/jina-embeddings-v3",  
        input=["good morning from litellm"],  
        dimensions=1536,  
        my_custom_param="my_custom_value", # any other jina ai specific parameters  
    )  
    
    
    
    curl -L -X POST 'http://0.0.0.0:4000/embeddings' \  
    -H 'Authorization: Bearer sk-1234' \  
    -H 'Content-Type: application/json' \  
    -d '{"input": ["good morning from litellm"], "model": "jina_ai/jina-embeddings-v3", "dimensions": 1536, "my_custom_param": "my_custom_value"}'  
    

  * API Key
  * Sample Usage - Embedding
  * Sample Usage - Rerank
  * Supported Models
  * Supported Optional Rerank Parameters
  * Supported Optional Embeddings Parameters
  * Provider-specific parameters