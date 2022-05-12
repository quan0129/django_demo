from django.contrib import admin
from django.urls import path
from .views import search, search_results, monitor_filter, detail_table


app_name = 'monitor_db_search'

urlpatterns = [
    path('', search, name='home'),
    path('search/', search_results, name='search_results'),
    path('filter/', monitor_filter, name='filter_results'),
    path('detail/<str:source>', detail_table, name='detail'),

]