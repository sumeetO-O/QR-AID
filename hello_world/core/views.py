from django.shortcuts import render

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "Django example",
        },
    )

def user(request):
    return render(
        request,
        "user.html",
        {
            "title": "USER 088",
        },
    )