"""Singleton configuration module"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    typedb_uri: str = "localhost:1729"
    typedb_username: str = "admin"
    typedb_password: str = "admin"
    typedb_database: str = "ontology_industries"


settings = Settings()
