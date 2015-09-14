from django.conf.urls import url

from hammer import views

urlpatterns = [
    url(r'^$', views.main, name='hammer'),
    url(r'^moderation_actions/', views.moderation_actions, name='hammer.moderation'),
    url(r'^edit_help_text/', views.edit_help_text, name='hammer.edit_help_text')
]
