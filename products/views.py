from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ViewSet):
    """
    a simple for viewset for returning a list of products with optional ordering and filtering by type
    """

    def list(self, request):
        order_column = request.query_params.get('col', 'name').lower()
        order_direction = request.query_params.get('dir', 'asc').lower()

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
