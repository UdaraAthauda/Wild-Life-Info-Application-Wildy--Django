from django.shortcuts import render, redirect
from .forms import *
from .models import *
from webapp.models import Snake
from django.contrib.auth.decorators import login_required


# write a blog page view
@login_required(login_url='user_login')
def write_blogs(request, pk):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        snake = Snake.objects.get(pk=pk)

        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.snake = snake
            blog.save()
            return redirect('blog_grid')
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


# read the blogs users wrote
def read_blogs(request, pk):
    snake = Snake.objects.get(pk=pk)
    blogs = BlogPost.objects.filter(snake=snake).order_by('-created_at')
    
    # Initialize an empty form for comments
    comment_form = CommentForm()
    
    # Create a dictionary to store comments for each blog
    blog_comments = {}
    
    # Get comments for each blog
    for blog in blogs:
        blog_comments[blog.id] = blog.comments.all().order_by('-created_at')
    
    context = {
        'blogs': blogs, 
        'snake': snake, 
        'comment_form': comment_form,
        'blog_comments': blog_comments
    }

    return render(request, 'read_blogs.html', context=context)

# add comment to a blog post
def add_comment(request, blog_id):
    blog = BlogPost.objects.get(pk=blog_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            if request.user.is_authenticated:
                comment.author = request.user
                
            comment.blog_post = blog
            comment.save()
    
    # Redirect back to the blog page
    return redirect('read_blogs', pk=blog.snake.pk)
