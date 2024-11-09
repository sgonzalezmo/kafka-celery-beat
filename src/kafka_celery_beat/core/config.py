from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application name
    APP_NAME: str = "kafka-celery-beat"
    # Variable for timezone
    TIMEZONE: str = "Europe/Madrid"
    # Celery environment variables
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    # Kafka read message schedule
    KAFKA_READ_MESSAGES_SCHEDULE: float = 60.0

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
