# 💰 Budgets, Rate Limits | liteLLM

On this page

Requirements:

  * Need to a postgres database (e.g. [Supabase](https://supabase.com/), [Neon](https://neon.tech/), etc) [**See Setup**](/docs/proxy/virtual_keys#setup)

## Set Budgets​

### Global Proxy​

Apply a budget across all calls on the proxy

**Step 1. Modify config.yaml**
    
    
    general_settings:  
      master_key: sk-1234  
      
    litellm_settings:  
      # other litellm settings  
      max_budget: 0 # (float) sets max budget as $0 USD  
      budget_duration: 30d # (str) frequency of reset - You can set duration as seconds ("30s"), minutes ("30m"), hours ("30h"), days ("30d").  
    

**Step 2. Start proxy**
    
    
    litellm /path/to/config.yaml  
    

**Step 3. Send test call**
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
        --header 'Autherization: Bearer sk-1234' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "gpt-3.5-turbo",  
        "messages": [  
            {  
            "role": "user",  
            "content": "what llm are you"  
            }  
        ],  
    }'  
    

### Team​

You can:

  * Add budgets to Teams

info

**Step-by step tutorial on setting, resetting budgets on Teams here (API or using Admin UI)**

👉 <https://docs.litellm.ai/docs/proxy/team_budgets>

#### **Add budgets to teams**​
    
    
    curl --location 'http://localhost:4000/team/new' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data-raw '{  
      "team_alias": "my-new-team_4",  
      "members_with_roles": [{"role": "admin", "user_id": "5c4a0aa3-a1e1-43dc-bd87-3c2da8382a3a"}],  
      "rpm_limit": 99  
    }'   
    

[**See Swagger**](https://litellm-api.up.railway.app/#/team%20management/new_team_team_new_post)

**Sample Response**
    
    
    {  
        "team_alias": "my-new-team_4",  
        "team_id": "13e83b19-f851-43fe-8e93-f96e21033100",  
        "admins": [],  
        "members": [],  
        "members_with_roles": [  
            {  
                "role": "admin",  
                "user_id": "5c4a0aa3-a1e1-43dc-bd87-3c2da8382a3a"  
            }  
        ],  
        "metadata": {},  
        "tpm_limit": null,  
        "rpm_limit": 99,  
        "max_budget": null,  
        "models": [],  
        "spend": 0.0,  
        "max_parallel_requests": null,  
        "budget_duration": null,  
        "budget_reset_at": null  
    }  
    

#### **Add budget duration to teams**​

`budget_duration`: Budget is reset at the end of specified duration. If not set, budget is never reset. You can set duration as seconds ("30s"), minutes ("30m"), hours ("30h"), days ("30d").
    
    
    curl 'http://0.0.0.0:4000/team/new' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data-raw '{  
      "team_alias": "my-new-team_4",  
      "members_with_roles": [{"role": "admin", "user_id": "5c4a0aa3-a1e1-43dc-bd87-3c2da8382a3a"}],  
      "budget_duration": 10s,  
    }'  
    

### Team Members​

Use this when you want to budget a users spend within a Team

#### Step 1. Create User​

Create a user with `user_id=ishaan`
    
    
    curl --location 'http://0.0.0.0:4000/user/new' \  
        --header 'Authorization: Bearer sk-1234' \  
        --header 'Content-Type: application/json' \  
        --data '{  
            "user_id": "ishaan"  
    }'  
    

#### Step 2. Add User to an existing Team - set `max_budget_in_team`​

Set `max_budget_in_team` when adding a User to a team. We use the same `user_id` we set in Step 1
    
    
    curl -X POST 'http://0.0.0.0:4000/team/member_add' \  
    -H 'Authorization: Bearer sk-1234' \  
    -H 'Content-Type: application/json' \  
    -d '{"team_id": "e8d1460f-846c-45d7-9b43-55f3cc52ac32", "max_budget_in_team": 0.000000000001, "member": {"role": "user", "user_id": "ishaan"}}'  
    

#### Step 3. Create a Key for Team member from Step 1​

