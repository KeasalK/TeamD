"""sportingGoods URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib import admin


# For debugging purposes
from django.conf import settings
from sportingGoods.inventory import views as prod_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', TemplateView.as_view(template_name='about.html')),
    url(r'^$', TemplateView.as_view(template_name='homepage.html')),
    url(r'^inventory/', include('sportingGoods.inventory.urls', namespace='inventory_ns')),
    url(r'^inventory/products/', prod_views.fetch_all_products),
    url(r'^cart/', TemplateView.as_view(template_name='order/cart.html')),
    url(r'^checkout/', TemplateView.as_view(template_name='order/checkout.html')),
    url(r'^confirmation/', TemplateView.as_view(template_name='order/confirmation.html')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        
    ]