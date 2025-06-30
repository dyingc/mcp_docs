# ElevenLabs | liteLLM

On this page

ElevenLabs provides high-quality AI voice technology, including speech-to-text capabilities through their transcription API.

Property| Details  
---|---  
Description| ElevenLabs offers advanced AI voice technology with speech-to-text transcription capabilities that support multiple languages and speaker diarization.  
Provider Route on LiteLLM| `elevenlabs/`  
Provider Doc| [ElevenLabs API ↗](https://elevenlabs.io/docs/api-reference)  
Supported Endpoints| `/audio/transcriptions`  
  
## Quick Start​

### LiteLLM Python SDK​

  * Basic Usage
  * Advanced Features
  * Async Usage

Basic audio transcription with ElevenLabs
    
    
    import litellm  
      
    # Transcribe audio file  
    with open("audio.mp3", "rb") as audio_file:  
        response = litellm.transcription(  
            model="elevenlabs/scribe_v1",  
            file=audio_file,  
            api_key="your-elevenlabs-api-key"  # or set ELEVENLABS_API_KEY env var  
        )  
      
    print(response.text)  
    

Audio transcription with advanced features
    
    
    import litellm  
      
    # Transcribe with speaker diarization and language specification  
    with open("audio.wav", "rb") as audio_file:  
        response = litellm.transcription(  
            model="elevenlabs/scribe_v1",  
            file=audio_file,  
            language="en",           # Language hint (maps to language_code)  
            temperature=0.3,         # Control randomness in transcription  
            diarize=True,           # Enable speaker diarization  
            api_key="your-elevenlabs-api-key"  
        )  
      
    print(f"Transcription: {response.text}")  
    print(f"Language: {response.language}")  
      
    # Access word-level timestamps if available  
    if hasattr(response, 'words') and response.words:  
        for word_info in response.words:  
            print(f"Word: {word_info['word']}, Start: {word_info['start']}, End: {word_info['end']}")  
    

Async audio transcription
    
    
    import litellm  
    import asyncio  
      
    async def transcribe_audio():  
        with open("audio.mp3", "rb") as audio_file:  
            response = await litellm.atranscription(  
                model="elevenlabs/scribe_v1",  
                file=audio_file,  
                api_key="your-elevenlabs-api-key"  
            )  
          
        return response.text  
      
    # Run async transcription  
    result = asyncio.run(transcribe_audio())  
    print(result)  
    

### LiteLLM Proxy​

#### 1\. Configure your proxy​

  * config.yaml
  * Environment Variables

ElevenLabs configuration in config.yaml
    
    
    model_list:  
      - model_name: elevenlabs-transcription  
        litellm_params:  
          model: elevenlabs/scribe_v1  
          api_key: os.environ/ELEVENLABS_API_KEY  
      
    general_settings:  
      master_key: your-master-key  
    

Required environment variables
    
    
    export ELEVENLABS_API_KEY="your-elevenlabs-api-key"  
    export LITELLM_MASTER_KEY="your-master-key"  
    

#### 2\. Start the proxy​

Start LiteLLM proxy server
    
    
    litellm --config config.yaml  
      
    # Proxy will be available at http://localhost:4000  
    

#### 3\. Make transcription requests​

  * Curl
  * OpenAI Python SDK
  * JavaScript/Node.js

Audio transcription with curl
    
    
    curl http://localhost:4000/v1/audio/transcriptions \  
      -H "Authorization: Bearer $LITELLM_API_KEY" \  
      -H "Content-Type: multipart/form-data" \  
      -F file="@audio.mp3" \  
      -F model="elevenlabs-transcription" \  
      -F language="en" \  
      -F temperature="0.3"  
    

Using OpenAI SDK with LiteLLM proxy
    
    
    from openai import OpenAI  
      
    # Initialize client with your LiteLLM proxy URL  
    client = OpenAI(  
        base_url="http://localhost:4000",  
        api_key="your-litellm-api-key"  
    )  
      
    # Transcribe audio file  
    with open("audio.mp3", "rb") as audio_file:  
        response = client.audio.transcriptions.create(  
            model="elevenlabs-transcription",  
            file=audio_file,  
            language="en",  
            temperature=0.3,  
            # ElevenLabs-specific parameters  
            diarize=True,  
            speaker_boost=True,  
            custom_vocabulary="technical,AI,machine learning"  
        )  
      
    print(response.text)  
    

Audio transcription with JavaScript
    
    
    import OpenAI from 'openai';  
    import fs from 'fs';  
      
    const openai = new OpenAI({  
      baseURL: 'http://localhost:4000',  
      apiKey: 'your-litellm-api-key'  
    });  
      
    async function transcribeAudio() {  
      const response = await openai.audio.transcriptions.create({  
        file: fs.createReadStream('audio.mp3'),  
        model: 'elevenlabs-transcription',  
        language: 'en',  
        temperature: 0.3,  
        diarize: true,  
        speaker_boost: true  
      });  
      
      console.log(response.text);  
    }  
      
    transcribeAudio();  
    

## Response Format​

ElevenLabs returns transcription responses in OpenAI-compatible format:

Example transcription response
    
    
    {  
      "text": "Hello, this is a sample transcription with multiple speakers.",  
      "task": "transcribe",  
      "language": "en",  
      "words": [  
        {  
          "word": "Hello",  
          "start": 0.0,  
          "end": 0.5  
        },  
        {  
          "word": "this",  
          "start": 0.5,  
          "end": 0.8  
        }  
      ]  
    }  
    

### Common Issues​

  1. **Invalid API Key** : Ensure `ELEVENLABS_API_KEY` is set correctly

  * Quick Start
    * LiteLLM Python SDK
    * LiteLLM Proxy
  * Response Format
    * Common Issues