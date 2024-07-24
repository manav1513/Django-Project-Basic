from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    address = models.CharField(max_length=122)

class Car(models.Model):
    name = models.CharField(max_length=122)
    model = models.CharField(max_length=122)

    def __str__(self) -> str:
        return self.name
 
  
