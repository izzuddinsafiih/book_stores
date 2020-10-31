from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.TextField(max_length=288)
    price = models.FloatField()
    description = models.TextField(max_length=1000)
    number_of_pages = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

#  Relationship - hubungan antara model yg ada

