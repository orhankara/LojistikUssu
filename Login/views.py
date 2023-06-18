from django.shortcuts import render
from django.http import HttpResponse
from Login import views

# Create your views here.
def LoginScreen(request):
    return render(request,'Login.html')