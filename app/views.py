from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sandhya(request):
    return HttpResponse('Haiii sandhyaa i miss u dear')

def chitti(request):
    return HttpResponse('<marquee><i><h1>chitti nanda are besties </h1></i></marquee>')
