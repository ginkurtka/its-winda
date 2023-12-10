from django.shortcuts import render
from .models import *

def home_view(request):
    latest_hotel = Hotel.objects.filter
    context = {'latest_hotel': latest_hotel}
    return render(request, 'home/home_page.html', context)
