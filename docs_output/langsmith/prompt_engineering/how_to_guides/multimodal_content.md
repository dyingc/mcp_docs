# Include multimodal content in a prompt | 🦜️🛠️ LangSmith

On this page

Some applications are based around multimodal content, like a chatbot that can answer questions about a PDF or image. In these cases, you'll want to include multimodal content in your prompt and test the model's ability to answer questions about the content.

The LangSmith Playground supports two methods for incorporating multimodal content in your prompts:

  1. Inline content: Embed static files (images, PDFs, audio) directly in your prompt. This is ideal when you want to consistently include the same multimodal content across all uses of the prompt. For example, you might include a reference image that helps ground the model's responses.
  2. Template variables: Create dynamic placeholders for attachments that can be populated with different content each time. This approach offers more flexibility, allowing you to:
     * Test how the model handles different inputs
     * Create reusable prompts that work with varying content

note

Not all models support multimodal content. Before using multimodal features in the playground, make sure your selected model supports the file types you want to use.

## Inline content​

Click the file icon in the message where you want to add multimodal content. Under the `Upload content` tab, you can upload a file and include it inline in the prompt.

![](/assets/images/upload_inline_multimodal_content-d03b52f53c7d1cf2803a77cd2de13997.png)

## Template variables​

Click the file icon in the message where you want to add multimodal content. Under the `Template variables` tab, you can create a template variable for a specific attachment type. Currently, only images, PDFs, and audio files (.wav, .mp3) are supported.

![](/assets/images/template_variable_multimodal_content-862ede6be2448dca42229792795b153d.png)

## Populate the template variable​

Once you've added a template variable, you can provide content for it using the panel on the right side of the screen. Simply click the `+` button to upload or select content that will be used to populate the template variable.

![](/assets/images/manual_prompt_multimodal-46db4dbdfc35eebbf2478f4efb5c9858.png)

## Run an evaluation​

After testing out your prompt manually, you can [run an evaluation](/evaluation/how_to_guides/evaluate_with_attachments?mode=ui) to see how the prompt performs over a golden dataset of examples.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Inline content
  * Template variables
  * Populate the template variable
  * Run an evaluation

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)