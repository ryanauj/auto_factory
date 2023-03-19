import os
import pytest


def pytest_configure(config):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")
