from django.shortcuts import render
from . import forms

# Create your views here.
def inventory(request):
    return render(request, 'inventory/inventory.html')

def add_product(request):
    product = 'Add product title'
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            action='POST_SUCCESSFUL'
        else:
            action='POST_FAILED'
    else:
        action='GET'
        form = forms.ProductForm(auto_id=False, initial={'product_image':'http://'})
    return render(request, 'inventory/product_form.html', {'action':action, 'form':form, 'product':product})
    