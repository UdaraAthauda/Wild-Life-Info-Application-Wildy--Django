from django.urls import path
from . import views

urlpatterns = [
    path('write_blogs/<int:pk>/', views.write_blogs, name="write_blogs"),
    path('blog_grid', views.blog_grid, name="blog_grid"),
    path('read_blogs/<int:pk>/', views.read_blogs, name="read_blogs"),
    path('add_comment/<int:blog_id>/', views.add_comment, name="add_comment"),
]
