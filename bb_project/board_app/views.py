from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *
from .filters import AdFilter
from .forms import AdForm


# def index(request):
#     return render(request, 'index.html')

class AdList(ListView):
    model = Ad
    template_name = 'board_app/ad_list.html'  # Путь к вашему шаблону ad_list.html
    context_object_name = 'adList'
    paginate_by = 3

    # def get_queryset(self):
    #     return Ad.objects.all() 

    def get_queryset(self):
        queryset = Ad.objects.all()
        self.filterset = AdFilter(self.request.GET, queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context
    

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
        context['date'] = self.object.date
        return context

class AdCreate(LoginRequiredMixin, CreateView):
    model = Ad
    form_class = AdForm
    template_name = 'board_app/ad_create.html'
    raise_exception = True

class AdEdit(LoginRequiredMixin, UpdateView):
    form_class = AdForm
    model = Ad
    template_name = 'ad_edit.html'
    raise_exception = True

class AdDelete(LoginRequiredMixin, DeleteView):
    model = Ad
    template_name = 'board_app/ad_delete.html'
    success_url = reverse_lazy('ad_list')
    raise_exception = True
