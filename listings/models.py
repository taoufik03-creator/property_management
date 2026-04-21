from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse

class Property(models.Model):
    title = models.CharField(max_length=100,unique=True)
    price = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("property-details",kwargs={"pk":self.id})