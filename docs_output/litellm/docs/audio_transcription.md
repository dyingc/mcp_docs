# /audio/transcriptions | liteLLM

On this page

Use this to loadbalance across Azure + OpenAI.

## Quick Start​

### LiteLLM Python SDK​
    
    
    from litellm import transcription  
    import os   
      
    # set api keys   
    os.environ["OPENAI_API_KEY"] = ""  
    audio_file = open("/path/to/audio.mp3", "rb")  
      
    response = transcription(model="whisper", file=audio_file)  
      
    print(f"response: {response}")  
    

### LiteLLM Proxy​

### Add model to config​

  * OpenAI
  * OpenAI + Azure

    
    
    model_list:  
    - model_name: whisper  
      litellm_params:  
        model: whisper-1  
        api_key: os.environ/OPENAI_API_KEY  
      model_info:  
        mode: audio_transcription  
          
    general_settings:  
      master_key: sk-1234  
    
    
    
    model_list:  
    - model_name: whisper  
      litellm_params:  
        model: whisper-1  
        api_key: os.environ/OPENAI_API_KEY  
      model_info:  
        mode: audio_transcription  
    - model_name: whisper  
      litellm_params:  
        model: azure/azure-whisper  
        api_version: 2024-02-15-preview  
        api_base: os.environ/AZURE_EUROPE_API_BASE  
        api_key: os.environ/AZURE_EUROPE_API_KEY  
      model_info:  
        mode: audio_transcription  
      
    general_settings:  
      master_key: sk-1234  
    

### Start proxy​
    
    
    litellm --config /path/to/config.yaml   
      
    # RUNNING on http://0.0.0.0:8000  
    

### Test​

  * Curl
  * OpenAI Python SDK

    
    
    curl --location 'http://0.0.0.0:8000/v1/audio/transcriptions' \  
    --header 'Authorization: Bearer sk-1234' \  
    --form 'file=@"/Users/krrishdholakia/Downloads/gettysburg.wav"' \  
    --form 'model="whisper"'  
    
    
    
    from openai import OpenAI  
    client = openai.OpenAI(  
        api_key="sk-1234",  
        base_url="http://0.0.0.0:8000"  
    )  
      
      
    audio_file = open("speech.mp3", "rb")  
    transcript = client.audio.transcriptions.create(  
      model="whisper",  
      file=audio_file  
    )  
    

## Supported Providers​

  * OpenAI
  * Azure
  * [Fireworks AI](/docs/providers/fireworks_ai#audio-transcription)
  * [Groq](/docs/providers/groq#speech-to-text---whisper)
  * [Deepgram](/docs/providers/deepgram)

  * Quick Start
    * LiteLLM Python SDK
    * LiteLLM Proxy
    * Add model to config
    * Start proxy
    * Test
  * Supported Providers