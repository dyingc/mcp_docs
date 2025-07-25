# Using an existing secret for your installation (Kubernetes only) | 🦜️🛠️ LangSmith

On this page

By default, LangSmith will provision several Kubernetes secrets to store sensitive information such as license keys, salts, and other configuration parameters. However, you may want to use an existing secret that you have already created in your Kubernetes cluster (or provisioned via some sort of secrets operator). This can be useful if you want to manage sensitive information in a centralized way or if you have specific security requirements.

By default we will provision the following secrets corresponding to different components of LangSmith:

  * `langsmith-secrets`: This secret contains the license key and some other basic configuration parameters. You can see the template for this secret [here](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/templates/secrets.yaml)
  * `langsmith-redis`: This secret contains the Redis connection string and password. You can see the template for this secret [here](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/templates/redis/secrets.yaml)
  * `langsmith-postgres`: This secret contains the Postgres connection string and password. You can see the template for this secret [here](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/templates/postgres/secrets.yaml)
  * `langsmith-clickhouse`: This secret contains the ClickHouse connection string and password. You can see the template for this secret [here](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/templates/clickhouse/secrets.yaml)

## Requirements​

  * An existing Kubernetes cluster
  * A way to create Kubernetes secrets in your cluster. This can be done using `kubectl`, a Helm chart, or a secrets operator like [Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets)

## Parameters​

You will need to create your own Kubernetes secrets that adhere to the structure of the secrets provisioned by the LangSmith Helm Chart.

warning

The secrets must have the same structure as the ones provisioned by the LangSmith Helm Chart (refer to the links above to see the specific secrets). If you miss any of the required keys, your LangSmith instance may not work correctly.

An example secret may look like this:
    
    
    apiVersion: v1  
    kind: Secret  
    metadata:  
      name: langsmith-existing-secrets  
      namespace: langsmith  
    stringData:  
      oauth_client_id: foo  
      oauth_client_secret: foo  
      oauth_issuer_url: foo  
      langsmith_license_key: foo  
      langgraph_cloud_license_key: foo  
      api_key_salt: foo  
      jwt_secret: foo  
      initial_org_admin_password: foo  
      blob_storage_access_key: foo  
      blob_storage_access_key_secret: foo  
      azure_storage_account_key: foo  
      azure_storage_connection_string: foo  
    

## Configuration​

With these secrets provisioned, you can configure your LangSmith instance to use the secrets directly to avoid passing in secret values through plaintext. You can do this by modifying the `langsmith_config.yaml` file for your LangSmith Helm Chart installation.

  * Helm

    
    
      
    config:  
    existingSecretName: "langsmith-secrets" # The name of the secret that contains the license key and other basic configuration parameters  
    redis:  
    external:  
      enabled: true # Set to true to use an external Redis instance. This secret is only needed if you are using an external Redis instance  
      existingSecretName: "langsmith-redis" # The name of the secret that contains the Redis connection string and password  
    postgres:  
    external:  
      enabled: true # Set to true to use an external Postgres instance. This secret is only needed if you are using an external Postgres instance  
      existingSecretName: "langsmith-postgres" # The name of the secret that contains the Postgres connection string and password  
    clickhouse:  
    external:  
      enabled: true # Set to true to use an external ClickHouse instance. This secret is only needed if you are using an external ClickHouse instance  
      existingSecretName: "langsmith-clickhouse" # The name of the secret that contains the ClickHouse connection string and password  
    

Once configured, you will need to update your LangSmith installation. You can follow our upgrade guide [here](/self_hosting/upgrades). If everything is configured correctly, your LangSmith instance should now be accessible via the Ingress. You can run the following to check that your secrets are being used correctly:
    
    
    kubectl describe deployment langsmith-backend | grep -i <secret-name>  
    

You should see something like this in the output:
    
    
    POSTGRES_DATABASE_URI:                    <set to the key 'connection_url' in secret <your-secret-name>  Optional: false  
    CLICKHOUSE_DB:                            <set to the key 'clickhouse_db' in secret <your-secret-name>   Optional: false  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Requirements
  * Parameters
  * Configuration

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)