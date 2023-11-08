#from django.http import HttpResponse
from django.shortcuts import render

from webprojects.forms import ClientForm

def homepage_view(request):
    return render(request, 'home.html')

def aboutuspage_view(request):
    return render(request,'aboutus.html')

def servicespage_view(request):
    return render(request,'services.html')

def gallerypage_view(request):
    return render(request,'gallery.html')

def contactuspage_view(request):
     if request.method == "POST":
         client_form = ClientForm(request.POST)

         if client_form.is_valid():
             client_form.save()
     else:
             client_form = ClientForm()
     #context = {
          # client_form,
     #}

     return render(request,"contact.html",{'form':client_form})


         