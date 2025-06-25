# ✨ Enterprise Features | liteLLM

On this page

tip

To get a license, get in touch with us [here](https://calendly.com/d/4mp-gd3-k5k/litellm-1-1-onboarding-chat)

Features:

  * **Security**
    * ✅ [SSO for Admin UI](/docs/proxy/ui#%E2%9C%A8-enterprise-features)
    * ✅ Audit Logs with retention policy
    * ✅ [JWT-Auth](/docs/proxy/token_auth)
    * ✅ Control available public, private routes (Restrict certain endpoints on proxy)
    * ✅ Control available public, private routes
    * ✅ [Secret Managers - AWS Key Manager, Google Secret Manager, Azure Key, Hashicorp Vault](/docs/secret)
    * ✅ [BETA] AWS Key Manager v2 - Key Decryption
    * ✅ IP address‑based access control lists
    * ✅ Track Request IP Address
    * ✅ [Use LiteLLM keys/authentication on Pass Through Endpoints](/docs/proxy/pass_through#%E2%9C%A8-enterprise---use-litellm-keysauthentication-on-pass-through-endpoints)
    * ✅ Set Max Request Size / File Size on Requests
    * ✅ Enforce Required Params for LLM Requests (ex. Reject requests missing ["metadata"]["generation_name"])
    * ✅ [Key Rotations](/docs/proxy/virtual_keys#-key-rotations)
  * **Customize Logging, Guardrails, Caching per project**
    * ✅ [Team Based Logging](/docs/proxy/team_logging) \- Allow each team to use their own Langfuse Project / custom callbacks
    * ✅ [Disable Logging for a Team](/docs/proxy/team_logging#disable-logging-for-a-team) \- Switch off all logging for a team/project (GDPR Compliance)
  * **Spend Tracking & Data Exports**
    * ✅ Tracking Spend for Custom Tags
    * ✅ [Set USD Budgets Spend for Custom Tags](/docs/proxy/provider_budget_routing#-tag-budgets)
    * ✅ [Set Model budgets for Virtual Keys](/docs/proxy/users#-virtual-key-model-specific)
    * ✅ [Exporting LLM Logs to GCS Bucket, Azure Blob Storage](/docs/proxy/proxy/bucket#%F0%9F%AA%A3-logging-gcs-s3-buckets)
    * ✅ [`/spend/report` API endpoint](/docs/proxy/cost_tracking#%E2%9C%A8-enterprise-api-endpoints-to-get-spend)
  * **Prometheus Metrics**
    * ✅ [Prometheus Metrics - Num Requests, failures, LLM Provider Outages](/docs/proxy/prometheus)
    * ✅ [`x-ratelimit-remaining-requests`, `x-ratelimit-remaining-tokens` for LLM APIs on Prometheus](/docs/proxy/prometheus#%E2%9C%A8-enterprise-llm-remaining-requests-and-remaining-tokens)
  * **Control Guardrails per API Key**
  * **Custom Branding**
    * ✅ Custom Branding + Routes on Swagger Docs
    * ✅ Public Model Hub
    * ✅ [Custom Email Branding](/docs/proxy/email#customizing-email-branding)

### Blocking web crawlers​

To block web crawlers from indexing the proxy server endpoints, set the `block_robots` setting to `true` in your `litellm_config.yaml` file.

litellm_config.yaml
    
    
    general_settings:  
      block_robots: true  
    

#### How it works​

When this is enabled, the `/robots.txt` endpoint will return a 200 status code with the following content:

robots.txt
    
    
    User-agent: *  
    Disallow: /  
    

### Required Params for LLM Requests​

Use this when you want to enforce all requests to include certain params. Example you need all requests to include the `user` and `["metadata]["generation_name"]` params.

  * Set on Config
  * Set on Key

**Step 1** Define all Params you want to enforce on config.yaml

This means `["user"]` and `["metadata]["generation_name"]` are required in all LLM Requests to LiteLLM
    
    
    general_settings:  
      master_key: sk-1234  
      enforced_params:    
        - user  
        - metadata.generation_name  
    
    
    
    curl -L -X POST 'http://0.0.0.0:4000/key/generate' \  
    -H 'Authorization: Bearer sk-1234' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "enforced_params": ["user", "metadata.generation_name"]  
    }'  
    

**Step 2 Verify if this works**

  * Invalid Request (No `user` passed)
  * Invalid Request (No `metadata` passed)
  * Valid Request

    
    
    curl --location 'http://localhost:4000/chat/completions' \  
        --header 'Authorization: Bearer sk-5fmYeaUEbAMpwBNT-QpxyA' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "gpt-3.5-turbo",  
        "messages": [  
            {  
            "role": "user",  
            "content": "hi"  
            }  
        ]  
    }'  
    

Expected Response
    
    
    {"error":{"message":"Authentication Error, BadRequest please pass param=user in request body. This is a required param","type":"auth_error","param":"None","code":401}}%   
    
    
    
    curl --location 'http://localhost:4000/chat/completions' \  
        --header 'Authorization: Bearer sk-5fmYeaUEbAMpwBNT-QpxyA' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "gpt-3.5-turbo",  
        "user": "gm",  
        "messages": [  
            {  
            "role": "user",  
            "content": "hi"  
            }  
        ],  
       "metadata": {}  
    }'  
    

Expected Response
    
    
    {"error":{"message":"Authentication Error, BadRequest please pass param=[metadata][generation_name] in request body. This is a required param","type":"auth_error","param":"None","code":401}}%   
    
    
    
    curl --location 'http://localhost:4000/chat/completions' \  
        --header 'Authorization: Bearer sk-5fmYeaUEbAMpwBNT-QpxyA' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "gpt-3.5-turbo",  
        "user": "gm",  
        "messages": [  
            {  
            "role": "user",  
            "content": "hi"  
            }  
        ],  
       "metadata": {"generation_name": "prod-app"}  
    }'  
    

Expected Response
    
    
    {"id":"chatcmpl-9XALnHqkCBMBKrOx7Abg0hURHqYtY","choices":[{"finish_reason":"stop","index":0,"message":{"content":"Hello! How can I assist you today?","role":"assistant"}}],"created":1717691639,"model":"gpt-3.5-turbo-0125","object":"chat.completion","system_fingerprint":null,"usage":{"completion_tokens":9,"prompt_tokens":8,"total_tokens":17}}%    
    

### Control available public, private routes​

**Restrict certain endpoints of proxy**

info

❓ Use this when you want to:

  * make an existing private route -> public
  * set certain routes as admin_only routes

#### Usage - Define public, admin only routes​

**Step 1** \- Set on config.yaml

Route Type| Optional| Requires Virtual Key Auth| Admin Can Access| All Roles Can Access| Description  
---|---|---|---|---|---  
`public_routes`| ✅| ❌| ✅| ✅| Routes that can be accessed without any authentication  
`admin_only_routes`| ✅| ✅| ✅| ❌| Routes that can only be accessed by [Proxy Admin](/docs/proxy/self_serve#available-roles)  
`allowed_routes`| ✅| ✅| ✅| ✅| Routes are exposed on the proxy. If not set then all routes exposed.  
  
`LiteLLMRoutes.public_routes` is an ENUM corresponding to the default public routes on LiteLLM. [You can see this here](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/_types.py)
    
    
    general_settings:  
      master_key: sk-1234  
      public_routes: ["LiteLLMRoutes.public_routes", "/spend/calculate"]     # routes that can be accessed without any auth  
      admin_only_routes: ["/key/generate"]  # Optional - routes that can only be accessed by Proxy Admin  
      allowed_routes: ["/chat/completions", "/spend/calculate", "LiteLLMRoutes.public_routes"] # Optional - routes that can be accessed by anyone after Authentication  
    

**Step 2** \- start proxy
    
    
    litellm --config config.yaml  
    

**Step 3** \- Test it

  * Test `public_routes`
  * Test `admin_only_routes`
  * Test `allowed_routes`

    
    
    curl --request POST \  
      --url 'http://localhost:4000/spend/calculate' \  
      --header 'Content-Type: application/json' \  
      --data '{  
        "model": "gpt-4",  
        "messages": [{"role": "user", "content": "Hey, how'\''s it going?"}]  
      }'  
    

🎉 Expect this endpoint to work without an `Authorization / Bearer Token`

**Successful Request**
    
    
     curl --location 'http://0.0.0.0:4000/key/generate' \  
    --header 'Authorization: Bearer <your-master-key>' \  
    --header 'Content-Type: application/json' \  
    --data '{}'  
    

**Un-successfull Request**
    
    
     curl --location 'http://0.0.0.0:4000/key/generate' \  
    --header 'Authorization: Bearer <virtual-key-from-non-admin>' \  
    --header 'Content-Type: application/json' \  
    --data '{"user_role": "internal_user"}'  
    

**Expected Response**
    
    
    {  
      "error": {  
        "message": "user not allowed to access this route. Route=/key/generate is an admin only route",  
        "type": "auth_error",  
        "param": "None",  
        "code": "403"  
      }  
    }  
    

**Successful Request**
    
    
     curl http://localhost:4000/chat/completions \  
    -H "Content-Type: application/json" \  
    -H "Authorization: Bearer sk-1234" \  
    -d '{  
    "model": "fake-openai-endpoint",  
    "messages": [  
        {"role": "user", "content": "Hello, Claude"}  
    ]  
    }'  
    

**Un-successfull Request**
    
    
     curl --location 'http://0.0.0.0:4000/embeddings' \  
    --header 'Content-Type: application/json' \  
    -H "Authorization: Bearer sk-1234" \  
    --data ' {  
    "model": "text-embedding-ada-002",  
    "input": ["write a litellm poem"]  
    }'  
    

**Expected Response**
    
    
    {  
      "error": {  
        "message": "Route /embeddings not allowed",  
        "type": "auth_error",  
        "param": "None",  
        "code": "403"  
      }  
    }  
    

## Spend Tracking​

### Custom Tags​

Requirements:

  * Virtual Keys & a database should be set up, see [virtual keys](https://docs.litellm.ai/docs/proxy/virtual_keys)

#### Usage - /chat/completions requests with request tags​

  * Set on Key
  * Set on Team
  * OpenAI Python v1.0.0+
  * OpenAI JS
  * Curl Request
  * Langchain

    
    
    curl -L -X POST 'http://0.0.0.0:4000/key/generate' \  
    -H 'Authorization: Bearer sk-1234' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "metadata": {  
            "tags": ["tag1", "tag2", "tag3"]  
        }  
    }  
      
    '  
    
    
    
    curl -L -X POST 'http://0.0.0.0:4000/team/new' \  
    -H 'Authorization: Bearer sk-1234' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "metadata": {  
            "tags": ["tag1", "tag2", "tag3"]  
        }  
    }  
      
    '  
    

Set `extra_body={"metadata": { }}` to `metadata` you want to pass
    
    
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
        ],  
        extra_body={  
            "metadata": {  
                "tags": ["model-anthropic-claude-v2.1", "app-ishaan-prod"] # 👈 Key Change  
            }  
        }  
    )  
      
    print(response)  
    
    
    
    const openai = require('openai');  
      
    async function runOpenAI() {  
      const client = new openai.OpenAI({  
        apiKey: 'sk-1234',  
        baseURL: 'http://0.0.0.0:4000'  
      });  
      
      try {  
        const response = await client.chat.completions.create({  
          model: 'gpt-3.5-turbo',  
          messages: [  
            {  
              role: 'user',  
              content: "this is a test request, write a short poem"  
            },  
          ],  
          metadata: {  
            tags: ["model-anthropic-claude-v2.1", "app-ishaan-prod"] // 👈 Key Change  
          }  
        });  
        console.log(response);  
      } catch (error) {  
        console.log("got this exception from server");  
        console.error(error);  
      }  
    }  
      
    // Call the asynchronous function  
    runOpenAI();  
    

Pass `metadata` as part of the request body
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "gpt-3.5-turbo",  
        "messages": [  
            {  
            "role": "user",  
            "content": "what llm are you"  
            }  
        ],  
        "metadata": {"tags": ["model-anthropic-claude-v2.1", "app-ishaan-prod"]}  
    }'  
    
    
    
    from langchain.chat_models import ChatOpenAI  
    from langchain.prompts.chat import (  
        ChatPromptTemplate,  
        HumanMessagePromptTemplate,  
        SystemMessagePromptTemplate,  
    )  
    from langchain.schema import HumanMessage, SystemMessage  
      
    chat = ChatOpenAI(  
        openai_api_base="http://0.0.0.0:4000",  
        model = "gpt-3.5-turbo",  
        temperature=0.1,  
        extra_body={  
            "metadata": {  
                "tags": ["model-anthropic-claude-v2.1", "app-ishaan-prod"]  
            }  
        }  
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
    

#### Viewing Spend per tag​

#### `/spend/tags` Request Format​
    
    
    curl -X GET "http://0.0.0.0:4000/spend/tags" \  
    -H "Authorization: Bearer sk-1234"  
    

#### `/spend/tags`Response Format​
    
    
    [  
      {  
        "individual_request_tag": "model-anthropic-claude-v2.1",  
        "log_count": 6,  
        "total_spend": 0.000672  
      },  
      {  
        "individual_request_tag": "app-ishaan-local",  
        "log_count": 4,  
        "total_spend": 0.000448  
      },  
      {  
        "individual_request_tag": "app-ishaan-prod",  
        "log_count": 2,  
        "total_spend": 0.000224  
      }  
    ]  
      
    

### Tracking Spend with custom metadata​

Requirements:

  * Virtual Keys & a database should be set up, see [virtual keys](https://docs.litellm.ai/docs/proxy/virtual_keys)

#### Usage - /chat/completions requests with special spend logs metadata​

  * Set on Key
  * Set on Team
  * OpenAI Python v1.0.0+
  * OpenAI JS
  * Curl Request
  * Langchain

    
    
    curl -L -X POST 'http://0.0.0.0:4000/key/generate' \  
    -H 'Authorization: Bearer sk-1234' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "metadata": {  
          "spend_logs_metadata": {  
              "hello": "world"  
          }  
        }  
    }  
      
    '  
    
    
    
    curl -L -X POST 'http://0.0.0.0:4000/team/new' \  
    -H 'Authorization: Bearer sk-1234' \  
    -H 'Content-Type: application/json' \  
    -d '{  
        "metadata": {  
          "spend_logs_metadata": {  
              "hello": "world"  
          }  
        }  
    }  
      
    '  
    

Set `extra_body={"metadata": { }}` to `metadata` you want to pass
    
    
    import openai  
    client = openai.OpenAI(  
        api_key="anything",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    # request sent to model set on litellm proxy, `litellm --model`  
    response = client.chat.completions.create(  
        model="gpt-3.5-turbo",  
        messages = [  
            {  
                "role": "user",  
                "content": "this is a test request, write a short poem"  
            }  
        ],  
        extra_body={  
            "metadata": {  
                "spend_logs_metadata": {  
                    "hello": "world"  
                }  
            }  
        }  
    )  
      
    print(response)  
    
    
    
    const openai = require('openai');  
      
    async function runOpenAI() {  
      const client = new openai.OpenAI({  
        apiKey: 'sk-1234',  
        baseURL: 'http://0.0.0.0:4000'  
      });  
      
      try {  
        const response = await client.chat.completions.create({  
          model: 'gpt-3.5-turbo',  
          messages: [  
            {  
              role: 'user',  
              content: "this is a test request, write a short poem"  
            },  
          ],  
          metadata: {  
            spend_logs_metadata: { // 👈 Key Change  
                hello: "world"  
            }  
          }  
        });  
        console.log(response);  
      } catch (error) {  
        console.log("got this exception from server");  
        console.error(error);  
      }  
    }  
      
    // Call the asynchronous function  
    runOpenAI();  
    

Pass `metadata` as part of the request body
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "gpt-3.5-turbo",  
        "messages": [  
            {  
            "role": "user",  
            "content": "what llm are you"  
            }  
        ],  
        "metadata": {  
            "spend_logs_metadata": {  
                "hello": "world"  
            }  
        }  
    }'  
    
    
    
    from langchain.chat_models import ChatOpenAI  
    from langchain.prompts.chat import (  
        ChatPromptTemplate,  
        HumanMessagePromptTemplate,  
        SystemMessagePromptTemplate,  
    )  
    from langchain.schema import HumanMessage, SystemMessage  
      
    chat = ChatOpenAI(  
        openai_api_base="http://0.0.0.0:4000",  
        model = "gpt-3.5-turbo",  
        temperature=0.1,  
        extra_body={  
            "metadata": {  
                "spend_logs_metadata": {  
                    "hello": "world"  
                }  
            }  
        }  
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
    

#### Viewing Spend w/ custom metadata​

#### `/spend/logs` Request Format​
    
    
    curl -X GET "http://0.0.0.0:4000/spend/logs?request_id=<your-call-id" \ # e.g.: chatcmpl-9ZKMURhVYSi9D6r6PJ9vLcayIK0Vm  
    -H "Authorization: Bearer sk-1234"  
    

#### `/spend/logs` Response Format​
    
    
    [  
        {  
            "request_id": "chatcmpl-9ZKMURhVYSi9D6r6PJ9vLcayIK0Vm",  
            "call_type": "acompletion",  
            "metadata": {  
                "user_api_key": "88dc28d0f030c55ed4ab77ed8faf098196cb1c05df778539800c9f1243fe6b4b",  
                "user_api_key_alias": null,  
                "spend_logs_metadata": { # 👈 LOGGED CUSTOM METADATA  
                    "hello": "world"  
                },  
                "user_api_key_team_id": null,  
                "user_api_key_user_id": "116544810872468347480",  
                "user_api_key_team_alias": null  
            },  
        }  
    ]  
    

## Guardrails - Secret Detection/Redaction​

❓ Use this to REDACT API Keys, Secrets sent in requests to an LLM.

Example if you want to redact the value of `OPENAI_API_KEY` in the following request

#### Incoming Request​
    
    
    {  
        "messages": [  
            {  
                "role": "user",  
                "content": "Hey, how's it going, API_KEY = 'sk_1234567890abcdef'",  
            }  
        ]  
    }  
    

#### Request after Moderation​
    
    
    {  
        "messages": [  
            {  
                "role": "user",  
                "content": "Hey, how's it going, API_KEY = '[REDACTED]'",  
            }  
        ]  
    }  
    

**Usage**

**Step 1** Add this to your config.yaml
    
    
    litellm_settings:  
      callbacks: ["hide_secrets"]  
    

**Step 2** Run litellm proxy with `--detailed_debug` to see the server logs
    
    
    litellm --config config.yaml --detailed_debug  
    

**Step 3** Test it with request

Send this request
    
    
    curl --location 'http://localhost:4000/chat/completions' \  
        --header 'Authorization: Bearer sk-1234' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "llama3",  
        "messages": [  
            {  
            "role": "user",  
            "content": "what is the value of my open ai key? openai_api_key=sk-1234998222"  
            }  
        ]  
    }'  
    

Expect to see the following warning on your litellm server logs
    
    
    LiteLLM Proxy:WARNING: secret_detection.py:88 - Detected and redacted secrets in message: ['Secret Keyword']  
    

You can also see the raw request sent from litellm to the API Provider
    
    
    POST Request Sent from LiteLLM:  
    curl -X POST \  
    https://api.groq.com/openai/v1/ \  
    -H 'Authorization: Bearer gsk_mySVchjY********************************************' \  
    -d {  
      "model": "llama3-8b-8192",  
      "messages": [  
        {  
          "role": "user",  
          "content": "what is the time today, openai_api_key=[REDACTED]"  
        }  
      ],  
      "stream": false,  
      "extra_body": {}  
    }  
    

### Secret Detection On/Off per API Key​

❓ Use this when you need to switch guardrails on/off per API Key

**Step 1** Create Key with `hide_secrets` Off

👉 Set `"permissions": {"hide_secrets": false}` with either `/key/generate` or `/key/update`

This means the `hide_secrets` guardrail is off for all requests from this API Key

  * /key/generate
  * /key/update

    
    
    curl --location 'http://0.0.0.0:4000/key/generate' \  
        --header 'Authorization: Bearer sk-1234' \  
        --header 'Content-Type: application/json' \  
        --data '{  
            "permissions": {"hide_secrets": false}  
    }'  
    
    
    
    # {"permissions":{"hide_secrets":false},"key":"sk-jNm1Zar7XfNdZXp49Z1kSQ"}    
    
    
    
    curl --location 'http://0.0.0.0:4000/key/update' \  
        --header 'Authorization: Bearer sk-1234' \  
        --header 'Content-Type: application/json' \  
        --data '{  
            "key": "sk-jNm1Zar7XfNdZXp49Z1kSQ",  
            "permissions": {"hide_secrets": false}  
    }'  
    
    
    
    # {"permissions":{"hide_secrets":false},"key":"sk-jNm1Zar7XfNdZXp49Z1kSQ"}    
    

