from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def projects(request):
    return HttpResponse('Buni loyiham')

def project(request, pk):
    return HttpResponse('Loyiha kodi' + '' + str(pk))