import os

if __name__ == "__main__":
    tested_dict = {
        'headline': ['content-dev...origin/content-dev'],
        'traced':   ['materials/01_intro_to_programming/00_introduction.ipynb'],
        'untraced': [
            'materials/01_intro_to_programming/.ipynb_checkpoints/',
            'status.txt'
        ]
    }

    def get_path(collected: list, result = None) -> dict:
        if result is None:
            result = dict()

        for path in collected:
            split_path = path.split(os.path.sep)

            if len(split_path) == 3:
                root = split_path[-3]
                lesson = split_path[-2]
                notebook = split_path[-1]
                result[path] = {
                    "root": root,
                    "lesson": lesson,
                    "notebook": notebook
                }

            elif len(split_path) == 2:
                lesson = split_path[-2]
                notebook = split_path[-1]
                result[path] = {"lesson": lesson, "notebook": notebook}

            elif len(split_path) == 1:
                notebook = split_path[-1]
                result[path] = {"notebook": notebook}

        return result


    for line in tested_dict:
        splitted_path = get_path(tested_dict.get(line))
        # from pprint import pprint
        # pprint(splitted_path)

