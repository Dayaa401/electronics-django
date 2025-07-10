from django.db import models
from .customer import Customer
from .product import Product
import datetime

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)  # delivered or not

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')


    def __str__(self):
        return f"{self.customer} -{self.product}"