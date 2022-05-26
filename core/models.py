from django.db import models
from djmoney.models.fields import MoneyField

#I should edit the limits for the charfield, not going to do that right now

class book(models.Model):

    book_name = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50)
    book_description = models.TextField()
    book_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.book_name

class review(models.Model):
    reviewer_name = models.CharField(max_length=50)
    pub_date = models.DateField(null=True)
    reviewer_response = models.TextField()

    def __str__(self):
        return self.reviewer_name