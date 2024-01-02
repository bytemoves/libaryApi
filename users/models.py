

# Create your models here.
from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    student_email = models.EmailField()
    username = models.CharField(max_length=100)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Staff(models.Model):
    staff_id = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=100)
    staff_job_type = models.CharField(max_length=100)
    email = models.EmailField()
