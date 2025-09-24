from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=20,null=True,default=None)
    address=models.CharField(max_length=100,null=True,default=None)
    profile_picture = models.ImageField(null=True,blank=True,upload_to=".")
    user = models.ForeignKey("UserManager.MySuperUser",on_delete=models.CASCADE)
