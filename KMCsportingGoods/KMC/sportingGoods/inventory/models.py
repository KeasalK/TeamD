from django.db import models

# Create your models here.
class Inventory(models.Model):
    product = models.CharField(max_length=30)
    sport = models.CharField(max_length=30)
    vendor = models.CharField(max_length=30)
    price = models.FloatField()
    size = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    product_image = models.URLField(max_length=1000)

    objects = models.Manager()

    class Meta:
        unique_together = ['product', 'vendor', 'color']

def create_process(_product, _sport, _vendor, _price, _size, _color, _product_image):
    inventory = Inventory(product=_product, sport=_sport, vendor=_vendor,
                    price=_price, size=_size, color=_color, product_image=_product_image)

    inventory.full_clean()
    inventory.save()

def fetch_all_products_process():
    return Inventory.objects.in_bulk()

def edit_process(_id, _product, _vendor, _sport, _price, _size, _color, _product_image):
    Inventory.objects.filter(id=_id).update(product=_product, vendor=_vendor, sport=_sport, price=_price, size=_size, color=_color, product_image=_product_image)

def delete_process(_id):
    Inventory.objects.filter(id=_id).delete()