# Configuring LangSmith for scale | 🦜️🛠️ LangSmith

On this page

A self-hosted LangSmith instance can handle a large number of traces. The default configuration for the deployment can handle substantial load, and you can configure your deployment to be able to achieve higher scale.

The table below contains high level guidance for LangSmith configurations, wheres cale is measured in terms of traces per second (TPS). The configuration recommendations also assume that you are using a relatively new version of the SDK and LangSmith (at least `0.10.69`). It is strongly recommended to run high load against a Kubernetes deployment of LangSmith.

Desired traces per second (TPS)| Queue pod replicas| Frontend replicas| Platform backend replicas| ClickHouse config| Redis cache size  
---|---|---|---|---|---  
**10 TPS**|  3 (default)| 1 (default)| 3 (default)| 4 vCPUs, 16 GB Memory (default)| 2 GB (default)  
**100 TPS**| **10**| **2**|  3 (default)| 4 vCPUs, 16 GB Memory (default)| **13+ GB**  
**1000 TPS**| **170**| **4**| **20**| **10 vCPUs, 48 GB Memory**| **200+ GB**  
  
note

Your exact usage pattern of the product may require more tuning of resources. If that is the case, please reach out to the LangSmith team for any questions.

## 10 Traces Per Second (TPS)​

The [default LangSmith configuration](/self_hosting/installation/kubernetes#prerequisites) can handle 10 TPS.

## 100 TPS​

To achieve 100 TPS, update your configuration as follows:

  * A Redis cache of at least 13 GB with a 1 hour TTL
  * 10 queue pod replicas
  * Increasing the ClickHouse PVC to store the traces
  * 2 frontend pods, which act as a reverse proxy for inbound requests
  * Blob storage enabled

Scaling up to this level will require roughly 24 vCPUs and 64 GB of memory for the pods in your Kubernetes cluster.

Below is an example `values.yaml` snippet for this configuration:
    
    
    config:  
      blobStorage:  
        ## Please also set the other keys to connect to your blob storage. See configuration section.  
        enabled: true  
      settings:  
        redisRunsExpirySeconds: "3600"  
      
    frontend:  
      deployment:  
        replicas: 2  
      
    queue:  
      deployment:  
        replicas: 10  
      
    redis:  
      statefulSet:  
        resources:  
          requests:  
            memory: 13Gi  
          limits:  
            memory: 13Gi  
      
      # -- For external redis instead use something like below --  
      # external:  
      #   enabled: true  
      #   connectionUrl: "<URL>" OR existingSecretName: "<SECRET-NAME>"  
      
    clickhouse:  
      statefulSet:  
        persistence:  
          # This may depend on your configured TTL.  
          # We recommend 60Gi for every shortlived TTL day if operating at this scale constantly.  
          size: 420Gi # This assumes 7 days TTL and operating a this scale constantly.  
    

note

Having an external Redis cache is recommended. You will need to ensure your Redis cache is configured with at least 13 GB instead of the resource configuration in the values file shown above.

## 1000 TPS​

To achieve 1000 TPS on a self-hosted Kubernetes LangSmith deployment, update your configuration as follows:

  * An external Redis cache of at least 200 GB with a 1 hour TTL
  * 10 vCPU and 48 GB of memory on your ClickHouse instance
  * 170 queue pods
  * 20 platform-backend pods
  * 4 frontend pods, which act as a reverse proxy for inbound requests
  * Blob storage enabled

Scaling up to this level will require roughly 220 vCPUs and 350 GB of memory for the pods in your Kubernetes cluster.

Below is a `values.yaml` snippet configuring the recommendations above:
    
    
    frontend:  
      deployment:  
        replicas: 4 # OR enable autoscaling to this level (example below)  
    # autoscaling:  
    #   enabled: true  
    #   maxReplicas: 4  
    #   minReplicas: 2  
      
    platformBackend:  
      deployment:  
        replicas: 20 # OR enable autoscaling to this level (example below)  
        resources:  
          requests:  
            cpu: "1600m"  
    # autoscaling:  
    #   enabled: true  
    #   maxReplicas: 20  
    #   minReplicas: 8  
      
    ## Note that we are actively working on improving performance of this service to reduce the number of replicas.  
    queue:  
      deployment:  
        replicas: 170 # OR enable autoscaling to this level (example below)  
        resources:  
          requests:  
            memory: "1.5Gi"  
    # autoscaling:  
    #   enabled: true  
    #   maxReplicas: 170  
    #   minReplicas: 40  
      
    ## Ensure your Redis cache is at least 200 GB  
    redis:  
      external:  
        enabled: true  
        existingSecretName: langsmith-redis-secret # Set the connection url for your external Redis instance (200+ GB)  
      
    clickhouse:  
      statefulSet:  
        persistence:  
          # This may depend on your configured TTL (see config section).  
          # We recommend 600Gi for every shortlived TTL day if operating at this scale constantly.  
          size: 4200Gi # This assumes 7 days TTL and operating a this scale constantly.  
        resources:  
          requests:  
            cpu: "10"  
            memory: "48Gi"  
          limits:  
            cpu: "16"  
            memory: "64Gi"  
      
    config:  
      blobStorage:  
        ## Please also set the other keys to connect to your blob storage. See configuration section.  
        enabled: true  
      settings:  
        redisRunsExpirySeconds: "3600"  
    # ttl:  
    #   enabled: true  
    #   ttl_period_seconds:  
    #     longlived: "7776000"  # 90 days  
    #     shortlived: "604800"  # 7 days  
      
    # These are important environment variables to set.  
    commonEnv:  
      - name: "CLICKHOUSE_ASYNC_INSERT_WAIT_PCT_FLOAT"  
        value: "0"  
    

important

Ensure that the Kubernetes cluster is configured with sufficent resources to scale to the recommended size. After deployment, all of the pods in the Kubernetes cluster should be in a `Running` state. Pods stuck in `Pending` may indicate that you are reaching node pool limits or need larger nodes.

Also, ensure that any ingress controller deployed on the cluster is able to handle the desired load to prevent bottlenecks.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * 10 Traces Per Second (TPS)
  * 100 TPS
  * 1000 TPS

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)