from typing import Protocol


class AIProvider(Protocol):
    async def analyze_text(self, prompt: str) -> str:
        ...