Set `user_id=ishaan` from step 1
    
    
    curl --location 'http://0.0.0.0:4000/key/generate' \  
        --header 'Authorization: Bearer sk-1234' \  
        --header 'Content-Type: application/json' \  
        --data '{  
            "user_id": "ishaan",  
            "team_id": "e8d1460f-846c-45d7-9b43-55f3cc52ac32"  
    }'  
    

Response from `/key/generate`

We use the `key` from this response in Step 4
    
    
    {"key":"sk-RV-l2BJEZ_LYNChSx2EueQ", "models":[],"spend":0.0,"max_budget":null,"user_id":"ishaan","team_id":"e8d1460f-846c-45d7-9b43-55f3cc52ac32","max_parallel_requests":null,"metadata":{},"tpm_limit":null,"rpm_limit":null,"budget_duration":null,"allowed_cache_controls":[],"soft_budget":null,"key_alias":null,"duration":null,"aliases":{},"config":{},"permissions":{},"model_max_budget":{},"key_name":null,"expires":null,"token_id":null}%   
    

#### Step 4. Make /chat/completions requests for Team member​

Use the key from step 3 for this request. After 2-3 requests expect to see The following error `ExceededBudget: Crossed spend within team`
    
    
    curl --location 'http://localhost:4000/chat/completions' \  
        --header 'Authorization: Bearer sk-RV-l2BJEZ_LYNChSx2EueQ' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "llama3",  
        "messages": [  
            {  
            "role": "user",  
            "content": "tes4"  
            }  
        ]  
    }'  
    

### Internal User​

Apply a budget across all calls an internal user (key owner) can make on the proxy.

info

For keys, with a 'team_id' set, the team budget is used instead of the user's personal budget.

To apply a budget to a user within a team, use team member budgets.

LiteLLM exposes a `/user/new` endpoint to create budgets for this.

You can:

  * Add budgets to users **Jump**
  * Add budget durations, to reset spend **Jump**

By default the `max_budget` is set to `null` and is not checked for keys

#### **Add budgets to users**​
    
    
    curl --location 'http://localhost:4000/user/new' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data-raw '{"models": ["azure-models"], "max_budget": 0, "user_id": "krrish3@berri.ai"}'   
    

[**See Swagger**](https://litellm-api.up.railway.app/#/user%20management/new_user_user_new_post)

**Sample Response**
    
    
    {  
        "key": "sk-YF2OxDbrgd1y2KgwxmEA2w",  
        "expires": "2023-12-22T09:53:13.861000Z",  
        "user_id": "krrish3@berri.ai",  
        "max_budget": 0.0  
    }  
    

#### **Add budget duration to users**​

`budget_duration`: Budget is reset at the end of specified duration. If not set, budget is never reset. You can set duration as seconds ("30s"), minutes ("30m"), hours ("30h"), days ("30d").
    
    
    curl 'http://0.0.0.0:4000/user/new' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data-raw '{  
      "team_id": "core-infra", # [OPTIONAL]  
      "max_budget": 10,  
      "budget_duration": 10s,  
    }'  
    

#### Create new keys for existing user​

Now you can just call `/key/generate` with that user_id (i.e. [krrish3@berri.ai](mailto:krrish3@berri.ai)) and:

  * **Budget Check** : [krrish3@berri.ai](mailto:krrish3@berri.ai)'s budget (i.e. $10) will be checked for this key
  * **Spend Tracking** : spend for this key will update [krrish3@berri.ai](mailto:krrish3@berri.ai)'s spend as well

    
    
    curl --location 'http://0.0.0.0:4000/key/generate' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data '{"models": ["azure-models"], "user_id": "krrish3@berri.ai"}'  
    

### Virtual Key​

Apply a budget on a key.

You can:

  * Add budgets to keys **Jump**
  * Add budget durations, to reset spend **Jump**

**Expected Behaviour**

  * Costs Per key get auto-populated in `LiteLLM_VerificationToken` Table
  * After the key crosses it's `max_budget`, requests fail
  * If duration set, spend is reset at the end of the duration

By default the `max_budget` is set to `null` and is not checked for keys

