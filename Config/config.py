from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    name: str


@dataclass
class Config:
    bot: TgBot
    admins: list[int] | None


def load_config(path: str | None = None) -> Config:
    """path to .env file"""
    env = Env()
    env.read_env(path)

    return Config(
        admins=None,
        bot=TgBot(
            token=env("BOT_TOKEN"),
            name=env("BOT_USERNAME")
        ),
    )
