from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Q


def home(request):

    if request.method == 'POST':
        searched = request.POST.get('searched')
        searched_snake_details = Snake.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched) | Q(description_translation__icontains=searched))

        context = {'searched_snake_details': searched_snake_details}

        return render(request, 'home.html', context=context)
    
   
        
    snake_details = Snake.objects.all()

    context = {'snake_details': snake_details}

    return render(request, 'home.html', context=context)