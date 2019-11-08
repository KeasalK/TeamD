from django.conf.urls import url
from . import views


app_name = 'order_ns'

urlpatterns = [
    url(r'^$', views.fetch_cart_items, name="cart"),
    url(r'^addItem/', views.add_cart_item, name="addItem"),
    url(r'^removeItem/', views.remove_cart_item, name="removeItem"),
    url(r'^checkout/', views.fetch_mini_cart_items, name="checkout"),
]