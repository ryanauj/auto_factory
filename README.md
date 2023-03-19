# Auto Factory

`auto-factory` is a custom `DjangoModelFactory` that automatically generates Faker data for your Django model fields.
It simplifies the process of creating test instances of your models, eliminating the need to manually define Faker values for each field.

## Installation

Install the package using pip:

```bash
pip install auto-factory
```

## Usage

To use `auto-factory` in your Django project, follow these steps:

1. Import the `AutoDjangoModelFactory` from the package:

```python
from auto_factory import AutoDjangoModelFactory
```

2. Create a factory for your model by inheriting from `AutoDjangoModelFactory`:

```python
from .models import MyModel

class MyModelFactory(AutoDjangoModelFactory):
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

