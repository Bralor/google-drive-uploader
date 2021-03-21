import os
import pytest
from drive_uploader.src.file_sorter import split_path, parse_path

PATH_1 = ['00_introduction.ipynb']
PATH_2 = ['01_intro_to_programming/00_introduction.ipynb']
PATH_3 = ['materials/01_intro_to_programming/00_introduction.ipynb']


class TestFileSorter:
    def test_split_path(self):
        pass

    @pytest.mark.parametrize("path_1", PATH_1)
    def test_parse_path_1(self, path_1):
        splitted_path = path_1.split(os.path.sep)
        assert parse_path(splitted_path) == {"notebook": "00_introduction.ipynb"}

    @pytest.mark.parametrize("path_2", PATH_2)
    def test_parse_path_2(self, path_2):
        splitted_path = path_2.split(os.path.sep)
        assert parse_path(splitted_path) == {
            "lesson": "01_intro_to_programming",
            "notebook": "00_introduction.ipynb"
        }

    @pytest.mark.parametrize("path_3", PATH_3)
    def test_parse_path_3(self, path_3):
        splitted_path = path_3.split(os.path.sep)
        assert parse_path(splitted_path) == {
            "root": "materials",
            "lesson": "01_intro_to_programming",
            "notebook": "00_introduction.ipynb"
        }

