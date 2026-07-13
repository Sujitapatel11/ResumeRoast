#Purpose: Application configuration and Env Vars
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    APP_NAME: str = "ResumeRoast"
    DEBUG: bool = True

    DATABASE_URL: str = "postgresql://resume_user:resume_pass@localhost:5433/resume_db"

    AI_MODE: str = "gemini"
    GEMINI_API_KEY: str = "YOUR_GEMINI_API_KEY"

    OLLAMA_BASE_URL: str = "http://host.docker.internal:11434/api/generate"

    # MinIO
    MINIO_ENDPOINT: str = "http://localhost:9000"
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin"
    MINIO_BUCKET: str = "resumes"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
settings = Settings()