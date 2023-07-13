from django.db import models


class Educational(models.Model):
    title= models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    url = models.URLField(blank=False)
    
    def __str__(self):
        return self.title
