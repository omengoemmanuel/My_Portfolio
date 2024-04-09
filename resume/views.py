from django.shortcuts import render, redirect

from .models import home, project, referees, New_Messages, servicess, blogs, works, portfolios, work_done_details, \
    feedback


# Create your views here.
def index(request):
    homes = home.objects.all()
    proj = project.objects.all()
    ref = referees.objects.all()
    return render(request, 'index.html', {'navbar': 'index', 'homes': homes, 'proj': proj, 'ref': ref})


def about(request):
    homes = home.objects.all()
    return render(request, 'about.html', {'homes': homes})


def blog(request):
    blogss = blogs.objects.all()
    return render(request, 'blog.html', {'blogss': blogss})


def services(request):
    service = servicess.objects.all()
    return render(request, 'services.html', {'service': service})


def work(request):
    workss = works.objects.all()
    return render(request, 'work.html', {'workss': workss})


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


def blogsingle(request):
    workdone = work_done_details.objects.all()
    reply = feedback.objects.all()
    feed = feedback.objects.count()
    return render(request, 'blog-single.html', {'workdone': workdone, 'reply': reply, 'feed': feed})


def workdetails(request):
    port = portfolios.objects.all()
    return render(request, 'work-details.html', {'port': port})


def feedbackdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        comment = request.POST.get('comment')

        feed = feedback(name=name, email=email, title=title, comment=comment)
        feed.save()
        return redirect("/blogsingle")

    return redirect("/blogsingle")
