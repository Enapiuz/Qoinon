from objects.models import Captcha, Faucet, Currency, FaucetCategory
from django.core.mail import send_mail


def get_main_faucets(session_key):
    try:
        btc = Currency.objects.filter(title_short_en='BTC').first()
        faucets = Faucet.objects.exclude(visible=False).filter(currency__id=btc.id).order_by('-reward_mid')[:10]
        for faucet in faucets:
            setattr(faucet, 'ttl', round(faucet.get_cooldown(session_key) / 60))
    except Exception:
        faucets = []

    return faucets


def get_life_widget():
    pass


def send_email_from_contact(form):
    send_mail(
        'New response from {0} - {1}'.format(form.name, form.email),
        form.text,
        'info@qoinon.com',
        ['enapiuz@gmail.com'],
        fail_silently=True
    )
