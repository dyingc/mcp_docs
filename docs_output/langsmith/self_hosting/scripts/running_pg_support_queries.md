# Running Support Queries against Postgres | 🦜️🛠️ LangSmith

On this page

This Helm repository contains queries to produce output that the LangSmith UI does not currently support directly (e.g. obtaining trace counts for multiple organizations in a single query).

This command takes a postgres connection string that contains an embedded name and password (which can be passed in from a call to a secrets manager) and executes a query from an input file. In the example below, we are using the `pg_get_trace_counts_daily.sql` input file in the `support_queries/postgres` directory.

### Prerequisites​

Ensure you have the following tools/items ready.

  1. kubectl

     * <https://kubernetes.io/docs/tasks/tools/>
  2. PostgreSQL client

     * <https://www.postgresql.org/download/>
  3. PostgreSQL database connection:

     * Host
     * Port
     * Username
       * If using the bundled version, this is `postgres`
     * Password
       * If using the bundled version, this is `postgres`
     * Database name
       * If using the bundled version, this is `postgres`
  4. Connectivity to the PostgreSQL database from the machine you will be running the migration script on.

     * If you are using the bundled version, you may need to port forward the postgresql service to your local machine.
     * Run `kubectl port-forward svc/langsmith-postgres 5432:5432` to port forward the postgresql service to your local machine.
  5. The script to run a support query

     * You can download the script from [here](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/scripts/run_support_query_pg.sh)

### Running the query script​

Run the following command to run the desired query:
    
    
    sh run_support_query_pg.sh <postgres_url> --input path/to/query.sql  
    

For example, if you are using the bundled version with port-forwarding, the command might look like:
    
    
    sh run_support_query_pg.sh "postgres://postgres:postgres@localhost:5432/postgres" --input support_queries/pg_get_trace_counts_daily.sql  
    

which will output the count of daily traces by workspace ID and organization ID. To extract this to a file add the flag `--output path/to/file.csv`

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Prerequisites
  * Running the query script

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)