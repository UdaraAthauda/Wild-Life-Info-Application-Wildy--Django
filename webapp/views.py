from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    snake_details = Snake.objects.all()

    context = {'snake_details': snake_details}

    return render(request, 'home.html', context=context)