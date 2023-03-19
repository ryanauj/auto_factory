# Copyright: See the LICENSE file.

"""Settings for auto_factory/django tests."""

import os

FACTORY_ROOT = os.path.join(
    os.path.abspath(
        os.path.dirname(__file__)
    ),  # /path/to/auto_factory/tests/django_app/
    os.pardir,  # /path/to/auto_factory/tests/
    os.pardir,  # /path/to/auto_factory
)

MEDIA_ROOT = os.path.join(FACTORY_ROOT, "tmp_test")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    },
    "replica": {
        "ENGINE": "django.db.backends.sqlite3",
    },
}


INSTALLED_APPS = ["django_app"]

MIDDLEWARE_CLASSES = ()

SECRET_KEY = "testing."

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}
