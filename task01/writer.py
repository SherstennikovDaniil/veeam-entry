import csv


class Writer:
    def __init__(self, name) -> None:
        self.name = name
        with open(self.name, "w", newline="") as f:
            writer = csv.writer(
                f, delimiter=":", quotechar="|", quoting=csv.QUOTE_MINIMAL
            )
            writer.writerow(["CPU", "RSS", "VMS", "FDS"])

    def write(self, cpu, rss, vms, fds) -> None:
        with open(self.name, "a", newline="") as f:
            writer = csv.writer(
                f, delimiter=":", quotechar="|", quoting=csv.QUOTE_MINIMAL
            )
            writer.writerow([cpu, rss, vms, fds])
