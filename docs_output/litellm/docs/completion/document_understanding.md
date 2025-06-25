# Using PDF Input | liteLLM

On this page

How to send / receive pdf's (other document types) to a `/chat/completions` endpoint

Works for:

  * Vertex AI models (Gemini + Anthropic)
  * Bedrock Models
  * Anthropic API Models
  * OpenAI API Models

## Quick Start​

### url​

  * SDK
  * PROXY

    
    
    from litellm.utils import supports_pdf_input, completion  
      
    # set aws credentials  
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
      
    # pdf url  
    file_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"  
      
    # model  
    model = "bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0"  
      
    file_content = [  
        {"type": "text", "text": "What's this file about?"},  
        {  
            "type": "file",  
            "file": {  
                "file_id": file_url,  
            }  
        },  
    ]  
      
      
    if not supports_pdf_input(model, None):  
        print("Model does not support image input")  
      
    response = completion(  
        model=model,  
        messages=[{"role": "user", "content": file_content}],  
    )  
    assert response is not None  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: bedrock-model  
        litellm_params:  
          model: bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0  
          aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID  
          aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY  
          aws_region_name: os.environ/AWS_REGION_NAME  
    

  2. Start the proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
    curl -X POST 'http://0.0.0.0:4000/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
        "model": "bedrock-model",  
        "messages": [  
            {"role": "user", "content": [  
                {"type": "text", "text": "What's this file about?"},  
                {  
                    "type": "file",  
                    "file": {  
                        "file_id": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",  
                    }  
                }  
            ]},  
        ]  
    }'  
    

### base64​

  * SDK
  * PROXY

    
    
    from litellm.utils import supports_pdf_input, completion  
      
    # set aws credentials  
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
      
    # pdf url  
    image_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"  
    response = requests.get(url)  
    file_data = response.content  
      
    encoded_file = base64.b64encode(file_data).decode("utf-8")  
    base64_url = f"data:application/pdf;base64,{encoded_file}"  
      
    # model  
    model = "bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0"  
      
    file_content = [  
        {"type": "text", "text": "What's this file about?"},  
        {  
            "type": "file",  
            "file": {  
                "file_data": base64_url,  
            }  
        },  
    ]  
      
      
    if not supports_pdf_input(model, None):  
        print("Model does not support image input")  
      
    response = completion(  
        model=model,  
        messages=[{"role": "user", "content": file_content}],  
    )  
    assert response is not None  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: bedrock-model  
        litellm_params:  
          model: bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0  
          aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID  
          aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY  
          aws_region_name: os.environ/AWS_REGION_NAME  
    

  2. Start the proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
    curl -X POST 'http://0.0.0.0:4000/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
        "model": "bedrock-model",  
        "messages": [  
            {"role": "user", "content": [  
                {"type": "text", "text": "What's this file about?"},  
                {  
                    "type": "file",  
                    "file": {  
                        "file_data": "data:application/pdf;base64...",  
                    }  
                }  
            ]},  
        ]  
    }'  
    

## Specifying format​

To specify the format of the document, you can use the `format` parameter.

  * SDK
  * PROXY

    
    
    from litellm.utils import supports_pdf_input, completion  
      
    # set aws credentials  
    os.environ["AWS_ACCESS_KEY_ID"] = ""  
    os.environ["AWS_SECRET_ACCESS_KEY"] = ""  
    os.environ["AWS_REGION_NAME"] = ""  
      
      
    # pdf url  
    file_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"  
      
    # model  
    model = "bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0"  
      
    file_content = [  
        {"type": "text", "text": "What's this file about?"},  
        {  
            "type": "file",  
            "file": {  
                "file_id": file_url,  
                "format": "application/pdf",  
            }  
        },  
    ]  
      
      
    if not supports_pdf_input(model, None):  
        print("Model does not support image input")  
      
    response = completion(  
        model=model,  
        messages=[{"role": "user", "content": file_content}],  
    )  
    assert response is not None  
    

  1. Setup config.yaml

    
    
    model_list:  
      - model_name: bedrock-model  
        litellm_params:  
          model: bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0  
          aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID  
          aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY  
          aws_region_name: os.environ/AWS_REGION_NAME  
    

  2. Start the proxy

    
    
    litellm --config /path/to/config.yaml  
    

  3. Test it!

    
    
    curl -X POST 'http://0.0.0.0:4000/chat/completions' \  
    -H 'Content-Type: application/json' \  
    -H 'Authorization: Bearer sk-1234' \  
    -d '{  
        "model": "bedrock-model",  
        "messages": [  
            {"role": "user", "content": [  
                {"type": "text", "text": "What's this file about?"},  
                {  
                    "type": "file",  
                    "file": {  
                        "file_id": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",  
                        "format": "application/pdf",  
                    }  
                }  
            ]},  
        ]  
    }'  
    

## Checking if a model supports pdf input​

  * SDK
  * PROXY

Use `litellm.supports_pdf_input(model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0")` -> returns `True` if model can accept pdf input
    
    
    assert litellm.supports_pdf_input(model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0") == True  
    

  1. Define bedrock models on config.yaml

    
    
    model_list:  
      - model_name: bedrock-model # model group name  
        litellm_params:  
          model: bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0  
          aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID  
          aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY  
          aws_region_name: os.environ/AWS_REGION_NAME  
        model_info: # OPTIONAL - set manually  
          supports_pdf_input: True  
    

  2. Run proxy server

    
    
    litellm --config config.yaml  
    

  3. Call `/model_group/info` to check if a model supports `pdf` input

    
    
    curl -X 'GET' \  
      'http://localhost:4000/model_group/info' \  
      -H 'accept: application/json' \  
      -H 'x-api-key: sk-1234'  
    

Expected Response
    
    
    {  
      "data": [  
        {  
          "model_group": "bedrock-model",  
          "providers": ["bedrock"],  
          "max_input_tokens": 128000,  
          "max_output_tokens": 16384,  
          "mode": "chat",  
          ...,  
          "supports_pdf_input": true, # 👈 supports_pdf_input is true  
        }  
      ]  
    }  
    

  * Quick Start
    * url
    * base64
  * Specifying format
  * Checking if a model supports pdf input