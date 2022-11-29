from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Client
from .forms import ClientForm

def indexPageView(request) :
    return render(request, 'webpages/index.html')

def aboutPageView(request) :
    return render(request, 'webpages/about.html')

def loginPageView(request) :
    return render(request, 'webpages/login.html')

def bootPageView(request) :
    return render(request, 'webpages/bootstrap.html')

def createAccPageView(request) :

    data = Client.objects.all()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ClientForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'webpages/createAccount.html', context)
