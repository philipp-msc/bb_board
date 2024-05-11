from django.contrib import admin
from django.urls import path

from board_app.views import *

urlpatterns = [
    # path('', index)
    path('', AdList.as_view())
]