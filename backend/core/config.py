from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Any
from pydantic import field_validator


class Config(BaseSettings):
    # Название проекта
    PROJECT_NAME: str = "ProteinApp"

    # URL подключения к PostgreSQL (async)
    DATABASE_URL: str = "postgresql+asyncpg://user:password@host:5432/db_name"

    # Разрешённые источники CORS
    ALLOWED_ORIGINS: str = "*"
    
    @property
    def allowed_origins_list(self):
        return [i.strip() for i in self.ALLOWED_ORIGINS.split(",") if i.strip()]


    # Секретный ключ для токенов, шифрования и т.д.
    SECRET_KEY: str = "supersecret"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Время жизни токена в минутах
    # Флаг отладки
    DEBUG: bool = False

    # Настройки сервера
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000

    SSL_KEYFILE: str = "key.pem"
    SSL_CERTFILE: str = "cert.pem"

    # Настройки источника конфигурации
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# Экземпляр, который ты импортируешь в main.py и других модулях
config = Config()