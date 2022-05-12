from django.contrib import admin
from .models import RawDataCaltalog


@admin.register(RawDataCaltalog)
class RawDataCaltalogAdmin(admin.ModelAdmin):
    list_display = ('source', 'source_type', 'destination', 'destination_type', 'description')