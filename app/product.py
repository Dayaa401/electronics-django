
from django.db import models
from .catogery import Catogery

class Product(models.Model):
    name=models.CharField(max_length=20)
    catogery=models.ForeignKey(Catogery,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='img/')
    desc=models.TextField()
    price=models.IntegerField()

    @staticmethod
    def get_catogery_id(get_id):
        if get_id:
            return Product.objects.filter(catogery=get_id)
        else:
            return Product.objects.all()
