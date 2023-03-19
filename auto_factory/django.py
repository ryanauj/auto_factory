import factory
from factory import Faker
from django.db import models


class AutoDjangoModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        abstract = True

    @staticmethod
    def get_faker_method_for_field(field):
        field_to_faker_map = {
            models.CharField: lambda f: Faker("word").generate({})[: f.max_length],
            models.TextField: lambda _: Faker("text").generate({}),
            models.EmailField: lambda _: Faker("email").generate({}),
            models.IntegerField: lambda _: Faker("random_int").generate({}),
            models.FloatField: lambda _: Faker("random_number", decimals=2).generate(
                {}
            ),
            models.DecimalField: lambda f: Faker(
                "pydecimal",
                left_digits=f.max_digits - f.decimal_places,
                right_digits=f.decimal_places,
            ).generate({}),
            models.DateField: lambda _: Faker(
                "date_between", start_date="-30d", end_date="today"
            ).generate({}),
            models.DateTimeField: lambda _: Faker(
                "date_time_between", start_date="-30d", end_date="now"
            ).generate({}),
            models.URLField: lambda _: Faker("url").generate({}),
            models.BooleanField: lambda _: Faker("boolean").generate({}),
        }

        faker_method = field_to_faker_map.get(type(field))
        return faker_method(field) if faker_method else None

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        fields = model_class._meta.fields

        for field in fields:
            if (
                not isinstance(
                    field, (models.AutoField, models.OneToOneField, models.ForeignKey)
                )
                and field.name not in kwargs
            ):
                faker_value = cls.get_faker_method_for_field(field)
                if faker_value:
                    kwargs[field.name] = faker_value

        return super()._create(model_class, *args, **kwargs)
