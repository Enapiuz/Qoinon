from django.shortcuts import render, redirect
from objects.models import Faucet
from django.core.urlresolvers import reverse
from django.http import JsonResponse

# Create your views here.

def main(req):
    start = req.GET.get('start')
    currency = req.GET.get('c')
    query = Faucet.objects

    if currency is not None:
        query = query.filter(currency__id=currency)

    if start is not None:
        query = query.filter(title_en=start)
        if len(query) == 0:
            response = redirect('hammer')
            if currency is not None:
                response['Location'] += '?c={0}'.format(currency)
            print(response['Location'])
            return response
        else:
            faucet = query.get()
    else:
        faucet = Faucet.get_random(query)

    next_link = reverse('hammer') + '?c={0}'.format(faucet.currency_id)
    
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

    fid = req.GET.get('id')
    name = req.GET.get('name')
    value = req.GET.get('value')

    faucet = Faucet.objects.get(pk=fid)
    if hasattr(faucet, name):
        setattr(faucet, name, value)
        faucet.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'err'})
