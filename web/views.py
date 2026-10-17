from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'web/index.html ')

def about(request):
    return render(request,'web/about.html ')

def contact(request):
    return render(request,'web/contact.html ')

def menu(request):
    return render(request,'web/menu.html ')

def services(request):
    return render(request,'web/services.html ')

def dashborad(request):
    return render(request,'web/dashborad.html')