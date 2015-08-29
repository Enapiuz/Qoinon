from django.conf.urls import url

from front import views

urlpatterns = [
    url(r'^$', views.hello, name='main'),
    url(r'^faucets/$', views.faucets, name='faucets'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^(.+)/$', views.faucet_about, name='faucet_about'),  # роут всегда последним должен быть
]
