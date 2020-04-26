from django.db import models

class register(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.TextField(max_length=12)
    Cpassword=models.TextField(max_length=12)

    @classmethod
    def filter(register, Email):
        pass

    @classmethod
    def authenticate(register, Email):
        pass


