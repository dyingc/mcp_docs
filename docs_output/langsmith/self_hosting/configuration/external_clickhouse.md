# Connect to an external ClickHouse database | 🦜️🛠️ LangSmith

On this page

ClickHouse is a high-performance, column-oriented database system. It allows for fast ingestion of data and is optimized for analytical queries.

LangSmith uses ClickHouse as the primary data store for traces and feedback. By default, self-hosted LangSmith will use an internal ClickHouse database that is bundled with the LangSmith instance. This is run as a stateful set in the same Kubernetes cluster as the LangSmith application or as a Docker container on the same host as the LangSmith application.

However, you can configure LangSmith to use an external ClickHouse database for easier management and scaling. By configuring an external ClickHouse database, you can manage backups, scaling, and other operational tasks for your database. While Clickhouse is not yet a native service in Azure, AWS, or Google Cloud, you can run LangSmith with an external ClickHouse database in the following ways:

  * [LangSmith-managed ClickHouse](/self_hosting/langsmith_managed_clickhouse)
  * Provision a [ClickHouse Cloud](https://clickhouse.cloud/) either directly or through a cloud provider marketplace:
    * [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/clickhouse.clickhouse_cloud?tab=Overview)
    * [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/clickhouse-public/clickhouse-cloud)
    * [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-jettukeanwrfc)
  * On a VM in your cloud provider

note

Using the first two options (LangSmith-managed ClickHouse or ClickHouse Cloud) will provision a Clickhouse service OUTSIDE of your VPC. However, both options support private endpoints, meaning that you can direct traffic to the ClickHouse service without exposing it to the public internet (eg via AWS PrivateLink, or GCP Private Service Connect).

Additionally, sensitive information can be configured to be not stored in Clickhouse. Please reach out to [support@langchain.dev](mailto:support@langchain.dev) for more information.

## Requirements​

  * A provisioned ClickHouse instance that your LangSmith application will have network access to (see above for options).
  * A user with admin access to the ClickHouse database. This user will be used to create the necessary tables, indexes, and views.
  * We support both standalone ClickHouse and externally managed clustered deployments. For clustered deployments, ensure all nodes are running the same version. Note that clustered setups are not supported with bundled ClickHouse installations.
  * We only support ClickHouse versions >= 23.9. Use of ClickHouse versions >= 24.2 requires LangSmith v0.6 or later. See the [LangSmith release notes](/self_hosting/release_notes) for more information.
  * We rely on a few configuration parameters to be set on your ClickHouse instance. These are detailed below:

    
    
    <profiles>  
      <default>  
          <async_insert>1</async_insert> # Turn on async insert  
          <async_insert_max_data_size>25000000</async_insert_max_data_size> # Flush data to disk after 25MB. You may need to adjust this based on your workload.  
          <wait_for_async_insert>0</wait_for_async_insert> # Disable waiting for async insert by default  
          <parallel_view_processing>1</parallel_view_processing> # Enable parallel view processing  
          <materialize_ttl_after_modify>0</materialize_ttl_after_modify> # Disable TTL materialization after modify  
          <wait_for_async_insert_timeout>120</wait_for_async_insert_timeout> # Set the timeout for waiting for async insert  
          <lightweight_deletes_sync>0</lightweight_deletes_sync> # Disable lightweight deletes sync  
      </default>  
    </profiles>  
    

Configuration parameters

Our system has been tuned to work with the above configuration parameters. Changing these parameters may result in unexpected behavior.

## HA Replicated Clickhouse Cluster​

warning

By default, the setup process above will only work with a single node Clickhouse cluster.

If you would like to use a multi-node Clickhouse cluster for HA, we support this with additional required configuration. This setup can use a Clickhouse cluster with multiple nodes where data replicated via Zookeeper or Clickhouse Keeper. For more information on Clickhouse replication, see [Clickhouse Data Replication Docs](https://clickhouse.com/docs/architecture/replication).

In order to setup LangSmith with a replicated multi-node Clickhouse setup:

  * You need to have a Clickhouse cluster that is setup with Keeper or Zookeeper for data replication and the appropriate settings. See [Clickhouse Replication Setup Docs](https://clickhouse.com/docs/architecture/replication).
  * You need to set the cluster setting in the LangSmith Configuration section, specifically the `cluster` settings to match your Clickhouse Cluster name. This will use the `Replicated` table engines when running the Clickhouse migrations.
  * If in addition to HA, you would like to load balance among the Clickhouse nodes (to distribute reads or writes), we suggest using a load balancer or DNS load balancing to round robin among your Clickhouse servers.
  * **Note** : You will need to enable your `cluster` setting before launching LangSmith for the first time and running the Clickhouse migrations. This is a requirement since the table engine will need to be created as a `Replicated` table engine vs the non replicated engine type.

When running migrations with `cluster` enabled, the migration will create the `Replicated` table engine flavor. This means that data will be replicated among the servers in the cluster. This is a master-master setup where any server can process reads, writes, or merges.

## LangSmith-managed ClickHouse​

  * If using LangSmith-managed ClickHouse, you will need to set up a VPC peering connection between the LangSmith VPC and the ClickHouse VPC. Please reach out to [support@langchain.dev](mailto:support@langchain.dev) for more information.
  * You will also need to set up Blob Storage. You can read more about Blob Storage in the [Blob Storage documentation](/self_hosting/configuration/blob_storage).

note

ClickHouse installations managed by LangSmith use a SharedMerge engine, which automatically clusters them and separates compute from storage.

## Parameters​

You will need to provide several parameters to your LangSmith installation to configure an external ClickHouse database. These parameters include:

  * Host: The hostname or IP address of the ClickHouse database
  * HTTP Port: The port that the ClickHouse database listens on for HTTP connections
  * Native Port: The port that the ClickHouse database listens on for [native connections](https://clickhouse.com/docs/en/interfaces/tcp)
  * Database: The name of the ClickHouse database that LangSmith should use
  * Username: The username to use to connect to the ClickHouse database
  * Password: The password to use to connect to the ClickHouse database
  * Cluster (Optional): The name of the ClickHouse cluster if using an external Clickhouse cluster. When set, LangSmith will run migrations on the cluster and replicate data across instances.

warning

Important considerations for clustered deployments:

  * Clustered setups must be configured on a fresh schema - existing standalone ClickHouse instances cannot be converted to clustered mode.
  * Clustering is only supported with externally managed ClickHouse deployments. It is not compatible with bundled ClickHouse installations as these do not include required ZooKeeper configurations.
  * When using a clustered deployment, LangSmith will automatically:
    * Run database migrations across all nodes in the cluster
    * Configure tables for data replication across the cluster

Note that while data is replicated across nodes, LangSmith does not configure distributed tables or handle query routing - queries will be directed to the specified host. You will need to handle any load balancing or query distribution at the infrastructure level if desired.

## Configuration​

With these parameters in hand, you can configure your LangSmith instance to use the provisioned ClickHouse database. You can do this by modifying the `config.yaml` file for your LangSmith Helm Chart installation or the `.env` file for your Docker installation.

  * Helm
  * Docker

    
    
      
    clickhouse:  
      external:  
        enabled: true  
        host: "host"  
        port: "http port"  
        nativePort: "native port"  
        user: "default"  
        password: "password"  
        database: "default"  
        tls: false  
        cluster: "my_cluster_name"  # Optional: Set this if using an external Clickhouse cluster  
    
    
    
    # In your .env file  
    CLICKHOUSE_HOST=langchain-clickhouse # Change to your Clickhouse host if using external Clickhouse. Otherwise, leave it as is  
    CLICKHOUSE_USER=default # Change to your Clickhouse user if needed  
    CLICKHOUSE_DB=default # Change to your Clickhouse database if needed  
    CLICKHOUSE_PORT=8123 # Change to your Clickhouse port if needed  
    CLICKHOUSE_TLS=false # Change to true if you are using TLS to connect to Clickhouse. Otherwise, leave it as is  
    CLICKHOUSE_PASSWORD=password # Change to your Clickhouse password if needed  
    CLICKHOUSE_NATIVE_PORT=9000 # Change to your Clickhouse native port if needed  
    CLICKHOUSE_CLUSTER=my_cluster_name # Optional: Set this if using an external Clickhouse cluster  
    

Once configured, you should be able to reinstall your LangSmith instance. If everything is configured correctly, your LangSmith instance should now be using your external ClickHouse database.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Requirements
  * HA Replicated Clickhouse Cluster
  * LangSmith-managed ClickHouse
  * Parameters
  * Configuration

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)