# Caching | liteLLM

On this page

note

For OpenAI/Anthropic Prompt Caching, go [here](/docs/completion/prompt_caching)

Cache LLM Responses. LiteLLM's caching system stores and reuses LLM responses to save costs and reduce latency. When you make the same request twice, the cached response is returned instead of calling the LLM API again.

### Supported Caches​

  * In Memory Cache
  * Disk Cache
  * Redis Cache
  * Qdrant Semantic Cache
  * Redis Semantic Cache
  * s3 Bucket Cache

## Quick Start​

  * redis cache
  * Qdrant Semantic cache
  * s3 cache
  * redis semantic cache
  * In Memory Cache
  * Disk Cache

Caching can be enabled by adding the `cache` key in the `config.yaml`

#### Step 1: Add `cache` to the config.yaml​
    
    
    model_list:  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: gpt-3.5-turbo  
      - model_name: text-embedding-ada-002  
        litellm_params:  
          model: text-embedding-ada-002  
      
    litellm_settings:  
      set_verbose: True  
      cache: True          # set cache responses to True, litellm defaults to using a redis cache  
    

#### [OPTIONAL] Step 1.5: Add redis namespaces, default ttl​

#### Namespace​

If you want to create some folder for your keys, you can set a namespace, like this:
    
    
    litellm_settings:  
      cache: true   
      cache_params:        # set cache params for redis  
        type: redis  
        namespace: "litellm.caching.caching"  
    

and keys will be stored like:
    
    
    litellm.caching.caching:<hash>  
    

#### Redis Cluster​

  * Set on config.yaml
  * Set on .env

    
    
    model_list:  
      - model_name: "*"  
        litellm_params:  
          model: "*"  
      
      
    litellm_settings:  
      cache: True  
      cache_params:  
        type: redis  
        redis_startup_nodes: [{"host": "127.0.0.1", "port": "7001"}]   
    

You can configure redis cluster in your .env by setting `REDIS_CLUSTER_NODES` in your .env

**Example`REDIS_CLUSTER_NODES`** value
    
    
    REDIS_CLUSTER_NODES = "[{"host": "127.0.0.1", "port": "7001"}, {"host": "127.0.0.1", "port": "7003"}, {"host": "127.0.0.1", "port": "7004"}, {"host": "127.0.0.1", "port": "7005"}, {"host": "127.0.0.1", "port": "7006"}, {"host": "127.0.0.1", "port": "7007"}]"  
    

note

Example python script for setting redis cluster nodes in .env:
    
    
    # List of startup nodes  
    startup_nodes = [  
        {"host": "127.0.0.1", "port": "7001"},  
        {"host": "127.0.0.1", "port": "7003"},  
        {"host": "127.0.0.1", "port": "7004"},  
        {"host": "127.0.0.1", "port": "7005"},  
        {"host": "127.0.0.1", "port": "7006"},  
        {"host": "127.0.0.1", "port": "7007"},  
    ]  
      
    # set startup nodes in environment variables  
    os.environ["REDIS_CLUSTER_NODES"] = json.dumps(startup_nodes)  
    print("REDIS_CLUSTER_NODES", os.environ["REDIS_CLUSTER_NODES"])  
    

#### Redis Sentinel​

  * Set on config.yaml
  * Set on .env

    
    
    model_list:  
      - model_name: "*"  
        litellm_params:  
          model: "*"  
      
      
    litellm_settings:  
      cache: true  
      cache_params:  
        type: "redis"  
        service_name: "mymaster"  
        sentinel_nodes: [["localhost", 26379]]  
        sentinel_password: "password" # [OPTIONAL]  
    

You can configure redis sentinel in your .env by setting `REDIS_SENTINEL_NODES` in your .env

**Example`REDIS_SENTINEL_NODES`** value
    
    
    REDIS_SENTINEL_NODES='[["localhost", 26379]]'  
    REDIS_SERVICE_NAME = "mymaster"  
    REDIS_SENTINEL_PASSWORD = "password"  
    

note

