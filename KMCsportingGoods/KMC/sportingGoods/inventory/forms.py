from django import forms
from datetime import date


SPORT = ((0, 'Baseball'), (1, 'Basketball'), (2, 'Football'),
        (3, 'Golf'), (4, 'Soccer'), (5, 'Softball'), (6, 'Tennis'))



class ProductForm(forms.Form):
    product = forms.CharField()
    sport = forms.ChoiceField(choices=SPORT)
    vendor = forms.CharField()
    price = forms.FloatField(min_value=0)
    size = forms.CharField()
    color = forms.CharField()
    product_image = forms.URLField()
    field_order = ['product', 'sport', 'vendor', 'price', 'size', 'color', 'product_image']
    
class EditProductForm(forms.Form):
    id = forms.IntegerField(widget = forms.HiddenInput(), required = False)
    product = forms.CharField()
    sport = forms.CharField()
    vendor = forms.CharField()
    price = forms.FloatField()
    size = forms.CharField()
    color = forms.CharField()
    product_image = forms.URLField()
    #Override the default field order, which is the declaration order
    field_order = ['product', 'sport', 'vendor', 'price', 'size', 'color', 'product_image']

def searchSportForKey(value):
    for element in SPORT:
        if(value in element):
            return element[0]
    return -1