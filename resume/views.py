from django.shortcuts import render
from .models import home,project


# Create your views here.
def index(request):
    homes = home.objects.all()
    proj = project.objects.all()
    return render(request, 'index.html', {'homes':homes, 'proj':proj})


def about(request):
    homes = home.objects.all()
    return render(request, 'about.html', {'homes':homes})


def blog(request):
    return render(request, 'blog.html')


def services(request):
    return render(request, 'services.html')


def work(request):
    return render(request, 'work.html')


def contact(request):
    return render(request, 'contact.html')