Example python script for setting redis cluster nodes in .env:
    
    
    # List of startup nodes  
    sentinel_nodes = [["localhost", 26379]]  
      
    # set startup nodes in environment variables  
    os.environ["REDIS_SENTINEL_NODES"] = json.dumps(sentinel_nodes)  
    print("REDIS_SENTINEL_NODES", os.environ["REDIS_SENTINEL_NODES"])  
    

#### TTL​
    
    
    litellm_settings:  
      cache: true   
      cache_params:        # set cache params for redis  
        type: redis  
        ttl: 600 # will be cached on redis for 600s  
        # default_in_memory_ttl: Optional[float], default is None. time in seconds.   
        # default_in_redis_ttl: Optional[float], default is None. time in seconds.   
    

#### SSL​

just set `REDIS_SSL="True"` in your .env, and LiteLLM will pick this up.
    
    
    REDIS_SSL="True"  
    

For quick testing, you can also use REDIS_URL, eg.:
    
    
    REDIS_URL="rediss://.."  
    

but we **don't** recommend using REDIS_URL in prod. We've noticed a performance difference between using it vs. redis_host, port, etc.

#### Step 2: Add Redis Credentials to .env​

Set either `REDIS_URL` or the `REDIS_HOST` in your os environment, to enable caching.
    
    
    REDIS_URL = ""        # REDIS_URL='redis://username:password@hostname:port/database'  
    ## OR ##   
    REDIS_HOST = ""       # REDIS_HOST='redis-18841.c274.us-east-1-3.ec2.cloud.redislabs.com'  
    REDIS_PORT = ""       # REDIS_PORT='18841'  
    REDIS_PASSWORD = ""   # REDIS_PASSWORD='liteLlmIsAmazing'  
    

**Additional kwargs**  
You can pass in any additional redis.Redis arg, by storing the variable + value in your os environment, like this:
    
    
    REDIS_<redis-kwarg-name> = ""  
    

[**See how it's read from the environment**](https://github.com/BerriAI/litellm/blob/4d7ff1b33b9991dcf38d821266290631d9bcd2dd/litellm/_redis.py#L40)

#### Step 3: Run proxy with config​
    
    
    $ litellm --config /path/to/config.yaml  
    

Caching can be enabled by adding the `cache` key in the `config.yaml`

#### Step 1: Add `cache` to the config.yaml​
    
    
    model_list:  
      - model_name: fake-openai-endpoint  
        litellm_params:  
          model: openai/fake  
          api_key: fake-key  
          api_base: https://exampleopenaiendpoint-production.up.railway.app/  
      - model_name: openai-embedding  
        litellm_params:  
          model: openai/text-embedding-3-small  
          api_key: os.environ/OPENAI_API_KEY  
      
    litellm_settings:  
      set_verbose: True  
      cache: True          # set cache responses to True, litellm defaults to using a redis cache  
      cache_params:  
        type: qdrant-semantic  
        qdrant_semantic_cache_embedding_model: openai-embedding # the model should be defined on the model_list  
        qdrant_collection_name: test_collection  
        qdrant_quantization_config: binary  
        similarity_threshold: 0.8   # similarity threshold for semantic cache  
    

#### Step 2: Add Qdrant Credentials to your .env​
    
    
    QDRANT_API_KEY = "16rJUMBRx*************"  
    QDRANT_API_BASE = "https://5392d382-45*********.cloud.qdrant.io"  
    

#### Step 3: Run proxy with config​
    
    
    $ litellm --config /path/to/config.yaml  
    

#### Step 4. Test it​
    
    
    curl -i http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-1234" \  
      -d '{  
        "model": "fake-openai-endpoint",  
        "messages": [  
          {"role": "user", "content": "Hello"}  
        ]  
      }'  
    

**Expect to see`x-litellm-semantic-similarity` in the response headers when semantic caching is one**

