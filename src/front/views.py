from django.http import HttpResponse
from django.shortcuts import render
from objects.models import Captcha, Faucet, Currency, WalletCategory


def hello(req):
    return render(req, 'front/layout.html')

def faucets(req):
    captchas = Captcha.objects.all()
    faucets = Faucet.objects.all()
    currencies = Currency.objects.all()
    wallets = WalletCategory.objects.all()

    return render(req, 'front/faucets/list.html', {
        'global_centered': True,
        'captchas': captchas,
        'faucets': faucets,
        'currencies': currencies,
        'wallets': wallets
    })

def faucet_about(req, faucet_title_en):
    faucet = Faucet.objects.get(title_en=faucet_title_en)

    return render(req, 'front/faucets/about.html', {
        'global_centered': True,
        'faucet': faucet
    })
