# Control Model Access | liteLLM

On this page

## **Restrict models by Virtual Key**​

Set allowed models for a key using the `models` param
    
    
    curl 'http://0.0.0.0:4000/key/generate' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data-raw '{"models": ["gpt-3.5-turbo", "gpt-4"]}'  
    

info

This key can only make requests to `models` that are `gpt-3.5-turbo` or `gpt-4`

Verify this is set correctly by

  * Allowed Access
  * Disallowed Access

    
    
    curl -i http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-1234" \  
      -d '{  
        "model": "gpt-4",  
        "messages": [  
          {"role": "user", "content": "Hello"}  
        ]  
      }'  
    

info

Expect this to fail since gpt-4o is not in the `models` for the key generated
    
    
    curl -i http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-1234" \  
      -d '{  
        "model": "gpt-4o",  
        "messages": [  
          {"role": "user", "content": "Hello"}  
        ]  
      }'  
    

### [API Reference](https://litellm-api.up.railway.app/#/key%20management/generate_key_fn_key_generate_post)​

## **Restrict models by`team_id`**​

`litellm-dev` can only access `azure-gpt-3.5`

**1\. Create a team via`/team/new`**
    
    
    curl --location 'http://localhost:4000/team/new' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data-raw '{  
      "team_alias": "litellm-dev",  
      "models": ["azure-gpt-3.5"]  
    }'   
      
    # returns {...,"team_id": "my-unique-id"}  
    

**2\. Create a key for team**
    
    
    curl --location 'http://localhost:4000/key/generate' \  
    --header 'Authorization: Bearer sk-1234' \  
    --header 'Content-Type: application/json' \  
    --data-raw '{"team_id": "my-unique-id"}'  
    

**3\. Test it**
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
        --header 'Content-Type: application/json' \  
        --header 'Authorization: Bearer sk-qo992IjKOC2CHKZGRoJIGA' \  
        --data '{  
            "model": "BEDROCK_GROUP",  
            "messages": [  
                {  
                    "role": "user",  
                    "content": "hi"  
                }  
            ]  
        }'  
    
    
    
    {"error":{"message":"Invalid model for team litellm-dev: BEDROCK_GROUP.  Valid models for team are: ['azure-gpt-3.5']\n\n\nTraceback (most recent call last):\n  File \"/Users/ishaanjaffer/Github/litellm/litellm/proxy/proxy_server.py\", line 2298, in chat_completion\n    _is_valid_team_configs(\n  File \"/Users/ishaanjaffer/Github/litellm/litellm/proxy/utils.py\", line 1296, in _is_valid_team_configs\n    raise Exception(\nException: Invalid model for team litellm-dev: BEDROCK_GROUP.  Valid models for team are: ['azure-gpt-3.5']\n\n","type":"None","param":"None","code":500}}%              
    

### [API Reference](https://litellm-api.up.railway.app/#/team%20management/new_team_team_new_post)​

## **Model Access Groups**​

Use model access groups to give users access to select models, and add new ones to it over time (e.g. mistral, llama-2, etc.)

**Step 1. Assign model, access group in config.yaml**
    
    
    model_list:  
      - model_name: gpt-4  
        litellm_params:  
          model: openai/fake  
          api_key: fake-key  
          api_base: https://exampleopenaiendpoint-production.up.railway.app/  
        model_info:  
          access_groups: ["beta-models"] # 👈 Model Access Group  
      - model_name: fireworks-llama-v3-70b-instruct  
        litellm_params:  
          model: fireworks_ai/accounts/fireworks/models/llama-v3-70b-instruct  
          api_key: "os.environ/FIREWORKS"  
        model_info:  
          access_groups: ["beta-models"] # 👈 Model Access Group  
    

  * Key Access Groups
  * Team Access Groups

**Create key with access group**
    
    
     curl --location 'http://localhost:4000/key/generate' \  
    -H 'Authorization: Bearer <your-master-key>' \  
    -H 'Content-Type: application/json' \  
    -d '{"models": ["beta-models"], # 👈 Model Access Group  
    			"max_budget": 0,}'  
    

Test Key

  * Allowed Access
  * Disallowed Access

    
    
    curl -i http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-<key-from-previous-step>" \  
      -d '{  
        "model": "gpt-4",  
        "messages": [  
          {"role": "user", "content": "Hello"}  
        ]  
      }'  
    

info

Expect this to fail since gpt-4o is not in the `beta-models` access group
    
    
    curl -i http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-<key-from-previous-step>" \  
      -d '{  
        "model": "gpt-4o",  
        "messages": [  
          {"role": "user", "content": "Hello"}  
        ]  
      }'  
    

Create Team
    
    
    curl --location 'http://localhost:4000/team/new' \  
    -H 'Authorization: Bearer sk-<key-from-previous-step>' \  
    -H 'Content-Type: application/json' \  
    -d '{"models": ["beta-models"]}'  
    

Create Key for Team
    
    
    curl --location 'http://0.0.0.0:4000/key/generate' \  
    --header 'Authorization: Bearer sk-<key-from-previous-step>' \  
    --header 'Content-Type: application/json' \  
    --data '{"team_id": "0ac97648-c194-4c90-8cd6-40af7b0d2d2a"}  
    

Test Key

  * Allowed Access
  * Disallowed Access

    
    
    curl -i http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-<key-from-previous-step>" \  
      -d '{  
        "model": "gpt-4",  
        "messages": [  
          {"role": "user", "content": "Hello"}  
        ]  
      }'  
    

info

Expect this to fail since gpt-4o is not in the `beta-models` access group
    
    
    curl -i http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-<key-from-previous-step>" \  
      -d '{  
        "model": "gpt-4o",  
        "messages": [  
          {"role": "user", "content": "Hello"}  
        ]  
      }'  
    

### ✨ Control Access on Wildcard Models​

Control access to all models with a specific prefix (e.g. `openai/*`).

Use this to also give users access to all models, except for a few that you don't want them to use (e.g. `openai/o1-*`).

info

Setting model access groups on wildcard models is an Enterprise feature.

See pricing [here](https://litellm.ai/#pricing)

Get a trial key [here](https://litellm.ai/#trial)

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: openai/*  
        litellm_params:  
          model: openai/*  
          api_key: os.environ/OPENAI_API_KEY  
        model_info:  
          access_groups: ["default-models"]  
      - model_name: openai/o1-*  
        litellm_params:  
          model: openai/o1-*  
          api_key: os.environ/OPENAI_API_KEY  
        model_info:  
          access_groups: ["restricted-models"]  
    

  2. Generate a key with access to `default-models`

    
    
    curl -L -X POST 'http://0.0.0.0:4000/key/generate' \  
    -H 'Authorization: Bearer sk-1234' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "models": ["default-models"],  
    }'  
    

  3. Test the key

  * Successful Request
  * Rejected Request

    
    
    curl -i http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-<key-from-previous-step>" \  
      -d '{  
        "model": "openai/gpt-4",  
        "messages": [  
          {"role": "user", "content": "Hello"}  
        ]  
      }'  
    
    
    
    curl -i http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-<key-from-previous-step>" \  
      -d '{  
        "model": "openai/o1-mini",  
        "messages": [  
          {"role": "user", "content": "Hello"}  
        ]  
      }'  
    

## [Role Based Access Control (RBAC)](/docs/proxy/jwt_auth_arch)​

  * **Restrict models by Virtual Key**
    * API Reference
  * **Restrict models by`team_id`**
    * API Reference
  * **Model Access Groups**
    * ✨ Control Access on Wildcard Models
  * Role Based Access Control (RBAC)