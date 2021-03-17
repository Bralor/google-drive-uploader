import os


class StatusParser:
    def __init__(self, project: str, filename: str = "status_out.txt"):
        self.project = project
        self.filename = filename

    def find_output(self) -> None:
        for root, _, files in os.walk(self.project):
            if self.filename in files:
                file_index = files.index(self.filename)
                self.abs_path = os.path.abspath(
                    os.path.join(
                        root,
                        files[file_index])
                )
                break
        else:
            raise FileNotFoundError(f"File {self.filename} does not exists!")

    def read_status(self, path: str) -> None:
        with open(path) as txt:
            self.status = txt.readlines()

    @staticmethod
    def parse_status(status: list) -> list:
        return [line.strip() for line in status]

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

