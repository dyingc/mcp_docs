# Connect to an external Redis database | 🦜️🛠️ LangSmith

On this page

LangSmith uses Redis to back our queuing/caching operations. By default, LangSmith Self-Hosted will use an internal Redis instance. However, you can configure LangSmith to use an external Redis instance (**strongly recommended in a production setting**). By configuring an external Redis instance, you can more easily manage backups, scaling, and other operational tasks for your Redis instance.

## Requirements​

  * A provisioned Redis instance that your LangSmith instance will have network access to. We recommend using a managed Redis service like:
    * [Amazon ElastiCache](https://aws.amazon.com/elasticache/redis/)
    * [Google Cloud Memorystore](https://cloud.google.com/memorystore)
    * [Azure Cache for Redis](https://azure.microsoft.com/en-us/services/cache/)
  * Note: We only officially support Redis versions >= 5.
  * We do not support Redis Cluster.
  * By default, we recommend an instance with at least 2 vCPUs and 8GB of memory. However, the actual requirements will depend on your tracing workload. We recommend monitoring your Redis instance and scaling up as needed.

Redis Cluster Not Supported

Certain tiers of managed Redis services may use Redis Cluster under the hood, but you can point to a single node in the cluster. For example on Azure Cache for Redis, the `Premium` tier and above use Redis Cluster, so you will need to use a lower tier.

## Connection String​

We use `redis-py` to connect to Redis. This library supports a variety of connection strings. You can find more information on the connection string format [here](https://redis-py.readthedocs.io/en/stable/#redis.StrictRedis.from_url).

You will need to assemble the connection string for your Redis instance. This connection string should include the following information:

  * Host
  * Database
  * Port
  * URL params

This will take the form of:
    
    
    "redis://host:port/db?<url_params>"  
    

An example connection string might look like:
    
    
    "redis://langsmith-redis:6379/0"  
    

To use SSL, you can use the `rediss://` prefix. An example connection string with SSL might look like:
    
    
    "rediss://langsmith-redis:6380/0?password=foo"  
    

## Configuration​

With your connection string in hand, you can configure your LangSmith instance to use an external Redis instance. You can do this by modifying the `values` file for your LangSmith Helm Chart installation or the `.env` file for your Docker installation.

  * Helm
  * Docker

    
    
      
    redis:  
      external:  
        enabled: true  
        connectionUrl: "Your connection url"  
    
    
    
    # In your .env file  
    REDIS_DATABASE_URI="Your connection url"  
    

Once configured, you should be able to reinstall your LangSmith instance. If everything is configured correctly, your LangSmith instance should now be using your external Redis instance.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Requirements
  * Connection String
  * Configuration

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)