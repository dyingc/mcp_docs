# Running Support Queries against Clickhouse | 🦜️🛠️ LangSmith

On this page

This Helm repository contains queries to produce output that the LangSmith UI does not currently support directly (e.g. obtaining query exception logs from Clickhouse).

This command takes a clickhouse connection string that contains an embedded name and password (which can be passed in from a call to a secrets manager) and executes a query from an input file. In the example below, we are using the `ch_get_query_exceptions.sql` input file in the `support_queries/clickhouse` directory.

### Prerequisites​

Ensure you have the following tools/items ready.

  1. kubectl

     * <https://kubernetes.io/docs/tasks/tools/>
  2. Clickhouse database credentials

     * Host
     * Port
     * Username
       * If using the bundled version, this is `default`
     * Password
       * If using the bundled version, this is `password`
     * Database name
       * If using the bundled version, this is `default`
  3. Connectivity to the Clickhouse database from the machine you will be running the migration script on.

     * If you are using the bundled version, you may need to port forward the clickhouse service to your local machine.
     * Run `kubectl port-forward svc/langsmith-clickhouse 8123:8123` to port forward the clickhouse service to your local machine.
  4. The script to run a support query

     * You can download the script from [here](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/scripts/run_support_query_ch.sh)

### Running the query script​

Run the following command to run the desired query:
    
    
    sh run_support_query_ch.sh <clickhouse_url> --input path/to/query.sql  
    

For example, if you are using the bundled version with port-forwarding, the command might look like:
    
    
    sh run_support_query_ch.sh "clickhouse://default:password@localhost:8123/default" --input support_queries/clickhouse/ch_get_query_exceptions.sql  
    

which will output query logs for all queries that have thrown exceptions in Clickhouse in the last 7 days. To extract this to a file add the flag `--output path/to/file.csv`

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Prerequisites
  * Running the query script

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)