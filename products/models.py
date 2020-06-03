from django.db import models

from djmoney.models.fields import MoneyField

PRODUCT_TYPES = (
    ('electrical', 'Electrical'),
    ('electronics', 'Electronics'),
    ('voucher', 'Voucher'),
    ('book', 'Book'),
    ('running', 'Running'),
    ('ceramics', 'Ceramics'),
    ('casual', 'Casual'),
)


class Product(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    type = models.CharField(max_length=12, choices=PRODUCT_TYPES)
    department = models.CharField(max_length=50)
    weight = models.PositiveIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]
