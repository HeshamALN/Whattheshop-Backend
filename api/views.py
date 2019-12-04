from .models import Salfa, Cart,CartSalfa
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
>>>>>>> profilebackend FEE MOSHKILAAgit add .git add .
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
	CreateAPIView
	)
from rest_framework.views import APIView
from .serializers import (
	UserCreateSerializer,
	SalfaInfoSerializer, 
	SalfaCreateUpdateSerializer,
	AddToCartSerializer,
	# CartSerializer, 
	ProfileSerializer

	)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwner
from rest_framework.response import Response

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer


class AddToCartView(CreateAPIView):
	serializer_class = AddToCartSerializer
	permission_classes = [IsAuthenticated,IsOwner,]


class CartCheckoutAPIView(APIView):
	
	permission_classes = [IsAuthenticated,]
	
	def post(self, request, format=None):
		cart = Cart.objects.get(user=self.request.user, checkout_status=False)
		cart.checkout_status = True
		cart.save()
		Cart.objects.create(user=self.request.user)
		return Response()

class ProfileAPIView(RetrieveAPIView):
<<<<<<< HEAD
	queryset = User.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated]
=======
	serializer_class = ProfileSerializer
	# permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return self.request.user
>>>>>>> profilebackend FEE MOSHKILAAgit add .git add .

# Not Needed Yet ! [for checkout feature]



class SalfaInfoView(ListAPIView):
	queryset = Salfa.objects.all()
	serializer_class = SalfaInfoSerializer
	permission_classes = [AllowAny,]


class SalfaCreateView(CreateAPIView):
	serializer_class = SalfaCreateUpdateSerializer
	permission_classes = [IsAuthenticated]

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