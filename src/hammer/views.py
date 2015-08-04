from django.shortcuts import render, redirect
from objects.models import Faucet
from django.core.urlresolvers import reverse

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
    admin_edit_link = reverse('admin:objects_faucet_change', args=(faucet.id,))

    return render(req, 'hammer/main.html', {
        'faucet': faucet,
        'next_link': next_link,
        'is_moderator': req.user.groups.filter(name='Moderators').exists(),
        'admin_edit_link': admin_edit_link
    })
