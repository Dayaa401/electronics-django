
from django.db import models
class Catogery(models.Model):
    name=models.CharField(max_length=20)
    image = models.ImageField(upload_to='catimage/', default='catimage/default.jpg')
    def __str__(self):
        return self.name

    
