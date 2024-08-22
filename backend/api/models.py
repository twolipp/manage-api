from django.db import models

# Create your models here.

class Programmer(models.Model):
    name = models.CharField(max_length=50)
    dob = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    quote = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"