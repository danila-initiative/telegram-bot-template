from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    user_bot_token: SecretStr


context = Settings()  # type: ignore
