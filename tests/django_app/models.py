from django.db import models


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