**Step 2** Test it with new key
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
        --header 'Authorization: Bearer sk-jNm1Zar7XfNdZXp49Z1kSQ' \  
        --header 'Content-Type: application/json' \  
        --data '{  
        "model": "llama3",  
        "messages": [  
            {  
            "role": "user",  
            "content": "does my openai key look well formatted OpenAI_API_KEY=sk-1234777"  
            }  
        ]  
    }'  
    

Expect to see `sk-1234777` in your server logs on your callback.

info

The `hide_secrets` guardrail check did not run on this request because api key=sk-jNm1Zar7XfNdZXp49Z1kSQ has `"permissions": {"hide_secrets": false}`

## Content Moderation​

### Content Moderation with LLM Guard​

Set the LLM Guard API Base in your environment
    
    
    LLM_GUARD_API_BASE = "http://0.0.0.0:8192" # deployed llm guard api  
    

Add `llmguard_moderations` as a callback
    
    
    litellm_settings:  
        callbacks: ["llmguard_moderations"]  
    

Now you can easily test it

  * Make a regular /chat/completion call

  * Check your proxy logs for any statement with `LLM Guard:`

Expected results:
    
    
    LLM Guard: Received response - {"sanitized_prompt": "hello world", "is_valid": true, "scanners": { "Regex": 0.0 }}  
    

