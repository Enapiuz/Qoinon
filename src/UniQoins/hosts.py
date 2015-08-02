from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'uniqoins\.com', settings.ROOT_URLCONF, name='main_host'),
    host(r'hammer\.uniqoins\.com', 'hammer.urls', name='hammer_host'),
)
