from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ItemListing(models.Model):
    name = models.CharField(max_length=1024)
    price = models.FloatField()
    serial_id = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.name


class ExtendUser(models.Model):
    r = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.r.username
