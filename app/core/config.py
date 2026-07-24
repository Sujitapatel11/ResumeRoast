#Purpose: Application configuration and Env Vars
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    APP_NAME: str = "CareerOS"
    DEBUG: bool = True

    DATABASE_URL: str = "postgresql+psycopg://careeros:password@localhost:5433/careeros"
    SQLITE_URL: str = "sqlite:///./careeros.db"
    
    # JWT Auth
    SECRET_KEY: str = "careeros_super_secret_jwt_key_2026_change_in_production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day

    # Redis
    REDIS_URL: str = "redis://localhost:6380/0"

    AI_MODE: str = "mock"
    GEMINI_API_KEY: str = "YOUR_GEMINI_API_KEY"

    OLLAMA_BASE_URL: str = "http://host.docker.internal:11434/api/generate"

    # MinIO
    MINIO_ENDPOINT: str = "http://localhost:9000"
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin"
    MINIO_BUCKET: str = "careeros"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
settings = Settings()