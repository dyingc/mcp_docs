# Custom LLM Pricing | liteLLM

On this page

Use this to register custom pricing for models.

There's 2 ways to track cost:

  * cost per token
  * cost per second

By default, the response cost is accessible in the logging object via `kwargs["response_cost"]` on success (sync + async). [**Learn More**](/docs/observability/custom_callback)

info

LiteLLM already has pricing for any model in our [model cost map](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json).

## Cost Per Second (e.g. Sagemaker)​

### Usage with LiteLLM Proxy Server​

**Step 1: Add pricing to config.yaml**
    
    
    model_list:  
      - model_name: sagemaker-completion-model  
        litellm_params:  
          model: sagemaker/berri-benchmarking-Llama-2-70b-chat-hf-4  
        model_info:  
          input_cost_per_second: 0.000420  
      - model_name: sagemaker-embedding-model  
        litellm_params:  
          model: sagemaker/berri-benchmarking-gpt-j-6b-fp16  
        model_info:  
          input_cost_per_second: 0.000420   
    

**Step 2: Start proxy**
    
    
    litellm /path/to/config.yaml  
    

**Step 3: View Spend Logs**

## Cost Per Token (e.g. Azure)​

### Usage with LiteLLM Proxy Server​
    
    
    model_list:  
      - model_name: azure-model  
        litellm_params:  
          model: azure/<your_deployment_name>  
          api_key: os.environ/AZURE_API_KEY  
          api_base: os.environ/AZURE_API_BASE  
          api_version: os.environ/AZURE_API_VERSION  
        model_info:  
          input_cost_per_token: 0.000421 # 👈 ONLY to track cost per token  
          output_cost_per_token: 0.000520 # 👈 ONLY to track cost per token  
    

## Override Model Cost Map​

You can override [our model cost map](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json) with your own custom pricing for a mapped model.

Just add a `model_info` key to your model in the config, and override the desired keys.

Example: Override Anthropic's model cost map for the `prod/claude-3-5-sonnet-20241022` model.
    
    
    model_list:  
      - model_name: "prod/claude-3-5-sonnet-20241022"  
        litellm_params:  
          model: "anthropic/claude-3-5-sonnet-20241022"  
          api_key: os.environ/ANTHROPIC_PROD_API_KEY  
        model_info:  
          input_cost_per_token: 0.000006  
          output_cost_per_token: 0.00003  
          cache_creation_input_token_cost: 0.0000075  
          cache_read_input_token_cost: 0.0000006  
    

## Set 'base_model' for Cost Tracking (e.g. Azure deployments)​

**Problem** : Azure returns `gpt-4` in the response when `azure/gpt-4-1106-preview` is used. This leads to inaccurate cost tracking

**Solution** ✅ : Set `base_model` on your config so litellm uses the correct model for calculating azure cost

Get the base model name from [here](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json)

Example config with `base_model`
    
    
    model_list:  
      - model_name: azure-gpt-3.5  
        litellm_params:  
          model: azure/chatgpt-v-2  
          api_base: os.environ/AZURE_API_BASE  
          api_key: os.environ/AZURE_API_KEY  
          api_version: "2023-07-01-preview"  
        model_info:  
          base_model: azure/gpt-4-1106-preview  
    

## Debugging​

If you're custom pricing is not being used or you're seeing errors, please check the following:

  1. Run the proxy with `LITELLM_LOG="DEBUG"` or the `--detailed_debug` cli flag

    
    
    litellm --config /path/to/config.yaml --detailed_debug  
    

  2. Check logs for this line:

    
    
    LiteLLM:DEBUG: utils.py:263 - litellm.acompletion  
    

  3. Check if 'input_cost_per_token' and 'output_cost_per_token' are top-level keys in the acompletion function.

    
    
    acompletion(  
      ...,  
      input_cost_per_token: my-custom-price,   
      output_cost_per_token: my-custom-price,  
    )  
    

If these keys are not present, LiteLLM will not use your custom pricing.

If the problem persists, please file an issue on [GitHub](https://github.com/BerriAI/litellm/issues).

  * Cost Per Second (e.g. Sagemaker)
    * Usage with LiteLLM Proxy Server
  * Cost Per Token (e.g. Azure)
    * Usage with LiteLLM Proxy Server
  * Override Model Cost Map
  * Set 'base_model' for Cost Tracking (e.g. Azure deployments)
  * Debugging