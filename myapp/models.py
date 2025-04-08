from django.db import models

class empdata(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128,default='')
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_no = models.BigIntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
