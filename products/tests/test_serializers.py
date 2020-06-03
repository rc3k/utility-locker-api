import pytest

from ..models import Product
from ..serializers import ProductSerializer


@pytest.mark.django_db
def test_serialize_single_product():
    product = Product.objects.get(id='Veronica-367')
    assert ProductSerializer(product).data == {
        'id': 'Veronica-367',
        'name': 'Amazon Echo',
        'description': 'Amazon Echo, White',
        'price': {
            'value': 149.99,
            'currency': 'GBP'
        },
        'type': 'electrical',
        'type_name': 'Electrical',
        'department': 'Entertainment',
        'weight': 1098
    }


@pytest.mark.django_db
def test_serialize_multiple_products():
    product1 = Product.objects.get(id='Veronica-367')
    product2 = Product.objects.get(id='AMZ50')
    assert ProductSerializer([product1, product2], many=True).data == [
        {
            'id': 'Veronica-367',
            'name': 'Amazon Echo',
            'description': 'Amazon Echo, White',
            'price': {
                'value': 149.99,
                'currency': 'GBP'
            },
            'type': 'electrical',
            'type_name': 'Electrical',
            'department': 'Entertainment',
            'weight': 1098
        },
        {
            'id': 'AMZ50',
            'name': 'Amazon Voucher',
            'description': 'Fifty Pounds Amazon Voucher Card',
            'price': {
                'value': 50.0,
                'currency': 'GBP'
            },
            'type': 'voucher',
            'type_name': 'Voucher',
            'department': 'Gifts',
            'weight': 5
        },
    ]
