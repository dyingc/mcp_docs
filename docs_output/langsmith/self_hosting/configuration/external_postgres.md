# Connect to an external Postgres database | 🦜️🛠️ LangSmith

On this page

LangSmith uses a Postgres database as the primary data store for transactional workloads and operational data (almost everything besides runs). By default, LangSmith Self-Hosted will use an internal Postgres database. However, you can configure LangSmith to use an external Postgres database (**strongly recommended in a production setting**). By configuring an external Postgres database, you can more easily manage backups, scaling, and other operational tasks for your database.

## Requirements​

  * A provisioned Postgres database that your LangSmith instance will have network access to. We recommend using a managed Postgres service like:
    * [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html)
    * [Google Cloud SQL](https://cloud.google.com/curated-resources/cloud-sql#section-1)
    * [Azure Database for PostgreSQL](https://azure.microsoft.com/en-us/products/postgresql#features)
  * Note: We only officially support Postgres versions >= 14.
  * A user with admin access to the Postgres database. This user will be used to create the necessary tables, indexes, and schemas.
  * This user will also need to have the ability to create extensions in the database. We use/will try to install the btree_gin, btree_gist, pgcrypto, citext, and pg_trgm extensions.
  * If using a schema other than public, ensure that you do not have any other schemas with the extensions enabled, or you must include that in your search path.
  * We do not currently support PGBouncer or other connection poolers. You must connect directly to the Postgres database.
  * By default, we recommend an instance with at least 2 vCPUs and 8GB of memory. However, the actual requirements will depend on your workload and the number of users you have. We recommend monitoring your Postgres instance and scaling up as needed.

## Connection String​

You will need to provide a connection string to your Postgres database. This connection string should include the following information:

  * Host
  * Port
  * Database
  * Username
  * Password(Make sure to url encode this if there are any special characters)
  * URL params

This will take the form of:
    
    
    username:password@host:port/database?<url_params>  
    

An example connection string might look like:
    
    
    myuser:mypassword@myhost:5432/mydatabase?sslmode=disable  
    

Without url parameters, the connection string would look like:
    
    
    myuser:mypassword@myhost:5432/mydatabase  
    

## Configuration​

With your connection string in hand, you can configure your LangSmith instance to use an external Postgres database. You can do this by modifying the `values` file for your LangSmith Helm Chart installation or the `.env` file for your Docker installation.

  * Helm
  * Docker

    
    
      
    postgres:  
      external:  
        enabled: true  
        connectionUrl: "Your connection url"  
    
    
    
    # In your .env file  
    POSTGRES_DATABASE_URI="Your connection url"  
    

Once configured, you should be able to reinstall your LangSmith instance. If everything is configured correctly, your LangSmith instance should now be using your external Postgres database.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Requirements
  * Connection String
  * Configuration

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)