from django.conf.urls import url

from front import views

urlpatterns = [
    url(r'^$', views.hello, name='main'),
    url(r'^faucets/$', views.faucets, name='faucets'),
    url(r'^faucets/about/([0-9])/$', views.faucet_about, name='faucet_about'),
]
