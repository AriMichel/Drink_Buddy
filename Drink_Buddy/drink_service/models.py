from django.db import models
from PIL import Image
import tempfile
import os

class UserLocation(models.Model):
    location = models.CharField(max_length=100)

class Drinks(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Drink/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


def compress_image(image):
    img = Image.open(image.path)
    # Adjust the compression level as needed (0-100)
    img.save(image.path, optimize=True, quality=40)
             
class Drink(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    recipe = models.TextField()
    timeofyear = models.CharField(max_length=100)
    timetodrink = models.CharField(max_length=100)
    socialsituation = models.CharField(max_length=100)
    mood = models.CharField(max_length=100)
    iscoffee = models.BooleanField(default=False)
    istea = models.BooleanField(default=False)
    isalcoholic = models.BooleanField(default=False)
    isnonalcoholic = models.BooleanField(default=False)
    imagefile = models.ImageField(upload_to='images/recipes', blank= True, null=True)
    temperatureoflocation = models.CharField(max_length=100)
    timeofday = models.CharField(max_length=100)


    
    def save(self, *args, **kwargs):
        if self.imagefile:
            compress_image(self.imagefile)

        super().save(*args, **kwargs)
