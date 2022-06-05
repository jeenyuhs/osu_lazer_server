import os
import configparser
from typing import Any


class Config:
    def __init__(self) -> None:
        self.config: configparser.ConfigParser = None

    def __getitem__(self, item: str) -> Any:
        return self.config[item]

    @classmethod
    def parse(cls, path: str) -> "Config":
        c = cls()

        if not os.path.exists(path):
            c._create(path)

        c.config = configparser.ConfigParser()
        c.config.read(path)

        return c

    def _create(self, path: str) -> None:
        print(f"Couldn't find `{path}`, creating config.")
        config = configparser.ConfigParser()

        config["database"] = {
            "host": "localhost",
            "user": "poop",
            "password": "dick",
            "db": "lazer",
            "autocommit": True,
        }

        with open(path, "w+") as file:
            config.write(file)
