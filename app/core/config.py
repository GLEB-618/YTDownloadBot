from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    BOT_TOKEN: str
    TELEGRAM_API_BASE_URL: str
    LOG_LEVEL: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()