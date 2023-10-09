from .models import Product
from .serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            products = Product.objects.all()
            print(products)
            serialized = ProductSerializer(products,many = True)
            return Response(data = serialized.data, status = status.HTTP_302_FOUND)
        except Product.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
    def retrieve(self, request, pk=None):
        try:
            product = Product.objects.get(id = pk)
            serialized = ProductSerializer(product)
            return Response(data = serialized.data, status = status.HTTP_302_FOUND)
        except product.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)   
        
        
    def create(self, request):
        deserialized = ProductSerializer(data = request.data)
        if deserialized.is_valid():
            deserialized.save()
            return Response(data = deserialized.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_406_NOT_ACCEPTABLE)
        
    def destroy(self, request, pk = None):
        try:
            product = Product.objects.get(id = pk)
            product.delete()
            return Response(status = status.HTTP_202_ACCEPTED)
        except product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        