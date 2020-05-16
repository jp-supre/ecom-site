from django.db import models


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500)


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address_num = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=3000,
                                  default="data:image/jpeg;base64,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")
