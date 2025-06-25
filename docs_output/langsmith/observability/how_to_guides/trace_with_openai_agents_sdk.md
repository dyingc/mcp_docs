# Trace with OpenAI Agents SDK | 🦜️🛠️ LangSmith

On this page

The [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) allows you to build agentic applications powered by OpenAI's models.

## Installation​

info

Requires Python SDK version `langsmith>=0.3.15`.

Install LangSmith with OpenAI Agents support:
    
    
    pip install "langsmith[openai-agents]"  
    

This will install both the LangSmith library and the OpenAI Agents SDK.

## Quick Start​

You can integrate LangSmith tracing with the OpenAI Agents SDK by using the `OpenAIAgentsTracingProcessor` class.
    
    
    import asyncio  
    from agents import Agent, Runner, set_trace_processors  
    from langsmith.wrappers import OpenAIAgentsTracingProcessor  
      
    async def main():  
        agent = Agent(  
            name="Captain Obvious",  
            instructions="You are Captain Obvious, the world's most literal technical support agent.",  
        )  
      
        question = "Why is my code failing when I try to divide by zero? I keep getting this error message."  
        result = await Runner.run(agent, question)  
        print(result.final_output)  
      
    if __name__ == "__main__":  
        set_trace_processors([OpenAIAgentsTracingProcessor()])  
        asyncio.run(main())  
    

The agent's execution flow, including all spans and their details, will be logged to LangSmith.

![OpenAI Agents SDK Trace in LangSmith](/assets/images/agent_trace-e915e199cfb66f774994e2db42420b27.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Installation
  * Quick Start

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)