from django.urls import path
from .views import (
	UserCreateAPIView, 
	SalfaInfoView, 
	SalfaUpdateView, 
	SalfaDeleteView, 
	SalfaCreateView,
	AddToCartView,
	CartCheckoutAPIView,
	)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
	path('login/', TokenObtainPairView.as_view() , name='login'),
	path('register/', UserCreateAPIView.as_view(), name='register'),
	path('info/', SalfaInfoView.as_view(), name='api-info'),
	path('create/', SalfaCreateView.as_view(), name='api-create'),
	path('update/<int:salfa_id>/', SalfaUpdateView.as_view(), name='api-update'),
	path('delete/<int:salfa_id>', SalfaDeleteView.as_view(), name='api-delete'),
	path('cart/add/', AddToCartView.as_view(), name="cart-add"),
	path('checkout/', CartCheckoutAPIView.as_view(), name="cart-checkout"),



]