from django.shortcuts import render
from homepage.models import *
import datetime

def home(request):

    context = {

    }

    return render(request, 'homepage/home.html', context)

def exec(request):

    context = {
        'execs2019':ExecMember.objects.filter(year_term_started=2019).order_by('sort_index'),
        'execs2020':ExecMember.objects.filter(year_term_started=2020).order_by('sort_index')
    }

    return render(request, 'homepage/exec.html', context)

def projects(request):

    context = {
        'current_projects':Project.objects.filter(past=0).order_by('title'),
        'past_projects':Project.objects.filter(past=1).order_by('title')
    }

    return render(request, 'homepage/projects.html', context)

def blog(request):

    context = {
        'posts':BlogPost.objects.all().order_by('-date')
    }

    return render(request, 'homepage/blog.html', context)

def events(request):

    context = {
        'events':Event.objects.filter(display=1).order_by('date'),
        'photos':EventImage.objects.filter(associated_event__title = "Generic Past Event"),
        'today':datetime.date.today
    }

    return render(request, 'homepage/events.html', context)

def subscribe(request):

    context = {

    }

    return render(request, 'homepage/subscribe.html', context)
