from django.contrib import admin
from django.conf.urls import *
from django.urls import path

urlpatterns = [
    url(r'^', include('products.urls', namespace='products_api')),
    path('admin/', admin.site.urls),
]
