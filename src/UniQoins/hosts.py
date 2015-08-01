from django.conf import settings
from django_hosts import patterns, host
from hammer import urls as hammer_urls

host_patterns = patterns('uniqoins.com',
    host(r'', settings.ROOT_URLCONF, name='main_host'),
    host(r'hammer', hammer_urls, name='hammer_host'),
)
