from django.conf.urls import url

from front import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^faucets/$', views.faucets, name='faucets'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^api/like_faucet/$', views.like_faucet, name='api.like_faucet'),
    url(r'^(.+)/$', views.faucet_about, name='faucet_about'),  # роут всегда последним должен быть
]
