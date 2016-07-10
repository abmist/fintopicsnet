from django.db import models
from django.conf import settings

class Contact(models.Model):

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=30)
    email = models.CharField(max_length=250)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)

    def __str__(self):
        return ' '.join([self.first_name, self.last_name,])