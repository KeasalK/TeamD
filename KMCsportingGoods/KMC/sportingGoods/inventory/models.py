from django.db import models

# Create your models here.
class Inventory(models.Model):
    product = models.CharField(max_length=30)
    sport = models.CharField(max_length=30)
    vender = models.CharField(max_length=30)
    price = models.IntegerField()
    size = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    product_image = models.URLField(max_length=1000)

    class Meta:
        unique_together = ['product', 'vender', 'color']