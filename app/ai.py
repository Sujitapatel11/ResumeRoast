#The abstract AI strategy and Concrete Implemenattions 
from typing import Protocol, Any
from google import genai
import httpx
from app.config import settings
#The interface i.e protocol
#This defines the rules. Any class that implements that claims to be "AIProvider"
#MUST IMPLEMENT THE "analyze_text" method.
class AIProvider(Protocol):
    async def analyze_text(self, prompt: str) -> str: ...
    #Implemenatation will go here next
class GeminiProvider:
    def __init__(self):
        #Configure the google genai client with our API key
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model = "gemini-flash-latest"
    async def analyze_text(self, prompt: str) -> str:
        """sends the prompt t Googles cloud ai using the nw=ew google-genai SDK. uses the client.aio AsyncIO interface to avoid blocking"""
        try:
            response = await self.client.aio.models.generate_content(
                model=self.model,
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Gemini Error: {str(e)}"
#The local Implementation (0LLAMA/LLAMA 3)
class LlamaProvider:
    def __init__(self):
        self.url = settings.OLLAMA_BASE_URL
        self.model_name = "llama3.2:1b"
    async def analyze_text(self, prompt: str) -> str:
        """ sends the prompt to a local OLLAMA instance via HTTP."""
        payload ={"model": self.model_name, 
        "prompt": prompt,
        "stream": False}
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.url, json=payload, timeout=60.0)
                response.raise_for_status()
                data = response.json()
                return data.get("response", "No response from OLLAMA")
            except httpx.RequestError as e:
                return f"OLLAMA Request Error: {str(e)}"
    #THE FACTORY
    #THIS FUNCTION ACTS AS A SWIHCBOARD
def get_ai_provider() -> AIProvider:
    if settings.AI_MODE == "local":
        return LlamaProvider()
    else:
        return GeminiProvider()
        