#### Step 1: Add `cache` to the config.yaml​
    
    
    model_list:  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: gpt-3.5-turbo  
      - model_name: text-embedding-ada-002  
        litellm_params:  
          model: text-embedding-ada-002  
      
    litellm_settings:  
      set_verbose: True  
      cache: True          # set cache responses to True  
      cache_params:        # set cache params for s3  
        type: s3  
        s3_bucket_name: cache-bucket-litellm   # AWS Bucket Name for S3  
        s3_region_name: us-west-2              # AWS Region Name for S3  
        s3_aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID  # us os.environ/<variable name> to pass environment variables. This is AWS Access Key ID for S3  
        s3_aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY  # AWS Secret Access Key for S3  
        s3_endpoint_url: https://s3.amazonaws.com  # [OPTIONAL] S3 endpoint URL, if you want to use Backblaze/cloudflare s3 buckets  
    

#### Step 2: Run proxy with config​
    
    
    $ litellm --config /path/to/config.yaml  
    

Caching can be enabled by adding the `cache` key in the `config.yaml`

#### Step 1: Add `cache` to the config.yaml​
    
    
    model_list:  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: gpt-3.5-turbo  
      - model_name: azure-embedding-model  
        litellm_params:  
          model: azure/azure-embedding-model  
          api_base: os.environ/AZURE_API_BASE  
          api_key: os.environ/AZURE_API_KEY  
          api_version: "2023-07-01-preview"  
      
    litellm_settings:  
      set_verbose: True  
      cache: True          # set cache responses to True  
      cache_params:  
        type: "redis-semantic"    
        similarity_threshold: 0.8   # similarity threshold for semantic cache  
        redis_semantic_cache_embedding_model: azure-embedding-model # set this to a model_name set in model_list  
    

#### Step 2: Add Redis Credentials to .env​

Set either `REDIS_URL` or the `REDIS_HOST` in your os environment, to enable caching.
    
    
    REDIS_URL = ""        # REDIS_URL='redis://username:password@hostname:port/database'  
    ## OR ##   
    REDIS_HOST = ""       # REDIS_HOST='redis-18841.c274.us-east-1-3.ec2.cloud.redislabs.com'  
    REDIS_PORT = ""       # REDIS_PORT='18841'  
    REDIS_PASSWORD = ""   # REDIS_PASSWORD='liteLlmIsAmazing'  
    

**Additional kwargs**  
You can pass in any additional redis.Redis arg, by storing the variable + value in your os environment, like this:
    
    
    REDIS_<redis-kwarg-name> = ""  
    

#### Step 3: Run proxy with config​
    
    
    $ litellm --config /path/to/config.yaml  
    

#### Step 1: Add `cache` to the config.yaml​
    
    
    litellm_settings:  
      cache: True  
      cache_params:  
        type: local  
    

#### Step 2: Run proxy with config​
    
    
    $ litellm --config /path/to/config.yaml  
    

#### Step 1: Add `cache` to the config.yaml​
    
    
    litellm_settings:  
      cache: True  
      cache_params:  
        type: disk  
        disk_cache_dir: /tmp/litellm-cache  # OPTIONAL, default to ./.litellm_cache  
    

#### Step 2: Run proxy with config​
    
    
    $ litellm --config /path/to/config.yaml  
    

## Usage​

### Basic​

  * /chat/completions
  * /embeddings

Send the same request twice:
    
    
    curl http://0.0.0.0:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -d '{  
         "model": "gpt-3.5-turbo",  
         "messages": [{"role": "user", "content": "write a poem about litellm!"}],  
         "temperature": 0.7  
       }'  
      
    curl http://0.0.0.0:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -d '{  
         "model": "gpt-3.5-turbo",  
         "messages": [{"role": "user", "content": "write a poem about litellm!"}],  
         "temperature": 0.7  
       }'  
    

Send the same request twice:
    
    
    curl --location 'http://0.0.0.0:4000/embeddings' \  
      --header 'Content-Type: application/json' \  
      --data ' {  
      "model": "text-embedding-ada-002",  
      "input": ["write a litellm poem"]  
      }'  
      
    curl --location 'http://0.0.0.0:4000/embeddings' \  
      --header 'Content-Type: application/json' \  
      --data ' {  
      "model": "text-embedding-ada-002",  
      "input": ["write a litellm poem"]  
      }'  
    

### Dynamic Cache Controls​