#### Turn on/off per key​

**1\. Update config**
    
    
    litellm_settings:  
        callbacks: ["llmguard_moderations"]  
        llm_guard_mode: "key-specific"  
    

**2\. Create new key**
    
    
    curl --location 'http://localhost:4000/key/generate' \  
    --header 'Authorization: Bearer sk-1234' \  
    --header 'Content-Type: application/json' \  
    --data '{  
        "models": ["fake-openai-endpoint"],  
        "permissions": {  
            "enable_llm_guard_check": true # 👈 KEY CHANGE  
        }  
    }'  
      
    # Returns {..'key': 'my-new-key'}  
    

**3\. Test it!**
    
    
    curl --location 'http://0.0.0.0:4000/v1/chat/completions' \  
    --header 'Content-Type: application/json' \  
    --header 'Authorization: Bearer my-new-key' \ # 👈 TEST KEY  
    --data '{"model": "fake-openai-endpoint", "messages": [  
            {"role": "system", "content": "Be helpful"},  
            {"role": "user", "content": "What do you know?"}  
        ]  
        }'  
    

#### Turn on/off per request​

**1\. Update config**
    
    
    litellm_settings:  
        callbacks: ["llmguard_moderations"]  
        llm_guard_mode: "request-specific"  
    

**2\. Create new key**
    
    
    curl --location 'http://localhost:4000/key/generate' \  
    --header 'Authorization: Bearer sk-1234' \  
    --header 'Content-Type: application/json' \  
    --data '{  
        "models": ["fake-openai-endpoint"],  
    }'  
      
    # Returns {..'key': 'my-new-key'}  
    

