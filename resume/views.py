from django.shortcuts import render, redirect
from .models import home, project, referees, New_Messages


# Create your views here.
def index(request):
    homes = home.objects.all()
    proj = project.objects.all()
    ref = referees.objects.all()
    return render(request, 'index.html', {'homes': homes, 'proj': proj, 'ref': ref})


def about(request):
    homes = home.objects.all()
    return render(request, 'about.html', {'homes': homes})


def blog(request):
    return render(request, 'blog.html')


def services(request):
    return render(request, 'services.html')


def work(request):
    return render(request, 'work.html')


def contact(request):
    return render(request, 'contact.html')


def sendmessage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        description = request.POST.get('description')

        msg = New_Messages(name=name, email=email, subject=subject, description=description)
        msg.save()

        return redirect("/")

    return redirect('/')

