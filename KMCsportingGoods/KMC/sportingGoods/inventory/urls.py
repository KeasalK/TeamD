from django.conf.urls import url
from . import views

app_name = 'inventory_ns'

urlpatterns = [
    url(r'^$', views.add_product, name='products'),
    url(r'^add_product/', views.add_product, name="add_product"),
]