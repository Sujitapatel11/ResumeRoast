# 🚀 ResumeRoast

> **An AI-Powered ATS Resume Analyzer & Resume Roaster built with FastAPI**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker)
![SQLModel](https://img.shields.io/badge/SQLModel-ORM-orange?style=for-the-badge)

</p>

---

# 📖 About the Project

ResumeRoast is a modern SaaS platform designed to help job seekers create ATS-friendly resumes and receive AI-powered feedback before applying for jobs.

Unlike traditional resume checkers, ResumeRoast aims to become an intelligent career assistant capable of analyzing resumes, identifying weak points, suggesting improvements, and optimizing resumes for Applicant Tracking Systems (ATS).

This project is currently under active development.

---

# 🎯 Project Vision

ResumeRoast will eventually provide:

- 📄 ATS Resume Analysis
- 🤖 AI Resume Roasting
- 📈 Resume Improvement Suggestions
- 🎯 Company-Specific Resume Optimization
- 📝 AI Resume Builder
- 📊 Resume History Dashboard
- 💳 SaaS Subscription Platform

---

# 🎓 Learning Journey

This project is being developed while following a professional FastAPI backend book.

The objective is not only to complete the project but also to understand every backend concept from first principles before building production-level SaaS features.

Every chapter is documented and implemented step by step.

---

# ✅ Progress So Far

## Chapter 1 — Project Setup

### Completed

- Python Virtual Environment
- Git & GitHub Repository
- Project Structure
- Development Environment

### Concepts Learned

- Virtual Environments
- Project Organization
- Git Workflow
- Dependency Management

---

## Chapter 2 — Core FastAPI Construction

### Completed

- FastAPI Application Setup
- Routing
- Health Check Endpoint
- Dependency Injection Basics

### Concepts Learned

- FastAPI Architecture
- Request Handling
- Path Operations
- Application Lifespan

---

## Chapter 3 — Data Layer

### Completed

- SQLModel Integration
- Pydantic Models
- Database Sessions
- PostgreSQL Connection
- Create Job API
- Read Jobs API

### Why SQLModel?

SQLModel combines the strengths of SQLAlchemy and Pydantic into a single developer-friendly library.

It allows the same model to be used for:

- Database Tables
- Data Validation
- API Serialization

This significantly reduces duplicate code and improves maintainability.

---

### Why PostgreSQL?

PostgreSQL was selected because it is:

- Open Source
- ACID Compliant
- Production Ready
- Highly Scalable
- Industry Standard
- Excellent with FastAPI

---

# 🏗️ Current Architecture

```text
                Client
                   │
                   ▼
             FastAPI Backend
                   │
                   ▼
               SQLModel ORM
                   │
                   ▼
            PostgreSQL Database
```

---

# 🛠️ Technology Stack

## Backend

- Python 3.14
- FastAPI
- SQLModel
- SQLAlchemy
- Pydantic

## Database

- PostgreSQL

## Infrastructure

- Docker
- Docker Compose
- Redis
- MinIO

## Development Environment

- WSL2
- Ubuntu
- VS Code
- Git
- GitHub

---

# 📂 Project Structure

```text
ResumeRoast/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   └── models.py
│
├── docker-compose.yaml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ✅ Features Implemented

- [x] FastAPI Project Setup
- [x] PostgreSQL Integration
- [x] SQLModel ORM
- [x] Docker Infrastructure
- [x] Create Job API
- [x] Read Jobs API

---

# 🗺️ Development Roadmap

## Backend Foundation

- [x] Project Setup
- [x] FastAPI Basics
- [x] Data Layer
- [ ] Update Job API
- [ ] Delete Job API
- [ ] Authentication
- [ ] JWT Authorization
- [ ] Alembic Migrations

---

## Resume Engine

- [ ] Resume Upload
- [ ] Resume Storage
- [ ] Resume Parsing
- [ ] Resume Versioning

---

## AI Engine

- [ ] ATS Score Generation
- [ ] Resume Roasting
- [ ] AI Resume Suggestions
- [ ] Resume Rewriting
- [ ] Company-Specific Optimization

---

## SaaS Platform

- [ ] User Authentication
- [ ] Dashboard
- [ ] Subscription Plans
- [ ] Payment Gateway
- [ ] User Analytics

---

# 🚀 Running the Project

Clone the repository

```bash
git clone https://github.com/Sujitapatel11/ResumeRoast.git
```

Navigate to the project

```bash
cd ResumeRoast
```

Activate the virtual environment

```bash
source .venv/bin/activate
```

Start Docker services

```bash
docker compose up -d
```

Run the FastAPI application

```bash
uvicorn app.main:app --reload --port 8001
```

API Documentation

```
http://127.0.0.1:8001/docs
```

---

# 📌 Current Status

🚧 Active Development

The backend foundation is currently being built by following a structured FastAPI learning roadmap.

Once the backend architecture is complete, AI-powered resume analysis and SaaS features will be implemented.

---

# 👩‍💻 Author

**Sujita Patel**

Engineering Student • Backend Developer • AI Engineer • SaaS Builder

GitHub: **https://github.com/Sujitapatel11**