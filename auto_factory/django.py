# Import necessary modules and create a global Faker instance
from decimal import Decimal
from django.db import models
import factory
from faker import Faker

faker_instance = Faker()


# Define a function to generate fake data for each field based on its type
def get_faker_method_for_field(field):
    field_map = {
        models.CharField: "word",
        models.TextField: "text",
        models.EmailField: "email",
        models.URLField: "url",
        models.IntegerField: "random_int",
        models.FloatField: "pyfloat",
        models.DecimalField: "pydecimal",
        models.BooleanField: "boolean",
        models.DateField: "date",
        models.DateTimeField: "date_time",
        models.TimeField: "time",
        models.UUIDField: "uuid4",
    }

    field_type = type(field)

    if field_type in field_map:
        faker_method_name = field_map[field_type]
        faker_method = getattr(faker_instance, faker_method_name)
        if field_type == models.DecimalField:
            # Generate a Decimal value with a maximum of 8 digits before the decimal point and 2 digits after
            return Decimal(faker_method(left_digits=8, right_digits=2))
        else:
            return faker_method()
    else:
        return None


# Define an abstract base factory class to generate fake data for Django models
class AutoDjangoModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        abstract = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        field_values = {}

        # Generate fake data for each field in the model class
        for field in model_class._meta.fields:
            if field.name not in kwargs and not isinstance(
                field, (models.AutoField, models.OneToOneField, models.ForeignKey)
            ):
                field_values[field.name] = get_faker_method_for_field(field)

        # Update the kwargs dictionary with the fake data for each field
        kwargs.update(field_values)

        # Call the _create method of the parent factory class to
        # create a new instance of the model class with the fake data
        return super()._create(model_class, *args, **kwargs)
