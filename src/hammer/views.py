from django.shortcuts import render

# Create your views here.

def hello(req):
    return render(req, 'hammer/hello.html')
