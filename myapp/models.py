from django.db import models

# Create your models here.
class user(models.Model):
    JID = models.CharField(max_length=15, primary_key=True, unique=True)
    name = models.CharField(max_length=15)
    gentle = models.CharField(max_length=2)
    phone = models.CharField(max_length=15, unique=True)
    gmail = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name