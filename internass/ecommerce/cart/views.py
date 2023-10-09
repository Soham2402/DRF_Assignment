from .models import User, Cart
from .serializers import CartSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action

class CartViewSet(viewsets.ViewSet):
    def list(self,request):
        try:
            user = User.objects.all()
            serialized = UserSerializer(user,many = True)
            return Response(data = serialized.data, status = status.HTTP_302_FOUND)
        except User.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
    
    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(id = pk)
            cart = Cart.objects.get(user=user)
            serialized = CartSerializer(cart)
            return Response(data = serialized.data, status = status.HTTP_302_FOUND)
        except Cart.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        
    # @action(detail=True, methods=['post'])
    # def addItem(self, request, pk=None):
    #     try:
    #         user = User.objects.get(id=pk)
    #         product_id = request.data.get('product_id')
    #         cart, created = Cart.objects.get_or_create(user=user)
    #         cart.products.add(product_id) 
    #         serialized = CartSerializer(cart)
    #         return Response(data=serialized.data, status=status.HTTP_201_CREATED)
    #     except User.DoesNotExist:
    #         return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=True, methods=['post'])
    def addItem(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            product_id = request.data.get('product_id')
            cart, created = Cart.objects.get_or_create(user=user)

            # Ensure that the Cart object is saved before adding products
            if created:
                cart.save()

            cart.products.add(product_id)
            serialized = CartSerializer(cart)
            return Response(data=serialized.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
