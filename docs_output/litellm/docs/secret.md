# Secret Manager | liteLLM

On this page

info

✨ **This is an Enterprise Feature**

[Enterprise Pricing](https://www.litellm.ai/#pricing)

[Contact us here to get a free trial](https://calendly.com/d/4mp-gd3-k5k/litellm-1-1-onboarding-chat)

LiteLLM supports **reading secrets (eg.`OPENAI_API_KEY`)** and **writing secrets (eg. Virtual Keys)** from Azure Key Vault, Google Secret Manager, Hashicorp Vault, and AWS Secret Manager.

## Supported Secret Managers​

  * AWS Key Management Service
  * AWS Secret Manager
  * Azure Key Vault
  * Google Secret Manager
  * Google Key Management Service
  * Hashicorp Vault

## AWS Secret Manager​

Store your proxy keys in AWS Secret Manager.

Feature| Support| Description  
---|---|---  
Reading Secrets| ✅| Read secrets e.g `OPENAI_API_KEY`  
Writing Secrets| ✅| Store secrets e.g `Virtual Keys`  
  
#### Proxy Usage​

  1. Save AWS Credentials in your environment

    
    
    os.environ["AWS_ACCESS_KEY_ID"] = ""  # Access key  
    os.environ["AWS_SECRET_ACCESS_KEY"] = "" # Secret access key  
    os.environ["AWS_REGION_NAME"] = "" # us-east-1, us-east-2, us-west-1, us-west-2  
    

  2. Enable AWS Secret Manager in config.

  * Read Keys from AWS Secret Manager
  * Write Virtual Keys to AWS Secret Manager
  * Read + Write Keys with AWS Secret Manager

    
    
    general_settings:  
      master_key: os.environ/litellm_master_key   
      key_management_system: "aws_secret_manager" # 👈 KEY CHANGE  
      key_management_settings:   
        hosted_keys: ["litellm_master_key"] # 👈 Specify which env keys you stored on AWS   
      
    

This will only store virtual keys in AWS Secret Manager. No keys will be read from AWS Secret Manager.
    
    
    general_settings:  
      key_management_system: "aws_secret_manager" # 👈 KEY CHANGE  
      key_management_settings:   
        store_virtual_keys: true # OPTIONAL. Defaults to False, when True will store virtual keys in secret manager  
        prefix_for_stored_virtual_keys: "litellm/" # OPTIONAL. If set, this prefix will be used for stored virtual keys in the secret manager  
        access_mode: "write_only" # Literal["read_only", "write_only", "read_and_write"]  
    
    
    
    general_settings:  
      master_key: os.environ/litellm_master_key   
      key_management_system: "aws_secret_manager" # 👈 KEY CHANGE  
      key_management_settings:   
        store_virtual_keys: true # OPTIONAL. Defaults to False, when True will store virtual keys in secret manager  
        prefix_for_stored_virtual_keys: "litellm/" # OPTIONAL. If set, this prefix will be used for stored virtual keys in the secret manager  
        access_mode: "read_and_write" # Literal["read_only", "write_only", "read_and_write"]  
        hosted_keys: ["litellm_master_key"] # OPTIONAL. Specify which env keys you stored on AWS  
    

  3. Run proxy

    
    
    litellm --config /path/to/config.yaml  
    

#### Using K/V pairs in 1 AWS Secret​

You can read multiple keys from a single AWS Secret using the `primary_secret_name` parameter:
    
    
    general_settings:  
      key_management_system: "aws_secret_manager"  
      key_management_settings:  
        hosted_keys: [  
          "OPENAI_API_KEY_MODEL_1",  
          "OPENAI_API_KEY_MODEL_2",  
        ]  
        primary_secret_name: "litellm_secrets" # 👈 Read multiple keys from one JSON secret  
    

The `primary_secret_name` allows you to read multiple keys from a single AWS Secret as a JSON object. For example, the "litellm_secrets" would contain:
    
    
    {  
      "OPENAI_API_KEY_MODEL_1": "sk-key1...",  
      "OPENAI_API_KEY_MODEL_2": "sk-key2..."  
    }  
    

This reduces the number of AWS Secrets you need to manage.

## Hashicorp Vault​

Feature| Support| Description  
---|---|---  
Reading Secrets| ✅| Read secrets e.g `OPENAI_API_KEY`  
Writing Secrets| ✅| Store secrets e.g `Virtual Keys`  
  
Read secrets from [Hashicorp Vault](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2)

**Step 1.** Add Hashicorp Vault details in your environment

LiteLLM supports two methods of authentication:

  1. TLS cert authentication - `HCP_VAULT_CLIENT_CERT` and `HCP_VAULT_CLIENT_KEY`
  2. Token authentication - `HCP_VAULT_TOKEN`

    
    
    HCP_VAULT_ADDR="https://test-cluster-public-vault-0f98180c.e98296b2.z1.hashicorp.cloud:8200"  
    HCP_VAULT_NAMESPACE="admin"  
      
    # Authentication via TLS cert  
    HCP_VAULT_CLIENT_CERT="path/to/client.pem"  
    HCP_VAULT_CLIENT_KEY="path/to/client.key"  
      
    # OR - Authentication via token  
    HCP_VAULT_TOKEN="hvs.CAESIG52gL6ljBSdmq*****"  
      
      
    # OPTIONAL  
    HCP_VAULT_REFRESH_INTERVAL="86400" # defaults to 86400, frequency of cache refresh for Hashicorp Vault  
    

**Step 2.** Add to proxy config.yaml
    
    
    general_settings:  
      key_management_system: "hashicorp_vault"  
      
      # [OPTIONAL SETTINGS]  
      key_management_settings:   
        store_virtual_keys: true # OPTIONAL. Defaults to False, when True will store virtual keys in secret manager  
        prefix_for_stored_virtual_keys: "litellm/" # OPTIONAL. If set, this prefix will be used for stored virtual keys in the secret manager  
        access_mode: "read_and_write" # Literal["read_only", "write_only", "read_and_write"]  
    

**Step 3.** Start + test proxy
    
    
    $ litellm --config /path/to/config.yaml  
    

[Quick Test Proxy](/docs/proxy/user_keys)

#### How it works​

**Reading Secrets** LiteLLM reads secrets from Hashicorp Vault's KV v2 engine using the following URL format:
    
    
    {VAULT_ADDR}/v1/{NAMESPACE}/secret/data/{SECRET_NAME}  
    

For example, if you have:

  * `HCP_VAULT_ADDR="https://vault.example.com:8200"`
  * `HCP_VAULT_NAMESPACE="admin"`
  * Secret name: `AZURE_API_KEY`

LiteLLM will look up:
    
    
    https://vault.example.com:8200/v1/admin/secret/data/AZURE_API_KEY  
    

#### Expected Secret Format​

LiteLLM expects all secrets to be stored as a JSON object with a `key` field containing the secret value.

For example, for `AZURE_API_KEY`, the secret should be stored as:
    
    
    {  
      "key": "sk-1234"  
    }  
    

**Writing Secrets**

When a Virtual Key is Created / Deleted on LiteLLM, LiteLLM will automatically create / delete the secret in Hashicorp Vault.

  * Create Virtual Key on LiteLLM either through the LiteLLM Admin UI or API

  * Check Hashicorp Vault for secret

LiteLLM stores secret under the `prefix_for_stored_virtual_keys` path (default: `litellm/`)

## Azure Key Vault​

#### Usage with LiteLLM Proxy Server​

  1. Install Proxy dependencies

    
    
    pip install 'litellm[proxy]' 'litellm[extra_proxy]'  
    

  2. Save Azure details in your environment

    
    
    export["AZURE_CLIENT_ID"]="your-azure-app-client-id"  
    export["AZURE_CLIENT_SECRET"]="your-azure-app-client-secret"  
    export["AZURE_TENANT_ID"]="your-azure-tenant-id"  
    export["AZURE_KEY_VAULT_URI"]="your-azure-key-vault-uri"  
    

  3. Add to proxy config.yaml

    
    
    model_list:   
        - model_name: "my-azure-models" # model alias   
            litellm_params:  
                model: "azure/<your-deployment-name>"  
                api_key: "os.environ/AZURE-API-KEY" # reads from key vault - get_secret("AZURE_API_KEY")  
                api_base: "os.environ/AZURE-API-BASE" # reads from key vault - get_secret("AZURE_API_BASE")  
      
    general_settings:  
      key_management_system: "azure_key_vault"  
    

You can now test this by starting your proxy:
    
    
    litellm --config /path/to/config.yaml  
    

[Quick Test Proxy](/docs/proxy/quick_start#using-litellm-proxy---curl-request-openai-package-langchain-langchain-js)

## Google Secret Manager​

Support for [Google Secret Manager](https://cloud.google.com/security/products/secret-manager)

  1. Save Google Secret Manager details in your environment

    
    
    GOOGLE_SECRET_MANAGER_PROJECT_ID="your-project-id-on-gcp" # example: adroit-crow-413218  
    

Optional Params
    
    
    export GOOGLE_SECRET_MANAGER_REFRESH_INTERVAL = ""            # (int) defaults to 86400  
    export GOOGLE_SECRET_MANAGER_ALWAYS_READ_SECRET_MANAGER = ""  # (str) set to "true" if you want to always read from google secret manager without using in memory caching. NOT RECOMMENDED in PROD  
    

  2. Add to proxy config.yaml

    
    
    model_list:  
      - model_name: fake-openai-endpoint  
        litellm_params:  
          model: openai/fake  
          api_base: https://exampleopenaiendpoint-production.up.railway.app/  
          api_key: os.environ/OPENAI_API_KEY # this will be read from Google Secret Manager  
      
    general_settings:  
      key_management_system: "google_secret_manager"  
    

You can now test this by starting your proxy:
    
    
    litellm --config /path/to/config.yaml  
    

[Quick Test Proxy](/docs/proxy/quick_start#using-litellm-proxy---curl-request-openai-package-langchain-langchain-js)

## Google Key Management Service​

Use encrypted keys from Google KMS on the proxy

Step 1. Add keys to env
    
    
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/credentials.json"  
    export GOOGLE_KMS_RESOURCE_NAME="projects/*/locations/*/keyRings/*/cryptoKeys/*"  
    export PROXY_DATABASE_URL_ENCRYPTED=b'\n$\x00D\xac\xb4/\x8e\xc...'  
    

Step 2: Update Config
    
    
    general_settings:  
      key_management_system: "google_kms"  
      database_url: "os.environ/PROXY_DATABASE_URL_ENCRYPTED"  
      master_key: sk-1234  
    

Step 3: Start + test proxy
    
    
    $ litellm --config /path/to/config.yaml  
    

And in another terminal
    
    
    $ litellm --test   
    

[Quick Test Proxy](/docs/proxy/user_keys)

## AWS Key Management V1​

tip

[BETA] AWS Key Management v2 is on the enterprise tier. Go [here for docs](/docs/proxy/enterprise#beta-aws-key-manager---key-decryption)

Use AWS KMS to storing a hashed copy of your Proxy Master Key in the environment.
    
    
    export LITELLM_MASTER_KEY="djZ9xjVaZ..." # 👈 ENCRYPTED KEY  
    export AWS_REGION_NAME="us-west-2"  
    
    
    
    general_settings:  
      key_management_system: "aws_kms"  
      key_management_settings:  
        hosted_keys: ["LITELLM_MASTER_KEY"] # 👈 WHICH KEYS ARE STORED ON KMS  
    

[**See Decryption Code**](https://github.com/BerriAI/litellm/blob/a2da2a8f168d45648b61279d4795d647d94f90c9/litellm/utils.py#L10182)

## **All Secret Manager Settings**​

All settings related to secret management
    
    
    general_settings:  
      key_management_system: "aws_secret_manager" # REQUIRED  
      key_management_settings:    
      
        # Storing Virtual Keys Settings  
        store_virtual_keys: true # OPTIONAL. Defaults to False, when True will store virtual keys in secret manager  
        prefix_for_stored_virtual_keys: "litellm/" # OPTIONAL.I f set, this prefix will be used for stored virtual keys in the secret manager  
          
        # Access Mode Settings  
        access_mode: "write_only" # OPTIONAL. Literal["read_only", "write_only", "read_and_write"]. Defaults to "read_only"  
          
        # Hosted Keys Settings  
        hosted_keys: ["litellm_master_key"] # OPTIONAL. Specify which env keys you stored on AWS  
      
        # K/V pairs in 1 AWS Secret Settings  
        primary_secret_name: "litellm_secrets" # OPTIONAL. Read multiple keys from one JSON secret on AWS Secret Manager  
    

  * Supported Secret Managers
  * AWS Secret Manager
  * Hashicorp Vault
  * Azure Key Vault
  * Google Secret Manager
  * Google Key Management Service
  * AWS Key Management V1
  * **All Secret Manager Settings**