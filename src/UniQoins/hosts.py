from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'qoinon\.com', settings.ROOT_URLCONF, name='main_host'),
    host(r'hammer\.qoinon\.com', 'hammer.urls', name='hammer_host'),
)
