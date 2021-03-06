from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.utils.http import urlencode
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
from dirtyfields import DirtyFieldsMixin


class Currency(models.Model):
    title_short_en = models.CharField(max_length=50)
    title_full_en = models.CharField(max_length=300)
    title_short_ru = models.CharField(max_length=50)
    title_full_ru = models.CharField(max_length=300)
    display = models.BooleanField(default=True)
    current_value = models.FloatField(default=0)

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


class Faucet(DirtyFieldsMixin, models.Model):
    href = models.CharField(max_length=1024)
    title_en = models.CharField(max_length=300, unique=True)
    title_ru = models.CharField(max_length=300, blank=True)
    append_wallet = models.BooleanField(
        default=True,
        help_text="Автоматически подставлять в конец ссылки наш подходящий адрес кошелька")
    update_time = models.IntegerField(help_text="Cooldown в минутах")
    visible = models.BooleanField(default=True)
    currency = models.ForeignKey(Currency, default=1)
    now_pays = models.BooleanField(default=True)
    malfunction = models.BooleanField(default=False)
    captcha = models.ForeignKey(Captcha)
    category = models.ForeignKey(FaucetCategory, default=4)
    iframe_ready = models.BooleanField(default=True, help_text="Возможность работы в iframe")
    help_text = models.TextField(blank=True)

    top = models.BooleanField(default=False)
    best = models.BooleanField(default=False)

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    image = models.ImageField(default='#', upload_to='faucets')
    views = models.IntegerField(default=0)

    reward_min = models.IntegerField(
        blank=True,
        null=True,
        # validators=[
        #     MinValueValidator(0)
        # ]
    )
    reward_max = models.IntegerField(
        blank=True,
        null=True,
        # validators=[
        #     MinValueValidator(0)
        # ]
    )
    reward_mid = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )
    minimum_withdraw = models.IntegerField(
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

    create_date = models.DateTimeField(default=timezone.now, blank=True)

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
        Возвращает True, если кран моложе недели
        """
        return timezone.now() - timezone.timedelta(days=7) > self.create_date

    def get_cooldown(self, prefix):
        return cache.ttl(str(prefix) + '.faucets.' + str(self.id))

    def get_absolute_url(self):
        return '/hammer?start=' + self.title_en


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


class FaucetHistory(models.Model):
    faucet = models.ForeignKey(Faucet, null=False)
    action_type = models.IntegerField(null=False, blank=False)
    action_text_ru = models.TextField(blank=False, null=False)
    action_text_en = models.TextField(blank=False, null=False)
    date = models.DateTimeField(default=timezone.now, blank=False, null=False)

    def __str__(self):
        return "{0} action at {1}".format(self.faucet.title_en, self.date)


# еще немного тухлятинки
@receiver(post_save, sender=Faucet)
def faucet_history_handler(sender, **kwargs):
    # с помощью django dirty fields определить измененные поля
    # на основе этого определить тип действия
    # и сформировать описание
    # записать изменения
    # и удалить всю историю кроме последних 100 записей

    history_states = {
        'added': 0,
        'updated': 1,
        'removed': 2
    }

    obj = kwargs['instance']

    if kwargs['created'] is True:
        FaucetHistory.objects.create(
            faucet=obj,
            action_type=history_states['added'],
            action_text_ru='Новый',
            action_text_en='New'
        )
    elif obj.is_dirty():
        fields = obj.get_dirty_fields()
        if len(fields) > 0:
            if 'visible' in fields:
                if getattr(obj, 'visible') is True:
                    FaucetHistory.objects.create(
                        faucet=obj,
                        action_type=history_states['updated'],
                        action_text_ru='Онлайн',
                        action_text_en='Online'
                    )
                else:
                    FaucetHistory.objects.create(
                        faucet=obj,
                        action_type=history_states['updated'],
                        action_text_ru='Оффлайн',
                        action_text_en='Gone offline'
                    )
