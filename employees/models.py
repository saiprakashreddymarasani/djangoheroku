from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

# Create your models here.
class Employee(models.Model):
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=15)
    dob=models.DateField()
    zipcode=models.CharField(max_length=5)

    def __str__(self):
        return "firstname is " + self.firstname + " lastname is " + self.lastname


class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=['firstname','lastname', 'dob', 'zipcode']

