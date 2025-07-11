# Install private nodes | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/creating-nodes/deploy/install-private-nodes.md "Edit this page")

# Install private nodes#

You can build your own nodes and install them in your n8n instance without publishing them on npm. This is useful for nodes that you create for internal use only at your company.

## Install your node in a Docker n8n instance#

If you're running n8n using Docker, you need to create a Docker image with the node installed in n8n. 

  1. Create a Dockerfile and paste the code from [this Dockerfile](https://github.com/n8n-io/n8n/blob/master/docker/images/n8n/Dockerfile).

Your Dockerfile should look like this:
         
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
         13
         14
         15
         16
         17
         18
         19
         20
         21
         22
         23
         24
         25
         26
         27
         28
         29
         30
         31
         32
         33
         34
         35
         36

| 
         
         FROM node:16-alpine
         
         ARG N8N_VERSION
         
         RUN if [ -z "$N8N_VERSION" ] ; then echo "The N8N_VERSION argument is missing!" ; exit 1; fi
         
         # Update everything and install needed dependencies
         RUN apk add --update graphicsmagick tzdata git tini su-exec
         
         # Set a custom user to not have n8n run as root
         USER root
         
         # Install n8n and the packages it needs to build it correctly.
         RUN apk --update add --virtual build-dependencies python3 build-base ca-certificates && \
         	npm config set python "$(which python3)" && \
         	npm_config_user=root npm install -g full-icu n8n@${N8N_VERSION} && \
         	apk del build-dependencies \
         	&& rm -rf /root /tmp/* /var/cache/apk/* && mkdir /root;
         
         
         # Install fonts
         RUN apk --no-cache add --virtual fonts msttcorefonts-installer fontconfig && \
         	update-ms-fonts && \
         	fc-cache -f && \
         	apk del fonts && \
         	find  /usr/share/fonts/truetype/msttcorefonts/ -type l -exec unlink {} \; \
         	&& rm -rf /root /tmp/* /var/cache/apk/* && mkdir /root
         
         ENV NODE_ICU_DATA /usr/local/lib/node_modules/full-icu
         
         WORKDIR /data
         
         COPY docker-entrypoint.sh /docker-entrypoint.sh
         ENTRYPOINT ["tini", "--", "/docker-entrypoint.sh"]
         
         EXPOSE 5678/tcp
           
  
---|---  
  
  2. Compile your custom node code (`npm run build` if you are using nodes starter). Copy the **node** and **credential** folders from within the **dist** folder into your container's `~/.n8n/custom/` directory. This makes them available to Docker.

  3. Download the [docker-entrypoint.sh](https://github.com/n8n-io/n8n/blob/master/docker/images/n8n/docker-entrypoint.sh) file, and place it in the same directory as your Dockerfile.

  4. Build your Docker image:
         
         1
         2
         3

| 
         
         # Replace <n8n-version-number> with the n8n release version number. 
         # For example, N8N_VERSION=0.177.0
         docker build --build-arg N8N_VERSION=<n8n-version-number> --tag=customizedn8n .
           
  
---|---  
  

You can now use your node in Docker.

## Install your node in a global n8n instance#

If you've installed n8n globally, make sure that you install your node inside n8n. n8n will find the module and load it automatically.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top