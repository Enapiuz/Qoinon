from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
import random


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
    href = models.CharField(max_length=1024)
    title_en = models.CharField(max_length=300, unique=True)
    title_ru = models.CharField(max_length=300, blank=True)
    append_wallet = models.BooleanField(default=True, help_text="Автоматически подставлять в конец ссылки наш подходящий адрес кошелька")
    update_time = models.IntegerField(help_text="Cooldown в минутах")
    visible = models.BooleanField(default=True)
    currency = models.ForeignKey(Currency, default=1)
    now_pays = models.BooleanField(default=True)
    malfunction = models.BooleanField(default=False)
    captcha = models.ForeignKey(Captcha)
    category = models.ForeignKey(FaucetCategory, default=4)
    iframe_ready = models.BooleanField(default=True, help_text="Возможность работы в iframe")

    top = models.BooleanField(default=False)
    best = models.BooleanField(default=False)

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    image = models.ImageField(default='#', upload_to='faucets')
    views = models.IntegerField(default=0)

    reward_min = models.FloatField(
        blank=True,
        null=True,
        # validators=[
        #     MinValueValidator(0)
        # ]
    )
    reward_max = models.FloatField(
        blank=True,
        null=True,
        # validators=[
        #     MinValueValidator(0)
        # ]
    )
    reward_mid = models.FloatField(
        validators=[
            MinValueValidator(0)
        ]
    )
    minimum_withdraw = models.FloatField(
        blank=True,
        null=True,
        # validators=[
        #     MinValueValidator(0)
        # ]
    )

    referral_percent = models.IntegerField(default=0, help_text="Сколько нам % с реферральной программы")

    meta_title = models.CharField(max_length=1024, help_text="Максимум 1024 символа", blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.ManyToManyField(MetaKeyword)

    create_date = models.DateTimeField(default=timezone.now(), blank=True)

    def __str__(self):
        return self.title_en

    def get_rating(self):
        return self.likes - self.dislikes

    def display_image(self):
        return "<img height='150' src='%s' />" % self.image.url
    display_image.allow_tags = True

    def real_href(self):
        """
        Выбиает все подходящие под кран наши кошельки и вставляет в конец
        адрес подходящего
        """
        if self.append_wallet:
            wallets = OurWallet.objects.filter(currency=self.currency).all()
            wallet = random.choice(wallets).address if len(wallets) > 0 else ''
            return self.href + wallet
        else:
            return self.href

    @staticmethod
    def get_random(query=None):
        selector = lambda: query.all() if query is not None else Faucet.objects.all()
        obj = random.choice(selector())
        return obj

    def is_new(self):
        """
        Возвращает True, если кран моложе недели или другого срока
        """
        return True

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

class OurWallet(models.Model):
    """
    Наши кошельки для подстановки в ротаторе на основе валюты
    """
    address = models.CharField(max_length=300)
    currency = models.ForeignKey(Currency)
    comments = models.TextField(blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.address, str(self.currency))
