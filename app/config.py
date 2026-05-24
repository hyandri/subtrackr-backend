from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME : str = "Subtrackr"
    ENVIRONMENT: str = "development"
    DEBUG : bool = True

    #database
    DATABASE_URL : str

    #JWT Authentication
    SECRET_KEY : str
    ALGORITHM : str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

def get_settings():
    return Settings()