from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str   #the name of the project
    SQLALCHEMY_DATABASE_URI:str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    class Config:
        env_file = ".env"

settings = Settings()