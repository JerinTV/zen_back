# users/urls.py
from django.urls import path
from .views import UserRegistrationView, MyTokenObtainPairView # Import your views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    # This is for your login (token obtain) endpoint, make sure it's here
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]