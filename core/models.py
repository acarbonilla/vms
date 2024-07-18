from django.contrib.auth.models import User
from django.db import models

# This is for ZFC employee


class Department(models.Model):
    name = models.CharField(max_length=20, verbose_name='Department')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class EmpName(models.Model):
    compId = models.CharField(max_length=20, primary_key=True, editable=True, verbose_name='Company ID')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Department')
    member = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)






