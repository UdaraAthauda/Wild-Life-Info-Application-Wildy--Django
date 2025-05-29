from django.shortcuts import render, redirect
from .forms import *
from .models import *
from webapp.models import Snake


# write a blog page view
def write_blogs(request, pk):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        snake = Snake.objects.get(pk=pk)

        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.snake = snake
            blog.save()
            return redirect('home')
        else:
            print('submit failed...............')
            return render(request, 'blog_post.html', context={'snake_details': snake, 'form': form})


    form = BlogPostForm()

    snake_details = Snake.objects.get(pk=pk)
    context = {'snake_details': snake_details, 'form': form}

    return render(request, 'blog_post.html', context=context)


# separate blog grid display according to the snake
def blog_grid(request):
    snake_details = Snake.objects.all()
    context = {'snake_details': snake_details}

    return render(request, 'blog_grid.html', context=context)
