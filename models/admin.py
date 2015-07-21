from django.contrib import admin
from .models import Wallet, WalletCategory, Faucet, MetaKeyword, Captcha, Currency, FaucetCategory


class WalletCategoryAdmin(admin.ModelAdmin):
    get_model_perms = lambda self, request: {}


class FaucetCategoryAdmin(admin.ModelAdmin):
    get_model_perms = lambda self, request: {}


class CaptchaAdmin(admin.ModelAdmin):
    get_model_perms = lambda self, request: {}


class CurrencyAdmin(admin.ModelAdmin):
    get_model_perms = lambda self, request: {}


class MetaKeyInline(admin.TabularInline):
    model = Faucet.meta_keywords.through
    extra = 1


class FaucetAdmin(admin.ModelAdmin):
    readonly_fields = ('display_image', )
    fieldsets = [
        ('Основное', {'fields': ['title_en', 'title_ru', 'href']}),
        ('Изображение', {'fields': ['image', 'display_image']}),
        ('Служебное',
         {'fields': ['currency', 'now_pays', 'captcha', 'category', 'update_time', 'visible', 'malfunction',
                     'referral_percent']}),
        ('Награда', {'fields': ['reward_min', 'reward_max', 'reward_mid', 'minimum_withdraw']}),
        ('Просмотры', {'fields': ['views']}),
        ('Лайки', {'fields': ['likes', 'dislikes']}),
        ('Meta', {'fields': ['meta_title', 'meta_description']})
    ]
    inlines = [MetaKeyInline]


admin.site.register(Wallet)
admin.site.register(WalletCategory, WalletCategoryAdmin)
admin.site.register(Faucet, FaucetAdmin)
admin.site.register(FaucetCategory, FaucetCategoryAdmin)
admin.site.register(MetaKeyword)
admin.site.register(Captcha, CaptchaAdmin)
admin.site.register(Currency, CurrencyAdmin)
