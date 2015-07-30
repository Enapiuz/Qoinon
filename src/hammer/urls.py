from django.conf.urls import url

from hammer import views

urlpatterns = [
    url(r'^$', views.main, name='hammer'),
]
