from django import template
from objects.models import Currency

register = template.Library()

@register.simple_tag
def btc_currency():
    try:
        btc = Currency.objects.filter(title_short_en='BTC').first()
        return float(btc.current_value)
    except Exception:
        return 0