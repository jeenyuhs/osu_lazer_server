import aiomysql
import aioredis

from lib.db import Database
from lib.config import Config
from models.user import APIUser

sql: Database = None
config: Config = None
players: dict[str, APIUser] = {}

redis: aioredis.Redis
