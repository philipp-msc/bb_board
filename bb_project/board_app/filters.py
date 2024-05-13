from django_filters import FilterSet
from .models import Ad


class AdFilter(FilterSet):
   class Meta:
        model = Ad
        fields = {
           'title': ['icontains'],
           'category': ['icontains'],
       }