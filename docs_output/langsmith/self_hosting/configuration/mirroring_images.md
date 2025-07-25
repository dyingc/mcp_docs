# Mirroring Images for your LangSmith installation | 🦜️🛠️ LangSmith

On this page

By default, LangSmith will pull images from our public Docker registry. However, if you are running LangSmith in an environment that does not have internet access, or if you would like to use a private Docker registry, you can mirror the images to your own registry and then configure your LangSmith installation to use those images.

## Requirements​

  * Authenticated access to a Docker registry that your Kubernetes cluster/machine has access to.
  * Docker installed on your local machine or a machine that has access to the Docker registry.
  * A Kubernetes cluster or a machine where you can run LangSmith.

## Mirroring the Images​

For your convenience, we have provided a script that will mirror the images for you. You can find the script in the [LangSmith Helm Chart repository](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/scripts/mirror_langsmith_images.sh)

To use the script, you will need to run the script with the following command specifying your registry and platform:
    
    
    bash mirror_images.sh <your-registry> [<platform>]  
    

Where `<your-registry>` is the URL of your Docker registry (e.g. `myregistry.com`) and `<platform>` is the platform you are using (e.g. `linux/amd64`, `linux/arm64`, etc.). If you do not specify a platform, it will default to `linux/amd64`.

For example, if your registry is `myregistry.com`, your platform is `linux/arm64`, and you want to use the latest version of the images, you would run:
    
    
    bash mirror_langsmith_images.sh --registry myregistry --platform linux/arm64 --version 0.10.66  
    

Note that this script will assume that you have Docker installed and that you are authenticated to your registry. It will also push the images to the specified registry with the same repository/tag as the original images.

Alternatively, you can pull, mirror, and push the images manually. The images that you will need to mirror are found in the `values.yaml` file of the LangSmith Helm Chart. These can be found here: [LangSmith Helm Chart values.yaml](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/values.yaml#L14)

Here is an example of how to mirror the images using Docker:
    
    
    # Pull the images from the public registry  
    docker pull langchain/langsmith-backend:latest  
    docker tag langchain/langsmith-backend:latest <your-registry>/langsmith-backend:latest  
    docker push <your-registry>/langsmith-backend:latest  
    

You will need to repeat this for each image that you want to mirror.

## Configuration​

Once the images are mirrored, you will need to configure your LangSmith installation to use the mirrored images. You can do this by modifying the `values.yaml` file for your LangSmith Helm Chart installation or the `.env` file for your Docker installation. Replace tag with the version you want to use, e.g. `0.10.66` for the latest version at the time of writing.
    
    
      
    <CodeTabs  
      tabs={[  
        HelmBlock(`  
    images:  
        imagePullSecrets: [] # Add your image pull secrets here if needed  
        registry: "" # Set this to your registry URL if you mirrored all images to the same registry using our script. Then you can remove the repository prefix from the images below.  
        aceBackendImage:  
          repository: "(your-registry)/langchain/langsmith-ace-backend"  
          pullPolicy: IfNotPresent  
          tag: "0.10.66"  
        backendImage:  
          repository: "(your-registry)/langchain/langsmith-backend"  
          pullPolicy: IfNotPresent  
          tag: "0.10.66"  
        frontendImage:  
          repository: "(your-registry)/langchain/langsmith-frontend"  
          pullPolicy: IfNotPresent  
          tag: "0.10.66"  
        hostBackendImage:  
          repository: "(your-registry)/langchain/hosted-langserve-backend"  
          pullPolicy: IfNotPresent  
          tag: "0.10.66"  
        operatorImage:  
          repository: "(your-registry)/langchain/langgraph-operator"  
          pullPolicy: IfNotPresent  
          tag: "6cc83a8"  
        platformBackendImage:  
          repository: "(your-registry)/langchain/langsmith-go-backend"  
          pullPolicy: IfNotPresent  
          tag: "0.10.66"  
        playgroundImage:  
          repository: "(your-registry)/langchain/langsmith-playground"  
          pullPolicy: IfNotPresent  
          tag: "0.10.66"  
        postgresImage:  
          repository: "(your-registry)/postgres"  
          pullPolicy: IfNotPresent  
          tag: "14.7"  
        redisImage:  
          repository: "(your-registry)/redis"  
          pullPolicy: IfNotPresent  
          tag: "7"  
        clickhouseImage:  
          repository: "(your-registry)/clickhouse/clickhouse-server"  
          pullPolicy: Always  
          tag: "24.8"  
    `),  
        DockerBlock(  
          `# In your .env file  
    _REGISTRY=your-registry # Set this to your registry URL if you mirrored all images to the same registry using our script. Otherwise you will need to manually set the repository for each image in the compose file.  
        `  
        ),  
      ]}  
    />  
      
    Once configured, you will need to update your LangSmith installation. You can follow our upgrade guide here: [Upgrading LangSmith](../upgrades).  
      
    If your upgrade is successful, your LangSmith instance should now be using the mirrored images from your Docker registry.  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Requirements
  * Mirroring the Images
  * Configuration

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)