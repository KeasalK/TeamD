from django.shortcuts import render
from . import forms, models
from django.core.exceptions import ValidationError
import sys

# Create your views here.
def inventory(request):
    return render(request, 'inventory/products.html')

def add_product(request):
    product = 'Add a new product'
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            sport = forms.SPORT[int(form.cleaned_data['sport'])][1]
            vendor = form.cleaned_data['vendor']
            price = form.cleaned_data['price']
            size = form.cleaned_data['size']
            color = form.cleaned_data['color']
            product_image = form.cleaned_data['product_image']

            try:
                models.create_process(product, sport, vendor, price, size, color, product_image)
                action = 'POST_SUCCESSFUL'
            except ValidationError as err:
                for err in err.messages:
                    form.add_error(None, err)
                action = 'POST_FAILED'
            except:
                print("Unexpected error: " + sys.exc_info()[0])
                form.add_error(None, 'Unexpected error - Please contact your system administrator')
                action = 'POST_FAILED'
        else:
            action = 'POST_FAILED'
    else:
        action='GET'
        form = forms.ProductForm(auto_id=False, initial={'product_image':'http://'})
    return render(request, 'inventory/product_form.html', {'action':action, 'form':form, 'product':product})
    
def fetch_all_products(request):
    prod_dict = models.fetch_all_products_process()
    return render(request, 'inventory/products.html', {'prod_dict': prod_dict})
