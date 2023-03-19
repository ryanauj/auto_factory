from django.db import models
import pytest

from auto_factory.django import AutoDjangoModelFactory


class TestModel(models.Model):
    char_field = models.CharField(max_length=100)
    text_field = models.TextField()
    email_field = models.EmailField()
    integer_field = models.IntegerField()
    float_field = models.FloatField()
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2)
    date_field = models.DateField()
    datetime_field = models.DateTimeField()
    url_field = models.URLField()
    boolean_field = models.BooleanField()


class TestModelFactory(AutoDjangoModelFactory):
    class Meta:
        model = TestModel


@pytest.mark.django_db
def test_auto_faker_django_model_factory():
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