from django.db import models

# Create your models here.


class Data(models.Model):
    name = models.CharField(max_length=50)
    pno = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    add = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name