import django_filters
from .models import RawDataCaltalog
from django_filters import CharFilter


class RawDataCaltalogFilter(django_filters.FilterSet):
    class Meta:
        model = RawDataCaltalog
        fields = ['source', 'destination', 'source_type', 'destination_type' ]