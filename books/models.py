from django.db import models


class Books(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    copies = models.IntegerField()
    
  