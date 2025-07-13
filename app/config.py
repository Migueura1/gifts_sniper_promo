from dataclasses import dataclass
from environs import Env
import os
from backend import read_license

MAX_CHANNELS_COUNT = 10
NOT_SET = -1
default_env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
default_json_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data'), 'snipe_config.json')
seq = ... 
default_license_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'license'), 'license.key')
default_logs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')

status = read_license(default_license_path)

@dataclass
class TgBot:
    token: str


@dataclass
class Logs:
    id: int


@dataclass 
class Config:
    tg_bot: TgBot
    logs: Logs


def load_config(path: str | None = default_env_path) -> Config:
    env = Env()

    env.read_env(path, override=True)

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')), logs=Logs(id=env('LOGS_CHANNEL_ID')))

