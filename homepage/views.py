from django.shortcuts import render
from homepage.models import *

def home(request):

    context = {

    }

    return render(request, 'homepage/home.html', context)

def exec(request):

    context = {
        'execs':ExecMember.objects.all().order_by('sort_index')
    }

    return render(request, 'homepage/exec.html', context)

def projects(request):

    context = {
        'projects':Project.objects.all().order_by('-date')
    }

    return render(request, 'homepage/projects.html', context)

def blog(request):

    context = {
        'posts':BlogPost.objects.all().order_by('-date')
    }

    return render(request, 'homepage/blog.html', context)

def events(request):

    context = {
        'events':Event.objects.all().order_by('date')
    }

    return render(request, 'homepage/events.html', context)

def subscribe(request):

    context = {

    }

    return render(request, 'homepage/subscribe.html', context)
