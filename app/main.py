from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from typing import Annotated, List
from contextlib import asynccontextmanager
#Import our local modules 
from app.database import create_db_and_tables, get_session
from app.models import Joblisting, AnalysisRequest
from app.ai import get_ai_provider, AIProvider

#LIFESPAN CONTEXT MANAGER
#This run code before the app starts and after it shut down.
#we use it to create our database tables automatically on startup.
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    print("Shutting down...")

app = FastAPI(
    title="ResumeRoast",
    description="This is an AI-powered ATS Resume Analyzer",
    version="1.0.0",
    lifespan=lifespan
)
#Define a Dependency Injection type alias
#This make our path operation cleaner.
SessionDep = Annotated[Session, Depends(get_session)]
AIDep = Annotated[AIProvider, Depends(get_ai_provider)]
#Job Routes
#Create a Job (POST)
@app.post("/jobs", response_model=Joblisting)
def create_job(job: Joblisting, session: SessionDep):
    """Create a new job listing in the database"""
    session.add(job) #Add to the "Shopping cart"
    session.commit() #chrckout (save to db)
    session.refresh(job) #get the new ID form the DB
    return job 
#list all the Jobs(Get)
@app.get("/jobs", response_model=List[Joblisting])
def list_jobs(session: SessionDep):
    """
     Retreive all open job positions

    """
    #Write the query : "SELECT * FROM Joblisting"
    statement = select(Joblisting)
    jobs = session.exec(statement).all()
    return jobs
@app.get("/")
def root():
    return {
        "message": "Welcome to ResumeRoast API 🚀"
    }


# Health check endpoint
@app.get("/health")
async def health_check():
    """A simple health check endpoint to verify that the API is running."""
    return {
        "status": "ok",
        "message": "ResumeRoast API is running smoothly!"
    }
@app.post("/analyze")
async def analyze_resume_text(request: AnalysisRequest, ai: AIDep):
    """ sends rwa text to configured AI provider. 
    Enforces a strict JSON output format (Score + Critique) to match PRD requirements.
    """
    prompts = f"""
    You are expert tech recruiter. Analyze the followig resume text againts a generic Senior Developer role.
    Return your response in this exact JSON format:
    {{
        "score": (interger 0-100),
        "critique": (string, concise summary of gaps and strengths)
    }}
    Resume Text:
    {request.text}
    """
    analysis = await ai.analyze_text(prompts)
    return {"analysis": analysis}