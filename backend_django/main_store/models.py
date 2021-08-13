from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ItemListing(models.Model):
    name = models.CharField(max_length=1024)
    price = models.FloatField()
    serial_id = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    item = models.ForeignKey(ItemListing, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    items = models.ManyToManyField(OrderItem)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
