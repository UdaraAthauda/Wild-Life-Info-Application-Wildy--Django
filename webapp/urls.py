from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<int:cat>/', views.category, name="category"),
    path('information/<int:pk>/', views.information, name="information"),
]
