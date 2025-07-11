# Queue mode environment variables | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/environment-variables/queue-mode.md "Edit this page")

# Queue mode environment variables#

File-based configuration

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](../../configuration-methods/#keeping-sensitive-data-in-separate-files) for more details.

You can run n8n in different modes depending on your needs. Queue mode provides the best scalability. Refer to [Queue mode](../../../scaling/queue-mode/) for more information.

Variable | Type | Default | Description  
---|---|---|---  
`QUEUE_BULL_PREFIX` | String | - | Prefix to use for all queue keys.  
`QUEUE_BULL_REDIS_DB` | Number | `0` | The Redis database used.  
`QUEUE_BULL_REDIS_HOST` | String | `localhost` | The Redis host.  
`QUEUE_BULL_REDIS_PORT` | Number | `6379` | The Redis port used.  
`QUEUE_BULL_REDIS_USERNAME` | String | - | The Redis username (needs Redis version 6 or above). Don't define it for Redis < 6 compatibility  
`QUEUE_BULL_REDIS_PASSWORD` | String | - | The Redis password.  
`QUEUE_BULL_REDIS_TIMEOUT_THRESHOLD` | Number | `10000` | The Redis timeout threshold (in ms).  
`QUEUE_BULL_REDIS_CLUSTER_NODES` | String | - | Expects a comma-separated list of Redis Cluster nodes in the format `host:port`, for the Redis client to initially connect to. If running in queue mode (`EXECUTIONS_MODE = queue`), setting this variable will create a Redis Cluster client instead of a Redis client, and n8n will ignore `QUEUE_BULL_REDIS_HOST` and `QUEUE_BULL_REDIS_PORT`.  
`QUEUE_BULL_REDIS_TLS` | Boolean | `false` | Enable TLS on Redis connections.  
`QUEUE_BULL_REDIS_DUALSTACK` | Boolean | `false` | Enable dual-stack support (IPv4 and IPv6) on Redis connections.  
`QUEUE_WORKER_TIMEOUT` (**deprecated**) | Number | `30` | **Deprecated** Use `N8N_GRACEFUL_SHUTDOWN_TIMEOUT` instead.  
  
How long should n8n wait (seconds) for running executions before exiting worker process on shutdown.  
`QUEUE_HEALTH_CHECK_ACTIVE` | Boolean | `false` | Whether to enable health checks (true) or disable (false).  
`QUEUE_HEALTH_CHECK_PORT` | Number | - | The port to serve health checks on.  
`QUEUE_WORKER_LOCK_DURATION` | Number | `30000` | How long (in ms) is the lease period for a worker to work on a message.  
`QUEUE_WORKER_LOCK_RENEW_TIME` | Number | `15000` | How frequently (in ms) should a worker renew the lease time.  
`QUEUE_WORKER_STALLED_INTERVAL` | Number | `30000` | How often should a worker check for stalled jobs (use 0 for never).  
`QUEUE_WORKER_MAX_STALLED_COUNT` | Number | `1` | Maximum amount of times a stalled job will be re-processed.  
  
## Multi-main setup#

Refer to [Configuring multi-main setup](../../../scaling/queue-mode/#configuring-multi-main-setup) for details.

Variable | Type | Default | Description  
---|---|---|---  
`N8N_MULTI_MAIN_SETUP_ENABLED` | Boolean | `false` | Whether to enable multi-main setup for queue mode (license required).  
`N8N_MULTI_MAIN_SETUP_KEY_TTL` | Number | `10` | Time to live (in seconds) for leader key in multi-main setup.  
`N8N_MULTI_MAIN_SETUP_CHECK_INTERVAL` | Number | `3` | Interval (in seconds) for leader check in multi-main setup.  
Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top