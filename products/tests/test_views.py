import json
import pytest

from django.test.client import RequestFactory

from ..views import ProductViewSet
from .fixtures import products


@pytest.mark.django_db
def test_products_viewset_list(products):
    request = RequestFactory().get('/products/')
    view = ProductViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == 200
    assert json.loads(response.rendered_content) == products


@pytest.mark.django_db
def test_products_viewset_list_order_by_price_ascending(products):
    request = RequestFactory().get('/products/?col={}&dir={}'.format('price', 'asc'))
    view = ProductViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == 200
    assert json.loads(response.rendered_content) == sorted(
        products, key=lambda product: product['price']['value']
    )


@pytest.mark.django_db
def test_products_viewset_list_order_by_price_descending(products):
    request = RequestFactory().get('/products/?col={}&dir={}'.format('price', 'desc'))
    view = ProductViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == 200
    assert json.loads(response.rendered_content) == sorted(
        products, key=lambda product: product['price']['value'], reverse=True
    )


@pytest.mark.django_db
def test_products_viewset_list_filter_by_type(products):
    request = RequestFactory().get('/products/?type={}'.format('electrical'))
    view = ProductViewSet.as_view({'get': 'list'})
    response = view(request)
    content = json.loads(response.rendered_content)
    assert len(content) == 7  # the number of electrical products
    assert all([product['type'] == 'electrical' for product in content])
