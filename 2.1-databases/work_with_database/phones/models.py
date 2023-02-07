from django.db import models


class Phone(models.Model):
    name = models.TextField(max_length=100)
    price = models.FloatField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100)
