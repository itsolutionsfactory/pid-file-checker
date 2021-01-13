from pathlib import Path

import psutil
import pytest


@pytest.fixture
def pid_file():
    pid_file = Path("celerybeat.pid")
    current_pid = psutil.Process().pid
    pid_file.write_text(str(current_pid))
    yield pid_file
    try:
        pid_file.unlink()
    except FileNotFoundError:
        # Explicitly silencing this error since tests may delete the file.
        pass
