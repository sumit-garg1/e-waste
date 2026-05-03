from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25,null=True,blank=True)
    email=models.EmailField(max_length=30)
    phone_no=models.CharField(max_length=12,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name
    