# General Upgrade Instructions | 🦜️🛠️ LangSmith

On this page

For general upgrade instructions, please follow the instructions below. Certain versions may have specific upgrade instructions, which will be detailed in more specific upgrade guides.

## Kubernetes(Helm)​

If you don't have the repo added, run the following command to add it:
    
    
    helm repo add langchain https://langchain-ai.github.io/helm/  
    

Update your local helm repo
    
    
    helm repo update  
    

Update your helm chart config file with any updates that are needed in the new version. These will be detailed in the release notes for the new version.

Run the following command to upgrade the chart(replace version with the version you want to upgrade to):

Namespace

If you are using a namespace other than the default namespace, you will need to specify the namespace in the `helm` and `kubectl` commands by using the `-n <namespace` flag.

Find the latest version of the chart. You can find this in the [Langsmith Helm Chart GitHub repository](https://github.com/langchain-ai/helm/releases) or by running the following command:
    
    
    helm search repo langchain/langsmith --versions  
    

You should see an output similar to this:
    
    
    langchain/langsmith     0.10.14         0.10.32         Helm chart to deploy the langsmith application ...  
    langchain/langsmith     0.10.13         0.10.32         Helm chart to deploy the langsmith application ...  
    langchain/langsmith     0.10.12         0.10.32         Helm chart to deploy the langsmith application ...  
    langchain/langsmith     0.10.11         0.10.29         Helm chart to deploy the langsmith application ...  
    langchain/langsmith     0.10.10         0.10.29         Helm chart to deploy the langsmith application ...  
    langchain/langsmith     0.10.9          0.10.29         Helm chart to deploy the langsmith application ...  
    

Choose the version you want to upgrade to (generally the latest version is recommended) and note the version number.
    
    
    helm upgrade <release-name> langchain/langsmith --version <version> --values <path-to-values-file>  
    

Verify that the upgrade was successful:
    
    
    helm status <release-name>  
    

All pods should be in the `Running` state. Verify that clickhouse is running and that both `migrations` jobs have completed.
    
    
    kubectl get pods  
      
    NAME                                     READY   STATUS      RESTARTS   AGE  
    langsmith-backend-95b6d54f5-gz48b        1/1     Running     0          15h  
    langsmith-pg-migrations-d2z6k            0/1     Completed   0          5h48m  
    langsmith-ch-migrations-gasvk            0/1     Completed   0          5h48m  
    langsmith-clickhouse-0                   1/1     Running     0          26h  
    langsmith-frontend-84687d9d45-6cg4r      1/1     Running     0          15h  
    langsmith-hub-backend-66ffb75fb4-qg6kl   1/1     Running     0          15h  
    langsmith-playground-85b444d8f7-pl589    1/1     Running     0          15h  
    langsmith-queue-d58cb64f7-87d68          1/1     Running     0          15h  
    

### Validate your deployment:​

  1. Run `kubectl get services`

Output should look something like:

    
    
    NAME                         TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)                      AGE  
    kubernetes                   ClusterIP      172.20.0.1       <none>          443/TCP                      27d  
    langsmith-backend            ClusterIP      172.20.22.34     <none>          1984/TCP                     21d  
    langsmith-clickhouse         ClusterIP      172.20.117.62    <none>          8123/TCP,9000/TCP            21d  
    langsmith-frontend           LoadBalancer   172.20.218.30    <external ip>   80:30093/TCP,443:31130/TCP   21d  
    langsmith-platform-backend   ClusterIP      172.20.232.183   <none>          1986/TCP                     21d  
    langsmith-playground         ClusterIP      172.20.167.132   <none>          3001/TCP                     21d  
    langsmith-postgres           ClusterIP      172.20.59.63     <none>          5432/TCP                     21d  
    langsmith-redis              ClusterIP      172.20.229.98    <none>          6379/TCP                     20d  
    

  2. Curl the external ip of the `langsmith-frontend` service:
         
         curl <external ip>/api/info  
         {"version":"0.5.7","license_expiration_time":"2033-05-20T20:08:06","batch_ingest_config":{"scale_up_qsize_trigger":1000,"scale_up_nthreads_limit":16,"scale_down_nempty_trigger":4,"size_limit":100,"size_limit_bytes":20971520}}  
         

