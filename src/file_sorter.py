import os
import sys


def split_path(all_paths: list, result = None) -> dict:
    if result is None:
        result = dict()

    for path in all_paths:
        split_path = path.split(os.path.sep)
        result[path] = parse_path(split_path)
    return result


def parse_path(split_path: list) -> dict:
    if len(split_path) == 3:
        root = split_path[-3]
        lesson = split_path[-2]
        notebook = split_path[-1]
        return {"root": root, "lesson": lesson, "notebook": notebook}

    elif len(split_path) == 2:
        lesson = split_path[-2]
        notebook = split_path[-1]
        return {"lesson": lesson, "notebook": notebook}

    elif len(split_path) == 1:
        notebook = split_path[-1]
        return {"notebook": notebook}


if __name__ == "__main__":
    # tested_dict = {
        # 'headline': ['content-dev...origin/content-dev'],
        # 'traced':   ['materials/01_intro_to_programming/00_introduction.ipynb'],
        # 'untraced': [
            # 'materials/01_intro_to_programming/.ipynb_checkpoints/',
            # 'status.txt'
        # ]
    # }
    tested_dict = sys.argv[1]

    for line in tested_dict:
        splitted_path = split_path(tested_dict.get(line))
        from pprint import pprint
        pprint(splitted_path)

