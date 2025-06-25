# Post-Call Rules | liteLLM

On this page

Use this to fail a request based on the output of an llm api call.

## Quick Start​

### Step 1: Create a file (e.g. post_call_rules.py)​
    
    
    def my_custom_rule(input): # receives the model response   
        if len(input) < 5:   
          return {  
                "decision": False,  
                "message": "This violates LiteLLM Proxy Rules. Response too short"  
          }  
        return {"decision": True}   # message not required since, request will pass  
    

### Step 2. Point it to your proxy​
    
    
    litellm_settings:  
      post_call_rules: post_call_rules.my_custom_rule  
    

### Step 3. Start + test your proxy​
    
    
    $ litellm /path/to/config.yaml  
    
    
    
    curl --location 'http://0.0.0.0:4000/v1/chat/completions' \  
    --header 'Content-Type: application/json' \  
    --header 'Authorization: Bearer sk-1234' \  
    --data '{  
      "model": "gpt-3.5-turbo",  
      "messages": [{"role":"user","content":"What llm are you?"}],  
      "temperature": 0.7,  
      "max_tokens": 10,  
    }'  
    

* * *

This will now check if a response is > len 5, and if it fails, it'll retry a call 3 times before failing.

### Response that fail the rule​

This is the response from LiteLLM Proxy on failing a rule
    
    
    {  
      "error":  
        {  
          "message":"This violates LiteLLM Proxy Rules. Response too short",  
          "type":null,  
          "param":null,  
          "code":500  
        }  
    }     
    

  * Quick Start
    * Step 1: Create a file (e.g. post_call_rules.py)
    * Step 2. Point it to your proxy
    * Step 3. Start + test your proxy
    * Response that fail the rule