**3\. Test it!**

  * OpenAI Python v1.0.0+
  * Curl Request

    
    
    import openai  
    client = openai.OpenAI(  
        api_key="sk-1234",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    # request sent to model set on litellm proxy, `litellm --model`  
    response = client.chat.completions.create(  
        model="gpt-3.5-turbo",  
        messages = [  
            {  
                "role": "user",  
                "content": "this is a test request, write a short poem"  
            }  
        ],  
        extra_body={ # pass in any provider-specific param, if not supported by openai, https://docs.litellm.ai/docs/completion/input#provider-specific-params  
            "metadata": {  
                "permissions": {  
                    "enable_llm_guard_check": True # 👈 KEY CHANGE  
                },  
            }  
        }  
    )  
      
    print(response)  
    
    
    
    curl --location 'http://0.0.0.0:4000/v1/chat/completions' \  
    --header 'Content-Type: application/json' \  
    --header 'Authorization: Bearer my-new-key' \ # 👈 TEST KEY  
    --data '{"model": "fake-openai-endpoint", "messages": [  
            {"role": "system", "content": "Be helpful"},  
            {"role": "user", "content": "What do you know?"}  
        ]  
        }'  
    

### Content Moderation with LlamaGuard​

Currently works with Sagemaker's LlamaGuard endpoint.

