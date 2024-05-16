from django.urls import path
from .views import SignUp

urlpatterns = [
    path('accounts/signup/', SignUp.as_view(), name='account_signup'),
]