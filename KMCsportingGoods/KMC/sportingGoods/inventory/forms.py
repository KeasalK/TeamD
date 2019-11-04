from django import forms
from datetime import date

SPORT = ((0, 'Baseball'), (1, 'Basketball'), (2, 'Football'),
        (3, 'Golf'), (4, 'Soccer'), (5, 'Softball'), (6, 'Tennis'))



class ProductForm(forms.Form):
    product = forms.CharField()
    sport = forms.ChoiceField(choices=SPORT)
    vender = forms.CharField()
    price = forms.IntegerField(min_value=0)
    size = forms.CharField()
    color = forms.CharField()
    product_image = forms.URLField()
    field_order = ['product', 'sport', 'vender', 'price', 'size', 'color', 'product_image']
    
