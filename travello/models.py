from django.db import models

# Create your models here.
class Destination(models.Model):
    
    name= models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Payments(models.Model):
    DestinationName = models.CharField(max_length=100)
    Name = models.CharField(max_length=50)
    Quantity = models.IntegerField()
    Price = models.IntegerField()
    
    def __str__(self):
        return self.Name