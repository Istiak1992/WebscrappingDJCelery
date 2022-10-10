from turtle import delay
from django.shortcuts import render
from .tasks import Task_Scrapper
from django.http import HttpResponse

# Create your views here.

def Hello(request):
   #Task_Hello()
    Task_Scrapper()
    return HttpResponse("Hey!")
