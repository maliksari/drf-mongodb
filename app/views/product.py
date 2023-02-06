from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from app.models import Product
from app.serializers.product import ProductSerializer


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
