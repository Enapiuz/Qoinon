from django.conf.urls import url

from hammer import views

urlpatterns = [
    url(r'^$', views.main, name='hammer'),
    url(r'^robots\.txt', views.robots_txt, name='hammer_robots_txt'),
    url(r'^moderation_actions/', views.moderation_actions, name='hammer.moderation'),
    url(r'^edit_help_text/', views.edit_help_text, name='hammer.edit_help_text')
]
