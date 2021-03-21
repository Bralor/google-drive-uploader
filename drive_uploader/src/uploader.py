import os
import sys
from pprint import pprint

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


class GDrive:
    def __init__(self, dirname):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(gauth)
        self.dirname = dirname

    def inspect_root(self):
        return self.drive.ListFile(
            {"q": "'root' in parents and trashed=false"}).GetList()

    def inspect_folder(self, dir_id):
        remote_folder = f"\'{dir_id}\' in parents and trashed=false"
        return self.drive.ListFile({"q": remote_folder}).GetList()

    def upload_files(self, destination, file):
        new_file = self.drive.CreateFile({
            "title": os.path.basename(file),
            "parents": [{"id": destination}]
        })
        new_file.SetContentFile(file)
        new_file.Upload()
        print(f"Title:{new_file['title']}, id: {new_file['id']}")

    def update_files(self, destination, file):
        new_file = self.drive.CreateFile({'id': destination})
        new_file.SetContentFile(file)
        new_file.Upload()
        print(f"title:{new_file['title']}, id: {new_file['id']}")

    def create_folder(self, parent_folder_id, subfolder_name):
        new_folder = self.drive.CreateFile({
            'title': subfolder_name,
            "parents": [{
                "kind": "drive#fileLink",
                "id": parent_folder_id}],
            "mimeType": "application/vnd.google-apps.folder"
        })
        new_folder.Upload()
        return new_folder

    @staticmethod
    def save_list_content(iterable):
        return {
            file["title"]: file["id"]
            for file in iterable
        }

    @staticmethod
    def find_notebook(content, notebook):
        for lesson in content:  # 01_lesson, 02_lesson
            for chapter in lesson:  # 00_introduction, 01_..., notes.txt
                if chapter == notebook:
                    return lesson.get(chapter)
                else:
                    continue
        return False

    @staticmethod
    def find_lesson(content, folder):
        for dir_c in content:    # 01_intro_to_programming, 02_conditions
            if dir_c == folder:  # "01_intro_to_programming" == "01_intro_to_programming"
                return content.get(dir_c)
            else:
                continue
        return False

