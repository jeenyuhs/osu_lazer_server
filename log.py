import colored
from typing import Any

DEBUG = colored.fg(107)
INFO = colored.fg(111)
CHAT = colored.fg(177)
WARNING = colored.fg(130)
ERROR = colored.fg(124)
RESET = colored.attr("reset")


def info(msg: Any) -> None:
    print(f"[{INFO}info{RESET}]\t  {msg}")


def chat(msg: Any) -> None:
    print(f"[{CHAT}chat{RESET}]\t  {msg}")


def debug(msg: Any) -> None:
    print(f"[{DEBUG}debug{RESET}]\t  {msg}")


def warn(msg: Any) -> None:
    print(f"[{WARNING}warn{RESET}]\t  {msg}")


def error(msg: Any) -> None:
    print(f"[{ERROR}error{RESET}]\t  {msg}")


def fail(msg: Any) -> None:
    print(f"[{ERROR}fail{RESET}]\t  {msg}")
