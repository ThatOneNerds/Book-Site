from django.db import models
from djmoney.models.fields import MoneyField

#I should edit the limits for the charfield, not going to do that right now

class Book(models.Model):

    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    img = models.ImageField(upload_to='static/images', height_field=None, width_field=None, null = True)

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField(null=True)
    response = models.TextField()

    def __str__(self):
        return self.reviewer_name