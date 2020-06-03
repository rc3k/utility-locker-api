from rest_framework import serializers

from .models import Product, PRODUCT_TYPES


class ProductSerializer(serializers.ModelSerializer):
    """
    creates a serialized representation of a product
    """

    price = serializers.SerializerMethodField()
    type_name = serializers.SerializerMethodField()

    def get_price(self, instance):
        return {
            'value': float(instance.price.amount),
            'currency': instance.price.currency.code,
        }

    def get_type_name(self, instance):
        return dict(PRODUCT_TYPES)[instance.type]

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'type',
            'type_name',
            'department',
            'weight'
        )
