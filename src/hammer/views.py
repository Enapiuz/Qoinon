from django.shortcuts import render, redirect
from objects.models import Faucet
from django.core.urlresolvers import reverse
from django_hosts import reverse as reverse_host
from django.http import JsonResponse
from django.core.cache import cache

# Create your views here.

def main(req):
    """
    Гавнокоооооод
    нужно больше менеджеров
    и обработки дополнительных параметров
    """
    cache_prefix = req.session.session_key

    start = req.GET.get('start')
    currency = req.GET.get('cur')
    query = Faucet.objects

    if currency is not None:
        query = query.filter(currency__id=currency)

    #  тут получить все просмотренные краны и исключить их из выборки
    in_cache_faucets = cache.keys(str(cache_prefix) + '.faucets.*')

    #  idшники просмотренных кранов
    excludes = [x.rsplit('.', 1)[1] for x in in_cache_faucets]

    query = query.exclude(id__in=excludes)

    if start is not None:
        query = query.filter(title_en=start)
        if len(query) == 0:
            response = redirect('hammer')
            if currency is not None:
                response['Location'] += '?cur={0}'.format(currency)
            return response
        else:
            faucet = query.get()
    else:
        if len(query) == 0:
            response = redirect(reverse_host('main_host', ('faucets',)))
            return response
        else:
            faucet = Faucet.get_random(query)

    #  записать кран в сессию
    cache.set(str(cache_prefix) + '.faucets.' + str(faucet.id), 1, timeout=faucet.update_time*60)

    next_link = reverse('hammer') + '?cur={0}'.format(faucet.currency_id)
    
    # турбо-костыль, починить admin namespace
    admin_edit_link = "https://uniqoins.com/admin/objects/faucet/{0}/".format(faucet.id)

    return render(req, 'hammer/main.html', {
        'faucet': faucet,
        'next_link': next_link,
        'is_moderator': req.user.groups.filter(name='Moderators').exists(),
        'admin_edit_link': admin_edit_link
    })

def moderation_actions(req):
    if not req.user.groups.filter(name='Moderators').exists():
        return JsonResponse({'status': 'not allowed'})

    is_true = lambda x: x == 'true'

    fid = req.GET.get('id')
    name = req.GET.get('name')
    value = is_true(req.GET.get('value'))

    faucet = Faucet.objects.get(pk=fid)
    if hasattr(faucet, name):
        setattr(faucet, name, value)
        faucet.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'err'})
