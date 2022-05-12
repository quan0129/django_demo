from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from . import models
from .filters import SearchFilter
from .forms import SearchForm


def homepage(request):
    return render(request, 'index.html')

def search(request):
    myFilter = SearchFilter(request.GET)
    context = {'searchFilter': myFilter}
    return render(request, 'search_apps.html', context)