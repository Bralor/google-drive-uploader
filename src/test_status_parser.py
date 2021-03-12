import pytest
from unittest.mock import Mock

from src.status_parser import StatusParser

DEFAULT_TXT = [
    '## content-dev...origin/content-dev\n',
    ' M materials/01_intro_to_programming/00_introduction.ipynb\n',
    '?? materials/01_intro_to_programming/.ipynb_checkpoints/\n',
    '?? status_out.txt\n'
]

PARSED_TXT = [
    '## content-dev...origin/content-dev',
    'M materials/01_intro_to_programming/00_introduction.ipynb',
    '?? materials/01_intro_to_programming/.ipynb_checkpoints/',
    '?? status_out.txt'
]

SORTED_TXT = {
    'headline': ['content-dev...origin/content-dev'],
    'traced': ['materials/01_intro_to_programming/00_introduction.ipynb'],
    'untraced': [
        'materials/01_intro_to_programming/.ipynb_checkpoints/',
        'status_out.txt']
}


class TestStatusParser:
    def test_incorrect_instance_creation(self):
        with pytest.raises(TypeError):
            test_instance = StatusParser()

    def test_correct_instance_creation(self):
        test_instance = StatusParser("foo")

    def test_incorrect_project_folder(self):
        test_instance = StatusParser("foo")
        assert test_instance.project != "bar"

    def test_correct_project_folder(self):
        test_instance = StatusParser("foo")
        assert test_instance.project == "foo"

    def test_default_filename(self):
        test_instance = StatusParser("foo")
        assert test_instance.filename == "status_out.txt"

    def test_find_output(self):
        with pytest.raises(FileNotFoundError):
            test_instance = StatusParser("foo")
            test_instance.find_output()

    def test_incorrect_read_status(self):
        with pytest.raises(FileNotFoundError):
            test_instance = StatusParser("foo")
            test_instance.read_status("bar")

    @pytest.mark.parametrize(
        "exp_txt, parsed_txt",
        [pytest.param(DEFAULT_TXT, PARSED_TXT)],
    )
    def test_correct_parse_status(self, exp_txt: list, parsed_txt: list):
        test_instance = StatusParser("foo")
        assert test_instance.parse_status(exp_txt) == parsed_txt

    @pytest.mark.parametrize(
        "parsed_txt, sorted_txt",
        [pytest.param(PARSED_TXT, SORTED_TXT)],
    )
    def test_correct_sort_status(self, parsed_txt: list, sorted_txt: dict):
        test_instance = StatusParser("foo")
        assert test_instance.sort_status(parsed_txt) == sorted_txt

    # def test_mocking_method(self):
        # test_instance = StatusParser("foo")
        # test_instance.read_status = Mock()
        # test_instance.read_status.return_value = ["a", "b", "c"]
        # assert test_instance.read_status() == ["a", "b", "c"]

