# Self-hosting LangSmith on Kubernetes | 🦜️🛠️ LangSmith

On this page

Enterprise License Required

Self-hosting LangSmith is an add-on to the Enterprise Plan designed for our largest, most security-conscious customers. See our [pricing page](https://www.langchain.com/pricing) for more detail, and contact us at [sales@langchain.dev](mailto:sales@langchain.dev) if you want to get a license key to trial LangSmith in your environment.

This guide will walk you through the process of deploying LangSmith to a Kubernetes cluster. We will use Helm to install LangSmith and its dependencies.

We've successfully tested LangSmith on the following Kubernetes distributions:

  * Google Kubernetes Engine (GKE)
  * Amazon Elastic Kubernetes Service (EKS)
  * Azure Kubernetes Service (AKS)
  * OpenShift
  * Minikube and Kind (for development purposes)

Terraform modules

We will be releasing Terraform modules the help in the provisioning of resources for LangSmith. You can find those in our [public Terraform repo](https://github.com/langchain-ai/terraform). For example, you can find a LangSmith module for creating AWS resources in the `modules/aws/langsmith` folder within our public Terraform repo.

## Prerequisites​

Ensure you have the following tools/items ready. Some items are marked optional:

  1. A working Kubernetes cluster that you can access via `kubectl`. Your cluster should have the following minimum requirements:

     1. Recommended: At least 16 vCPUs, 64GB Memory available

        * You may need to tune resource requests/limits for all of our different services based off of organization size/usage
        * We recommend using a cluster autoscaler to handle scaling up/down of nodes based on resource usage
        * We recommend setting up the metrics server so that autoscaling can be turned on
        * You must have a node with at least 4 vCPUs and 16GB of memory **allocatable** as ClickHouse will request this amount of resources by default.
     2. Valid Dynamic PV provisioner or PVs available on your cluster.

        * We will be using a `PostgreSQL` database, `Redis` cache, and `ClickHouse` database for storing traces. These services require persistent storage.
        * Our base installation, which assumes no external databases, will try to install these services inside your cluster. To enable persistence, we will try to provision volumes for these services.
        * If using PVs in your cluster, we highly recommend setting up backups in a production environment.
        * **We strongly encourage using a storage class backed by SSDs for better performance. We recommend 7000 IOPS and 1000 MiB/s throughput.**
        * On EKS, you may need to ensure you have the `ebs-csi-driver` installed and configured for dynamic provisioning. Refer to the [EBS CSI Driver documentation](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html) for more information.

You can verify this by running:
    
    kubectl get storageclass  
    

The output should show at least one storage class with a provisioner that supports dynamic provisioning. For example:
    
    NAME            PROVISIONER                 RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE  
      gp2 (default)   ebs.csi.eks.amazonaws.com   Delete          WaitForFirstConsumer   true                   161d  
    

note

We highly recommend using a storage class that supports volume expansion. This is because traces can potentially require a lot of disk space and your volumes may need to be resized over time.

Refer to the [Kubernetes documentation](https://kubernetes.io/docs/concepts/storage/storage-classes/) for more information on storage classes.

  2. Helm

     1. To install `helm` refer to the [Helm documentation](https://helm.sh/docs/intro/install/)
  3. LangSmith License Key

     1. You can get this from your Langchain representative. Contact us at [sales@langchain.dev](mailto:sales@langchain.dev) for more information.
  4. Api Key Salt

     1. This is a secret key that you can generate. It should be a random string of characters.
     2. You can generate this using the following command:
    
    openssl rand -base64 32  
    

  5. JWT Secret (Optional but used for basic auth)

     1. This is a secret key that you can generate. It should be a random string of characters.
     2. You can generate this using the following command:
    
    openssl rand -base64 32  
    

  6. Egress to `https://beacon.langchain.com` (if not running in offline mode)

     1. LangSmith requires egress to `https://beacon.langchain.com` for license verification and usage reporting. This is required for LangSmith to function properly. You can find more information on egress requirements in the [Egress](/self_hosting/egress) section.
  7. Configuration

     1. There are several configuration options that you can set in the `langsmith_config.yaml` file. You can find more information on specific configuration options in the [Configuration](/self_hosting/configuration) section.
     2. If you are new to Kubernetes or Helm, we’d recommend starting with one of the example configurations in the examples directory of the Helm Chart repository here: [LangSmith helm chart examples](https://github.com/langchain-ai/helm/tree/main/charts/langsmith/examples).
     3. You can see a full list of configuration options in the `values.yaml` file in the Helm Chart repository here: [LangSmith Helm Chart](https://github.com/langchain-ai/helm/tree/main/charts/langsmith/values.yaml)

## Configure your Helm Charts:​

  1. Create a new file called `langsmith_config.yaml` with the configuration options from the previous step.

  2. At a minimum, you will need to set the following configuration options (using basic auth):
         
         config:  
           langsmithLicenseKey: "<your license key>"  
           apiKeySalt: "<your api key salt>"  
           authType: mixed  
           basicAuth:  
             enabled: true  
             initialOrgAdminEmail: "admin@langchain.dev" # Change this to your admin email address  
             initialOrgAdminPassword: "secure-password" # Must be at least 12 characters long and have at least one lowercase, uppercase, and symbol  
             jwtSecret: <your jwt salt> # A random string of characters used to sign JWT tokens for basic auth.  
         

## Deploying to Kubernetes:​

  1. Verify that you can connect to your Kubernetes cluster(note: We highly suggest installing into an empty namespace)

     1. Run `kubectl get pods`

Output should look something like:
            
            kubectl get pods                                                                                                                                                                     ⎈ langsmith-eks-2vauP7wf 21:07:46  
            No resources found in default namespace.  
            

Namespace

If you are using a namespace other than the default namespace, you will need to specify the namespace in the `helm` and `kubectl` commands by using the `-n <namespace>` flag.

  2. Ensure you have the Langchain Helm repo added. (skip this step if you are using local charts)
         
         helm repo add langchain https://langchain-ai.github.io/helm/  
         "langchain" has been added to your repositories  
         

  3. Find the latest version of the chart. You can find the available versions in the [Helm Chart repository](https://github.com/langchain-ai/helm/releases).

     * We generally recommend using the latest version.
     * You can also run `helm search repo langchain/langsmith --versions` to see the available versions. The output will look something like this:
    
    langchain/langsmith     0.10.14         0.10.32         Helm chart to deploy the langsmith application ...  
    langchain/langsmith     0.10.13         0.10.32         Helm chart to deploy the langsmith application ...  
    langchain/langsmith     0.10.12         0.10.32         Helm chart to deploy the langsmith application ...  
    langchain/langsmith     0.10.11         0.10.29         Helm chart to deploy the langsmith application ...  
    langchain/langsmith     0.10.10         0.10.29         Helm chart to deploy the langsmith application ...  
    

  4. Run `helm install langsmith langchain/langsmith --values langsmith_config.yaml --version <version> -n <namespace> --debug`

     * Replace `<namespace>` with the namespace you want to deploy LangSmith to.
     * Replace `<version>` with the version of LangSmith you want to install from the previous step. Most users should install the latest version available.

Once the `helm install` command runs and finishes successfully, you should see output similar to this:
    
    NAME: langsmith  
    LAST DEPLOYED: Fri Sep 17 21:08:47 2021  
    NAMESPACE: langsmith  
    STATUS: deployed  
    REVISION: 1  
    TEST SUITE: None  
    

This may take a few minutes to complete as it will create several Kubernetes resources and run several jobs to initialize the database and other services.

  5. Run `kubectl get pods` Output should now look something like this (note the exact pod names may vary based on the version and configuration you used):
         
         langsmith-backend-6ff46c99c4-wz22d       1/1     Running   0          3h2m  
         langsmith-frontend-6bbb94c5df-8xrlr      1/1     Running   0          3h2m  
         langsmith-hub-backend-5cc68c888c-vppjj   1/1     Running   0          3h2m  
         langsmith-playground-6d95fd8dc6-x2d9b    1/1     Running   0          3h2m  
         langsmith-postgres-0                     1/1     Running   0          9h  
         langsmith-queue-5898b9d566-tv6q8         1/1     Running   0          3h2m  
         langsmith-redis-0                        1/1     Running   0          9h  
         

## Validate your deployment:​

  1. Run `kubectl get services`

Output should look something like:
         
         NAME                    TYPE           CLUSTER-IP       EXTERNAL-IP                                                               PORT(S)        AGE  
         langsmith-backend       ClusterIP      172.20.140.77    <none>                                                                    1984/TCP       35h  
         langsmith-frontend      LoadBalancer   172.20.253.251   <external ip>                                                             80:31591/TCP   35h  
         langsmith-hub-backend   ClusterIP      172.20.112.234   <none>                                                                    1985/TCP       35h  
         langsmith-playground    ClusterIP      172.20.153.194   <none>                                                                    3001/TCP       9h  
         langsmith-postgres      ClusterIP      172.20.244.82    <none>                                                                    5432/TCP       35h  
         langsmith-redis         ClusterIP      172.20.81.217    <none>                                                                    6379/TCP       35h  
         

  2. Curl the external ip of the `langsmith-frontend` service:
         
         curl <external ip>/api/tenants  
         [{"id":"00000000-0000-0000-0000-000000000000","has_waitlist_access":true,"created_at":"2023-09-13T18:25:10.488407","display_name":"Personal","config":{"is_personal":true,"max_identities":1},"tenant_handle":"default"}]%  
         

  3. Visit the external ip for the `langsmith-frontend` service on your browser

The LangSmith UI should be visible/operational

![./static/langsmith_ui.png](/assets/images/langsmith_ui-a308960b13a121598b5c577e7587adfe.png)

## Using LangSmith​

Now that LangSmith is running, you can start using it to trace your code. You can find more information on how to use self-hosted LangSmith in the [self-hosted usage guide](/self_hosting/usage).

Your LangSmith instance is now running but may not be fully setup yet.

If you used one of the basic configs, you will have a default admin user account created for you. You can log in with the email address and password you specified in the `langsmith_config.yaml` file.

As a next step, it is strongly recommended you work with your infrastructure administrators to:

  * Setup DNS for your LangSmith instance to enable easier access
  * Configure SSL to ensure in-transit encryption of traces submitted to LangSmith
  * Configure LangSmith with [Single Sign-On](/self_hosting/configuration/sso) to secure your LangSmith instance
  * Connect LangSmith to external Postgres and Redis instances

Review our [configuration section](/self_hosting/configuration) for more information on how to configure these options.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Prerequisites
  * Configure your Helm Charts:
  * Deploying to Kubernetes:
  * Validate your deployment:
  * Using LangSmith

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)