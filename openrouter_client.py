import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_BASE = os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")
MODEL_NAME = os.getenv("OPENROUTER_MODEL_NAME", "google/gemini-2.0-flash-001")

if not OPENROUTER_API_KEY:
    raise ValueError("Please set the OPENROUTER_API_KEY environment variable.")

def get_llm(model: str = None):
    """
    Create a LangChain OpenAI-compatible client for OpenRouter.
    Reads model and API base from environment if not supplied.
    """
    return ChatOpenAI(
        openai_api_base=OPENROUTER_API_BASE,
        openai_api_key=OPENROUTER_API_KEY,
        model=model or MODEL_NAME,
    )

def ask_gemini(prompt: str, model: str = None) -> str:
    """
    Sends the prompt to the configured OpenRouter Gemini model and returns the content.
    """
    llm = get_llm(model)
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    prompt = "What are the benefits of using OpenRouter with Google Gemini models?"
    answer = ask_gemini(prompt)
    print("Gemini says:", answer)
