from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, PRODUCT_TYPES
from .serializers import ProductSerializer


class ProductViewSet(ViewSet):
    """
    a simple viewset for retrieving a list of products with optional ordering and filtering by type
    """

    def list(self, request):
        order_column = request.query_params.get('column', 'name').lower()
        order_direction = request.query_params.get('direction', 'asc').lower()

        queryset = Product.objects.all().order_by(
            '{}{}'.format(
                '-' if order_direction == 'desc' else '',
                order_column
            )
        )

        type = request.query_params.get('type', None)
        if type:
            queryset = queryset.filter(type=type)

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_product_types(request):
    """
    a simple viewset for retrieving a list of product types
    """
    return Response([{
        'key': key,
        'value': value,
    } for key, value in sorted(PRODUCT_TYPES, key=lambda pt: pt[1])])
