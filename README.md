# AutoFaker Factory

`autofaker-factory` is a custom `DjangoModelFactory` that automatically generates Faker data for your Django model fields.
It simplifies the process of creating test instances of your models, eliminating the need to manually define Faker values for each field.

## Installation

Install the package using pip:

```bash
pip install autofaker-factory
```

## Usage

To use `autofaker-factory` in your Django project, follow these steps:

1. Import the `AutoFakerDjangoModelFactory` from the package:

```python
from autofaker_factory import AutoFakerDjangoModelFactory
```

2. Create a factory for your model by inheriting from `AutoFakerDjangoModelFactory`:

```python
from .models import MyModel

class MyModelFactory(AutoFakerDjangoModelFactory):
    class Meta:
        model = MyModel
```

3. Use the factory to create test instances of your models:

```python
my_model_instance = MyModelFactory()
```

By default, `autofaker-factory` will generate values for all fields in your model, except for `AutoField`, `OneToOneField`, and `ForeignKey`.
If you want to override the generated values, you can pass them as keyword arguments:

```python
my_model_instance = MyModelFactory(field_name="custom_value")
```

## License

This project is licensed under the MIT License.

