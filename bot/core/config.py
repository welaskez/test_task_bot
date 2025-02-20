import logging

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggingConfig(BaseModel):
    level: int = logging.INFO
    format: str = "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool
    echo_pool: bool
    pool_size: int
    max_overflow: int

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class RedisConfig(BaseModel):
    host: str
    port: int
    decode_responses: bool = True

    def get_url(self) -> str:
        return f"redis://{self.host}:{self.port}/"


class CeleryConfig(BaseModel):
    app_name: str = "tasks"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "tests/.env.test"),
        env_prefix="BOT_CONFIG__",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="allow",
    )

    bot_token: str
    redis: RedisConfig
    db: DatabaseConfig
    logging: LoggingConfig = LoggingConfig()
    celery: CeleryConfig = CeleryConfig()


settings = Settings()
