from dataclasses import dataclass
from environs import Env


@dataclass()
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str

@dataclass()
class TgBot:
    token: str
    admin_ids: list[int]

@dataclass()
class Config:
    tgBot: TgBot
    db: DatabaseConfig

env: Env = Env()
env.read_env()

config = Config(
    tgBot=TgBot(
        token=env('BOT_TOKEN'),
        admin_ids=list(map(int,env.list('ADMIN_IDS')))
    ),
    databasec
)