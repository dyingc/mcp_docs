# Provider Files Endpoints | liteLLM

On this page

Files are used to upload documents that can be used with features like Assistants, Fine-tuning, and Batch API.

Use this to call the provider's `/files` endpoints directly, in the OpenAI format.

## Quick Start​

  * Upload a File
  * List Files
  * Retrieve File Information
  * Delete File
  * Get File Content

  * LiteLLM PROXY Server
  * SDK

  1. Setup config.yaml

    
    
    # for /files endpoints  
    files_settings:  
      - custom_llm_provider: azure  
        api_base: https://exampleopenaiendpoint-production.up.railway.app  
        api_key: fake-key  
        api_version: "2023-03-15-preview"  
      - custom_llm_provider: openai  
        api_key: os.environ/OPENAI_API_KEY  
    

  2. Start LiteLLM PROXY Server

    
    
    litellm --config /path/to/config.yaml  
      
    ## RUNNING on http://0.0.0.0:4000  
    

  3. Use OpenAI's /files endpoints

Upload a File
    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        api_key="sk-...",  
        base_url="http://0.0.0.0:4000/v1"  
    )  
      
    client.files.create(  
        file=wav_data,  
        purpose="user_data",  
        extra_body={"custom_llm_provider": "openai"}  
    )  
    

List Files
    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        api_key="sk-...",  
        base_url="http://0.0.0.0:4000/v1"  
    )  
      
    files = client.files.list(extra_body={"custom_llm_provider": "openai"})  
    print("files=", files)  
    

Retrieve File Information
    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        api_key="sk-...",  
        base_url="http://0.0.0.0:4000/v1"  
    )  
      
    file = client.files.retrieve(file_id="file-abc123", extra_body={"custom_llm_provider": "openai"})  
    print("file=", file)  
    

Delete File
    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        api_key="sk-...",  
        base_url="http://0.0.0.0:4000/v1"  
    )  
      
    response = client.files.delete(file_id="file-abc123", extra_body={"custom_llm_provider": "openai"})  
    print("delete response=", response)  
    

Get File Content
    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        api_key="sk-...",  
        base_url="http://0.0.0.0:4000/v1"  
    )  
      
    content = client.files.content(file_id="file-abc123", extra_body={"custom_llm_provider": "openai"})  
    print("content=", content)  
    

**Upload a File**
    
    
     from litellm  
    import os   
      
    os.environ["OPENAI_API_KEY"] = "sk-.."  
      
    file_obj = await litellm.acreate_file(  
        file=open("mydata.jsonl", "rb"),  
        purpose="fine-tune",  
        custom_llm_provider="openai",  
    )  
    print("Response from creating file=", file_obj)  
    

**List Files**
    
    
     files = await litellm.alist_files(  
        custom_llm_provider="openai",  
        limit=10  
    )  
    print("files=", files)  
    

**Retrieve File Information**
    
    
     file = await litellm.aretrieve_file(  
        file_id="file-abc123",  
        custom_llm_provider="openai"  
    )  
    print("file=", file)  
    

**Delete File**
    
    
     response = await litellm.adelete_file(  
        file_id="file-abc123",  
        custom_llm_provider="openai"  
    )  
    print("delete response=", response)  
    

**Get File Content**
    
    
     content = await litellm.afile_content(  
        file_id="file-abc123",  
        custom_llm_provider="openai"  
    )  
    print("file content=", content)  
    

## **Supported Providers** :​

### OpenAI​

### [Azure OpenAI](/docs/providers/azure#azure-batches-api)​

### [Vertex AI](/docs/providers/vertex#batch-apis)​

## [Swagger API Reference](https://litellm-api.up.railway.app/#/files)​

  * Quick Start
  * **Supported Providers** :
    * OpenAI
    * Azure OpenAI
    * Vertex AI
  * Swagger API Reference