# ⚡ Best Practices for Production | liteLLM

On this page

## 1\. Use this config.yaml​

Use this config.yaml in production (with your own LLMs)
    
    
    model_list:  
      - model_name: fake-openai-endpoint  
        litellm_params:  
          model: openai/fake  
          api_key: fake-key  
          api_base: https://exampleopenaiendpoint-production.up.railway.app/  
      
    general_settings:  
      master_key: sk-1234      # enter your own master key, ensure it starts with 'sk-'  
      alerting: ["slack"]      # Setup slack alerting - get alerts on LLM exceptions, Budget Alerts, Slow LLM Responses  
      proxy_batch_write_at: 60 # Batch write spend updates every 60s  
      database_connection_pool_limit: 10 # limit the number of database connections to = MAX Number of DB Connections/Number of instances of litellm proxy (Around 10-20 is good number)  
      
      # OPTIONAL Best Practices  
      disable_spend_logs: True # turn off writing each transaction to the db. We recommend doing this is you don't need to see Usage on the LiteLLM UI and are tracking metrics via Prometheus  
      disable_error_logs: True # turn off writing LLM Exceptions to DB  
      allow_requests_on_db_unavailable: True # Only USE when running LiteLLM on your VPC. Allow requests to still be processed even if the DB is unavailable. We recommend doing this if you're running LiteLLM on VPC that cannot be accessed from the public internet.  
      
    litellm_settings:  
      request_timeout: 600    # raise Timeout error if call takes longer than 600 seconds. Default value is 6000seconds if not set  
      set_verbose: False      # Switch off Debug Logging, ensure your logs do not have any debugging on  
      json_logs: true         # Get debug logs in json format  
    

Set slack webhook url in your env
    
    
    export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/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"  
    

Turn off FASTAPI's default info logs
    
    
    export LITELLM_LOG="ERROR"  
    

info

