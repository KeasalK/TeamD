from django.shortcuts import render
from . import models
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.http import HttpResponseRedirect
import sys
from sportingGoods.inventory.models import Inventory


# ** TO DO **
# 1. Models for cart created
# 2. Finish views for cart with the methods to store cart info to db
# 3. don't need to import inventory.views here; need to import cart create/edit functions to inventory.views
#   this should be in the form of a helper function to pass the product info to the cart.views functions
#  This method will be invoked by the "add to cart" btn in the product_popup.html 
# 4. then cart table in db should be created; cart_item.html will display each item in the cart table from the db
#  similar to the product_thumbnail.html file
# 5. cleanup comments from all files and delete excess/unneeded code

# The following will get the menu_target and set created to True or False and the get() portion automatically handles the
# error condition if the object is not found... 
# menu_target, created = Menu.objects.get_or_create(name='name')


# filter() and exclude() methods useful for getting certain objects from the db
# save(), update(), update_or_create() -- great for saving/updating objects in a db
# update_fields() can be used to only update certain fields
## Store.objects.get(id=1).update(name='new Name')


# Create your views here.
def cart(request):
    return render(request, 'order/cart.html')

def fetch_cart_items(request):
    item_dict = models.fetch_cart_items_process()
    return render(request, 'order/cart.html', {'item_dict': item_dict})

# only used for the mini cart on the checkout page; delete if that is not used
def fetch_mini_cart_items(request):
    item_dict = models.fetch_cart_items_process()
    return render(request, 'order/checkout.html', {'item_dict': item_dict})

def add_cart_item(request):
    id = request.POST.get('id')
    item = Inventory.objects.get(id=id)
    try:
        cart_item = models.fetch_cart_item_process(item.product)
        models.add_cart_item_process(cart_item.id)
    except ObjectDoesNotExist:
        models.create_cart_process(item.product, item.price, item.product_image, 1, item.price)

    return HttpResponseRedirect('/order')

def remove_cart_item(request):
    id = request.POST.get('id')
    item = models.Cart.objects.get(id=id)
    if item.quantity > 1:
        models.remove_cart_item_process(id)
    else:
        models.delete_cart_item_process(id)

    return HttpResponseRedirect('/order')


def delete_cart_item(request):
    id = request.POST.get('id', '')
    if(id == ''):
        return HttpResponseRedirect('/')
    else:
        id = id.replace('popup', '')
    try:
        models.delete_cart_item_process(id)
    except:
        print('Unexpected error: ', + sys.exc_info()[0])
    return HttpResponseRedirect('/')
