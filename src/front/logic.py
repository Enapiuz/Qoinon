from objects.models import Captcha, Faucet, Currency, FaucetCategory


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
