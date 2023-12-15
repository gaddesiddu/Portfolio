from django.shortcuts import render, HttpResponse
from home.models import Contact


# Create your views here.
def home(request):
    context = {"name": "siddu", "course": "Django"}
    return render(request, "home.html", context)


def about(request):
    context = {"name": "siri", "course": "IIT"}
    return render(request, "about.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        desc = request.POST["desc"]
        # print(name, email, desc)
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()

    return render(request, "contact.html")


def projects(request):
    return render(request, "projects.html")
