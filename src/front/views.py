from django.http import HttpResponse
from django.shortcuts import render
from objects.models import Captcha, Faucet, Currency, FaucetCategory
from front.models import FaqItem
from django.core.cache import cache


def hello(req):
    return render(req, 'front/layout.html')

def faucets(req):
    captchas = Captcha.objects.all()

    faucets = cache.get('all_faucets_cache')
    if faucets is None:
        faucets = Faucet.objects.all()
        cache.set('all_faucets_cache', faucets, 120)
    currencies = Currency.objects.all()
    categories = FaucetCategory.objects.all()

    for faucet in faucets:
        setattr(faucet, 'ttl', round(faucet.get_cooldown(req.session.session_key) / 60))

    return render(req, 'front/faucets/list.html', {
        'global_centered': True,
        'captchas': captchas,
        'faucets': faucets,
        'currencies': currencies,
        'categories': categories
    })

def faucet_about(req, faucet_title_en):
    faucet = Faucet.objects.get(title_en=faucet_title_en)

    return render(req, 'front/faucets/about.html', {
        'global_centered': True,
        'faucet': faucet
    })

def faq(req):
    return render(req, 'front/faq/index.html', {
        'global_centered': True,
        'qas': FaqItem.objects.all()
    })

def contacts(req):
    return render(req, 'front/contacts/index.html', {
        'global_centered': True
    })