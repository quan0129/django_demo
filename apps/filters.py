import django_filters
from .models import *


class SearchFilter(django_filters.FilterSet):
    class Meta:
        model = raw_data_caltalog
        fields = {'id', 'source'}