from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import LogoutView

from . import views
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('account/profile/', ProfileView.as_view(), name='profileview'),
    path('account/signup/', UserRegView.as_view(), name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/logout/', LogoutView.as_view(), name='logout'),
    path('Cat/<int:pk>/', views.Cat_detail, name='Cat_detail'),
    path('account/passwordchange/', views.change_password, name='passwordchange'),
]