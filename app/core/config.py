from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "micromosaic"
    database_url: str = "sqlite:///micromosaic.db"
    secret_key: str = "8AF328BF39BC3583D7D2943A51EFC"

    class Config:
        env_file = ".env"

settings = Settings()