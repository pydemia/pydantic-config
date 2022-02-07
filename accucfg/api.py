from pydantic import BaseModel, BaseSettings
from pydantic.dataclasses import dataclass
import types as t
import validators as v

from os import path, environ

from typing import Dict, List, Any, NamedTuple
from collections import namedtuple
from autologging import logged


# __all__ = [
#     # "Config",
#     # "LocalConfig",
#     # "ProdConfig",
#     # "TestConfig",
#     # "conf",
#     "AIIPConfig",
# ]


@dataclass
class Config:
    """
    기본 Configuration
    """
    BASE_DIR: str = "/config"
    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True
    DEBUG: bool = False
    TEST_MODE: bool = False
    DB_URL: str = environ.get("DB_URL", "mysql+pymysql://aiip_runtime:P@s$w0rd@systemdb:3306/aiip_runtime_db?charset=utf8mb4")


class Settings(BaseSettings):
    app_name: str = "core"
    use_ns_nodeselector: bool = False

    class Config:
        env_file = "config.env"
        env_file_encoding = "utf-8"