Parameter| Type| Description  
---|---|---  
`ttl`|  _Optional(int)_|  Will cache the response for the user-defined amount of time (in seconds)  
`s-maxage`|  _Optional(int)_|  Will only accept cached responses that are within user-defined range (in seconds)  
`no-cache`|  _Optional(bool)_|  Will not store the response in cache.  
`no-store`|  _Optional(bool)_|  Will not cache the response  
`namespace`|  _Optional(str)_|  Will cache the response under a user-defined namespace  
  
Each cache parameter can be controlled on a per-request basis. Here are examples for each parameter:

### `ttl`​

Set how long (in seconds) to cache a response.

  * OpenAI Python SDK
  * curl

    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        api_key="your-api-key",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    chat_completion = client.chat.completions.create(  
        messages=[{"role": "user", "content": "Hello"}],  
        model="gpt-3.5-turbo",  
        extra_body={  
            "cache": {  
                "ttl": 300  # Cache response for 5 minutes  
            }  
        }  
    )  
    
    
    
    curl http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-1234" \  
      -d '{  
        "model": "gpt-3.5-turbo",  
        "cache": {"ttl": 300},  
        "messages": [  
          {"role": "user", "content": "Hello"}  
        ]  
      }'  
    

### `s-maxage`​

Only accept cached responses that are within the specified age (in seconds).

  * OpenAI Python SDK
  * curl

    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        api_key="your-api-key",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    chat_completion = client.chat.completions.create(  
        messages=[{"role": "user", "content": "Hello"}],  
        model="gpt-3.5-turbo",  
        extra_body={  
            "cache": {  
                "s-maxage": 600  # Only use cache if less than 10 minutes old  
            }  
        }  
    )  
    
    
    
    curl http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-1234" \  
      -d '{  
        "model": "gpt-3.5-turbo",  
        "cache": {"s-maxage": 600},  
        "messages": [  
          {"role": "user", "content": "Hello"}  
        ]  
      }'  
    

### `no-cache`​

Force a fresh response, bypassing the cache.

  * OpenAI Python SDK
  * curl

    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        api_key="your-api-key",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    chat_completion = client.chat.completions.create(  
        messages=[{"role": "user", "content": "Hello"}],  
        model="gpt-3.5-turbo",  
        extra_body={  
            "cache": {  
                "no-cache": True  # Skip cache check, get fresh response  
            }  
        }  
    )  
    
    
    
    curl http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-1234" \  
      -d '{  
        "model": "gpt-3.5-turbo",  
        "cache": {"no-cache": true},  
        "messages": [  
          {"role": "user", "content": "Hello"}  
        ]  
      }'  
    

### `no-store`​

Will not store the response in cache.

  * OpenAI Python SDK
  * curl

    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        api_key="your-api-key",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    chat_completion = client.chat.completions.create(  
        messages=[{"role": "user", "content": "Hello"}],  
        model="gpt-3.5-turbo",  
        extra_body={  
            "cache": {  
                "no-store": True  # Don't cache this response  
            }  
        }  
    )  
    
    
    
    curl http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-1234" \  
      -d '{  
        "model": "gpt-3.5-turbo",  
        "cache": {"no-store": true},  
        "messages": [  
          {"role": "user", "content": "Hello"}  
        ]  
      }'  
    

### `namespace`​

Store the response under a specific cache namespace.

  * OpenAI Python SDK
  * curl

    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        api_key="your-api-key",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    chat_completion = client.chat.completions.create(  
        messages=[{"role": "user", "content": "Hello"}],  
        model="gpt-3.5-turbo",  
        extra_body={  
            "cache": {  
                "namespace": "my-custom-namespace"  # Store in custom namespace  
            }  
        }  
    )  
    
    
    
    curl http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-1234" \  
      -d '{  
        "model": "gpt-3.5-turbo",  
        "cache": {"namespace": "my-custom-namespace"},  
        "messages": [  
          {"role": "user", "content": "Hello"}  
        ]  
      }'  
    

## Set cache for proxy, but not on the actual llm api call​

Use this if you just want to enable features like rate limiting, and loadbalancing across multiple instances.

Set `supported_call_types: []` to disable caching on the actual api call.
    
    
    litellm_settings:  
      cache: True  
      cache_params:  
        type: redis  
        supported_call_types: []   
    

## Debugging Caching - `/cache/ping`​

