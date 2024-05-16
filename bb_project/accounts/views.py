from allauth.account.views import SignupView
from django.urls import reverse_lazy
from django.urls import include
from .forms import CustomSignupForm

class SignUp(SignupView):
    form_class = CustomSignupForm

    def get_success_url(self):
        return reverse_lazy('ad_list')