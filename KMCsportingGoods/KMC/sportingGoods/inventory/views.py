from django.shortcuts import render
from . import forms, models
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
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
                    form.add_error(None, 'Unexpected error - Please contact your system administrator')
                    action = 'POST_FAILED'
        else:
            action ='POST_FAILED'
    else:
        action ='GET'
        form = forms.ProductForm(auto_id=False, initial={'product_image':'http://'})
    return render(request, 'inventory/product_form.html', {'action':action, 'form':form, 'product':product})
    
def fetch_all_products(request):
    prod_dict = models.fetch_all_products_process()
    return render(request, 'inventory/products.html', {'prod_dict': prod_dict})

def fetch_softball(request):
    sb_dict = models.fetch_softball()
    return render(request, 'inventory/softball.html', {'sb_dict': sb_dict})

def fetch_baseball(request):
    base_dict = models.fetch_baseball()
    return render(request, 'inventory/baseball.html', {'base_dict': base_dict})

def fetch_basketball(request):
    bask_dict = models.fetch_basketball()
    return render(request, 'inventory/basketball.html', {'bask_dict': bask_dict})

def fetch_football(request):
    fb_dict = models.fetch_football()
    return render(request, 'inventory/football.html', {'fb_dict': fb_dict})

def fetch_golf(request):
    golf_dict = models.fetch_golf()
    return render(request, 'inventory/golf.html', {'golf_dict': golf_dict})

def fetch_soccer(request):
    soc_dict = models.fetch_soccer()
    return render(request, 'inventory/soccer.html', {'soc_dict': soc_dict})

def fetch_tennis(request):
    ten_dict = models.fetch_tennis()
    return render(request, 'inventory/tennis.html', {'ten_dict': ten_dict})

def edit_prod(request):
    id = request.POST.get('id', '')
    if(id == ''):
        return HttpResponseRedirect('/')
    
    title = "Edit Product"
    
    form = forms.ProductForm()

    if('popup' in id):
        action = ''
        id = id.replace('popup', '')
        try:
            prod = models.fetch_all_products_process(id)
            form = forms.ProductForm(auto_id=False, initial={'id':prod.id,'product':prod.product,'sport':forms.searchSportForKey(prod.sport),'vendor':prod.vendor,'price':prod.price,'size':prod.size,'color':prod.color,'product_image':prod.product_image})
        except ValidationError as err:
            for err in err.messages:
                form.add_error(None, err)
            action = 'ERROR'
        except:
            print('Unexpected error: ' + str(sys.exc_info()[0]))
            action = 'ERROR'
    else:
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
                models.edit_process(id, product, vendor, sport, price, size, color, product_image)
                action = 'EDIT_SUCCESSFUL'
            except ValidationError as err:
                for err in err.messages:
                    form.add_error(None, err)
                action = 'ERROR'
            except:
                print('Unexpected error: ' + sys.exc_info()[0])
                form.add_error(None, 'Unexpected error - Please contact your system administrator')
                action = 'ERROR'
        else:
            action = 'ERROR'
    return render(request, 'inventory/edit_prod_form.html', {'action': action, 'form': form, 'title': title})

def delete_prod(request):
    id = request.POST.get('id', '')
    if(id == ''):
        return HttpResponseRedirect('/')
    else:
        id = id.replace('popup', '')
    try:
        models.delete_process(id)
    except:
        print('Unexpected error: ', + sys.exc_info()[0])
    return HttpResponseRedirect('/')

