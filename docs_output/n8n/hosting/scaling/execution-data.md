# Execution data | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/scaling/execution-data.md "Edit this page")

# Execution data#

Depending on your executions settings and volume, your n8n database can grow in size and run out of storage.

To avoid this, n8n recommends that you don't save unnecessary data, and enable pruning of old executions data.

To do this, configure the corresponding [environment variables](../../configuration/environment-variables/executions/).

## Reduce saved data#

Configuration at workflow level

You can also configure these settings on an individual workflow basis using the [workflow settings](../../../workflows/settings/).

You can select which executions data n8n saves. For example, you can save only executions that result in an `Error`.
    
    
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
    11
    12

| 
    
    
    # npm
    # Save executions ending in errors
    export EXECUTIONS_DATA_SAVE_ON_ERROR=all
    
    # Save successful executions
    export EXECUTIONS_DATA_SAVE_ON_SUCCESS=all
    
    # Don't save node progress for each execution
    export EXECUTIONS_DATA_SAVE_ON_PROGRESS=false
    
    # Don't save manually launched executions
    export EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false
      
  
---|---  
      
    
    1
    2
    3
    4
    5
    6
    7
    8
    9

| 
    
    
    # Docker
    docker run -it --rm \
     --name n8n \
     -p 5678:5678 \
     -e EXECUTIONS_DATA_SAVE_ON_ERROR=all \
     -e EXECUTIONS_DATA_SAVE_ON_SUCCESS=none \
     -e EXECUTIONS_DATA_SAVE_ON_PROGRESS=true \
     -e EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false \
     docker.n8n.io/n8nio/n8n
      
  
---|---  
      
    
    1
    2
    3
    4
    5
    6
    7

| 
    
    
    # Docker Compose
    n8n:
        environment:
          - EXECUTIONS_DATA_SAVE_ON_ERROR=all
          - EXECUTIONS_DATA_SAVE_ON_SUCCESS=none
          - EXECUTIONS_DATA_SAVE_ON_PROGRESS=true
          - EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false
      
  
---|---  
  
## Enable data pruning#

You can enable data pruning to automatically delete finished executions after a given time. If you don't set `EXECUTIONS_DATA_MAX_AGE`, 336 hours (14 days) is the default.

You can choose to prune finished executions data before the time set in `EXECUTIONS_DATA_MAX_AGE`, using `EXECUTIONS_DATA_PRUNE_MAX_COUNT`. This sets a maximum number of executions to store in the database. Once you reach the limit, n8n starts to delete the oldest execution records. This can help with database performance issues, especially if you use SQLite. The database size can still exceed the limit you set: old executions that haven't finished running don't get deleted, even if they would otherwise be subject to deletion.
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9

| 
    
    
    # npm
    # Activate automatic data pruning
    export EXECUTIONS_DATA_PRUNE=true
    
    # Number of hours after execution that n8n deletes data
    export EXECUTIONS_DATA_MAX_AGE=168
    
    # Number of executions to store
    export EXECUTIONS_DATA_PRUNE_MAX_COUNT=50000
      
  
---|---  
      
    
    1
    2
    3
    4
    5
    6
    7

| 
    
    
    # Docker
    docker run -it --rm \
     --name n8n \
     -p 5678:5678 \
     -e EXECUTIONS_DATA_PRUNE=true \
     -e EXECUTIONS_DATA_MAX_AGE=168 \
     docker.n8n.io/n8nio/n8n
      
  
---|---  
      
    
    1
    2
    3
    4
    5
    6

| 
    
    
    # Docker Compose
    n8n:
        environment:
          - EXECUTIONS_DATA_PRUNE=true
          - EXECUTIONS_DATA_MAX_AGE=168
    	  	- EXECUTIONS_DATA_PRUNE_MAX_COUNT=50000
      
  
---|---  
  
SQLite

If you run n8n using the default SQLite database, the disk space of any pruned data isn't automatically freed up but rather reused for future executions data. To free up this space configure the `DB_SQLITE_VACUUM_ON_STARTUP` [environment variable](../../configuration/environment-variables/database/#sqlite) or manually run the [VACUUM](https://www.sqlite.org/lang_vacuum.html) operation.

Binary data pruning

Binary data pruning operates on the active binary data mode. For example, if your instance stored data in S3, and you later switched to filesystem mode, n8n only prunes binary data in the filesystem. This may change in future.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top