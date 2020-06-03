import json
import os

from django.db import migrations, models

from djmoney.money import Money

from products.models import PRODUCT_TYPES


def forwards(apps, schema_editor):
    module_dir = os.path.dirname(__file__)
    Product = apps.get_model("products", "Product")

    db_alias = schema_editor.connection.alias
    product_types = {v: k for k, v in PRODUCT_TYPES}

    with open(os.path.join(module_dir, 'products.json')) as json_file:
        product_list = json.load(json_file)
        product_objects = [
            Product(
                id=product_item['id'],
                name=product_item['name'],
                description=product_item['description'],
                price=Money(product_item['price']['value'], product_item['price']['currency']),
                type=product_types[product_item['type']],
                department=product_item['department'],
                weight=int(product_item['weight'][:-1])
            ) for product_item in product_list
        ]
        Product.objects.using(db_alias).bulk_create(set(product_objects))


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, reverse_code=migrations.RunPython.noop),
    ]
