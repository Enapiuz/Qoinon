from django.http import HttpResponse
from django.shortcuts import render
from objects.models import Captcha, Faucet


def hello(req):
    return render(req, 'front/layout.html')

def faucets(req):
    captchas = Captcha.objects.all()
    faucets = Faucet.objects.all()

    return render(req, 'front/faucets/list.html', {
        'captchas': captchas,
        'faucets': faucets
    })

def faucet_about(req, faucet_title_en):
    faucet = Faucet.objects.get(title_en=faucet_title_en)

    return render(req, 'front/faucets/about.html', {
        'faucet': faucet
    })
