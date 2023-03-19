import os
import django
import pytest

django.setup()


def pytest_configure(config):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")
