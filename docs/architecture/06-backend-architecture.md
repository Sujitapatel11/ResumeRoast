CareerOS Master Blueprint
Part 6 – Backend Architecture
1. Backend Philosophy
CareerOS follows Feature-First Modular Architecture. Every business capability lives inside its own
module while common infrastructure remains centralized.
2. Folder Structure
CareerOS/
app/
core/
database/
modules/
services/
shared/
tests/
main.py
3. Core Layer
config.py
security.py
dependencies.py
middleware.py
logging.py
exceptions.py
Purpose: configuration, authentication, middleware and application-wide infrastructure.
4. Database Layer
session.py
base.py
repositories/
migrations/
Purpose: database session management, repositories and schema migrations.
5. Module Layer
auth/
users/
profiles/
resumes/
companies/
roadmap/
learning/
interviews/
applications/
community/
analytics/
subscriptions/
notifications/
Each module owns its routers, schemas, models and business services.
6. Services Layer
ai/
storage/
pdf/
email/
search/
notification/
Purpose: reusable business services shared across modules.
7. Shared Layer
schemas/
constants/
enums/
utils/
Purpose: reusable objects with no business ownership.
8. Dependency Rules
Routers call Services.
Services use Repositories.
Repositories access Database.
Modules never directly access another module's repositories.
Shared code contains no business logic.
9. Request Flow
Client
fi Middleware
fi Router
fi Validation
fi Service
fi Repository
fi PostgreSQL / MinIO / Redis / AI
fi Response
10. Background Jobs
Long-running work such as resume analysis, notifications, report generation and future AI
processing should execute asynchronously using background workers when required.
11. Logging & Error Handling
Centralized logging.
Structured error responses.
Global exception handlers.
Correlation IDs for future production debugging.
12. Testing Strategy
Unit Tests
Integration Tests
API Tests
End-to-End Tests
Each feature must include automated tests before merging.
13. Engineering Standards
Single Responsibility Principle.
Thin Routers.
Business Logic in Services.
Repository Pattern.
Environment variables only.
No hardcoded secrets.
Consistent naming conventions.
14. CTO Decision Record
Accepted:
Feature-first modular monolith
FastAPI
SQLModel
Repository pattern
Service layer
Dependency Injection
Rejected:
Fat routers
Business logic in controllers
Shared global state
Premature microservice