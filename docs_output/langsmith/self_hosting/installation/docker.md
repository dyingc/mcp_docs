# Self-hosting LangSmith with Docker | 🦜️🛠️ LangSmith

On this page

Enterprise License Required

Self-hosting LangSmith is an add-on to the Enterprise Plan designed for our largest, most security-conscious customers. See our [pricing page](https://www.langchain.com/pricing) for more detail, and contact us at [sales@langchain.dev](mailto:sales@langchain.dev) if you want to get a license key to trial LangSmith in your environment.

This guide provides instructions for installing and setting up your environment to run LangSmith locally using Docker. You can do this either by using the LangSmith SDK or by using Docker Compose directly.

## Prerequisites​

  1. Ensure Docker is installed and running on your system. You can verify this by running:
         
         docker info  
         

If you don't see any server information in the output, make sure Docker is installed correctly and launch the Docker daemon.
     1. Recommended: At least 4 vCPUs, 16GB Memory available on your machine.
        * You may need to tune resource requests/limits for all of our different services based off of organization size/usage
     2. Disk Space: LangSmith can potentially require a lot of disk space. Ensure you have enough disk space available.
  2. LangSmith License Key
     1. You can get this from your Langchain representative. Contact us at [sales@langchain.dev](mailto:sales@langchain.dev) for more information.
  3. Api Key Salt
     1. This is a secret key that you can generate. It should be a random string of characters.
     2. You can generate this using the following command:
    
    openssl rand -base64 32  
    

  4. Egress to `https://beacon.langchain.com` (if not running in offline mode)
     1. LangSmith requires egress to `https://beacon.langchain.com` for license verification and usage reporting. This is required for LangSmith to function properly. You can find more information on egress requirements in the [Egress](/self_hosting/egress) section.
  5. Configuration
     1. There are several configuration options that you can set in the `.env` file. You can find more information on the available configuration options in the [Configuration](/self_hosting/configuration) section.

## Running via Docker Compose​

The following explains how to run the LangSmith using Docker Compose. This is the most flexible way to run LangSmith without Kubernetes. The default configuration for Docker Compose is intended for local testing only and not for instances where any services are exposed to the public internet. **In production, we highly recommend using a secured Kubernetes environment.**

### 1\. Fetch the LangSmith `docker-compose.yml` file​

You can find the `docker-compose.yml` file and related files in the LangSmith SDK repository here: [_LangSmith Docker Compose File_](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/docker-compose/docker-compose.yaml)

Copy the `docker-compose.yml` file and all files in that directory from the LangSmith SDK to your project directory.

  * Ensure that you copy the `users.xml` file as well.

### 2\. Configure environment variables​

  1. Copy the `.env.example` file from the LangSmith SDK to your project directory and rename it to `.env`.
  2. Configure the appropriate values in the `.env` file. You can find the available configuration options in the [Configuration](/self_hosting/configuration) section.

You can also set these environment variables in the `docker-compose.yml` file directly or export them in your terminal. We recommend setting them in the `.env` file.

### 2\. Start server​

Start the LangSmith application by executing the following command in your terminal:
    
    
    docker-compose up  
    

You can also run the server in the background by running:
    
    
    docker-compose up -d  
    

### Validate your deployment:​

  1. Curl the exposed port of the `cli-langchain-frontend-1` container:
         
         curl localhost:1980/info  
         {"version":"0.5.7","license_expiration_time":"2033-05-20T20:08:06","batch_ingest_config":{"scale_up_qsize_trigger":1000,"scale_up_nthreads_limit":16,"scale_down_nempty_trigger":4,"size_limit":100,"size_limit_bytes":20971520}}  
         

  2. Visit the exposed port of the `cli-langchain-frontend-1` container on your browser

The Langsmith UI should be visible/operational at `http://localhost:1980`

![.langsmith_ui.png](/assets/images/langsmith_ui-a308960b13a121598b5c577e7587adfe.png)

### Checking the logs​

If, at any point, you want to check if the server is running and see the logs, run
    
    
    docker-compose logs  
    

### Stopping the server​
    
    
    docker-compose down  
    

## Using LangSmith​

Now that LangSmith is running, you can start using it to trace your code. You can find more information on how to use self-hosted LangSmith in the [self-hosted usage guide](/self_hosting/usage).

Your LangSmith instance is now running but may not be fully setup yet.

If you used one of the basic configs, you may have deployed a no-auth configuration. In this state, there is no authentication or concept of user accounts nor API keys and traces can be submitted directly without an API key so long as the hostname is passed to the LangChain tracer/LangSmith SDK.

As a next step, it is strongly recommended you work with your infrastructure administrators to:

  * Setup DNS for your LangSmith instance to enable easier access
  * Configure SSL to ensure in-transit encryption of traces submitted to LangSmith
  * Configure LangSmith for [oauth authentication](/self_hosting/configuration/sso) or [basic authentication](/self_hosting/configuration/basic_auth) to secure your LangSmith instance
  * Secure access to your Docker environment to limit access to only the LangSmith frontend and API
  * Connect LangSmith to secured Postgres and Redis instances

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Prerequisites
  * Running via Docker Compose
    * 1\. Fetch the LangSmith `docker-compose.yml` file
    * 2\. Configure environment variables
    * 2\. Start server
    * Validate your deployment:
    * Checking the logs
    * Stopping the server
  * Using LangSmith

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)