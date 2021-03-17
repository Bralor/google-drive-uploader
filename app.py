import os
import argparse

from src.status_parser import StatusParser
from src.file_sorter import split_path
from src.uploader import GDrive


def main():
    print("Running main...")
    parser = StatusParser(args.upload)
    parser.find_output()
    parser.read_status(parser.abs_path)
    dirname = os.path.dirname(parser.abs_path)
    parsed_status = parser.parse_status(parser.status)
    sorted_status = parser.sort_status(parsed_status)

    all_updates = [
        split_path(sorted_status.get(line))
        for line in sorted_status
    ]

    uploader = GDrive(dirname)
    inspect_root = uploader.inspect_root()
    root_dict = uploader.save_list_content(inspect_root)

    dir_engeto = uploader.inspect_folder(root_dict.get("engeto_collabs"))
    lessons = uploader.save_list_content(dir_engeto)  # 01_lesson, 02_lesson

    all_lessons = []
    for lesson in lessons:
        dir_lesson = uploader.inspect_folder(lessons.get(lesson))
        dict_of_files = uploader.save_list_content(dir_lesson)
        all_lessons.append(dict_of_files)

    for paths in all_updates:
        for path in paths:
            file_path = path

            if os.path.splitext(file_path)[-1] == ".ipynb":
                notebook = paths.get(file_path).get("notebook")
                lesson = paths.get(file_path).get("lesson")
                parent_dir = root_dict.get("engeto_collabs")

                if (file_id := uploader.find_notebook(all_lessons, notebook)) \
                        and uploader.find_lesson(lessons, lesson):
                    print(f"Updating file: {notebook}")
                    uploader.update_files(file_id, os.path.join(dirname, file_path))

                elif not (folder_id := uploader.find_lesson(lessons, lesson)):
                    print(f"Creating new folder: {lesson}")
                    new_cl_folder = uploader.create_folder(parent_dir, lesson)
                    lessons[lesson] = new_cl_folder["id"]
                    print(f"Uploading file: {notebook}")
                    uploader.upload_files(new_cl_folder["id"], os.path.join(dirname, file_path))

                elif uploader.find_lesson(lessons, lesson) \
                    and not (file_id := uploader.find_notebook(all_lessons, notebook)):
                    remote_dir_id = lessons.get(lesson)  # '1x8fkMqA5u8lo0WMs0GKeZheG-fLxXjeT'
                    print(f"Uploading file: {notebook}")
                    uploader.upload_files(remote_dir_id, os.path.join(dirname, file_path))


    print(f"File: {args.upload}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--upload", action="store",
                        metavar="PATH", help="upload existing file to GDrive")
    args = parser.parse_args()

    if args.upload:
        main()
    elif args:
        parser.print_help()