How to enable this in your config.yaml:
    
    
    litellm_settings:  
       callbacks: ["llamaguard_moderations"]  
       llamaguard_model_name: "sagemaker/jumpstart-dft-meta-textgeneration-llama-guard-7b"  
    

Make sure you have the relevant keys in your environment, eg.:
    
    
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
    

#### Customize LlamaGuard prompt​

To modify the unsafe categories llama guard evaluates against, just create your own version of [this category list](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/llamaguard_prompt.txt)

Point your proxy to it
    
    
    callbacks: ["llamaguard_moderations"]  
      llamaguard_model_name: "sagemaker/jumpstart-dft-meta-textgeneration-llama-guard-7b"  
      llamaguard_unsafe_content_categories: /path/to/llamaguard_prompt.txt  
    

### Content Moderation with Google Text Moderation​

Requires your GOOGLE_APPLICATION_CREDENTIALS to be set in your .env (same as VertexAI).

How to enable this in your config.yaml:
    
    
    litellm_settings:  
       callbacks: ["google_text_moderation"]  
    

#### Set custom confidence thresholds​

Google Moderations checks the test against several categories. [Source](https://cloud.google.com/natural-language/docs/moderating-text#safety_attribute_confidence_scores)

#### Set global default confidence threshold​

By default this is set to 0.8. But you can override this in your config.yaml.
    
    
    litellm_settings:   
        google_moderation_confidence_threshold: 0.4   
    

#### Set category-specific confidence threshold​

Set a category specific confidence threshold in your config.yaml. If none set, the global default will be used.
    
    
    litellm_settings:   
        toxic_confidence_threshold: 0.1  
    

Here are the category specific values:

Category| Setting  
---|---  
"toxic"| toxic_confidence_threshold: 0.1  
"insult"| insult_confidence_threshold: 0.1  
"profanity"| profanity_confidence_threshold: 0.1  
"derogatory"| derogatory_confidence_threshold: 0.1  
"sexual"| sexual_confidence_threshold: 0.1  
"death_harm_and_tragedy"| death_harm_and_tragedy_threshold: 0.1  
"violent"| violent_threshold: 0.1  
"firearms_and_weapons"| firearms_and_weapons_threshold: 0.1  
"public_safety"| public_safety_threshold: 0.1  
"health"| health_threshold: 0.1  
"religion_and_belief"| religion_and_belief_threshold: 0.1  
"illicit_drugs"| illicit_drugs_threshold: 0.1  
"war_and_conflict"| war_and_conflict_threshold: 0.1  
"politics"| politics_threshold: 0.1  
"finance"| finance_threshold: 0.1  
"legal"| legal_threshold: 0.1  
  
## Swagger Docs - Custom Routes + Branding​

info

Requires a LiteLLM Enterprise key to use. Get a free 2-week license [here](https://forms.gle/sTDVprBs18M4V8Le8)

Set LiteLLM Key in your environment
    
    
    LITELLM_LICENSE=""  
    

#### Customize Title + Description​

In your environment, set:
    
    
    DOCS_TITLE="TotalGPT"  
    DOCS_DESCRIPTION="Sample Company Description"  
    

#### Customize Routes​

Hide admin routes from users.

In your environment, set:
    
    
    DOCS_FILTERED="True" # only shows openai routes to user  
    

## Enable Blocked User Lists​

If any call is made to proxy with this user id, it'll be rejected - use this if you want to let users opt-out of ai features
    
    
    litellm_settings:   
         callbacks: ["blocked_user_check"]   
         blocked_user_list: ["user_id_1", "user_id_2", ...]  # can also be a .txt filepath e.g. `/relative/path/blocked_list.txt`   
    

### How to test​

  * OpenAI Python v1.0.0+
  * Curl Request

Set `user=<user_id>` to the user id of the user who might have opted out.
    
    
    import openai  
    client = openai.OpenAI(  
        api_key="sk-1234",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    # request sent to model set on litellm proxy, `litellm --model`  
    response = client.chat.completions.create(  
        model="gpt-3.5-turbo",  
        messages = [  
            {  
                "role": "user",  
                "content": "this is a test request, write a short poem"  
            }  
        ],  
        user="user_id_1"  
    )  
      
    print(response)  
    
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
    --header 'Content-Type: application/json' \  
    --data ' {  
          "model": "gpt-3.5-turbo",  
          "messages": [  
            {  
              "role": "user",  
              "content": "what llm are you"  
            }  
          ],  
          "user": "user_id_1" # this is also an openai supported param   
        }  
    '  
    

info

[Suggest a way to improve this](https://github.com/BerriAI/litellm/issues/new/choose)

### Using via API​

**Block all calls for a customer id**
    
    
    curl -X POST "http://0.0.0.0:4000/customer/block" \  
    -H "Authorization: Bearer sk-1234" \   
    -D '{  
    "user_ids": [<user_id>, ...]   
    }'  
    

**Unblock calls for a user id**
    
    
    curl -X POST "http://0.0.0.0:4000/user/unblock" \  
    -H "Authorization: Bearer sk-1234" \   
    -D '{  
    "user_ids": [<user_id>, ...]   
    }'  
    

## Enable Banned Keywords List​
    
    
    litellm_settings:   
         callbacks: ["banned_keywords"]  
         banned_keywords_list: ["hello"] # can also be a .txt file - e.g.: `/relative/path/keywords.txt`  
    

### Test this​
    
    
    curl --location 'http://0.0.0.0:4000/chat/completions' \  
    --header 'Content-Type: application/json' \  
    --data ' {  
          "model": "gpt-3.5-turbo",  
          "messages": [  
            {  
              "role": "user",  
              "content": "Hello world!"  
            }  
          ]  
        }  
    '  
    

