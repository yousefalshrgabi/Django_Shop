from django.db import models
class Delivery(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
