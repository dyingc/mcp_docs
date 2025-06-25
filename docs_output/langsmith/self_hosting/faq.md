# Frequently Asked Questions: | 🦜️🛠️ LangSmith

On this page

### _I can't create API keys or manage users in the UI, what's wrong?_​

  * You have likely deployed LangSmith without setting up SSO. LangSmith requires SSO to manage users and API keys. You can find more information on setting up SSO in the [configuration section.](/self_hosting/configuration/sso)

### _How does load balancing/ingress work_?​

  * You will need to expose the frontend container/service to your applications/users. This will handle routing to all downstream services.
  * You will need to terminate SSL at the ingress level. We recommend using a managed service like AWS ALB, GCP Load Balancer, or Nginx.

### _How can we authenticate to the application?_​

  * Currently, our self-hosted solution supports SSO with OAuth2.0 and OIDC as an authn solution. Note, we do offer a no-auth solution but highly recommend setting up oauth before moving into production.

You can find more information on setting up SSO in the [configuration section.](/self_hosting/configuration/sso)

### _Can I use external storage services?_​

  * You can configure LangSmith to use external versions of all storage services. In a production setting, we strongly recommend using external storage services. Check out the [configuration section](/self_hosting/configuration) for more information.

### _Does my application need egress to function properly?_​

Our deployment only needs egress for a few things (most of which can reside within your VPC):

  * Fetching images (If mirroring your images, this may not be needed)
  * Talking to any LLM endpoints
  * Talking to any external storage services you may have configured
  * Fetching OAuth information
  * Subscription Metrics and Operational Metadata (if not running in offline mode)
    * Requires egress to `https://beacon.langchain.com`
    * See [Egress](/self_hosting/egress) for more information

Your VPC can set up rules to limit any other access.  
Note: We require the `X-Organization-Id` and `X-Tenant-Id` headers to be allowed to be passed through to the backend service. These are used to determine which organization and workspace (previously called "tenant") the request is for.

### _Resource requirements for the application?_​

  * In kubernetes, we recommend a minimum helm configuration which can be found in [here](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/examples/medium_size.yaml). For docker, we recommend a minimum of 16GB of RAM and 4 CPUs.
  * For Postgres, we recommend a minimum of 8GB of RAM and 2 CPUs.
  * For Redis, we recommend 4GB of RAM and 2 CPUs.
  * For Clickhouse, we recommend 32GB of RAM and 8 CPUs.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * _I can't create API keys or manage users in the UI, what's wrong?_
  * _How does load balancing/ingress work_?
  * _How can we authenticate to the application?_
  * _Can I use external storage services?_
  * _Does my application need egress to function properly?_
  * _Resource requirements for the application?_

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)