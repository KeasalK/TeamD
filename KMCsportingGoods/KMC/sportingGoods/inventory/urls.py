from django.conf.urls import url
from . import views

#Delete when products urls gets completely built out
from django.views.generic import TemplateView

app_name = 'inventory_ns'

urlpatterns = [
    url(r'^$', views.fetch_all_products),
    url(r'^add_product/', views.add_product, name="add_product"),
    url(r'^editprod/', views.edit_prod, name="editprod"),
    url(r'^deleteprod/', views.delete_prod, name="deleteprod"),
]