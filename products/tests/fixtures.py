import pytest


@pytest.fixture
def products():
    return [{
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
    }, {
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
    }, {
        'id': 'ASC-19-RUN',
        'name': 'Asics Gel-Nimbus 19',
        'description': 'Asics Gel-Nimbus 19 Running shoes',
        'price': {
            'value': 108.5,
            'currency': 'GBP'
        },
        'type': 'running',
        'type_name': 'Running',
        'department': 'Shoes',
        'weight': 150
    }, {
        'id': 'BSH-DRL-876',
        'name': 'Bosch Cordless Drill',
        'description': 'Cordless drill with 12W charging unit',
        'price': {
            'value': 159.99,
            'currency': 'GBP'
        },
        'type': 'electrical',
        'type_name': 'Electrical',
        'department': 'DIY',
        'weight': 1579
    }, {
        'id': 'FM-345-A',
        'name': 'Breville Food Mixer 800W',
        'description': 'Breville food mixer with bowl and multiple mixing arms. 800W max power',
        'price': {
            'value': 69.99,
            'currency': 'GBP'
        },
        'type': 'electrical',
        'type_name': 'Electrical',
        'department': 'Cookware',
        'weight': 2370
    }, {
        'id': 'Canon EF III Lens',
        'name': 'Canon EF 75-300mm f/4.0-5.6 III Lens',
        'description': 'Canon EF 75-300mm f/4.0-5.6 III Lens',
        'price': {
            'value': 124.76,
            'currency': 'GBP'
        },
        'type': 'electrical',
        'type_name': 'Electrical',
        'department': 'Photography and Art',
        'weight': 460
    }, {
        'id': 'CLN-CDE-BOOK',
        'name': 'Clean Code',
        'description': 'Clean Code: A Handbook of Agile Software Craftsmanship (Robert C. Martin)',
        'price': {
            'value': 18.99,
            'currency': 'GBP'
        },
        'type': 'book',
        'type_name': 'Book',
        'department': 'Books and Stationery',
        'weight': 220
    }, {
        'id': 'KSCL',
        'name': 'Kitchen Scales',
        'description': 'Traditional Kitchen Scales',
        'price': {
            'value': 79.99,
            'currency': 'GBP'
        },
        'type': 'electrical',
        'type_name': 'Electrical',
        'department': 'Cookwares',
        'weight': 1057
    }, {
        'id': 'Happy-Mug',
        'name': 'Mr Happy Mug',
        'description': 'Mr Men Mug. Mr Happy. 300ml',
        'price': {
            'value': 8.5,
            'currency': 'GBP'
        },
        'type': 'ceramics',
        'type_name': 'Ceramics',
        'department': 'Home',
        'weight': 110
    }, {
        'id': 'DRVTHR-BOOK',
        'name': 'Pass the Driving Test',
        'description': 'Book - Pass your driving test - Penguin publishers',
        'price': {
            'value': 7.99,
            'currency': 'GBP'
        },
        'type': 'book',
        'type_name': 'Book',
        'department': 'Books and Stationery',
        'weight': 57
    }, {
        'id': 'RPi-0',
        'name': 'Raspberry Pi Zero',
        'description': 'Raspberry PI Zero Computer',
        'price': {
            'value': 4.8,
            'currency': 'GBP'
        },
        'type': 'electrical',
        'type_name': 'Electrical',
        'department': 'Computing',
        'weight': 30
    }, {
        'id': 'SGN-2',
        'name': 'Samsung Galaxy Note 2',
        'description': 'Samsung tablet computer',
        'price': {
            'value': 299.99,
            'currency': 'GBP'
        },
        'type': 'electrical',
        'type_name': 'Electrical',
        'department': 'Computing',
        'weight': 569
    }, {
        'id': 'Sket-Twinc-156',
        'name': 'Sketcher Twinkle Toes',
        'description': 'Pink Sketcher Twinkle Toe sandals with light up sole',
        'price': {
            'value': 19.99,
            'currency': 'GBP'
        },
        'type': 'casual',
        'type_name': 'Casual',
        'department': 'Shoes',
        'weight': 100
    }, {
        'id': 'Flashgun',
        'name': 'YongNuo YN-560 III Flashgun',
        'description': 'YongNuo YN-560 III Flashgun',
        'price': {
            'value': 47.95,
            'currency': 'GBP'
        },
        'type': 'electronics',
        'type_name': 'Electronics',
        'department': 'Photography and Art',
        'weight': 260
    }]
