from django.db import models

# Create your models here.

class WalletCategory(models.Model):
    title_rus = models.CharField(max_length=300)
    title_eng = models.CharField(max_length=300)

    def __str__(self):
        return self.title_eng

class Wallet(models.Model):
    title_rus = models.CharField(max_length=300)
    title_eng = models.CharField(max_length=300)
    category = models.ForeignKey(WalletCategory)
    min_withdraw = models.IntegerField()
    currencies_count = models.IntegerField()

    def __str__(self):
        return self.title_eng