#### **Add budgets to keys**​
    
    
    curl 'http://0.0.0.0:4000/key/generate' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data-raw '{  
      "team_id": "core-infra", # [OPTIONAL]  
      "max_budget": 10,  
    }'  
    

Example Request to `/chat/completions` when key has crossed budget
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
      --header 'Content-Type: application/json' \  
      --header 'Authorization: Bearer <generated-key>' \  
      --data ' {  
      "model": "azure-gpt-3.5",  
      "user": "e09b4da8-ed80-4b05-ac93-e16d9eb56fca",  
      "messages": [  
          {  
          "role": "user",  
          "content": "respond in 50 lines"  
          }  
      ],  
    }'  
    

Expected Response from `/chat/completions` when key has crossed budget
    
    
    {  
      "detail":"Authentication Error, ExceededTokenBudget: Current spend for token: 7.2e-05; Max Budget for Token: 2e-07"  
    }     
    

#### **Add budget duration to keys**​

`budget_duration`: Budget is reset at the end of specified duration. If not set, budget is never reset. You can set duration as seconds ("30s"), minutes ("30m"), hours ("30h"), days ("30d").
    
    
    curl 'http://0.0.0.0:4000/key/generate' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data-raw '{  
      "team_id": "core-infra", # [OPTIONAL]  
      "max_budget": 10,  
      "budget_duration": 10s,  
    }'  
    

### ✨ Virtual Key (Model Specific)​

Apply model specific budgets on a key. Example:

  * Budget for `gpt-4o` is $0.0000001, for time period `1d` for `key = "sk-12345"`
  * Budget for `gpt-4o-mini` is $10, for time period `30d` for `key = "sk-12345"`

info

✨ This is an Enterprise only feature [Get Started with Enterprise here](https://www.litellm.ai/#pricing)

The spec for `model_max_budget` is **`Dict[str, GenericBudgetInfo]`**
    
    
    curl 'http://0.0.0.0:4000/key/generate' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data-raw '{  
      "model_max_budget": {"gpt-4o": {"budget_limit": "0.0000001", "time_period": "1d"}}  
    }'  
    

#### Make a test request​

We expect the first request to succeed, and the second request to fail since we cross the budget for `gpt-4o` on the Virtual Key

**[Langchain, OpenAI SDK Usage Examples](/docs/proxy/user_keys#request-format)**

  * Successful Call 
  * Unsuccessful call

    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
    --header 'Content-Type: application/json' \  
    --header 'Authorization: Bearer <sk-generated-key>' \  
    --data ' {  
          "model": "gpt-4o",  
          "messages": [  
            {  
              "role": "user",  
              "content": "testing request"  
            }  
          ]  
        }  
    '  
    

Expect this to fail since since we cross the budget `model=gpt-4o` on the Virtual Key
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
    --header 'Content-Type: application/json' \  
    --header 'Authorization: Bearer <sk-generated-key>' \  
    --data ' {  
          "model": "gpt-4o",  
          "messages": [  
            {  
              "role": "user",  
              "content": "testing request"  
            }  
          ]  
        }  
    '  
    

Expected response on failure
    
    
    {  
        "error": {  
            "message": "LiteLLM Virtual Key: 9769f3f6768a199f76cc29xxxx, key_alias: None, exceeded budget for model=gpt-4o",  
            "type": "budget_exceeded",  
            "param": null,  
            "code": "400"  
        }  
    }  
    

### Customers​

Use this to budget `user` passed to `/chat/completions`, **without needing to create a key for every user**

**Step 1. Modify config.yaml** Define `litellm.max_end_user_budget`
    
    
    general_settings:  
      master_key: sk-1234  
      
    litellm_settings:  
      max_end_user_budget: 0.0001 # budget for 'user' passed to /chat/completions  
    

  2. Make a /chat/completions call, pass 'user' - First call Works

    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
            --header 'Content-Type: application/json' \  
            --header 'Authorization: Bearer sk-zi5onDRdHGD24v0Zdn7VBA' \  
            --data ' {  
            "model": "azure-gpt-3.5",  
            "user": "ishaan3",  
            "messages": [  
                {  
                "role": "user",  
                "content": "what time is it"  
                }  
            ]  
            }'  
    

  3. Make a /chat/completions call, pass 'user' - Call Fails, since 'ishaan3' over budget

    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
            --header 'Content-Type: application/json' \  
            --header 'Authorization: Bearer sk-zi5onDRdHGD24v0Zdn7VBA' \  
            --data ' {  
            "model": "azure-gpt-3.5",  
            "user": "ishaan3",  
            "messages": [  
                {  
                "role": "user",  
                "content": "what time is it"  
                }  
            ]  
            }'  
    

