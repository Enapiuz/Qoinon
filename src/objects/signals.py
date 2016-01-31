from django.db.models.signals import pre_save
from django.dispatch import receiver
from objects.models import Faucet, FaucetHistory


@receiver(pre_save, sender=Faucet)
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
    if obj.is_dirty:
        fields = obj.get_dirty_fields()
        if len(fields) > 0:
            if 'visible' in fields:
                if fields['visible'] is True:
                    FaucetHistory.objects.create(
                            faucet=obj,
                            action_type=history_states['updated'],
                            action_text_ru='',
                            action_text_en='Online'
                    )
                else:
                    FaucetHistory.objects.create(
                            faucet=obj,
                            action_type=history_states['updated'],
                            action_text_ru='',
                            action_text_en='Gone offline'
                    )
