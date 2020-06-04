from rest_framework import routers

from django.conf.urls import url

from .views import ProductViewSet, get_product_types

app_name = 'products'
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls + [
    url(r'^producttypes/$', get_product_types, name='get_product_types'),
]