Error
    
    
    {"error":{"message":"Budget has been exceeded: User ishaan3 has exceeded their budget. Current spend: 0.0008869999999999999; Max Budget: 0.0001","type":"auth_error","param":"None","code":401}}%                  
    

## Reset Budgets​

Reset budgets across keys/internal users/teams/customers

`budget_duration`: Budget is reset at the end of specified duration. If not set, budget is never reset. You can set duration as seconds ("30s"), minutes ("30m"), hours ("30h"), days ("30d").

  * Internal Users
  * Keys
  * Teams

    
    
    curl 'http://0.0.0.0:4000/user/new' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data-raw '{  
      "max_budget": 10,  
      "budget_duration": 10s, # 👈 KEY CHANGE  
    }'  
    
    
    
    curl 'http://0.0.0.0:4000/key/generate' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data-raw '{  
      "max_budget": 10,  
      "budget_duration": 10s, # 👈 KEY CHANGE  
    }'  
    
    
    
    curl 'http://0.0.0.0:4000/team/new' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data-raw '{  
      "max_budget": 10,  
      "budget_duration": 10s, # 👈 KEY CHANGE  
    }'  
    

**Note:** By default, the server checks for resets every 10 minutes, to minimize DB calls.

To change this, set `proxy_budget_rescheduler_min_time` and `proxy_budget_rescheduler_max_time`

E.g.: Check every 1 seconds
    
    
    general_settings:   
      proxy_budget_rescheduler_min_time: 1  
      proxy_budget_rescheduler_max_time: 1  
    

## Set Rate Limits​

You can set:

  * tpm limits (tokens per minute)
  * rpm limits (requests per minute)
  * max parallel requests
  * rpm / tpm limits per model for a given key

  * Per Team
  * Per Internal User
  * Per Key
  * Per API Key Per model
  * For customers

Use `/team/new` or `/team/update`, to persist rate limits across multiple keys for a team.
    
    
    curl --location 'http://0.0.0.0:4000/team/new' \  
    --header 'Authorization: Bearer sk-1234' \  
    --header 'Content-Type: application/json' \  
    --data '{"team_id": "my-prod-team", "max_parallel_requests": 10, "tpm_limit": 20, "rpm_limit": 4}'   
    

