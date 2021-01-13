import pytest

from pid_file_checker.checker import checker
from pid_file_checker.exceptions import InvalidPidError


def test_no_file(pid_file):
    pid_file.unlink()
    with pytest.raises(FileNotFoundError):
        checker(pid_file)


def test_no_int(pid_file):
    pid_file.write_text("coucou")
    with pytest.raises(InvalidPidError):
        checker(pid_file)


def test_not_a_pid(pid_file):
    pid_file.write_text("999999999")
    with pytest.raises(InvalidPidError):
        checker(pid_file)


def test_valid_pid(pid_file):
    checker(pid_file)
