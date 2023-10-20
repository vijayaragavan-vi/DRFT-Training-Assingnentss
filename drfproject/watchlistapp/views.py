from django.http import HttpResponse
from django.shortcuts import render


def HelloworldView(request):
    return HttpResponse('hello_world.html')