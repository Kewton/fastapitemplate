from pydantic_settings import BaseSettings  # pydantic_settingsからインポート
from pydantic import Field


class Settings(BaseSettings):
    CONFIG_TEST: str = Field(default="sss", env="CONFIG_TEST")
    LOG_DIR: str = Field(default="./", env="LOG_DIR")
    LOG_LEVEL: str = Field(default="./", env="LOG_LEVEL")

    class Config:
        env_file = ".env"  # .envファイルを使用して環境変数を読み込む設定


# インスタンス生成
settings = Settings()
