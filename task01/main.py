from typing import List, Mapping
import psutil
import os
from time import sleep


def track(path: str, interval: int) -> None:
    p = os.path.abspath(os.path.normpath(path))
    proc = psutil.Popen(p)
    pass


def write_to_csv(smth):
    pass


if __name__ == "__main__":
    path = input("Введите путь: ")
    _int = int(input("Введите интервал: "))
    track(path=path, interval=_int)
