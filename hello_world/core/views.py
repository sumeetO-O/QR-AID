import os
from django.shortcuts import render
from twilio.rest import Client


account_sid = "AC88e3c2ea39b17c2a4c5b909706bd0f1b"
auth_token = "9e939875e5954017e13eeccb6971bfc2"

users = [
    {'id': 1, 'name': "BILHAL HING", 'hp1': "+91882569338"},
    {'id': 2, 'name': "GOKUL", 'hp1': "+916369373450"},
    {'id': 3, 'name': "CIBIN", 'hp1': "+916380099741"}
]

hospital = [
    {'id': 1, 'name': "AIIMS HOSPITAL", 'pn': "+916369373450"},
    {'id': 2, 'name': "AROGYA HOSPITAL", 'pn': "+916369373450"},
    {'id': 3, 'name': "LIINK BING HOSPITAL", 'pn': "+916369373450"},
    {'id': 4, 'name': "NAREAYANA HOSPITAL", 'pn': "+916369373450"},
    {'id': 5, 'name': "KPR HOSPITAL", 'pn': "+916369373450"},
    {'id': 6, 'name': "KMCH HOSPITAL", 'pn': "+916369373450"}
]

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "QR-AID",
        },
    )

def user(request, pk):
    user = None
    for i in users:
        if i['id'] == int(pk):
            user = i
    context = {"title": "ALERTED!!!", "user": user}
    print(user)
    return render(request, "user.html", context)