Check that the version matches the version you upgraded to.

  3. Visit the external ip for the `langsmith-frontend` service on your browser

The Langsmith UI should be visible/operational

![.langsmith_ui.png](/assets/images/langsmith_ui-a308960b13a121598b5c577e7587adfe.png)

## Docker​

Upgrading the Docker version of LangSmith is a bit more involved than the Helm version and may require a small amount of downtime. Please follow the instructions below to upgrade your Docker version of LangSmith.

  1. Update your `docker-compose.yml` file to the file used in the latest release. You can find this in the [LangSmith SDK GitHub repository](https://github.com/langchain-ai/langsmith-sdk/blob/main/python/langsmith/cli/docker-compose.yaml)
  2. Update your `.env` file with any new environment variables that are required in the new version. These will be detailed in the release notes for the new version.
  3. Run the following command to stop your current LangSmith instance:

    
    
    docker-compose down  
    

  4. Run the following command to start your new LangSmith instance in the background:

    
    
    docker-compose up -d  
    

If everything ran successfully, you should see all the LangSmith containers running and healthy.
    
    
    CONTAINER ID   IMAGE                                  COMMAND                  CREATED        STATUS                        PORTS                                                      NAMES  
    e1c8f01a4ffc   langchain/langsmith-frontend:0.5.7     "/entrypoint.sh ngin…"   10 hours ago   Up 40 seconds                 0.0.0.0:80->80/tcp, 8080/tcp                               cli-langchain-frontend-1  
    39e1394846b9   langchain/langsmith-backend:0.5.7      "/bin/sh -c 'exec uv…"   10 hours ago   Up 40 seconds                 0.0.0.0:1984->1984/tcp                                     cli-langchain-backend-1  
    f8688dd58f2f   langchain/langsmith-go-backend:0.5.7   "./smith-go"             10 hours ago   Up 40 seconds                 0.0.0.0:1986->1986/tcp                                     cli-langchain-platform-backend-1  
    006f1303b04d   langchain/langsmith-backend:0.5.7      "saq app.workers.que…"   10 hours ago   Up 40 seconds                                                                            cli-langchain-queue-1  
    73a90242ed3a   redis:7                                "docker-entrypoint.s…"   10 hours ago   Up About a minute (healthy)   0.0.0.0:63791->6379/tcp                                    cli-langchain-redis-1  
    eecf75ca672b   postgres:14.7                          "docker-entrypoint.s…"   10 hours ago   Up About a minute (healthy)   0.0.0.0:5433->5432/tcp                                     cli-langchain-db-1  
    3aa5652a864d   clickhouse/clickhouse-server:23.9      "/entrypoint.sh"         10 hours ago   Up About a minute (healthy)   9009/tcp, 0.0.0.0:8124->8123/tcp, 0.0.0.0:9001->9000/tcp   cli-langchain-clickhouse-1  
    84edc329a37f   langchain/langsmith-playground:0.5.7   "docker-entrypoint.s…"   10 hours ago   Up About a minute             0.0.0.0:3001->3001/tcp                                     cli-langchain-playground-1  
    

### Validate your deployment:​

  1. Curl the exposed port of the `cli-langchain-frontend-1` container:
         
         curl localhost:80/info  
         {"version":"0.5.7","license_expiration_time":"2033-05-20T20:08:06","batch_ingest_config":{"scale_up_qsize_trigger":1000,"scale_up_nthreads_limit":16,"scale_down_nempty_trigger":4,"size_limit":100,"size_limit_bytes":20971520}}  
         

1 . Visit the exposed port of the `cli-langchain-frontend-1` container on your browser

The Langsmith UI should be visible/operational

![.langsmith_ui.png](/assets/images/langsmith_ui-a308960b13a121598b5c577e7587adfe.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Kubernetes(Helm)
    * Validate your deployment:
  * Docker
    * Validate your deployment:

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)