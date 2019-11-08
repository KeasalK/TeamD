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
    url(r'^softball/', views.fetch_softball, name="softball"),
    url(r'^baseball/', views.fetch_baseball, name="baseball"),
    url(r'^basketball/', views.fetch_basketball, name="basketball"),
    url(r'^football/', views.fetch_football, name="football"),
    url(r'^golf/', views.fetch_golf, name="golf"),
    url(r'^soccer/', views.fetch_soccer, name="soccer"),
    url(r'^tennis/', views.fetch_tennis, name="tennis"),
]