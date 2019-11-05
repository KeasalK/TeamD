from django.conf.urls import url
from . import views

#Delete when products urls gets completely built out
from django.views.generic import TemplateView

app_name = 'inventory_ns'

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='products.html')),
    url(r'^add_product/', views.add_product, name="add_product"),
]