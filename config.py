import configparser
from dataclasses import dataclass


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str
    port: int


@dataclass
class Config:
    db: DbConfig


def load_config(file_name: str):
    config = configparser.ConfigParser()
    config.read(file_name)

    return Config(
        db=DbConfig(**config["db"]),
    )
