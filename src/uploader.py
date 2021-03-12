import os
import sys
from pprint import pprint

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


class GDrive:
    def __init__(self):
        self.files = ["05_languages.png", "python_inst.png"]
        # self.creds = "client_secrets.json"

        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(gauth)

    def inspect_root(self):
        return self.drive.ListFile(
            {"q": "'root' in parents and trashed=false"}).GetList()

    def inspect_folder(self, dir_id):
        remote_folder = f"\'{dir_id}\' in parents and trashed=false"
        return self.drive.ListFile({"q": remote_folder}).GetList()

    def upload_files(self, destination, file):
        new_file = self.drive.CreateFile({
            "title": file.split(os.path.sep)[1],
            "parents": [{"id": destination}]
        })
        new_file.SetContentFile(file)
        new_file.Upload()
        print(f"title:{new_file['title']}, id: {new_file['id']}")

    def update_files(self, destination, file):
        new_file = self.drive.CreateFile({'id': destination})
        new_file.SetContentFile(file)
        new_file.Upload()
        print(f"title:{new_file['title']}, id: {new_file['id']}")

    @staticmethod
    def save_list_content(iterable):
        return {
            file["title"]: file["id"]
            for file in iterable
        }


if __name__ == "__main__":
    upload = GDrive()
    inspect_root = upload.inspect_root()
    root_dict = upload.save_list_content(inspect_root)
    # pprint(root_dict)

    dir_engeto = upload.inspect_folder(root_dict.get("engeto_collabs"))
    lessons = upload.save_list_content(dir_engeto)  # 01_lesson, 02_lesson
    # pprint(lessons)

    all_lessons = []
    for lesson in lessons:
        dir_lesson = upload.inspect_folder(lessons.get(lesson))
        dict_of_files = upload.save_list_content(dir_lesson)
        all_lessons.append(dict_of_files)
    # pprint(all_lessons)

    def content_checker(content, file):
        for lesson in content:  # 01_lesson, 02_lesson
            for chapter in lesson:  # 00_introduction, 01_..., notes.txt
                if chapter == file:
                    return lesson.get(chapter)
                else:
                    continue
        return False


    tested_status_3 = {
        'samples/notes.txt': {
            'lesson': '01_lesson',
            'notebook': 'notes.txt'
        }
    }

    tested_files = [tested_status_3]

    for tested_file in tested_files:  # "notes.txt"
        file_path = (list(tested_file.keys())[0]) # "samples/notes.txt"
        notebook = tested_file.get(file_path).get("notebook")  # "notes.txt"

        if (file_id := content_checker(all_lessons, notebook)):  # False
            if notebook:  # 00_introduction.ipynb
                lesson = tested_file.get(file_path).get("lesson")  # 01_intro_to_programming
                print("Uploading and updating file")
                upload.update_files(file_id, file_path)

        else:
            if notebook: # True
                lesson = tested_file.get(file_path).get("lesson")  # 01_lesson
                remote_dir_id = lessons.get(lesson)  # '1x8fkMqA5u8lo0WMs0GKeZheG-fLxXjeT'
                print("Just uploading file..")
                upload.upload_files(remote_dir_id, file_path)

