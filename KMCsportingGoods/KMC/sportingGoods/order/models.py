from django.db import models

# Create your models here.
class Cart(models.Model):
    product = models.CharField(max_length=30)
    price = models.FloatField()
    product_image = models.URLField(max_length=1000)
    quantity = models.IntegerField(default=1)
    subtotal = models.FloatField()

    objects = models.Manager()


def create_cart_process(_product, _price, _product_image, _quantity, _subtotal):
    # quant = 1
    cart = Cart(product=_product, price=_price, product_image=_product_image, quantity = 1, subtotal = _price)
    cart.full_clean()
    cart.save()

def fetch_cart_items_process():
    return Cart.objects.in_bulk()

def fetch_cart_item_process(name):
    return Cart.objects.get(product=name)

def add_cart_item_process(_id):
    item = Cart.objects.get(id=_id)
    _quantity = item.quantity + 1
    _subtotal = item.price * _quantity
    Cart.objects.filter(id=_id).update(subtotal=_subtotal, quantity=_quantity)

def delete_cart_item_process(_id):
    Cart.objects.filter(id=_id).delete()

def remove_cart_item_process(_id):
    item = Cart.objects.get(id=_id)
    _quantity = item.quantity - 1
    _subtotal = item.price * _quantity
    Cart.objects.filter(id=_id).update(subtotal=_subtotal, quantity=_quantity)