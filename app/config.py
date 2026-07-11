#Purpose: Application configuration and Env Vars
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    #APPP CONFIG
    APP_NAME: str = "ResumeRoast"
    DEBUG: bool = True
    #database confug
    DATABASE_URL: str = "postgresql://resume_user:resume_pass@localhost:5433/resume_db"
    #AI Config
    #Modes: "Gemini" or "local"
    AI_MODE: str = "gemini"
    #Gemini config (Get key from aistudio.google.com)
    GEMINI_API_KEY: str = "YOUR_GEMINI_API_KEY"
    #Local AI config
    OLLAMA_BASE_URL: str = "http://host.docker.internal:11434/api/generate"
    model_config = SettingsConfigDict(env_files=".env", extra="ignore")
#Initialize settings
settings = Settings()