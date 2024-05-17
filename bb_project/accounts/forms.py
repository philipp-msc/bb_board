from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives



from allauth.account.forms import SignupForm
from django.core.mail import send_mail


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    def save(self, request):
        user = super().save(request)

        subject = 'Добро пожаловать на наш портал!'
        text = f'{user.username}, вы успешно зарегистрировались на сайте!'
        html = (
            f'<b>{user.username}</b>, вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/products">сайте</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        return user