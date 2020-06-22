from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def contacts_view(request, *args, **kwargs):
    return render(request, "contacts.html",{})

def administration_view(request, *args, **kwargs):
    return render(request, "administration.html",{})

def departments_view(request, *args, **kwargs):
    return render(request, "departments.html",{})


def internactiv_view(request, *args, **kwargs):
    return render(request, "internactiv.html",{})

def pubinfo_view(request, *args, **kwargs):
    return render(request, "pubinfo.html",{})


