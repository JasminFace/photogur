from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import Picture, Comment

def root_path(request):
    return HttpResponseRedirect('pictures/')

def pictures(request):
    context = {
        'title': 'Home',
        'collection':Picture.objects.all()
        }
    response = render(request, 'pictures.html', context)
    return HttpResponse(response)

def picture_show(request, id):
    picture = Picture.objects.get(pk=id)
    context = {
        'title': picture.title,
        'picture': picture
        }
    response = render(request, 'picture.html', context)
    return HttpResponse(response)