from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    OPERATOR = (1, 'operator')
    OWNER = (2, 'owner')
    ADMIN = (3, 'admin')

    USER_TYPE_CHOICES = (
        OPERATOR,
        OWNER,
        ADMIN,
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,
            default=OPERATOR[0])
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    displayed_name = models.CharField(max_length=100, blank=True)


class Value(models.Model):
    name = models.CharField(max_length=100)
    attribute = models.ForeignKey(Attribute, on_delete = models.CASCADE, related_name='values')


class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    quantity = models.IntegerField()
    price = models.FloatField()
    attribute_values = models.ManyToManyField(Value)
    image = models.ImageField(blank=True)
