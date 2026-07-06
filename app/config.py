from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name:str = "Recipes"
    debug: bool = True

    class Config:
        anc_file = ".env"

settings = Settings()