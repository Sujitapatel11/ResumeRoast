CareerOS Master Blueprint
Part 7 – AI Architecture
1. AI Philosophy
CareerOS is not an AI chatbot. AI is an infrastructure layer that powers intelligent features.
Business logic always stays inside CareerOS.
2. AI Provider Factory
All requests pass through one Provider Factory.
CareerOS fi AI Factory fi Gemini / GPT / Claude / Groq / DeepSeek / Ollama.
No module talks directly to an LLM.
3. Provider Responsibilities
Gemini: General analysis and reasoning.
GPT: Advanced writing and complex reasoning.
Claude: Long-document processing.
Groq: Fast inference.
DeepSeek: Cost-effective reasoning.
Ollama: Local/private inference.
4. AI Routing Strategy
Choose provider based on:
• Feature type
• Cost
• Latency
• User subscription
• Provider availability
Fallback automatically if a provider fails.
5. Prompt Management
Store prompts as versioned templates.
Separate system prompts, task prompts and output schemas.
Never hardcode prompts inside routers.
6. Structured Output
Require JSON responses wherever possible.
Validate responses before using them.
Reject malformed outputs and retry if needed.
7. AI Safety
Validate user input.
Limit prompt injection.
Filter harmful content.
Protect API keys with environment variables.
Log failures without exposing sensitive data.
8. Caching
Cache repeated AI responses using Redis when appropriate to reduce latency and API costs.
9. Cost Optimization
Use cheaper models for simple tasks.
Reserve premium models for high-value features.
Track token usage and per-feature cost.
10. Future Evolution
Support model benchmarking, prompt A/B testing, fine-tuned models and self-hosted inference
without changing application modules.
11. CTO Decision Record
Accepted:
AI Provider Factory
Prompt versioning
Structured JSON output
Provider fallback
Environment-based configuration
Rejected:
Vendor lock-in
Hardcoded prompts
Single-provider dependency
Business logic inside prompt