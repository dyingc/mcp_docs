# CLI Arguments | liteLLM

On this page

Cli arguments, --host, --port, --num_workers

## \--host​

  * **Default:** `'0.0.0.0'`
  * The host for the server to listen on.
  * **Usage:**
        
        litellm --host 127.0.0.1  
        

  * **Usage - set Environment Variable:** `HOST`

    
    
    export HOST=127.0.0.1  
    litellm  
    

## \--port​

  * **Default:** `4000`
  * The port to bind the server to.
  * **Usage:**
        
        litellm --port 8080  
        

  * **Usage - set Environment Variable:** `PORT`
        
        export PORT=8080  
        litellm  
        

## \--num_workers​

  * **Default:** `1`
  * The number of uvicorn workers to spin up.
  * **Usage:**
        
        litellm --num_workers 4  
        

  * **Usage - set Environment Variable:** `NUM_WORKERS`
        
        export NUM_WORKERS=4  
        litellm  
        

## \--api_base​

  * **Default:** `None`
  * The API base for the model litellm should call.
  * **Usage:**
        
        litellm --model huggingface/tinyllama --api_base https://k58ory32yinf1ly0.us-east-1.aws.endpoints.huggingface.cloud  
        

## \--api_version​

  * **Default:** `None`
  * For Azure services, specify the API version.
  * **Usage:**
        
        litellm --model azure/gpt-deployment --api_version 2023-08-01 --api_base https://<your api base>"  
        

## \--model or -m​

  * **Default:** `None`
  * The model name to pass to Litellm.
  * **Usage:**
        
        litellm --model gpt-3.5-turbo  
        

## \--test​

  * **Type:** `bool` (Flag)
  * Proxy chat completions URL to make a test request.
  * **Usage:**
        
        litellm --test  
        

## \--health​

  * **Type:** `bool` (Flag)
  * Runs a health check on all models in config.yaml
  * **Usage:**
        
        litellm --health  
        

## \--alias​

  * **Default:** `None`
  * An alias for the model, for user-friendly reference.
  * **Usage:**
        
        litellm --alias my-gpt-model  
        

## \--debug​

  * **Default:** `False`
  * **Type:** `bool` (Flag)
  * Enable debugging mode for the input.
  * **Usage:**
        
        litellm --debug  
        

  * **Usage - set Environment Variable:** `DEBUG`
        
        export DEBUG=True  
        litellm  
        

## \--detailed_debug​

  * **Default:** `False`
  * **Type:** `bool` (Flag)
  * Enable debugging mode for the input.
  * **Usage:**
        
        litellm --detailed_debug  
        

  * **Usage - set Environment Variable:** `DETAILED_DEBUG`
        
        export DETAILED_DEBUG=True  
        litellm  
        

#### \--temperature​

  * **Default:** `None`
  * **Type:** `float`
  * Set the temperature for the model.
  * **Usage:**
        
        litellm --temperature 0.7  
        

## \--max_tokens​

  * **Default:** `None`
  * **Type:** `int`
  * Set the maximum number of tokens for the model output.
  * **Usage:**
        
        litellm --max_tokens 50  
        

## \--request_timeout​

  * **Default:** `6000`
  * **Type:** `int`
  * Set the timeout in seconds for completion calls.
  * **Usage:**
        
        litellm --request_timeout 300  
        

## \--drop_params​

  * **Type:** `bool` (Flag)
  * Drop any unmapped params.
  * **Usage:**
        
        litellm --drop_params  
        

## \--add_function_to_prompt​

  * **Type:** `bool` (Flag)
  * If a function passed but unsupported, pass it as a part of the prompt.
  * **Usage:**
        
        litellm --add_function_to_prompt  
        

## \--config​

  * Configure Litellm by providing a configuration file path.
  * **Usage:**
        
        litellm --config path/to/config.yaml  
        

## \--telemetry​

  * **Default:** `True`
  * **Type:** `bool`
  * Help track usage of this feature.
  * **Usage:**
        
        litellm --telemetry False  
        

## \--log_config​

  * **Default:** `None`
  * **Type:** `str`
  * Specify a log configuration file for uvicorn.
  * **Usage:**
        
        litellm --log_config path/to/log_config.conf  
        

## \--skip_server_startup​

  * **Default:** `False`
  * **Type:** `bool` (Flag)
  * Skip starting the server after setup (useful for DB migrations only).
  * **Usage:**
        
        litellm --skip_server_startup  
        

  * \--host
  * \--port
  * \--num_workers
  * \--api_base
  * \--api_version
  * \--model or -m
  * \--test
  * \--health
  * \--alias
  * \--debug
  * \--detailed_debug
  * \--max_tokens
  * \--request_timeout
  * \--drop_params
  * \--add_function_to_prompt
  * \--config
  * \--telemetry
  * \--log_config
  * \--skip_server_startup