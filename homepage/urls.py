from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exec/', views.exec, name='home'),
    path('projects/', views.projects, name='home'),
    path('blog/', views.blog, name='home'),
    path('events/', views.events, name='home'),
    path('subscribe/', views.subscribe, name='home'),
    path('subscribe/<submitted>/', views.subscribe, name='home'),
]
