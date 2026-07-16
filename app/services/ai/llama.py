import httpx

from app.core.config import settings


class LlamaProvider:
    def __init__(self):
        self.url = settings.OLLAMA_BASE_URL
        self.model_name = "llama3.2:1b"

    async def analyze_text(self, prompt: str) -> str:
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    self.url,
                    json=payload,
                    timeout=60.0,
                )

                response.raise_for_status()

                data = response.json()

                return data.get(
                    "response",
                    "No response from OLLAMA",
                )

            except httpx.RequestError as e:
                return f"OLLAMA Request Error: {str(e)}"