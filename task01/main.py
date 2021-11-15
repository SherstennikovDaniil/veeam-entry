from typing import List, Mapping
import psutil
import os
from time import sleep


def track(path: str, interval: int) -> None:
    p = os.path.normpath(path)  # removed abspath so can run any terminal commands
    pid = psutil.Popen(
        p, shell=True
    ).pid  # shell=True and chmod +x fixed permission issues
    proc = psutil.Process(pid)
    while True:
        with proc.oneshot():
            cpu = proc.cpu_percent()
            mem = proc.memory_full_info()
            rss = mem[0]
            vms = mem[1]
        sleep(interval)
    pass


def write_to_csv(smth):
    pass


if __name__ == "__main__":
    path = input("Path or command: ")
    _int = int(input("Record interval (seconds): "))
    track(path=path, interval=_int)
