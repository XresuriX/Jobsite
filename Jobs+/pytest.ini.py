import pytest

from src import settings
import src


[pytest]
exportDJANGO_SETTINGS_MODULE=src.settings.local


python_files = tests.py test_*.py *_tests.py

"""markers =
    slow: slow running test"""