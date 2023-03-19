import pytest
import os
import django

from auto_factory import AutoDjangoModelFactory
from tests.django_app.models import TestModel

# Setup Django before importing Django models.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.django_app.settings")
django.setup()


class TestModelFactory(AutoDjangoModelFactory):
    class Meta:
        model = TestModel


@pytest.mark.django_db
def test_auto_django_model_factory():
    instance = TestModelFactory()

    assert instance.char_field is not None
    assert len(instance.char_field) <= 100

    assert instance.text_field is not None

    assert instance.email_field is not None
    assert "@" in instance.email_field

    assert isinstance(instance.integer_field, int)

    assert isinstance(instance.float_field, float)

    assert instance.decimal_field is not None
    assert instance.decimal_field.as_tuple().exponent == -2

    assert instance.date_field is not None

    assert instance.datetime_field is not None

    assert instance.url_field is not None
    assert instance.url_field.startswith("http")

    assert isinstance(instance.boolean_field, bool)
