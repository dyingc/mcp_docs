# Deleting Traces | 🦜️🛠️ LangSmith

On this page

The LangSmith UI does not currently support the deletion of an individual trace. This, however, can be accomplished by directly removing the trace from all materialized views in ClickHouse (except the runs_history views) and the runs and feedback tables themselves.

This command can either be run using a trace ID as an argument or using a file that is a list of trace IDs.

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
  3. Connectivity to the Clickhouse database from the machine you will be running the `delete_trace_by_id` script on.

     * If you are using the bundled version, you may need to port forward the clickhouse service to your local machine.
     * Run `kubectl port-forward svc/langsmith-clickhouse 8123:8123` to port forward the clickhouse service to your local machine.
  4. The script to delete a trace

     * You can download the script from [here](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/scripts/delete_trace_by_id.sh)

### Running the deletion script for a single trace​

Run the following command to run the trace deletion script using a single trace ID:
    
    
    sh delete_trace_by_id.sh <clickhouse_url> --trace_id <trace_id>  
    

For example, if you are using the bundled version with port-forwarding, the command would look like:
    
    
    sh delete_trace_by_id.sh "clickhouse://default:password@localhost:8123/default" --trace_id 4ec70ec7-0808-416a-b836-7100aeec934b  
    

If you visit the Langsmith UI, you should now see specified trace ID is no longer present nor reflected in stats.

### Running the deletion script for a multiple traces from a file with one trace ID per line​

Run the following command to run the trace deletion script using a list of trace IDs:
    
    
    sh delete_trace_by_id.sh <clickhouse_url> --file <path/to/foo.txt>  
    

For example, if you are using the bundled version with port-forwarding, the command would look like:
    
    
    sh delete_trace_by_id.sh "clickhouse://default:password@localhost:8123/default" --file path/to/traces.txt  
    

If you visit the Langsmith UI, you should now see all the specified traces have been removed.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Prerequisites
  * Running the deletion script for a single trace
  * Running the deletion script for a multiple traces from a file with one trace ID per line

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)