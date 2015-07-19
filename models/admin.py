from django.contrib import admin
from .models import Wallet, WalletCategory

# Register your models here.

admin.site.register(Wallet)
admin.site.register(WalletCategory)
