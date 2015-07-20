from django.db import models


class Currency(models.Model):
    title_short_en = models.CharField(max_length=50)
    title_full_en = models.CharField(max_length=300)
    title_short_ru = models.CharField(max_length=50)
    title_full_ru = models.CharField(max_length=300)

    def __str__(self):
        return "{0}, {1}".format(self.title_full_en, self.title_short_en)

class Captcha(models.Model):
    title_en = models.CharField(max_length=300)
    title_ru = models.CharField(max_length=300)

    def __str__(self):
        return self.title_en

class MetaKeyword(models.Model):
    text_en = models.CharField(max_length=300)
    text_ru = models.CharField(max_length=300)

    def __str__(self):
        return self.text_en

class FaucetCategory(models.Model):
    title_en = models.CharField(max_length=300)
    title_ru = models.CharField(max_length=300)

class Faucet(models.Model):
    href = models.CharField(max_length=1024)
    title_en = models.CharField(max_length=300)
    title_ru = models.CharField(max_length=300)
    update_time = models.TimeField(help_text="Cooldown")
    visible = models.BooleanField(default=False)
    currency = models.ForeignKey(Currency)
    now_pays = models.BooleanField(default=True)
    malfunction = models.BooleanField(default=False)
    captcha = models.ForeignKey(Captcha)
    category = models.ForeignKey(FaucetCategory, null=True)

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    views = models.IntegerField(default=0)

    reward_min = models.FloatField(default=0)
    reward_max = models.FloatField(default=0)
    reward_mid = models.FloatField(default=0)

    meta_title = models.CharField(max_length=1024, help_text="Максимум 1024 символа")
    meta_description = models.TextField()
    meta_keywords = models.ManyToManyField(MetaKeyword)

    def __str__(self):
        return self.title_en

class WalletCategory(models.Model):
    title_ru = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)

    def __str__(self):
        return self.title_en

class Wallet(models.Model):
    title_ru = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    category = models.ForeignKey(WalletCategory)
    min_withdraw = models.IntegerField(help_text="Минимальная сумма вывода")
    currencies_count = models.IntegerField()

    def __str__(self):
        return self.title_eng

