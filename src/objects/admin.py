from django.contrib import admin
from objects.models import Wallet, WalletCategory, Faucet, MetaKeyword, Captcha, Currency, FaucetCategory, OurWallet
from django_summernote.admin import SummernoteModelAdmin


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


class FaucetAdmin(SummernoteModelAdmin):
    # TODO понять как называть фильтры
    list_filter = ('currency__title_short_en', 'category__title_en', 'captcha__title_en', 'visible')
    ordering = ['title_en']
    search_fields = ['title_en']
    readonly_fields = ('display_image', 'create_date')
    fieldsets = [
        ('Основное', {'fields': ['title_en', 'title_ru', 'href', 'append_wallet', 'iframe_ready']}),
        ('Изображение', {'fields': ['image', 'display_image']}),
        ('Служебное',
         {'fields': ['currency', 'now_pays', 'captcha', 'category', 'update_time', 'visible', 'malfunction',
                     'referral_percent', 'top', 'best', 'help_text']}),
        ('Награда', {'fields': ['reward_min', 'reward_max', 'reward_mid', 'minimum_withdraw']}),
        ('Просмотры', {'fields': ['views']}),
        ('Лайки', {'fields': ['likes', 'dislikes']}),
        ('Meta', {'fields': ['meta_title', 'meta_description']}),
        ('Информация', {'fields': ['create_date']})
    ]
    inlines = [MetaKeyInline]


admin.site.register(Wallet)
admin.site.register(WalletCategory, WalletCategoryAdmin)
admin.site.register(Faucet, FaucetAdmin)
admin.site.register(FaucetCategory, FaucetCategoryAdmin)
admin.site.register(MetaKeyword)
admin.site.register(Captcha, CaptchaAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(OurWallet)
