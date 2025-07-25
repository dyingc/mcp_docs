# Enable blob storage | 🦜️🛠️ LangSmith

On this page

By default, LangSmith stores run inputs, outputs, errors, manifests, extras, and events in ClickHouse. If you so choose, you can instead store this information in blob storage, which has a couple of notable benefits:

  1. In high trace environments, inputs, outputs, errors, manifests, extras, and events may balloon the size of your databases.
  2. If using LangSmith Managed ClickHouse, you may want sensitive information in blob storage that resides in your environment. To alleviate this, LangSmith supports storing run inputs, outputs, errors, manifests, extras, events, and attachments in an external blob storage system.

## Requirements​

note

Azure blob storage is available in Beta on Helm chart versions 0.8.9 and greater.  
While in Beta, [deleting trace projects](/observability/concepts#deleting-traces-from-langsmith) is not supported.

  * Access to a valid blob storage service
    * [Amazon S3](https://aws.amazon.com/s3/)
    * [Google Cloud Storage (GCS)](https://cloud.google.com/storage?hl=en)
    * [Azure Blob Storage [BETA]](https://azure.microsoft.com/en-us/products/storage/blobs)
  * A bucket/directory in your blob storage to store the data. We highly recommend creating a separate bucket/directory for LangSmith data.
    * **If you are using TTLs** , you will need to set up a lifecycle policy to delete old data. You can find more information on configuring TTLs [here](/self_hosting/configuration/ttl). These policies should mirror the TTLs you have set in your LangSmith configuration, or you may experience data loss. See here on how to setup the lifecycle rules for TTLs for blob storage.
  * Credentials to permit LangSmith Services to access the bucket/directory
    * You will need to provide your LangSmith instance with the necessary credentials to access the bucket/directory. Read the authentication section below for more information.
  * If using S3 or GCS, an API url for your blob storage service
    * This will be the URL that LangSmith uses to access your blob storage system
    * For Amazon S3, this will be the URL of the S3 endpoint. Something like: `https://s3.amazonaws.com` or `https://s3.us-west-1.amazonaws.com` if using a regional endpoint.
    * For Google Cloud Storage, this will be the URL of the GCS endpoint. Something like: `https://storage.googleapis.com`

## Authentication​

### Amazon S3​

To authenticate to [Amazon S3](https://aws.amazon.com/s3/), you will need to create an IAM policy granting admin permissions on your bucket. This will look something like the following:
    
    
    {  
      "Version": "2012-10-17",  
      "Statement": [  
        {  
          "Effect": "Allow",  
          "Action": "s3:*",  
          "Resource": [  
            "arn:aws:s3:::your-bucket-name",  
            "arn:aws:s3:::your-bucket-name/*"  
          ]  
        }  
      ]  
    }  
    

Once you have the correct policy, there are two ways to authenticate with Amazon S3:

  1. [**(Recommended) IAM Role for Service Account**](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html): You can create an IAM role for your LangSmith instance and attach the policy to that role. You can then provide the role to LangSmith. This is the recommended way to authenticate with Amazon S3 in production.
     1. You will need to create an IAM role with the policy attached.
     2. You will need to allow LangSmith service accounts to assume the role. The `langsmith-queue`, `langsmith-backend`, and `langsmith-platform-backend` service accounts will need to be able to assume the role.

Service Account Names

The service account names will be different if you are using a custom release name. You can find the service account names by running `kubectl get serviceaccounts` in your cluster.

     3. You will need to provide the role ARN to LangSmith. You can do this by adding the `eks.amazonaws.com/role-arn: "<role_arn>"` annotation to the `queue`, `backend`, and `platform-backend` services in your Helm Chart installation.
  2. [**Access Key and Secret Key**](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html): You can provide LangSmith with an access key and secret key. This is the simplest way to authenticate with Amazon S3. However, it is not recommended for production use as it is less secure.
     1. You will need to create a user with the policy attached. Then you can provision an access key and secret key for that user.

### Google Cloud Storage​

To authenticate with [Google Cloud Storage](https://cloud.google.com/storage?hl=en), you will need to create a [`service account`](https://cloud.google.com/iam/docs/service-account-overview) with the necessary permissions to access your bucket.

Your service account will need the `Storage Admin` role or a custom role with equivalent permissions. This can be scoped to the bucket that LangSmith will be using.

Once you have a provisioned service account, you will need to generate a [`HMAC key`](https://cloud.google.com/storage/docs/authentication/hmackeys) for that service account. This key and secret will be used to authenticate with Google Cloud Storage.

### Azure Blob Storage​

To authenticate with [Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs), you will need to use one of the following methods to grant LangSmith workloads permission to access your [container](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction#containers) (listed in order of precedence):

  1. [Storage account and access key](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage)
  2. [Connection string](https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string)
  3. [Workload identity](https://azure.github.io/azure-workload-identity/docs/introduction.html) (recommended), managed identity, or environment variables supported by [`DefaultAzureCredential`](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication?tabs=bash#2-authenticate-with-azure). This is the default authentication method when configuration for either option above is not present.
     1. To use workload identity, add the label `azure.workload.identity/use: true` to the `queue`, `backend`, and `platform-backend` deployments. Additionally, add the `azure.workload.identity/client-id` annotation to the corresponding service accounts, which should be an existing Azure AD Application's client ID or user-assigned managed identity's client ID. See [Azure's documentation](https://azure.github.io/azure-workload-identity/docs/topics/service-account-labels-and-annotations.html) for additional details.

note

Some deployments may need further customization of the connection configuration using a Service URL Override instead of the default service URL (`https://<storage_account_name>.blob.core.windows.net/`). For example, this override is necessary in order to use a different blob storage domain (e.g. government or china).

## CH Search​

By default, LangSmith will still store tokens for search in ClickHouse. If you are using LangSmith Managed Clickhouse, you may want to disable this feature to avoid sending potentially sensitive information to ClickHouse. You can do this in your blob storage configuration.

## Configuration​

After creating your bucket and obtaining the necessary credentials, you can configure LangSmith to use your blob storage system.

  * Helm
  * Docker

    
    
      
    config:  
      blobStorage:  
        enabled: true  
        engine: "S3" # Or "Azure"  
        chSearchEnabled: true # Set to false if you want to disable CH search (Recommended for LangSmith Managed Clickhouse)  
        bucketName: "your-bucket-name"  
        apiURL: "Your connection url"  
        accessKey: "Your access key" # Optional. Only required if using S3 access key and secret key  
        accessKeySecret: "Your access key secret" # Optional. Only required if using access key and secret key  
        # The following blob storage configuration values are for Azure and require blobStorage.engine = "Azure". Omit otherwise.  
        azureStorageAccountName: "Your storage account name" # Optional. Only required if using storage account and access key.  
        azureStorageAccountKey: "Your storage account access key" # Optional. Only required if using storage account and access key.  
        azureStorageContainerName: "your-container-name" # Required  
        azureStorageConnectionString: "" # Optional.  
        azureStorageServiceUrlOverride: "" # Optional   
      
     backend: # Optional, only required if using IAM role for service account on AWS or workload identity on AKS  
       deployment:  # Azure only  
         labels:  
           azure.workload.identity/use: true  
       serviceAccount:  
         annotations:  
           azure.workload.identity/client-id: "<client_id>" # Azure only  
           eks.amazonaws.com/role-arn: "<role_arn>" # AWS only   
      
     platformBackend: # Optional, only required if using IAM role for service account on AWS or workload identity on AKS  
       deployment:  # Azure only  
         labels:  
           azure.workload.identity/use: true  
       serviceAccount:  
         annotations:  
           azure.workload.identity/client-id: "<client_id>" # Azure only  
           eks.amazonaws.com/role-arn: "<role_arn>" # AWS only   
      
     queue: # Optional, only required if using IAM role for service account on AWS or workload identity on AKS  
       deployment:  # Azure only  
         labels:  
           azure.workload.identity/use: true  
       serviceAccount:  
         annotations:  
           azure.workload.identity/client-id: "<client_id>" # Azure only  
           eks.amazonaws.com/role-arn: "<role_arn>" # AWS only  
    
    
    
    # In your .env file  
    FF_BLOB_STORAGE_ENABLED=false # Set to true if you want to enable blob storage  
    BLOB_STORAGE_ENGINE=S3 # Or Azure  
    BLOB_STORAGE_BUCKET_NAME=langsmith-blob-storage # Required for using S3. Change to your desired blob storage bucket name  
    BLOB_STORAGE_API_URL=https://s3.us-west-2.amazonaws.com # Change to your desired blob storage API URL  
    BLOB_STORAGE_ACCESS_KEY=your-access-key # Change to your desired blob storage access key  
    BLOB_STORAGE_ACCESS_KEY_SECRET=your-access-key-secret # Change to your desired blob storage access key secret  
    AZURE_STORAGE_ACCOUNT_NAME=your-storage-account-name # Optional. Only required if using storage account and access key.  
    AZURE_STORAGE_ACCOUNT_KEY=your-storage-account-key # Optional. Only required if using storage account and access key.  
    AZURE_STORAGE_CONTAINER_NAME=your-container-name # Required for using Azure blob storage. Change to your desired container name  
    AZURE_STORAGE_CONNECTION_STRING=BlobEndpoint=https://storagesample.blob.core.windows.net;SharedAccessSignature=signature; # Optional.  
    AZURE_STORAGE_SERVICE_URL_OVERRIDE=https://your.override.domain.net # Optional  
    

Using an existing secret

If using an access key and secret, you can also provide an existing Kubernetes secret that contains the authentication information. This is recommended over providing the access key and secret key directly in your config. See the [generated secret template](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/templates/secrets.yaml) for the expected secret keys.

## TTL Configuration​

If using the [TTL](/self_hosting/configuration/ttl) feature with LangSmith, you'll also have to configure TTL rules for your blob storage. Trace information stored on blob storage is stored on a particular prefix path, which determines the TTL for the data. When a trace's retention is extended, its corresponding blob storage path changes to ensure that it matches the new extended retention.

The following TTL prefix are used:

  * `ttl_s/`: Short term TTL, configured for 14 days.
  * `ttl_l/`: Long term TTL, configured for 400 days.

If you have customized the TTLs in your LangSmith configuration, you will need to adjust the TTLs in your blob storage configuration to match.

### Amazon S3​

If using S3 for your blob storage, you will need to setup a filter lifecycle configuration that matches the prefixes above. You can find information for this [in the Amazon Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html#intro-lifecycle-rules-filter).

As an example, if you are using Terraform to manage your S3 bucket, you would setup something like this:
    
    
      rule {  
        id      = "short-term-ttl"  
        prefix  = "ttl_s/"  
        enabled = true  
      
        expiration {  
          days = 14  
        }  
      }  
      
      rule {  
        id      = "long-term-ttl"  
        prefix  = "ttl_l/"  
        enabled = true  
      
        expiration {  
          days = 400  
        }  
      }  
    

### Google Cloud Storage​

You will need to setup lifecycle conditions for your GCS buckets that you are using. You can find information for this [in the Google Documentation](https://cloud.google.com/storage/docs/lifecycle#conditions), specifically using matchesPrefix.

As an example, if you are using Terraform to manage your GCS bucket, you would setup something like this:
    
    
      lifecycle_rule {  
        condition {  
          age            = 14  
          matches_prefix = ["ttl_s"]  
        }  
        action {  
          type = "Delete"  
        }  
      }  
      
      lifecycle_rule {  
        condition {  
          age            = 400  
          matches_prefix = ["ttl_l"]  
        }  
        action {  
          type = "Delete"  
        }  
      }  
    

### Azure blob storage​

You will need to configure a [lifecycle management policy](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-policy-configure) on the container in order to expire objects matching the prefixes above.

As an example, if you are [using Terraform to manage your blob storage container](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_management_policy), you would setup something like this:
    
    
    resource "azurerm_storage_management_policy" "example" {  
      storage_account_id = "my-storage-account-id"  
      
      rule {  
        name = "base"  
        enabled = true  
        type = "Lifecycle"  
        filters {  
          prefix_match = ["my-container/ttl_s"]  
          blob_types = ["blockBlob"]  
        }  
        actions {  
          base_blob {  
            delete_after_days_since_creation_greater_than = 14  
          }  
          snapshot {  
            delete_after_days_since_creation_greater_than = 14  
          }  
          version {  
            delete_after_days_since_creation_greater_than = 14  
          }  
        }  
      }  
      
      rule {  
        name = "extended"  
        enabled = true  
        type = "Lifecycle"  
        filters {  
          prefix_match = ["my-container/ttl_l"]  
          blob_types = ["blockBlob"]  
        }  
         actions {  
          base_blob {  
            delete_after_days_since_creation_greater_than = 400  
          }  
          snapshot {  
            delete_after_days_since_creation_greater_than = 400  
          }  
          version {  
            delete_after_days_since_creation_greater_than = 400  
          }  
        }  
      }  
    }  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Requirements
  * Authentication
    * Amazon S3
    * Google Cloud Storage
    * Azure Blob Storage
  * CH Search
  * Configuration
  * TTL Configuration
    * Amazon S3
    * Google Cloud Storage
    * Azure blob storage

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)