from google import genai

from app.core.config import settings


class GeminiProvider:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model = "gemini-flash-latest"

    async def analyze_text(self, prompt: str) -> str:
        try:
            response = await self.client.aio.models.generate_content(
                model=self.model,
                contents=prompt,
            )
            return response.text

        except Exception as e:
            return f"Gemini Error: {str(e)}"