from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Q

# home page view
def home(request):

    if request.method == 'POST':
        searched = request.POST.get('searched')
        searched_snake_details = Snake.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched) | Q(description_translation__icontains=searched))

        context = {'searched_snake_details': searched_snake_details}

        return render(request, 'home.html', context=context)
    
   
        
    snake_details = Snake.objects.all()

    context = {'snake_details': snake_details}

    return render(request, 'home.html', context=context)


# category page view
def category(request, cat):
    get_category = VenomType.objects.get(pk=cat)
    snake_details = Snake.objects.filter(is_venomous=get_category)

    if request.method == 'POST':
        searched = request.POST.get('searched')
        searched_snake_details = Snake.objects.filter(Q(is_venomous=get_category) & Q(name__icontains=searched) | Q(description__icontains=searched) | Q(description_translation__icontains=searched))

        context = {'searched_snake_details': searched_snake_details}

        return render(request, 'category.html', context=context)

    context = {'snake_details': snake_details}

    return render(request, 'category.html', context=context)

# single animal information display view
def information(request, pk):
    snake_details = Snake.objects.get(pk=pk)

    context = {'snake': snake_details}

    return render(request, 'information.html', context=context)