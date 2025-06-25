# /moderations | liteLLM

On this page

### Usage​

  * LiteLLM Python SDK
  * LiteLLM Proxy Server

    
    
    from litellm import moderation  
      
    response = moderation(  
        input="hello from litellm",  
        model="text-moderation-stable"  
    )  
    

For `/moderations` endpoint, there is **no need to specify`model` in the request or on the litellm config.yaml**

Start litellm proxy server
    
    
    litellm  
    

  * OpenAI Python SDK
  * Curl Request

    
    
    from openai import OpenAI  
      
    # set base_url to your proxy server  
    # set api_key to send to proxy server  
    client = OpenAI(api_key="<proxy-api-key>", base_url="http://0.0.0.0:4000")  
      
    response = client.moderations.create(  
        input="hello from litellm",  
        model="text-moderation-stable" # optional, defaults to `omni-moderation-latest`  
    )  
      
    print(response)  
    
    
    
    curl --location 'http://0.0.0.0:4000/moderations' \  
        --header 'Content-Type: application/json' \  
        --header 'Authorization: Bearer sk-1234' \  
        --data '{"input": "Sample text goes here", "model": "text-moderation-stable"}'  
    

## Input Params​

LiteLLM accepts and translates the [OpenAI Moderation params](https://platform.openai.com/docs/api-reference/moderations) across all supported providers.

### Required Fields​

  * `input`: _string or array_ \- Input (or inputs) to classify. Can be a single string, an array of strings, or an array of multi-modal input objects similar to other models.
    * If string: A string of text to classify for moderation
    * If array of strings: An array of strings to classify for moderation
    * If array of objects: An array of multi-modal inputs to the moderation model, where each object can be:
      * An object describing an image to classify with:
        * `type`: _string, required_ \- Always `image_url`
        * `image_url`: _object, required_ \- Contains either an image URL or a data URL for a base64 encoded image
      * An object describing text to classify with:
        * `type`: _string, required_ \- Always `text`
        * `text`: _string, required_ \- A string of text to classify

### Optional Fields​

  * `model`: _string (optional)_ \- The moderation model to use. Defaults to `omni-moderation-latest`.

## Output Format​

Here's the exact json output and type you can expect from all moderation calls:

[**LiteLLM follows OpenAI's output format**](https://platform.openai.com/docs/api-reference/moderations/object)
    
    
    {  
      "id": "modr-AB8CjOTu2jiq12hp1AQPfeqFWaORR",  
      "model": "text-moderation-007",  
      "results": [  
        {  
          "flagged": true,  
          "categories": {  
            "sexual": false,  
            "hate": false,  
            "harassment": true,  
            "self-harm": false,  
            "sexual/minors": false,  
            "hate/threatening": false,  
            "violence/graphic": false,  
            "self-harm/intent": false,  
            "self-harm/instructions": false,  
            "harassment/threatening": true,  
            "violence": true  
          },  
          "category_scores": {  
            "sexual": 0.000011726012417057063,  
            "hate": 0.22706663608551025,  
            "harassment": 0.5215635299682617,  
            "self-harm": 2.227119921371923e-6,  
            "sexual/minors": 7.107352217872176e-8,  
            "hate/threatening": 0.023547329008579254,  
            "violence/graphic": 0.00003391829886822961,  
            "self-harm/intent": 1.646940972932498e-6,  
            "self-harm/instructions": 1.1198755256458526e-9,  
            "harassment/threatening": 0.5694745779037476,  
            "violence": 0.9971134662628174  
          }  
        }  
      ]  
    }  
      
    

## **Supported Providers**​

Provider  
---  
OpenAI  
  
  * Usage
  * Input Params
    * Required Fields
    * Optional Fields
  * Output Format
  * **Supported Providers**