## Public Model Hub​

Share a public page of available models for users

## [BETA] AWS Key Manager - Key Decryption​

This is a beta feature, and subject to changes.

**Step 1.** Add `USE_AWS_KMS` to env
    
    
    USE_AWS_KMS="True"  
    

**Step 2.** Add `LITELLM_SECRET_AWS_KMS_` to encrypted keys in env
    
    
    LITELLM_SECRET_AWS_KMS_DATABASE_URL="AQICAH.."  
    

LiteLLM will find this and use the decrypted `DATABASE_URL="postgres://.."` value in runtime.

**Step 3.** Start proxy
    
    
    $ litellm  
    

How it works?

  * Key Decryption runs before server starts up. [**Code**](https://github.com/BerriAI/litellm/blob/8571cb45e80cc561dc34bc6aa89611eb96b9fe3e/litellm/proxy/proxy_cli.py#L445)
  * It adds the decrypted value to the `os.environ` for the python process.

**Note:** Setting an environment variable within a Python script using os.environ will not make that variable accessible via SSH sessions or any other new processes that are started independently of the Python script. Environment variables set this way only affect the current process and its child processes.

## Set Max Request / Response Size on LiteLLM Proxy​

Use this if you want to set a maximum request / response size for your proxy server. If a request size is above the size it gets rejected + slack alert triggered

#### Usage​

**Step 1.** Set `max_request_size_mb` and `max_response_size_mb`

For this example we set a very low limit on `max_request_size_mb` and expect it to get rejected

info

In production we recommend setting a `max_request_size_mb` / `max_response_size_mb` around `32 MB`
    
    
    model_list:  
      - model_name: fake-openai-endpoint  
        litellm_params:  
          model: openai/fake  
          api_key: fake-key  
          api_base: https://exampleopenaiendpoint-production.up.railway.app/  
    general_settings:   
      master_key: sk-1234  
      
      # Security controls  
      max_request_size_mb: 0.000000001 # 👈 Key Change - Max Request Size in MB. Set this very low for testing   
      max_response_size_mb: 100 # 👈 Key Change - Max Response Size in MB  
    

**Step 2.** Test it with `/chat/completions` request
    
    
    curl http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-1234" \  
      -d '{  
        "model": "fake-openai-endpoint",  
        "messages": [  
          {"role": "user", "content": "Hello, Claude!"}  
        ]  
      }'  
    

**Expected Response from request** We expect this to fail since the request size is over `max_request_size_mb`
    
    
    {"error":{"message":"Request size is too large. Request size is 0.0001125335693359375 MB. Max size is 1e-09 MB","type":"bad_request_error","param":"content-length","code":400}}  
    

  * Blocking web crawlers
  * Required Params for LLM Requests
  * Control available public, private routes
  * Spend Tracking
    * Custom Tags
    * Tracking Spend with custom metadata
  * Guardrails - Secret Detection/Redaction
    * Secret Detection On/Off per API Key
  * Content Moderation
    * Content Moderation with LLM Guard
    * Content Moderation with LlamaGuard
    * Content Moderation with Google Text Moderation
  * Swagger Docs - Custom Routes + Branding
  * Enable Blocked User Lists
    * How to test
    * Using via API
  * Enable Banned Keywords List
    * Test this
  * Public Model Hub
  * [BETA] AWS Key Manager - Key Decryption
  * Set Max Request / Response Size on LiteLLM Proxy