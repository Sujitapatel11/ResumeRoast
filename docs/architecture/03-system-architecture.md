CareerOS Master Blueprint
Part 3 – Complete System Architecture
1. Architecture Philosophy
CareerOS uses a Modular Monolith for V1. Modules are isolated by responsibility while sharing one
deployment. This keeps development simple and supports future migration to microservices.
2. High-Level Architecture
Client fi FastAPI API fi Business Modules fi AI Platform / PostgreSQL / MinIO / Redis fi External
AI Providers
3. Backend Architecture
Layers: Core, Database, Modules, Services, Shared, Tests. Business logic belongs in services.
Routers stay thin.
4. Frontend Architecture
React UI fi Components fi Hooks fi API Client fi Backend.
5. Module Flow
Authentication fi Profile fi Resume Intelligence fi Company Intelligence fi Roadmap fi Learning
fi Interview fi Applications fi Analytics.
6. AI Platform
All AI calls go through an AI Provider Factory that can route to Gemini, GPT, Claude, Groq,
DeepSeek or Ollama.
7. Data Layer
PostgreSQL stores structured data. MinIO stores resume files. Redis provides caching and session
acceleration.
8. Request Lifecycle
Request fi Authentication fi Validation fi Service fi Repository fi Database/AI/Storage fi
Response.
9. Dependency Rules
Modules communicate through services only. Shared code lives in shared/. Configuration belongs
in core/.
10. Folder Blueprint
CareerOS/app, core, database, modules, services, shared, tests, main.py
11. Scaling Strategy
V1 Modular Monolith fi Background Workers fi Separate AI Service fi Separate Community
Service fi Event-driven architecture when justified.
12. CTO Decision Record
Accepted: FastAPI, PostgreSQL, Redis, MinIO, AI Provider Factory, Modular Monolith. Rejected for
V1: Microservices, Kubernetes, Service Mesh, multiple databases