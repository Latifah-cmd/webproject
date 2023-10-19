#from django.http import HttpResponse
from django.shortcuts import render

def homepage_view(request):
    return render(request, 'home.html')

def aboutuspage_view(request):
    return render(request,'aboutus.html')

def contactuspage_view(request):
    return render(request,'contact.html')

def servicespage_view(request):
    return render(request,'services.html')

def gallerypage_view(request):
    return render(request,'gallery.html')