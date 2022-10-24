from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def wish(request):
    sure = 'sure, good morning'
    return HttpResponse(f'Can you say good morning : {sure}')