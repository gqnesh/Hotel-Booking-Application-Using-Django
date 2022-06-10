from django.db import models

# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name
    

class Hotels(models.Model):
    HotelName = models.CharField(max_length=50)
    HotelAddress = models.TextField()
    HotelImages = models.ImageField(upload_to='images/')
    Price = models.IntegerField()
    Hotelcategory = models.ManyToManyField(Category)

    def __str__(self):
        return self.HotelName
