from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *
from .filters import AdFilter
from .forms import AdForm, ResponseForm




class AdList(ListView):
    model = Ad
    template_name = 'board_app/ad_list.html'  # Путь к вашему шаблону ad_list.html
    context_object_name = 'adList'
    paginate_by = 3


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
        context['category'] = self.object.get_category_display()        
        context['author'] = self.object.author
        context['title'] = self.object.title
        context['text'] = self.object.text
        context['upload'] = self.object.upload
        context['date'] = self.object.date
        context['form'] = ResponseForm() 
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

@login_required
def add_response_to_ad(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.ad = ad
            response.author = request.user
            response.save()

            send_mail(
                subject='Новый отклик на ваше объявление',
                message=f'Пользователь {request.user.username} оставил отклик на ваше объявление "{ad.title}".',
                from_email=None,  
                recipient_list=[ad.author.email],
            )
            return redirect('ad_detail', pk=pk)
    else:
        form = ResponseForm()
    return render(request, 'board_app/add_response_to_ad.html', {'form': form, 'ad': ad})

class UserAdsListView(ListView):
    model = Ad
    template_name = 'board_app/user_ads.html'
    context_object_name = 'user_ads'
    paginate_by = 10

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['pk'])
        return Ad.objects.filter(author=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = User.objects.get(pk=self.kwargs['pk'])
        return context

def delete_response(request, pk, response_pk):
    response = get_object_or_404(Response, pk=response_pk)
    if request.method == 'POST':
        response.delete()
    return redirect('ad_detail', pk=pk)

def accept_response(request, pk, response_pk):
    response = get_object_or_404(Response, pk=response_pk)

    if request.user != response.ad.author:
        return redirect('ad_detail', pk=pk)
    
    if request.method == 'POST':
        response.accepted = True
        response.save()
        
    return redirect('ad_detail', pk=pk)