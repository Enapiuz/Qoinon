from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from objects.models import Captcha, Faucet, Currency, FaucetCategory
from front.models import FaqItem
from django.core.cache import cache


def main(req):
    btc = Currency.objects.filter(title_short_en='BTC').first()
    faucets = Faucet.objects.filter(currency__id=btc.id).order_by('-reward_mid')[:10]
    return render(req, 'front/main/index.html', {
        'global_centered': True,
        'faucets': faucets
    })

def faucets(req):
    captchas = Captcha.objects.all()

    # faucets = cache.get('all_faucets_cache')
    # if faucets is None:
    faucets = Faucet.objects.order_by('-reward_mid')
        # cache.set('all_faucets_cache', faucets, 120)
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

def like_faucet(req):
    like_type = req.GET.get('type')
    faucet_id = req.GET.get('faucet_id')

    try:
        faucet = Faucet.objects.get(pk=int(faucet_id))
        if int(like_type) == 1:
            faucet.likes += 1
        if int(like_type) == 2:
            faucet.dislikes += 1

        faucet.save()

        result = 1
        likes = faucet.get_rating()
    except Exception:
        result = 0
        likes = 0


    return JsonResponse({
        'success': result,
        'likes': likes
    })