from random import randint
from django.http import JsonResponse
from django.shortcuts import render, redirect
from objects.models import Captcha, Faucet, Currency, FaucetCategory
from .models import FaqItem, FaqCategory, ContactForm
from .forms import ContactsForm


def main(req):
    btc = Currency.objects.filter(title_short_en='BTC').first()
    faucets = Faucet.objects.exclude(visible=False).filter(currency__id=btc.id).order_by('-reward_mid')[:10]
    for faucet in faucets:
        setattr(faucet, 'ttl', round(faucet.get_cooldown(req.session.session_key) / 60))
    return render(req, 'front/main/index.html', {
        'global_color_inverse': True,
        'global_centered': True,
        'faucets': faucets,
        'background_id': 'components/images/foto%s.png' % randint(1, 4)
    })

def faucets(req):
    captchas = Captcha.objects.all()

    # faucets = cache.get('all_faucets_cache')
    # if faucets is None:
    faucets = Faucet.objects.exclude(visible=False).order_by('-reward_mid')
        # cache.set('all_faucets_cache', faucets, 120)
    currencies = Currency.objects.order_by('id')
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
    faqs = FaqItem.objects.filter(visible=True).exclude(category__isnull=True).order_by('position')
    categories = FaqCategory.objects.all()

    return render(req, 'front/faq/index.html', {
        'global_centered': True,
        'faqs': faqs,
        'categories': categories
    })

def contacts(req):
    if req.method == 'POST':
        form = ContactsForm(req.POST)
        if form.is_valid():
            contact = ContactForm()
            contact.name = form.cleaned_data['name']
            contact.email = form.cleaned_data['email']
            contact.text = form.cleaned_data['text']
            contact.save()

            # TODO: отправляем письмо

            return redirect("/contacts/")
    else:
        form = ContactsForm()

    return render(req, 'front/contacts/index.html', {
        'global_centered': True,
        'form': form
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

def robots_txt(req):
    return render(req, 'front/main/main_robots.html', content_type='text/plain')