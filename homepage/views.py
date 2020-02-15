from django.shortcuts import render
from homepage.models import *
import datetime

def home(request):
    context = {}
    return render(request, 'homepage/home.html', context)

def projects(request):
    context = {
        'projects':[(a,a.projectimage_set.all(),a.projectimage_set.all().count()) for a in Project.objects.all().order_by('title')],
    }
    return render(request, 'homepage/projects.html', context)

def events(request):
    events = [(a,a.eventimage_set.all().first()) for a in Event.objects.filter(display=1).order_by('date')]
    context = {
        'events':events,
        'events_reversed':events[::-1],
        'photos':EventImage.objects.filter(associated_event__title = "Generic Past Event"),
        'today':datetime.date.today
    }
    return render(request, 'homepage/events.html', context)

def blog(request):
    context = {
        'posts':[(a,a.blogpostimage_set.all(),a.blogpostimage_set.all().count()) for a in BlogPost.objects.all().order_by('-date')]
    }
    return render(request, 'homepage/blog.html', context)

def exec(request):
    context = {
        'execs2019':ExecMember.objects.filter(year_term_started=2019).order_by('sort_index'),
        'execs2020':ExecMember.objects.filter(year_term_started=2020).order_by('sort_index')
    }
    return render(request, 'homepage/exec.html', context)

def subscribe(request, submitted=""):
    if not submitted == "":
        test_field = [a.email for a in Subscriber.objects.all()]
        duplicate = False
        r_email = request.GET['email']

        for test in test_field:
            if test == r_email:
                duplicate = True
                break

        if not duplicate:
            b = Subscriber(name=request.GET['name'],email=r_email,comment=request.GET['comment'])
            b.save()
        return render(request, 'homepage/subscribe_thanks.html', {})
    else:
        return render(request, 'homepage/subscribe.html', {})
