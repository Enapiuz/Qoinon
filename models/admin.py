from django.contrib import admin
from .models import Wallet, WalletCategory, Faucet, MetaKeyword, Captcha, Currency


class FaucetAdmin(admin.ModelAdmin):
    """
    Пока заглушка, чтобы не забыть описание
    """
    fieldsets = [
        ('Likes', {'fields': ['likes', 'dislikes']})
    ]

admin.site.register(Wallet)
admin.site.register(WalletCategory)
admin.site.register(Faucet)
admin.site.register(MetaKeyword)
admin.site.register(Captcha)
admin.site.register(Currency)
