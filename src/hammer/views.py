from django.shortcuts import render, redirect
from objects.models import Faucet
from django.core.urlresolvers import reverse
from django_hosts import reverse as reverse_host
from django.http import JsonResponse
from django.core.cache import cache


def main(req):
    """
    Гавнокоооооод
    нужно больше менеджеров
    и обработки дополнительных параметров
    """
    cache_prefix = req.session.session_key

    start = req.GET.get('start')
    currency = req.GET.get('cur')
    captcha = req.GET.get('cpt')
    wallet = req.GET.get('cat')
    ut_min = req.GET.get('tmin')
    ut_max = req.GET.get('tmax')
    query = Faucet.objects.order_by('-reward_mid')

    if currency is not None:
        query = query.filter(currency__id=currency) 
        
    if captcha is not None:
        query = query.filter(captcha__id=captcha)
        
    if wallet is not None:
        query = query.filter(category__id=wallet)
        
    if ut_min is not None:
        query = query.filter(update_time__gt=ut_min)
        
    if ut_max is not None:
        query = query.filter(update_time__lt=ut_max)

    if start is None:
        """
        Если смотрим конкретный кран, то так уж и быть - показать, если еще на кд
        """
        in_cache_faucets = cache.keys(str(cache_prefix) + '.faucets.*')
        excludes = [x.rsplit('.', 1)[1] for x in in_cache_faucets]
        query = query.exclude(id__in=excludes)

    if start is not None:  # если смотрми конкретный кран
        query = query.filter(title_en=start)  # фильтр по крану
        if len(query) == 0:  # если нет результатов (напр. нет крана) показать все краны по валюте
            response = redirect('hammer')
            if currency is not None:
                response['Location'] += '?cur={0}'.format(currency)
            return response
        else:
            faucet = query.get()
    else:  # смотрим просто рядовой кран
        if len(query) == 0:
            """
            Если все краны на кд и есть фильтр помимо валюты - оставляем только валюту
            """
            if captcha or wallet or ut_min or ut_min or ut_max:
                response = redirect('hammer')
                if currency is not None:
                    response['Location'] += '?cur={0}'.format(currency)
                return response
            else:
                response = redirect(reverse_host('faucets', host='main_host', scheme='https'))
                return response
        else:
            faucet = query[0]

    #  записать кран в сессию
    cache.set(str(cache_prefix) + '.faucets.' + str(faucet.id), 1, timeout=faucet.update_time*60)

    next_link = reverse('hammer') + '?cur={0}'.format(faucet.currency_id)
    
    if captcha is not None:
        next_link = next_link + '&cpt=' + captcha
        
    if wallet is not None:
        next_link = next_link + '&cat=' + wallet
        
    if ut_min is not None:
        next_link = next_link + '&tmin=' + ut_min
        
    if ut_max is not None:
        next_link = next_link + '&tmax=' + ut_max
    
    # турбо-костыль, починить admin namespace
    admin_edit_link = "https://uniqoins.com/admin/objects/faucet/{0}/".format(faucet.id)

    if faucet.currency.title_short_en == "BTC":
        cookie_faucet = req.COOKIES.get('address' + str(faucet.currency.id))
        if cookie_faucet is not None and not cookie_faucet == '':
            faucetbox_link = "https://faucetbox.com/en/check/" + str(cookie_faucet)
        else:
            faucetbox_link = ''
    else:
        faucetbox_link = ''

    return render(req, 'hammer/main.html', {
        'faucet': faucet,
        'labels': _make_labels(faucet),
        'next_link': next_link,
        'is_moderator': req.user.groups.filter(name='Moderators').exists(),
        'admin_edit_link': admin_edit_link,
        'faucetbox_link': faucetbox_link
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

def edit_help_text(req):
    if not req.user.groups.filter(name='Moderators').exists():
        return JsonResponse({'status': 'not allowed'})

    fid = req.GET.get('id')
    text = req.GET.get('text')

    faucet = Faucet.objects.get(pk=fid)
    faucet.help_text = text
    faucet.save()

    return JsonResponse({'status': 'ok'})

def _make_labels(faucet):
    labels = []

    labels.append({
        'title': faucet.captcha.title_en,
        'type': 'captcha'
    })

    labels.append({
        'title': str(faucet.update_time) + ' min.',
        'type': 'time'
    })

    labels.append({
        'title': faucet.category.title_en,
        'type': 'category'
    })

    if faucet.malfunction:
        labels.append({
            'title': 'Malfunction',
            'type': 'bad'
        })

    if not faucet.now_pays:
        labels.append({
            'title': 'Not pays',
            'type': 'bad'
        })

    if faucet.top:
        labels.append({
            'title': 'Top',
            'type': 'top'
        })

    if faucet.best:
        labels.append({
            'title': 'Best',
            'type': 'top'
        })


    return labels