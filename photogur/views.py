from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import Picture, Comment

def pictures(request):
    context = {'collection':Picture.objects.all()}
    response = render(request, 'pictures.html', context)
    return HttpResponse(response)