LiteLLM Proxy exposes a `/cache/ping` endpoint to test if the cache is working as expected

**Usage**
    
    
    curl --location 'http://0.0.0.0:4000/cache/ping'  -H "Authorization: Bearer sk-1234"  
    

**Expected Response - when cache healthy**
    
    
    {  
        "status": "healthy",  
        "cache_type": "redis",  
        "ping_response": true,  
        "set_cache_response": "success",  
        "litellm_cache_params": {  
            "supported_call_types": "['completion', 'acompletion', 'embedding', 'aembedding', 'atranscription', 'transcription']",  
            "type": "redis",  
            "namespace": "None"  
        },  
        "redis_cache_params": {  
            "redis_client": "Redis<ConnectionPool<Connection<host=redis-16337.c322.us-east-1-2.ec2.cloud.redislabs.com,port=16337,db=0>>>",  
            "redis_kwargs": "{'url': 'redis://:******@redis-16337.c322.us-east-1-2.ec2.cloud.redislabs.com:16337'}",  
            "async_redis_conn_pool": "BlockingConnectionPool<Connection<host=redis-16337.c322.us-east-1-2.ec2.cloud.redislabs.com,port=16337,db=0>>",  
            "redis_version": "7.2.0"  
        }  
    }  
    

## Advanced​

### Control Call Types Caching is on for - (`/chat/completion`, `/embeddings`, etc.)​

By default, caching is on for all call types. You can control which call types caching is on for by setting `supported_call_types` in `cache_params`

**Cache will only be on for the call types specified in`supported_call_types`**
    
    
    litellm_settings:  
      cache: True  
      cache_params:  
        type: redis  
        supported_call_types: ["acompletion", "atext_completion", "aembedding", "atranscription"]  
                              # /chat/completions, /completions, /embeddings, /audio/transcriptions  
    

### Set Cache Params on config.yaml​
    
    
    model_list:  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: gpt-3.5-turbo  
      - model_name: text-embedding-ada-002  
        litellm_params:  
          model: text-embedding-ada-002  
      
    litellm_settings:  
      set_verbose: True  
      cache: True          # set cache responses to True, litellm defaults to using a redis cache  
      cache_params:         # cache_params are optional  
        type: "redis"  # The type of cache to initialize. Can be "local" or "redis". Defaults to "local".  
        host: "localhost"  # The host address for the Redis cache. Required if type is "redis".  
        port: 6379  # The port number for the Redis cache. Required if type is "redis".  
        password: "your_password"  # The password for the Redis cache. Required if type is "redis".  
          
        # Optional configurations  
        supported_call_types: ["acompletion", "atext_completion", "aembedding", "atranscription"]  
                          # /chat/completions, /completions, /embeddings, /audio/transcriptions  
    

### Deleting Cache Keys - `/cache/delete`​

In order to delete a cache key, send a request to `/cache/delete` with the `keys` you want to delete

Example
    
    
    curl -X POST "http://0.0.0.0:4000/cache/delete" \  
      -H "Authorization: Bearer sk-1234" \  
      -d '{"keys": ["586bf3f3c1bf5aecb55bd9996494d3bbc69eb58397163add6d49537762a7548d", "key2"]}'  
    
    
    
    # {"status":"success"}  
    

#### Viewing Cache Keys from responses​

You can view the cache_key in the response headers, on cache hits the cache key is sent as the `x-litellm-cache-key` response headers
    
    
    curl -i --location 'http://0.0.0.0:4000/chat/completions' \  
        --header 'Authorization: Bearer sk-1234' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "gpt-3.5-turbo",  
        "user": "ishan",  
        "messages": [  
            {  
            "role": "user",  
            "content": "what is litellm"  
            }  
        ],  
    }'  
    

Response from litellm proxy
    
    
    date: Thu, 04 Apr 2024 17:37:21 GMT  
    content-type: application/json  
    x-litellm-cache-key: 586bf3f3c1bf5aecb55bd9996494d3bbc69eb58397163add6d49537762a7548d  
      
    {  
        "id": "chatcmpl-9ALJTzsBlXR9zTxPvzfFFtFbFtG6T",  
        "choices": [  
            {  
                "finish_reason": "stop",  
                "index": 0,  
                "message": {  
                    "content": "I'm sorr.."  
                    "role": "assistant"  
                }  
            }  
        ],  
        "created": 1712252235,  
    }  
                   
    

