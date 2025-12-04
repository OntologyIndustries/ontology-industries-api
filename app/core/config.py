"""Singleton configuration module"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    typedb_uri: str = "localhost:1729"
    typedb_username: str = "admin"
    typedb_password: str = "password"
    typedb_database: str = "ontology_industries"


settings = Settings()
