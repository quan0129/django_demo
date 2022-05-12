from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'apps'
urlpatterns = [
    path('', views.homepage, name='index'),
    path('search/', views.search)
    # path('<int:question_id>/', views.detail_question, name='detail'),
    # path('<int:question_id>/vote/', views.vote_question, name='vote'),
]