[**See Swagger**](https://litellm-api.up.railway.app/#/team%20management/new_team_team_new_post)

**Expected Response**
    
    
    {  
        "key": "sk-sA7VDkyhlQ7m8Gt77Mbt3Q",  
        "expires": "2024-01-19T01:21:12.816168",  
        "team_id": "my-prod-team",  
    }  
    

Use `/user/new` or `/user/update`, to persist rate limits across multiple keys for internal users.
    
    
    curl --location 'http://0.0.0.0:4000/user/new' \  
    --header 'Authorization: Bearer sk-1234' \  
    --header 'Content-Type: application/json' \  
    --data '{"user_id": "krrish@berri.ai", "max_parallel_requests": 10, "tpm_limit": 20, "rpm_limit": 4}'   
    

[**See Swagger**](https://litellm-api.up.railway.app/#/user%20management/new_user_user_new_post)

**Expected Response**
    
    
    {  
        "key": "sk-sA7VDkyhlQ7m8Gt77Mbt3Q",  
        "expires": "2024-01-19T01:21:12.816168",  
        "user_id": "krrish@berri.ai",  
    }  
    

Use `/key/generate`, if you want them for just that key.
    
    
    curl --location 'http://0.0.0.0:4000/key/generate' \  
    --header 'Authorization: Bearer sk-1234' \  
    --header 'Content-Type: application/json' \  
    --data '{"max_parallel_requests": 10, "tpm_limit": 20, "rpm_limit": 4}'   
    

**Expected Response**
    
    
    {  
        "key": "sk-ulGNRXWtv7M0lFnnsQk0wQ",  
        "expires": "2024-01-18T20:48:44.297973",  
        "user_id": "78c2c8fc-c233-43b9-b0c3-eb931da27b84"  // 👈 auto-generated  
    }  
    

**Set rate limits per model per api key**

Set `model_rpm_limit` and `model_tpm_limit` to set rate limits per model per api key

Here `gpt-4` is the `model_name` set on the [litellm config.yaml](/docs/proxy/configs)
    
    
    curl --location 'http://0.0.0.0:4000/key/generate' \  
    --header 'Authorization: Bearer sk-1234' \  
    --header 'Content-Type: application/json' \  
    --data '{"model_rpm_limit": {"gpt-4": 2}, "model_tpm_limit": {"gpt-4":}}'   
    

**Expected Response**
    
    
    {  
        "key": "sk-ulGNRXWtv7M0lFnnsQk0wQ",  
        "expires": "2024-01-18T20:48:44.297973",  
    }  
    

**Verify Model Rate Limits set correctly for this key**

**Make /chat/completions request check if`x-litellm-key-remaining-requests-gpt-4` returned**
    
    
    curl -i http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-ulGNRXWtv7M0lFnnsQk0wQ" \  
      -d '{  
        "model": "gpt-4",  
        "messages": [  
          {"role": "user", "content": "Hello, Claude!ss eho ares"}  
        ]  
      }'  
    

**Expected headers**
    
    
     x-litellm-key-remaining-requests-gpt-4: 1  
    x-litellm-key-remaining-tokens-gpt-4: 179  
    

These headers indicate:

  * 1 request remaining for the GPT-4 model for key=`sk-ulGNRXWtv7M0lFnnsQk0wQ`
  * 179 tokens remaining for the GPT-4 model for key=`sk-ulGNRXWtv7M0lFnnsQk0wQ`

info

You can also create a budget id for a customer on the UI, under the 'Rate Limits' tab.

Use this to set rate limits for `user` passed to `/chat/completions`, without needing to create a key for every user

#### Step 1. Create Budget​

Set a `tpm_limit` on the budget (You can also pass `rpm_limit` if needed)
    
    
    curl --location 'http://0.0.0.0:4000/budget/new' \  
    --header 'Authorization: Bearer sk-1234' \  
    --header 'Content-Type: application/json' \  
    --data '{  
        "budget_id" : "free-tier",  
        "tpm_limit": 5  
    }'  
    

#### Step 2. Create `Customer` with Budget​

We use `budget_id="free-tier"` from Step 1 when creating this new customers
    
    
    curl --location 'http://0.0.0.0:4000/customer/new' \  
    --header 'Authorization: Bearer sk-1234' \  
    --header 'Content-Type: application/json' \  
    --data '{  
        "user_id" : "palantir",  
        "budget_id": "free-tier"  
    }'  
    

#### Step 3. Pass `user_id` id in `/chat/completions` requests​

Pass the `user_id` from Step 2 as `user="palantir"`
    
    
    curl --location 'http://localhost:4000/chat/completions' \  
        --header 'Authorization: Bearer sk-1234' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "llama3",  
        "user": "palantir",  
        "messages": [  
            {  
            "role": "user",  
            "content": "gm"  
            }  
        ]  
    }'  
    

## Set default budget for ALL internal users​

Use this to set a default budget for users who you give keys to.

