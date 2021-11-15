import psutil
import os
import datetime
from time import sleep
import csv

from writer import Writer


def track(path: str, interval: int) -> None:
    p = os.path.normpath(path)  # removed abspath so can run any terminal commands
    command = p.split("/")[0]
    name = command + datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".csv"
    writer = Writer(name)
    # shell=True and chmod +x fixed permission issues
    pid = psutil.Popen(p, shell=True).pid
    proc = psutil.Process(pid)
    while True:
        try:
            with proc.oneshot():
                cpu = proc.cpu_percent()
                mem = proc.memory_full_info()
                rss = mem[0]
                vms = mem[1]
                fds = proc.num_fds()
            writer.write(cpu, rss, vms, fds)
            sleep(interval)
        except psutil.AccessDenied:
            print("Process finished.")
            break
    pass


if __name__ == "__main__":
    path = input("Path or command: ")
    _int = int(input("Record interval (seconds): "))
    track(path=path, interval=_int)
