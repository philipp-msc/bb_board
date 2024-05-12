from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import *


# def index(request):
#     return render(request, 'index.html')

class AdList(ListView):
    model = Ad
    template_name = 'bb_project/ad_list.html'  # Путь к вашему шаблону ad_list.html
    context_object_name = 'ads'
