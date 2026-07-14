from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlmodel import Session, select
from typing import Annotated, List
from contextlib import asynccontextmanager

import uuid
import io
import pypdf

# Import our local modules
from app.database.database import create_db_and_tables, get_session
from app.modules.jobs.modules import Joblisting, AnalysisRequest
from app.ai import get_ai_provider, AIProvider
from app.services.storage import init_storage, get_s3_client
from app.core.config import settings


# LIFESPAN CONTEXT MANAGER
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Startup: Creating database tables...")
    create_db_and_tables()

    print("Startup: Checking Object Storage....")
    init_storage()

    yield

    print("Shutting down...")


app = FastAPI(
    title="ResumeRoast",
    description="This is an AI-powered ATS Resume Analyzer",
    version="1.0.0",
    lifespan=lifespan
)

# Dependency Injection
SessionDep = Annotated[Session, Depends(get_session)]
AIDep = Annotated[AIProvider, Depends(get_ai_provider)]


# -----------------------------
# Root
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "Welcome to ResumeRoast API 🚀"
    }


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "message": "ResumeRoast API is running smoothly!"
    }


# -----------------------------
# Job Routes
# -----------------------------
@app.post("/jobs", response_model=Joblisting)
def create_job(job: Joblisting, session: SessionDep):
    """Create a new job listing"""

    session.add(job)
    session.commit()
    session.refresh(job)

    return job


@app.get("/jobs", response_model=List[Joblisting])
def list_jobs(session: SessionDep):
    """Retrieve all job listings"""

    statement = select(Joblisting)
    jobs = session.exec(statement).all()

    return jobs


# -----------------------------
# Resume Analysis
# -----------------------------
@app.post("/analyze")
async def analyze_resume_text(request: AnalysisRequest, ai: AIDep):
    """
    Sends raw resume text to configured AI provider.
    """

    prompts = f"""
You are an expert tech recruiter.

Analyze the following resume against a generic Senior Developer role.

Return your response in this exact JSON format:

{{
    "score": (integer 0-100),
    "critique": (string, concise summary of strengths and weaknesses)
}}

Resume Text:

{request.text}
"""

    analysis = await ai.analyze_text(prompts)

    return {
        "analysis": analysis
    }


# -----------------------------
# Resume Upload
# -----------------------------
@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Accepts a PDF file, validates it, extracts text,
    and uploads it to MinIO.
    """

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Corrupt or invalid PDF file."
        )

    await file.seek(0)

    content = await file.read()

    try:
        pdf_reader = pypdf.PdfReader(io.BytesIO(content))

        extracted_text = ""

        for page in pdf_reader.pages:
            extracted_text += page.extract_text() or ""

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to extract text: {str(e)}"
        )

    file_id = str(uuid.uuid4())
    s3_key = f"{file_id}.pdf"

    try:
        s3 = get_s3_client()

        s3.put_object(
            Bucket=settings.MINIO_BUCKET,
            Key=s3_key,
            Body=content,
            ContentType="application/pdf"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Storage Error: {str(e)}"
        )

    return {
        "file_id": file_id,
        "filename": file.filename,
        "s3_key": s3_key,
        "extracted_text_preview": extracted_text[:200] + "..."
    }