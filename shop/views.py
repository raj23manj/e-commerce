from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text_var = 'rendering text value'
    return HttpResponse(text_var)