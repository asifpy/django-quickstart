from django.shortcuts import render

from core.constants import PACKAGES

def index(request):
    return render(request, 'index.html', {'packages': PACKAGES})