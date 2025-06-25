# Proxy - Load Balancing | liteLLM

On this page

Load balance multiple instances of the same model

The proxy will handle routing requests (using LiteLLM's Router). **Set`rpm` in the config if you want maximize throughput**

info

For more details on routing strategies / params, see [Routing](/docs/routing)

## Quick Start - Load Balancing​

#### Step 1 - Set deployments on config​

**Example config below**. Here requests with `model=gpt-3.5-turbo` will be routed across multiple instances of `azure/gpt-3.5-turbo`
    
    
    model_list:  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: azure/<your-deployment-name>  
          api_base: <your-azure-endpoint>  
          api_key: <your-azure-api-key>  
          rpm: 6      # Rate limit for this deployment: in requests per minute (rpm)  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: azure/gpt-turbo-small-ca  
          api_base: https://my-endpoint-canada-berri992.openai.azure.com/  
          api_key: <your-azure-api-key>  
          rpm: 6  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: azure/gpt-turbo-large  
          api_base: https://openai-france-1234.openai.azure.com/  
          api_key: <your-azure-api-key>  
          rpm: 1440  
      
    router_settings:  
      routing_strategy: simple-shuffle # Literal["simple-shuffle", "least-busy", "usage-based-routing","latency-based-routing"], default="simple-shuffle"  
      model_group_alias: {"gpt-4": "gpt-3.5-turbo"} # all requests with `gpt-4` will be routed to models with `gpt-3.5-turbo`  
      num_retries: 2  
      timeout: 30                                  # 30 seconds  
      redis_host: <your redis host>                # set this when using multiple litellm proxy deployments, load balancing state stored in redis  
      redis_password: <your redis password>  
      redis_port: 1992  
    

info

Detailed information about [routing strategies can be found here](/docs/routing)

#### Step 2: Start Proxy with config​
    
    
    $ litellm --config /path/to/config.yaml  
    

### Test - Simple Call​

Here requests with model=gpt-3.5-turbo will be routed across multiple instances of azure/gpt-3.5-turbo

👉 Key Change: `model="gpt-3.5-turbo"`

**Check the`model_id` in Response Headers to make sure the requests are being load balanced**

  * OpenAI Python v1.0.0+
  * Curl Request
  * Langchain

    
    
    import openai  
    client = openai.OpenAI(  
        api_key="anything",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    response = client.chat.completions.create(  
        model="gpt-3.5-turbo",  
        messages = [  
            {  
                "role": "user",  
                "content": "this is a test request, write a short poem"  
            }  
        ]  
    )  
      
    print(response)  
    
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "gpt-3.5-turbo",  
        "messages": [  
            {  
            "role": "user",  
            "content": "what llm are you"  
            }  
        ]  
    }'  
    
    
    
    from langchain.chat_models import ChatOpenAI  
    from langchain.prompts.chat import (  
        ChatPromptTemplate,  
        HumanMessagePromptTemplate,  
        SystemMessagePromptTemplate,  
    )  
    from langchain.schema import HumanMessage, SystemMessage  
    import os   
      
    os.environ["OPENAI_API_KEY"] = "anything"  
      
    chat = ChatOpenAI(  
        openai_api_base="http://0.0.0.0:4000",  
        model="gpt-3.5-turbo",  
    )  
      
    messages = [  
        SystemMessage(  
            content="You are a helpful assistant that im using to make a test request to."  
        ),  
        HumanMessage(  
            content="test from litellm. tell me why it's amazing in 1 sentence"  
        ),  
    ]  
    response = chat(messages)  
      
    print(response)  
    

### Test - Loadbalancing​

In this request, the following will occur:

  1. A rate limit exception will be raised
  2. LiteLLM proxy will retry the request on the model group (default is 3).

    
    
    curl -X POST 'http://0.0.0.0:4000/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
      "model": "gpt-3.5-turbo",  
      "messages": [  
            {"role": "user", "content": "Hi there!"}  
        ],  
        "mock_testing_rate_limit_error": true  
    }'  
    

[**See Code**](https://github.com/BerriAI/litellm/blob/6b8806b45f970cb2446654d2c379f8dcaa93ce3c/litellm/router.py#L2535)

## Load Balancing using multiple litellm instances (Kubernetes, Auto Scaling)​

LiteLLM Proxy supports sharing rpm/tpm shared across multiple litellm instances, pass `redis_host`, `redis_password` and `redis_port` to enable this. (LiteLLM will use Redis to track rpm/tpm usage )

Example config
    
    
    model_list:  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: azure/<your-deployment-name>  
          api_base: <your-azure-endpoint>  
          api_key: <your-azure-api-key>  
          rpm: 6      # Rate limit for this deployment: in requests per minute (rpm)  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: azure/gpt-turbo-small-ca  
          api_base: https://my-endpoint-canada-berri992.openai.azure.com/  
          api_key: <your-azure-api-key>  
          rpm: 6  
    router_settings:  
      redis_host: <your redis host>  
      redis_password: <your redis password>  
      redis_port: 1992  
    

## Router settings on config - routing_strategy, model_group_alias​

Expose an 'alias' for a 'model_name' on the proxy server.
    
    
    model_group_alias: {  
      "gpt-4": "gpt-3.5-turbo"  
    }  
    

These aliases are shown on `/v1/models`, `/v1/model/info`, and `/v1/model_group/info` by default.

litellm.Router() settings can be set under `router_settings`. You can set `model_group_alias`, `routing_strategy`, `num_retries`,`timeout` . See all Router supported params [here](https://github.com/BerriAI/litellm/blob/1b942568897a48f014fa44618ec3ce54d7570a46/litellm/router.py#L64)

### Usage​

Example config with `router_settings`
    
    
    model_list:  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: azure/<your-deployment-name>  
          api_base: <your-azure-endpoint>  
          api_key: <your-azure-api-key>  
      
    router_settings:  
      model_group_alias: {"gpt-4": "gpt-3.5-turbo"} # all requests with `gpt-4` will be routed to models   
    

### Hide Alias Models​

Use this if you want to set-up aliases for:

  1. typos
  2. minor model version changes
  3. case sensitive changes between updates

    
    
    model_list:  
      - model_name: gpt-3.5-turbo  
        litellm_params:  
          model: azure/<your-deployment-name>  
          api_base: <your-azure-endpoint>  
          api_key: <your-azure-api-key>  
      
    router_settings:  
      model_group_alias:  
        "GPT-3.5-turbo": # alias  
          model: "gpt-3.5-turbo"  # Actual model name in 'model_list'  
          hidden: true             # Exclude from `/v1/models`, `/v1/model/info`, `/v1/model_group/info`  
    

### Complete Spec​
    
    
    model_group_alias: Optional[Dict[str, Union[str, RouterModelGroupAliasItem]]] = {}  
      
      
    class RouterModelGroupAliasItem(TypedDict):  
        model: str  
        hidden: bool  # if 'True', don't return on `/v1/models`, `/v1/model/info`, `/v1/model_group/info`  
    

  * Quick Start - Load Balancing
    * Test - Simple Call
    * Test - Loadbalancing
  * Load Balancing using multiple litellm instances (Kubernetes, Auto Scaling)
  * Router settings on config - routing_strategy, model_group_alias
    * Usage
    * Hide Alias Models
    * Complete Spec