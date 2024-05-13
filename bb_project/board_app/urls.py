from django.contrib import admin
from django.urls import path

from board_app.views import *

urlpatterns = [
    # path('', index)
    path('', AdList.as_view(),name='ad_list'),
    path('ad/<int:pk>/', AdDetail.as_view(),name='ad_detail'),
    path('create/', AdCreate.as_view(), name='ad_create'),
    path('ad/<int:pk>/edit', AdEdit.as_view(), name='ad_edit'),
    path('ad/<int:pk>/delete', AdDelete.as_view(), name='ad_delete'),
]