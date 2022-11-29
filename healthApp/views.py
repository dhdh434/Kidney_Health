from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def indexPageView(request) :
    return render(request, 'webpages/index.html')

def aboutPageView(request) :
    return render(request, 'webpages/about.html')

def loginPageView(request) :
    return render(request, 'webpages/login.html')

def bootPageView(request) :
    return render(request, 'webpages/bootstrap.html')

def createAccPageView(request) :
    return render(request, 'webpages/createAccount.html')
