from django.db import models  # type: ignore
from django.contrib.auth.models import User # type: ignore

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30,null=True)
    designation = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    building_name = models.CharField(max_length=50,null=True)
    street = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=50,null=True)
    pincode = models.CharField(max_length=50,null=True)
    district = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=20,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Analysis(models.Model):
    date=models.DateField(auto_now_add=True,null=True)
    users=models.ForeignKey(Users, on_delete=models.CASCADE,null=True)
    img = models.FileField(null=True)
    details=models.CharField(max_length=500)


class CrimeFiles(models.Model):
    created_at=models.DateField(auto_now_add=True,null=True)
    updated_at=models.DateField(auto_now=True,null=True)
    date_reported=models.DateField()
    crimeno=models.CharField(max_length=500,null=True)
    crimetype=models.CharField(max_length=500)
    location=models.CharField(max_length=500)
    district=models.CharField(max_length=500)
    state=models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    report = models.FileField(null=True)
    users=models.ForeignKey(Users, on_delete=models.CASCADE,null=True)


class ChatAdmin(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=200)
    sender = models.CharField(max_length=20)