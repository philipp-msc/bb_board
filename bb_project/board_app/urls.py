from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from board_app.views import *

urlpatterns = [
    # path('', index)
    path('', AdList.as_view(),name='ad_list'),
    path('ad/<int:pk>/', AdDetail.as_view(),name='ad_detail'),
    path('create/', AdCreate.as_view(), name='ad_create'),
    path('ad/<int:pk>/edit', AdEdit.as_view(), name='ad_edit'),
    path('ad/<int:pk>/delete', AdDelete.as_view(), name='ad_delete'),
    path('ad/<int:pk>/add_response/', add_response_to_ad, name='add_response_to_ad'),
    path('user/<int:pk>/', UserAdsListView.as_view(), name='user_ads'),
    path('ad/<int:pk>/delete_response/<int:response_pk>/', views.delete_response, name='delete_response'),
    path('ad/<int:pk>/accept_response/<int:response_pk>/', views.accept_response, name='accept_response'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)