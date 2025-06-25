# /completions | liteLLM

On this page

### Usage​

  * LiteLLM Python SDK
  * LiteLLM Proxy Server

    
    
    from litellm import text_completion  
      
    response = text_completion(  
        model="gpt-3.5-turbo-instruct",  
        prompt="Say this is a test",  
        max_tokens=7  
    )  
    

  1. Define models on config.yaml

    
    
    model_list:  
      - model_name: gpt-3.5-turbo-instruct  
        litellm_params:  
          model: text-completion-openai/gpt-3.5-turbo-instruct # The `text-completion-openai/` prefix will call openai.completions.create  
          api_key: os.environ/OPENAI_API_KEY  
      - model_name: text-davinci-003  
        litellm_params:  
          model: text-completion-openai/text-davinci-003  
          api_key: os.environ/OPENAI_API_KEY  
    

  2. Start litellm proxy server

    
    
    litellm --config config.yaml  
    

  * OpenAI Python SDK
  * Curl Request

    
    
    from openai import OpenAI  
      
    # set base_url to your proxy server  
    # set api_key to send to proxy server  
    client = OpenAI(api_key="<proxy-api-key>", base_url="http://0.0.0.0:4000")  
      
    response = client.completions.create(  
        model="gpt-3.5-turbo-instruct",  
        prompt="Say this is a test",  
        max_tokens=7  
    )  
      
    print(response)  
    
    
    
    curl --location 'http://0.0.0.0:4000/completions' \  
        --header 'Content-Type: application/json' \  
        --header 'Authorization: Bearer sk-1234' \  
        --data '{  
            "model": "gpt-3.5-turbo-instruct",  
            "prompt": "Say this is a test",  
            "max_tokens": 7  
        }'  
    

## Input Params​

LiteLLM accepts and translates the [OpenAI Text Completion params](https://platform.openai.com/docs/api-reference/completions) across all supported providers.

### Required Fields​

  * `model`: _string_ \- ID of the model to use
  * `prompt`: _string or array_ \- The prompt(s) to generate completions for

### Optional Fields​

  * `best_of`: _integer_ \- Generates best_of completions server-side and returns the "best" one
  * `echo`: _boolean_ \- Echo back the prompt in addition to the completion.
  * `frequency_penalty`: _number_ \- Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency.
  * `logit_bias`: _map_ \- Modify the likelihood of specified tokens appearing in the completion
  * `logprobs`: _integer_ \- Include the log probabilities on the logprobs most likely tokens. Max value of 5
  * `max_tokens`: _integer_ \- The maximum number of tokens to generate.
  * `n`: _integer_ \- How many completions to generate for each prompt.
  * `presence_penalty`: _number_ \- Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far.
  * `seed`: _integer_ \- If specified, system will attempt to make deterministic samples
  * `stop`: _string or array_ \- Up to 4 sequences where the API will stop generating tokens
  * `stream`: _boolean_ \- Whether to stream back partial progress. Defaults to false
  * `suffix`: _string_ \- The suffix that comes after a completion of inserted text
  * `temperature`: _number_ \- What sampling temperature to use, between 0 and 2.
  * `top_p`: _number_ \- An alternative to sampling with temperature, called nucleus sampling.
  * `user`: _string_ \- A unique identifier representing your end-user

## Output Format​

Here's the exact JSON output format you can expect from completion calls:

[**Follows OpenAI's output format**](https://platform.openai.com/docs/api-reference/completions/object)

  * Non-Streaming Response
  * Streaming Response

    
    
    {  
      "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",  
      "object": "text_completion",  
      "created": 1589478378,  
      "model": "gpt-3.5-turbo-instruct",  
      "system_fingerprint": "fp_44709d6fcb",  
      "choices": [  
        {  
          "text": "\n\nThis is indeed a test",  
          "index": 0,  
          "logprobs": null,  
          "finish_reason": "length"  
        }  
      ],  
      "usage": {  
        "prompt_tokens": 5,  
        "completion_tokens": 7,  
        "total_tokens": 12  
      }  
    }  
      
    
    
    
    {  
      "id": "cmpl-7iA7iJjj8V2zOkCGvWF2hAkDWBQZe",  
      "object": "text_completion",  
      "created": 1690759702,  
      "choices": [  
        {  
          "text": "This",  
          "index": 0,  
          "logprobs": null,  
          "finish_reason": null  
        }  
      ],  
      "model": "gpt-3.5-turbo-instruct"  
      "system_fingerprint": "fp_44709d6fcb",  
    }  
      
    

## **Supported Providers**​

Provider| Link to Usage  
---|---  
OpenAI| [Usage](/docs/providers/text_completion_openai)  
Azure OpenAI| [Usage](/docs/providers/azure)  
  
  * Usage
  * Input Params
    * Required Fields
    * Optional Fields
  * Output Format
  * **Supported Providers**