from app.core.config import settings

from app.services.ai.provider import AIProvider
from app.services.ai.gemini import GeminiProvider
from app.services.ai.llama import LlamaProvider


def get_ai_provider() -> AIProvider:
    if settings.AI_MODE == "local":
        return LlamaProvider()

    return GeminiProvider()