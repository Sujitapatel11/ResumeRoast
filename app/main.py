from fastapi import FastAPI

app = FastAPI(
    title="ResumeRoast",
    description="This is an AI-powered ATS Resume Analyzer",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to ResumeRoast API 🚀"
    }