### **Set Caching Default Off - Opt in only **​

  1. **Set`mode: default_off` for caching**

    
    
    model_list:  
      - model_name: fake-openai-endpoint  
        litellm_params:  
          model: openai/fake  
          api_key: fake-key  
          api_base: https://exampleopenaiendpoint-production.up.railway.app/  
      
    # default off mode  
    litellm_settings:  
      set_verbose: True  
      cache: True  
      cache_params:  
        mode: default_off # 👈 Key change cache is default_off  
    

  2. **Opting in to cache when cache is default off**

  * OpenAI Python SDK
  * curl

    
    
    import os  
    from openai import OpenAI  
      
    client = OpenAI(api_key=<litellm-api-key>, base_url="http://0.0.0.0:4000")  
      
    chat_completion = client.chat.completions.create(  
        messages=[  
            {  
                "role": "user",  
                "content": "Say this is a test",  
            }  
        ],  
        model="gpt-3.5-turbo",  
        extra_body = {        # OpenAI python accepts extra args in extra_body  
            "cache": {"use-cache": True}  
        }  
    )  
    
    
    
    curl http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-1234" \  
      -d '{  
        "model": "gpt-3.5-turbo",  
        "cache": {"use-cache": True}  
        "messages": [  
          {"role": "user", "content": "Say this is a test"}  
        ]  
      }'  
    

## Supported `cache_params` on proxy config.yaml​
    
    
    cache_params:  
      # ttl   
      ttl: Optional[float]  
      default_in_memory_ttl: Optional[float]  
      default_in_redis_ttl: Optional[float]  
      
      # Type of cache (options: "local", "redis", "s3")  
      type: s3  
      
      # List of litellm call types to cache for  
      # Options: "completion", "acompletion", "embedding", "aembedding"  
      supported_call_types: ["acompletion", "atext_completion", "aembedding", "atranscription"]  
                          # /chat/completions, /completions, /embeddings, /audio/transcriptions  
      
      # Redis cache parameters  
      host: localhost  # Redis server hostname or IP address  
      port: "6379"  # Redis server port (as a string)  
      password: secret_password  # Redis server password  
      namespace: Optional[str] = None,  
        
      
      # S3 cache parameters  
      s3_bucket_name: your_s3_bucket_name  # Name of the S3 bucket  
      s3_region_name: us-west-2  # AWS region of the S3 bucket  
      s3_api_version: 2006-03-01  # AWS S3 API version  
      s3_use_ssl: true  # Use SSL for S3 connections (options: true, false)  
      s3_verify: true  # SSL certificate verification for S3 connections (options: true, false)  
      s3_endpoint_url: https://s3.amazonaws.com  # S3 endpoint URL  
      s3_aws_access_key_id: your_access_key  # AWS Access Key ID for S3  
      s3_aws_secret_access_key: your_secret_key  # AWS Secret Access Key for S3  
      s3_aws_session_token: your_session_token  # AWS Session Token for temporary credentials  
      
    

## Advanced - user api key cache ttl​

Configure how long the in-memory cache stores the key object (prevents db requests)
    
    
    general_settings:  
      user_api_key_cache_ttl: <your-number> #time in seconds  
    

By default this value is set to 60s.

  * Supported Caches
  * Quick Start
  * Usage
    * Basic
    * Dynamic Cache Controls
    * `ttl`
    * `s-maxage`
    * `no-cache`
    * `no-store`
    * `namespace`
  * Set cache for proxy, but not on the actual llm api call
  * Debugging Caching - `/cache/ping`
  * Advanced
    * Control Call Types Caching is on for - (`/chat/completion`, `/embeddings`, etc.)
    * Set Cache Params on config.yaml
    * Deleting Cache Keys - `/cache/delete`
    * **Set Caching Default Off - Opt in only **
  * Supported `cache_params` on proxy config.yaml
  * Advanced - user api key cache ttl