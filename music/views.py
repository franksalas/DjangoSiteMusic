from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the music app homepage!")


def detail(request, album_id):
    return HttpResponse('<h2>  Details for album id </h2>')
