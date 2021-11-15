import psutil
import os
import datetime
from time import sleep
import csv


def track(path: str, interval: int) -> None:
    p = os.path.normpath(path)  # removed abspath so can run any terminal commands
    name = (
        p.split("/")[0] + datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".csv"
    )
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
            sleep(interval)
        except psutil.AccessDenied:
            print("Process finished.")
            break
    pass


class Writer:
    def __init__(self, name) -> None:
        self.name = name
        with open(self.name, "w", newline="") as f:
            writer = csv.writer(
                f, delimiter=":", quotechar="|", quoting=csv.QUOTE_MINIMAL
            )
            writer.writerow(["CPU", "RSS", "VMS", "FDS"])

    def write(cpu, rss, vms) -> None:
        pass


if __name__ == "__main__":
    path = input("Path or command: ")
    _int = int(input("Record interval (seconds): "))
    track(path=path, interval=_int)
