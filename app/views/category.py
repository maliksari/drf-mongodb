import time

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

from app.models import Category
from app.serializers.category import CategorySerializer, CategoryProductSerializer


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryProductsView(APIView):

    @swagger_auto_schema(operation_description="Kategoriye ait ürünleri listler", tags=['Category-Products'])
    def get(self, request, pk):
        categories = Category.objects.prefetch_related('products').get(id=pk)
        serializer = CategoryProductSerializer(categories, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllCategoryProductsView(APIView):

    @swagger_auto_schema(operation_description="Kategorileri ve kategoriye ait ürünlerin listesini döner", tags=['Category-Products'])
    def get(self, request):
        categories = Category.objects.prefetch_related('products').all()
        serializer = CategoryProductSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TestAPI(APIView):
    @swagger_auto_schema(operation_description="Test amaçlı", tags=['Test'])
    def get(self, request):
        import json
        start_time = time.perf_counter()
        time.sleep(5)
        duration = time.time() - start_time
        response = {"message": "Hello world!", "duration": duration}
        logger.warning('Test log ' + json.dumps(response))
        
        return Response(response)
