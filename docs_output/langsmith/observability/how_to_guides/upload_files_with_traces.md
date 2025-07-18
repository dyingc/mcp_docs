# Upload files with traces | 🦜️🛠️ LangSmith

Recommended Reading

Before diving into this content, it would be helpful to read the following guides:

  * [Trace with LangSmith using the traceable decorator or wrapper](/observability/how_to_guides/annotate_code#use-traceable--traceable)

Minimum SDK Versions

The following features are available in the following SDK versions:

  * Python SDK: >=0.1.141
  * JS/TS SDK: >=0.2.5

LangSmith supports uploading binary files (such as images, audio, videos, PDFs, and CSVs) with your traces. This is particularly useful when working with LLM pipelines using multimodal inputs or outputs.

In both the Python and TypeScript SDKs, attachments can be added to your traces by specifying the MIME type and binary content of each file. This guide explains how to define and trace attachments using the `Attachment` type in Python and `Uint8Array` / `ArrayBuffer` in TypeScript.

  * Python
  * TypeScript

In the Python SDK, you can use the `Attachment` type to add files to your traces. Each `Attachment` requires:

  * `mime_type` (str): The MIME type of the file (e.g., `"image/png"`).
  * `data` (bytes | Path): The binary content of the file, or the file path.

You can also define an attachment with a tuple tuple of the form `(mime_type, data)` for convenience. 

Simply decorate a function with `@traceable` and include your `Attachment` instances as arguments. Note that to use the file path instead of the raw bytes, you need to set the `dangerously_allow_filesystem` flag to `True` in your traceable decorator.
    
    
    from langsmith import traceable  
    from langsmith.schemas import Attachment  
    from pathlib import Path  
    import os  
      
      
    # Must set dangerously_allow_filesystem to True if you want to use file paths  
    @traceable(dangerously_allow_filesystem=True)  
    def trace_with_attachments(  
      val: int,  
      text: str,  
      image: Attachment,  
      audio: Attachment,  
      video: Attachment,  
      pdf: Attachment,  
      csv: Attachment,  
    ):  
      return f"Processed: {val}, {text}, {len(image.data)}, {len(audio.data)}, {len(video.data)}, {len(pdf.data), {len(csv.data)}}"  
      
      
    # Helper function to load files as bytes  
    def load_file(file_path: str) -> bytes:  
      with open(file_path, "rb") as f:  
          return f.read()  
      
      
    # Load files and create attachments  
    image_data = load_file("my_image.png")  
    audio_data = load_file("my_mp3.mp3")  
    video_data = load_file("my_video.mp4")  
    pdf_data = load_file("my_document.pdf")  
    image_attachment = Attachment(mime_type="image/png", data=image_data)  
    audio_attachment = Attachment(mime_type="audio/mpeg", data=audio_data)  
    video_attachment = Attachment(mime_type="video/mp4", data=video_data)  
    pdf_attachment = ("application/pdf", pdf_data) # Can just define as tuple of (mime_type, data)  
    csv_attachment = Attachment(mime_type="text/csv", data=Path(os.getcwd()) / "my_csv.csv")  
      
    # Define other parameters  
      
    val = 42  
    text = "Hello, world!"  
      
    # Call the function with traced attachments  
      
    result = trace_with_attachments(  
    val=val,  
    text=text,  
    image=image_attachment,  
    audio=audio_attachment,  
    video=video_attachment,  
    pdf=pdf_attachment,  
    csv=csv_attachment,  
    )  
    

In the TypeScript SDK, you can add attachments to traces by using `Uint8Array` or `ArrayBuffer` as data types. Each attachment's MIME type is specified within `extractAttachments`:

  * `Uint8Array`: Useful for handling binary data directly.
  * `ArrayBuffer`: Represents fixed-length binary data, which can be converted to `Uint8Array` as needed.

Wrap your function with `traceable` and include your attachments within the `extractAttachments` option.

In the TypeScript SDK, the `extractAttachments` function is an optional parameter in the `traceable` configuration. When the traceable-wrapped function is invoked, it extracts binary data (e.g., images, audio files) from your inputs and logs them alongside other trace data, specifying their MIME types.

Note that you cannot directly pass in a file path in the TypeScript SDK, as accessing local files is not supported in all runtime environments.
    
    
    type AttachmentData = Uint8Array | ArrayBuffer;
    type Attachments = Record<string, [string, AttachmentData]>;
    
    extractAttachments?: (
    ...args: Parameters<Func>
    ) => [Attachments | undefined, KVMap];
    
    
    
    import { traceable } from "langsmith/traceable";  
      
    const traceableWithAttachments = traceable(  
    (  
    val: number,  
    text: string,  
    attachment: Uint8Array,  
    attachment2: ArrayBuffer,  
    attachment3: Uint8Array,  
    attachment4: ArrayBuffer,  
    attachment5: Uint8Array,  
    ) =>  
    `Processed: ${val}, ${text}, ${attachment.length}, ${attachment2.byteLength}, ${attachment3.length}, ${attachment4.byteLength}, ${attachment5.byteLength}`,  
    {  
    name: "traceWithAttachments",  
    extractAttachments: (  
    val: number,  
    text: string,  
    attachment: Uint8Array,  
    attachment2: ArrayBuffer,  
    attachment3: Uint8Array,  
    attachment4: ArrayBuffer,  
    attachment5: Uint8Array,  
    ) => [  
    {  
    "image inputs": ["image/png", attachment],  
    "mp3 inputs": ["audio/mpeg", new Uint8Array(attachment2)],  
    "video inputs": ["video/mp4", attachment3],  
    "pdf inputs": ["application/pdf", new Uint8Array(attachment4)],  
    "csv inputs": ["text/csv", new Uint8Array(attachment5)]  
    },  
    { val, text },  
    ],  
    }  
    );  
      
    const fs = Deno // or Node.js fs module  
      
    const image = await fs.readFile("my_image.png"); // Uint8Array  
    const mp3Buffer = await fs.readFile("my_mp3.mp3");  
    const mp3ArrayBuffer = mp3Buffer.buffer; // Convert to ArrayBuffer  
      
    const video = await fs.readFile("my_video.mp4"); // Uint8Array  
    const pdfBuffer = await fs.readFile("my_document.pdf");  
    const pdfArrayBuffer = pdfBuffer.buffer; // Convert to ArrayBuffer  
    const csv = await fs.readFile("test-vals.csv"); // Uint8Array  
      
    // Define example parameters  
    const val = 42;  
    const text = "Hello, world!";  
      
    // Call traceableWithAttachments with the files  
    const result = await traceableWithAttachments(val, text, image, mp3ArrayBuffer, video, pdfArrayBuffer, csv);  
    

Here is how the above would look in the LangSmith UI. You can expand each attachment to view its contents. ![](/assets/images/trace_with_attachments-fcee2de7720714915d3d264b61f2064d.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)