from django.shortcuts import render, redirect
from objects.models import Faucet

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

    return render(req, 'hammer/main.html', {
        'faucet': faucet
    })
