import sys


class StatusParser:
    def __init__(self, filename: str):
        self.filename = filename

    def read_status(self):
        with open(self.filename) as txt:
            self.status = txt.readlines()

    def parse_status(self):
        return [line.strip() for line in self.status]

    @staticmethod
    def sort_status(source: list, status: dict = None) -> dict:
        if status is None:
            status = {
                "headline": [],
                "traced": [],
                "untraced": []
            }

        for line in source:
            if line.startswith("##"):
                status["headline"].append(line.split(maxsplit=1)[1])
            elif line.startswith("M"):
                status["traced"].append(line.split(maxsplit=1)[1])
            elif line.startswith("??"):
                status["untraced"].append(line.split(maxsplit=1)[1])

        return status


if __name__ == "__main__":
    # status_file = sys.argv[1]
    parser = StatusParser("./samples/testing_status.txt")
    parser.read_status()
    status = parser.parse_status()
    sorted_status = parser.sort_status(status)
    # from pprint import pprint
    # pprint(sorted_status)

