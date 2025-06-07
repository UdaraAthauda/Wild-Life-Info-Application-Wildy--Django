from django.urls import path
from . import views

urlpatterns = [
    path('user_signup/', views.user_signup, name='user_signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('delete_account/', views.delete_account, name='delete_account'),
]
