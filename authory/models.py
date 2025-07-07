from django.db import models

# Create your models here.
class Email_code(models.Model):
    email = models.EmailField(unique=True)
    emailcode = models.CharField(max_length=4)
    time= models.DateTimeField(auto_now_add=True)