This will apply when a user has [`user_role="internal_user"`](/docs/proxy/self_serve#available-roles) (set this via `/user/new` or `/user/update`).

This will NOT apply if a key has a team_id (team budgets will apply then). [Tell us how we can improve this!](https://github.com/BerriAI/litellm/issues)

  1. Define max budget in your config.yaml

    
    
    model_list:   
      - model_name: "gpt-3.5-turbo"  
        litellm_params:  
          model: gpt-3.5-turbo  
          api_key: os.environ/OPENAI_API_KEY  
      
    litellm_settings:  
      max_internal_user_budget: 0 # amount in USD  
      internal_user_budget_duration: "1mo" # reset every month  
    

  2. Create key for user

    
    
    curl -L -X POST 'http://0.0.0.0:4000/key/generate' \  
    -H 'Authorization: Bearer sk-1234' \  
    -H 'Content-Type: application/json' \  
    -d '{}'  
    

Expected Response:
    
    
    {  
      ...  
      "key": "sk-X53RdxnDhzamRwjKXR4IHg"  
    }  
    

  3. Test it!

    
    
    curl -L -X POST 'http://0.0.0.0:4000/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-X53RdxnDhzamRwjKXR4IHg' \  
    -d '{  
        "model": "gpt-3.5-turbo",  
        "messages": [{"role": "user", "content": "Hey, how's it going?"}]  
    }'  
    

Expected Response:
    
    
    {  
        "error": {  
            "message": "ExceededBudget: User=<user_id> over budget. Spend=3.7e-05, Budget=0.0",  
            "type": "budget_exceeded",  
            "param": null,  
            "code": "400"  
        }  
    }  
    

### [BETA] Multi-instance rate limiting​

Enable multi-instance rate limiting with the env var `EXPERIMENTAL_MULTI_INSTANCE_RATE_LIMITING="True"`

Changes:

  * This moves to using async_increment instead of async_set_cache when updating current requests/tokens.
  * The in-memory cache is synced with redis every 0.01s, to avoid calling redis for every request.
  * In testing, this was found to be 2x faster than the previous implementation, and reduced drift between expected and actual fails to at most 10 requests at high-traffic (100 RPS across 3 instances).

## Grant Access to new model​

Use model access groups to give users access to select models, and add new ones to it over time (e.g. mistral, llama-2, etc.).

Difference between doing this with `/key/generate` vs. `/user/new`? If you do it on `/user/new` it'll persist across multiple keys generated for that user.

**Step 1. Assign model, access group in config.yaml**
    
    
    model_list:  
      - model_name: text-embedding-ada-002  
        litellm_params:  
          model: azure/azure-embedding-model  
          api_base: "os.environ/AZURE_API_BASE"  
          api_key: "os.environ/AZURE_API_KEY"  
          api_version: "2023-07-01-preview"  
        model_info:  
          access_groups: ["beta-models"] # 👈 Model Access Group  
    

**Step 2. Create key with access group**
    
    
    curl --location 'http://localhost:4000/user/new' \  
    -H 'Authorization: Bearer <your-master-key>' \  
    -H 'Content-Type: application/json' \  
    -d '{"models": ["beta-models"], # 👈 Model Access Group  
    			"max_budget": 0}'  
    

## Create new keys for existing internal user​

Just include user_id in the `/key/generate` request.
    
    
    curl --location 'http://0.0.0.0:4000/key/generate' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data '{"models": ["azure-models"], "user_id": "krrish@berri.ai"}'  
    

## API Specification​

### `GenericBudgetInfo`​

A Pydantic model that defines budget information with a time period and limit.
    
    
    class GenericBudgetInfo(BaseModel):  
        budget_limit: float  # The maximum budget amount in USD  
        time_period: str    # Duration string like "1d", "30d", etc.  
    

#### Fields:​

  * `budget_limit` (float): The maximum budget amount in USD
  * `time_period` (str): Duration string specifying the time period for the budget. Supported formats:
    * Seconds: "30s"
    * Minutes: "30m"
    * Hours: "30h"
    * Days: "30d"

#### Example:​
    
    
    {  
      "budget_limit": "0.0001",  
      "time_period": "1d"  
    }  
    

  * Set Budgets
    * Global Proxy
    * Team
    * Team Members
    * Internal User
    * Virtual Key
    * ✨ Virtual Key (Model Specific)
    * Customers
  * Reset Budgets
  * Set Rate Limits
  * Set default budget for ALL internal users
    * [BETA] Multi-instance rate limiting
  * Grant Access to new model
  * Create new keys for existing internal user
  * API Specification
    * `GenericBudgetInfo`