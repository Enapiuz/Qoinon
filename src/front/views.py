from django.http import HttpResponse
from django.shortcuts import render
from objects.models import Captcha


def hello(req):
    return render(req, 'front/layout.html')

def faucets(req):
    captchas = Captcha.objects.all()
    return render(req, 'front/faucets.html', {
        'captchas': captchas
    })
