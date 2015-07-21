from django.http import HttpResponse
from django.shortcuts import render


def hello(req):
    return render(req, 'front/layout.html')
