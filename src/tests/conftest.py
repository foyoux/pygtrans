import os.path
from pathlib import Path

import pytest


@pytest.fixture
def data():
    return {'pytest': 'fixture'}


@pytest.fixture
def base():
    return Path(os.path.dirname(__file__))
