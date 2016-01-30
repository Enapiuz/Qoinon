from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Faucet, FaucetHistory
from django.utils import timezone


@receiver(pre_save, sender=Faucet)
def faucet_history_handler(sender, **kwargs):
    # с помощью django dirty fields определить измененные поля
    # на основе этого определить тип действия
    # и сформировать описание
    # записать изменения
    # и удалить всю историю кроме последних 100 записей
    pass
