# Log multimodal traces | 🦜️🛠️ LangSmith

LangSmith supports logging and rendering images as part of traces. This is currently supported for multimodal LLM runs.

In order to log images, use `wrap_openai`/ `wrapOpenAI` in Python or TypeScript respectively and pass an image URL or base64 encoded image as part of the input.

  * Python
  * TypeScript

    
    
    from openai import OpenAI  
    from langsmith.wrappers import wrap_openai  
      
    client = wrap_openai(OpenAI())  
      
    response = client.chat.completions.create(  
    model="gpt-4-turbo",  
    messages=[  
      {  
        "role": "user",  
        "content": [  
          {"type": "text", "text": "What’s in this image?"},  
          {  
            "type": "image_url",  
            "image_url": {  
              "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",  
            },  
          },  
        ],  
      }  
    ],  
    )  
    print(response.choices[0])  
    
    
    
    import OpenAI from "openai";  
    import { wrapOpenAI } from "langsmith/wrappers";  
      
    // Wrap the OpenAI client to automatically log traces  
    const wrappedClient = wrapOpenAI(new OpenAI());  
      
    const response = await wrappedClient.chat.completions.create({  
      model: "gpt-4-turbo",  
      messages: [  
        {  
          role: "user",  
          content: [  
            { type: "text", text: "What’s in this image?" },  
            {  
              type: "image_url",  
              image_url: {  
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",  
              },  
            },  
          ],  
        },  
      ],  
    });  
    console.log(response.choices[0]);  
    

The image will be rendered as part of the trace in the LangSmith UI.

![](/assets/images/multimodal-e77e726bc11754954d00c417a2df4276.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)