Need Help or want dedicated support ? Talk to a founder [here]: (<https://calendly.com/d/4mp-gd3-k5k/litellm-1-1-onboarding-chat>)

## 2\. Recommended Machine Specifications​

For optimal performance in production, we recommend the following minimum machine specifications:

Resource| Recommended Value  
---|---  
CPU| 2 vCPU  
Memory| 4 GB RAM  
  
These specifications provide:

  * Sufficient compute power for handling concurrent requests
  * Adequate memory for request processing and caching

## 3\. On Kubernetes - Use 1 Uvicorn worker [Suggested CMD]​

Use this Docker `CMD`. This will start the proxy with 1 Uvicorn Async Worker

(Ensure that you're not setting `run_gunicorn` or `num_workers` in the CMD).
    
    
    CMD ["--port", "4000", "--config", "./proxy_server_config.yaml"]  
    

## 4\. Use Redis 'port','host', 'password'. NOT 'redis_url'​

If you decide to use Redis, DO NOT use 'redis_url'. We recommend using redis port, host, and password params.

`redis_url`is 80 RPS slower

This is still something we're investigating. Keep track of it [here](https://github.com/BerriAI/litellm/issues/3188)

### Redis Version Requirement​

Component| Minimum Version  
---|---  
Redis| 7.0+  
  
Recommended to do this for prod:
    
    
    router_settings:  
      routing_strategy: usage-based-routing-v2   
      # redis_url: "os.environ/REDIS_URL"  
      redis_host: os.environ/REDIS_HOST  
      redis_port: os.environ/REDIS_PORT  
      redis_password: os.environ/REDIS_PASSWORD  
      
    litellm_settings:  
      cache: True  
      cache_params:  
        type: redis  
        host: os.environ/REDIS_HOST  
        port: os.environ/REDIS_PORT  
        password: os.environ/REDIS_PASSWORD  
    

## 5\. Disable 'load_dotenv'​

Set `export LITELLM_MODE="PRODUCTION"`

This disables the load_dotenv() functionality, which will automatically load your environment credentials from the local `.env`.

## 6\. If running LiteLLM on VPC, gracefully handle DB unavailability​

When running LiteLLM on a VPC (and inaccessible from the public internet), you can enable graceful degradation so that request processing continues even if the database is temporarily unavailable.

**WARNING: Only do this if you're running LiteLLM on VPC, that cannot be accessed from the public internet.**

#### Configuration​

litellm config.yaml
    
    
    general_settings:  
      allow_requests_on_db_unavailable: True  
    

#### Expected Behavior​

When `allow_requests_on_db_unavailable` is set to `true`, LiteLLM will handle errors as follows:

Type of Error| Expected Behavior| Details  
---|---|---  
Prisma Errors| ✅ Request will be allowed| Covers issues like DB connection resets or rejections from the DB via Prisma, the ORM used by LiteLLM.  
Httpx Errors| ✅ Request will be allowed| Occurs when the database is unreachable, allowing the request to proceed despite the DB outage.  
Pod Startup Behavior| ✅ Pods start regardless| LiteLLM Pods will start even if the database is down or unreachable, ensuring higher uptime guarantees for deployments.  
Health/Readiness Check| ✅ Always returns 200 OK| The /health/readiness endpoint returns a 200 OK status to ensure that pods remain operational even when the database is unavailable.  
LiteLLM Budget Errors or Model Errors| ❌ Request will be blocked| Triggered when the DB is reachable but the authentication token is invalid, lacks access, or exceeds budget limits.  
  
## 7\. Disable spend_logs & error_logs if not using the LiteLLM UI​

By default, LiteLLM writes several types of logs to the database:

  * Every LLM API request to the `LiteLLM_SpendLogs` table
  * LLM Exceptions to the `LiteLLM_SpendLogs` table

If you're not viewing these logs on the LiteLLM UI, you can disable them by setting the following flags to `True`:
    
    
    general_settings:  
      disable_spend_logs: True    # Disable writing spend logs to DB  
      disable_error_logs: True    # Disable writing error logs to DB  
    

[More information about what the Database is used for here](/docs/proxy/db_info)

## 8\. Use Helm PreSync Hook for Database Migrations [BETA]​

To ensure only one service manages database migrations, use our [Helm PreSync hook for Database Migrations](https://github.com/BerriAI/litellm/blob/main/deploy/charts/litellm-helm/templates/migrations-job.yaml). This ensures migrations are handled during `helm upgrade` or `helm install`, while LiteLLM pods explicitly disable migrations.

  1. **Helm PreSync Hook** :
     * The Helm PreSync hook is configured in the chart to run database migrations during deployments.
     * The hook always sets `DISABLE_SCHEMA_UPDATE=false`, ensuring migrations are executed reliably.

Reference Settings to set on ArgoCD for `values.yaml`
    
    
    db:  
      useExisting: true # use existing Postgres DB  
      url: postgresql://ishaanjaffer0324:... # url of existing Postgres DB  
    

  2. **LiteLLM Pods** :

     * Set `DISABLE_SCHEMA_UPDATE=true` in LiteLLM pod configurations to prevent them from running migrations.

Example configuration for LiteLLM pod:
    
    env:  
      - name: DISABLE_SCHEMA_UPDATE  
        value: "true"  
    

## 9\. Set LiteLLM Salt Key​

If you plan on using the DB, set a salt key for encrypting/decrypting variables in the DB.

Do not change this after adding a model. It is used to encrypt / decrypt your LLM API Key credentials

We recommend - <https://1password.com/password-generator/> password generator to get a random hash for litellm salt key.
    
    
    export LITELLM_SALT_KEY="sk-1234"  
    

[**See Code**](https://github.com/BerriAI/litellm/blob/036a6821d588bd36d170713dcf5a72791a694178/litellm/proxy/common_utils/encrypt_decrypt_utils.py#L15)

## 10\. Use `prisma migrate deploy`​

Use this to handle db migrations across LiteLLM versions in production

  * ENV
  * CLI

    
    
    USE_PRISMA_MIGRATE="True"  
    
    
    
    litellm --use_prisma_migrate  
    

Benefits:

The migrate deploy command:

  * **Does not** issue a warning if an already applied migration is missing from migration history
  * **Does not** detect drift (production database schema differs from migration history end state - for example, due to a hotfix)
  * **Does not** reset the database or generate artifacts (such as Prisma Client)
  * **Does not** rely on a shadow database

### How does LiteLLM handle DB migrations in production?​

  1. A new migration file is written to our `litellm-proxy-extras` package. [See all](https://github.com/BerriAI/litellm/tree/main/litellm-proxy-extras/litellm_proxy_extras/migrations)

  2. The core litellm pip package is bumped to point to the new `litellm-proxy-extras` package. This ensures, older versions of LiteLLM will continue to use the old migrations. [See code](https://github.com/BerriAI/litellm/blob/52b35cd8093b9ad833987b24f494586a1e923209/pyproject.toml#L58)

  3. When you upgrade to a new version of LiteLLM, the migration file is applied to the database. [See code](https://github.com/BerriAI/litellm/blob/52b35cd8093b9ad833987b24f494586a1e923209/litellm-proxy-extras/litellm_proxy_extras/utils.py#L42)

### Read-only File System​

If you see a `Permission denied` error, it means the LiteLLM pod is running with a read-only file system.

To fix this, just set `LITELLM_MIGRATION_DIR="/path/to/writeable/directory"` in your environment.

LiteLLM will use this directory to write migration files.

## Extras​

### Expected Performance in Production​

1 LiteLLM Uvicorn Worker on Kubernetes

Description| Value  
---|---  
Avg latency| `50ms`  
Median latency| `51ms`  
`/chat/completions` Requests/second| `100`  
`/chat/completions` Requests/minute| `6000`  
`/chat/completions` Requests/hour| `360K`  
  
### Verifying Debugging logs are off​

You should only see the following level of details in logs on the proxy server
    
    
    # INFO:     192.168.2.205:11774 - "POST /chat/completions HTTP/1.1" 200 OK  
    # INFO:     192.168.2.205:34717 - "POST /chat/completions HTTP/1.1" 200 OK  
    # INFO:     192.168.2.205:29734 - "POST /chat/completions HTTP/1.1" 200 OK  
    

  * 1\. Use this config.yaml
  * 2\. Recommended Machine Specifications
  * 3\. On Kubernetes - Use 1 Uvicorn worker [Suggested CMD]
  * 4\. Use Redis 'port','host', 'password'. NOT 'redis_url'
    * Redis Version Requirement
  * 5\. Disable 'load_dotenv'
  * 6\. If running LiteLLM on VPC, gracefully handle DB unavailability
  * 7\. Disable spend_logs & error_logs if not using the LiteLLM UI
  * 8\. Use Helm PreSync Hook for Database Migrations [BETA]
  * 9\. Set LiteLLM Salt Key
  * 10\. Use `prisma migrate deploy`
    * How does LiteLLM handle DB migrations in production?
    * Read-only File System
  * Extras
    * Expected Performance in Production
    * Verifying Debugging logs are off