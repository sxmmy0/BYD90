"""
Core configuration settings for BYD90 Backend
"""
import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import EmailStr, PostgresDsn, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 30 days

    # Server Settings
    PROJECT_NAME: str = "BYD90 - Beyond Ninety"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "AI-powered athlete performance platform"

    # CORS Settings
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(
        cls, v: Union[str, List[str], None]
    ) -> List[str]:
        if v is None:
            return ["http://localhost:3000", "http://127.0.0.1:3000"]
        if isinstance(v, str) and v.strip():
            if not v.startswith("["):
                return [i.strip() for i in v.split(",") if i.strip()]
            return [v]
        elif isinstance(v, list):
            return v
        return ["http://localhost:3000", "http://127.0.0.1:3000"]

    # Database Settings
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "byd90_user"
    POSTGRES_PASSWORD: str = "byd90_password"
    POSTGRES_DB: str = "byd90_db"
    POSTGRES_PORT: str = "5432"
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(
        cls, v: Optional[str], values: Dict[str, Any]
    ) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            username=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=int(values.get("POSTGRES_PORT", "5432")),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    # Redis Settings
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: Optional[str] = None

    # Email Settings
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    # AI/ML Settings
    OPENAI_API_KEY: Optional[str] = None
    HUGGING_FACE_API_KEY: Optional[str] = None

    # AWS Settings
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    AWS_REGION: str = "us-east-1"
    AWS_S3_BUCKET: Optional[str] = None

    # Security Settings
    ALGORITHM: str = "HS256"
    PASSWORD_MIN_LENGTH: int = 8

    # Application Settings
    USERS_OPEN_REGISTRATION: bool = True
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48

    # File Upload Settings
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_IMAGE_EXTENSIONS: List[str] = ["jpg", "jpeg", "png", "gif", "webp"]

    # Athlete/Coach Settings
    SUPPORTED_SPORTS: List[str] = [
        "football",
        "basketball",
        "soccer",
        "tennis",
        "volleyball",
        "baseball",
        "hockey",
        "swimming",
        "track_field",
        "golf",
    ]

    # AI Recommendation Settings
    RECOMMENDATION_CACHE_TTL: int = 3600  # 1 hour
    MAX_RECOMMENDATIONS_PER_REQUEST: int = 10

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
