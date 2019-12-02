from .models import Salfa, Cart,CartSalfa
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
	)
from .serializers import (
	UserCreateSerializer,
	SalfaInfoSerializer, 
	SalfaCreateUpdateSerializer,
	AddToCartSerializer,
	# CartSerializer
	)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwner

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer


class AddToCartView(CreateAPIView):
	serializer_class = AddToCartSerializer
	permission_classes = [IsAuthenticated,IsOwner,]

	
	
# Not Needed Yet ! [for checkout feature]

# class CartAPIView(RetrieveAPIView):
# 	queryset = Cart.objects.all()
# 	serializer_class = CartSerializer
# 	lookup_field = 'id'
# 	permission_classes = [IsAuthenticated, IsOwner,]


class SalfaInfoView(ListAPIView):
	queryset = Salfa.objects.all()
	serializer_class = SalfaInfoSerializer
	permission_classes = [AllowAny,]


class SalfaCreateView(CreateAPIView):
	serializer_class = SalfaCreateUpdateSerializer
	permission_classes = [IsAuthenticated,]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class SalfaUpdateView(RetrieveUpdateAPIView):
	queryset = Salfa.objects.all()
	serializer_class = SalfaCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'salfa_id'
	permission_classes = [IsAuthenticated,IsOwner]


class SalfaDeleteView(DestroyAPIView):
	queryset = Salfa.objects.all()
	serializer_class = SalfaInfoSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'salfa_id'
	permission_classes = [IsAuthenticated,IsAdminUser]