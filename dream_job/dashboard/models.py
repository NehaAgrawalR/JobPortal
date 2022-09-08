from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class SeekerUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=11,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10)
    utype = models.CharField(max_length=15)

    def _str_(self):
        return self.user.username

class Provider(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=11,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10)
    company = models.CharField(max_length=100)
    utype = models.CharField(max_length=15)
    status = models.CharField(max_length=20)

    def _str_(self):
        return self.user.username
    
    
class Job(models.Model):
    provider = models.ForeignKey(Provider,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100)
    salary = models.FloatField(max_length=10)
    image = models.FileField()
    description = models.CharField(max_length=300)
    experience = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    creationdate = models.DateField()

    def _str_(self):
        return self.title
