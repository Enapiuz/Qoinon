from django.shortcuts import render
from objects.models import Faucet

# Create your views here.

def main(req):
    faucet = Faucet.get_random()
    return render(req, 'hammer/main.html', {
        'faucet': faucet
    })
