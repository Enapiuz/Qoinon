from django.db import models
from django.core.validators import MinValueValidator


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

    def __str__(self):
        return self.title_en

class Faucet(models.Model):
    href = models.CharField(max_length=1024, help_text="Для автоматической подстановки подходящего кошелька вписать WALLET в место, где он должен быть")
    title_en = models.CharField(max_length=300)
    title_ru = models.CharField(max_length=300)
    update_time = models.IntegerField(help_text="Cooldown")
    visible = models.BooleanField(default=True)
    currency = models.ForeignKey(Currency)
    now_pays = models.BooleanField(default=True)
    malfunction = models.BooleanField(default=False)
    captcha = models.ForeignKey(Captcha)
    category = models.ForeignKey(FaucetCategory)

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    image = models.ImageField(default='#', upload_to='faucets')
    views = models.IntegerField(default=0)

    reward_min = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )
    reward_max = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )
    reward_mid = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )
    minimum_withdraw = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    referral_percent = models.IntegerField(default=0, help_text="Сколько нам % с реферральной программы")

    meta_title = models.CharField(max_length=1024, help_text="Максимум 1024 символа", blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.ManyToManyField(MetaKeyword)

    def __str__(self):
        return self.title_en

    def display_image(self):
        return "<img height='150' src='%s' />" % self.image.url
    display_image.allow_tags = True

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

