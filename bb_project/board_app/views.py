from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from .models import *


# def index(request):
#     return render(request, 'index.html')

class AdList(ListView):
    model = Ad
    template_name = 'board_app/ad_list.html'  # Путь к вашему шаблону ad_list.html
    context_object_name = 'adList'

    def get_queryset(self):
        return Ad.objects.all() 
    

class AdDetail(DetailView):
    model = Ad
    template_name = 'board_app/ad_detail.html'
    context_object_name = 'adDetail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.object.category
        context['author'] = self.object.author
        context['title'] = self.object.title
        context['text'] = self.object.text
        context['upload'] = self.object.upload
        return context

class AdCreate(CreateView):
    model = Ad
    template_name = 'board_app/ad_create.html'
    fields = '__all__'