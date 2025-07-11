# Architectural overview | 🦜️🛠️ LangSmith

On this page

Enterprise License Required

Self-Hosted LangSmith is an add-on to the Enterprise Plan designed for our largest, most security-conscious customers. See our [pricing page](https://www.langchain.com/pricing) for more detail, and contact us at [sales@langchain.dev](mailto:sales@langchain.dev) if you want to get a license key to trial LangSmith in your environment.

LangSmith can be run via Kubernetes (recommended) or Docker in a Cloud environment that you control.

The LangSmith application consists of several components including 5 LangSmith servers and 3 stateful services:

  * LangSmith Frontend
  * LangSmith Backend
  * LangSmith Platform Backend
  * LangSmith Playground
  * LangSmith Queue
  * LangSmith ACE(Arbitrary Code Execution) Backend
  * ClickHouse
  * Postgres
  * Redis

![./static/self_hosted_architecture_diagram.png](/assets/images/self_hosted_architecture_diagram-fbad3c8ee6b44e73b0eb451e003bab1b.png)

To access the LangSmith UI and send API requests, you will need to expose the LangSmith Frontend service. Depending on your installation method, this can be a load balancer or a port exposed on the host machine.

## Storage Services​

note

LangSmith Self-Hosted will bundle all storage services by default. LangSmith can be configured to use external versions of all storage services. In a production setting, we **strongly recommend using external Storage Services**.

### ClickHouse​

[ClickHouse](https://clickhouse.com/docs/en/intro) is a high-performance, column-oriented SQL database management system (DBMS) for online analytical processing (OLAP).

LangSmith uses ClickHouse as the primary data store for traces and feedback (high-volume data).

### PostgreSQL​

[PostgreSQL](https://www.postgresql.org/about/) is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads

LangSmith uses Postgres as the primary data store for transactional workloads and operational data (almost everything besides traces and feedback).

### Redis​

[Redis](https://github.com/redis/redis) is a powerful in-memory key-value database that persists on disk. By holding data in memory, Redis offers high performance for operations like caching.

LangSmith uses Redis to back queuing/caching operations.

## Services​

### LangSmith Frontend​

The frontend uses Nginx to serve the LangSmith UI and route API requests to the other servers. This serves as the entrypoint for the application and is the only component that must be exposed to users.

### LangSmith Backend​

The backend is the primary entrypoint for API requests and handles the majority of the business logic for the application. This includes handling requests from the frontend and sdk, preparing traces for ingestion, and supporting the hub API.

### LangSmith Queue​

The queue handles incoming traces and feedback to ensure that they are ingested and persisted into the traces and feedback datastore asynchronously, handling checks for data integrity and ensuring successful insert into the datastore, handling retries in situations such as database errors or the temporary inability to connect to the database.

### LangSmith Platform Backend​

The platform backend is an internal service that primarily handles authentication and other high-volume tasks. The user should not need to interact with this service directly.

### LangSmith Playground​

The playground is a service that handles forwarding requests to various LLM APIs to support the LangSmith Playground feature. This can also be used to connect to your own custom model servers.

### LangSmith ACE(Arbitrary Code Execution) Backend​

The ACE backend is a service that handles executing arbitrary code in a secure environment. This is used to support running custom code within LangSmith.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Storage Services
    * ClickHouse
    * PostgreSQL
    * Redis
  * Services
    * LangSmith Frontend
    * LangSmith Backend
    * LangSmith Queue
    * LangSmith Platform Backend
    * LangSmith Playground
    * LangSmith ACE(Arbitrary Code Execution) Backend

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)