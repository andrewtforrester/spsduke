from django.shortcuts import render

def home(request):
    return render(request, 'homepage/home.html', {})

def exec(request):
    return render(request, 'homepage/exec.html', {})

def projects(request):
    return render(request, 'homepage/projects.html', {})

def blog(request):
    return render(request, 'homepage/blog.html', {})

def events(request):
    return render(request, 'homepage/events.html', {})

def subscribe(request):
    return render(request, 'homepage/subscribe.html', {})
