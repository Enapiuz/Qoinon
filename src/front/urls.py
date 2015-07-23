from django.conf.urls import url

from front import views

urlpatterns = [
    url(r'^$', views.hello, name='main'),
    url(r'^faucets/$', views.faucets, name='faucets'),
]
