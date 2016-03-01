SECRET_KEY = 'SuperSecretKay'
DEBUG = True

POSTGRESQL_SETTINGS = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'name',
    'USER': 'user',
    'PASSWORD': 'pass',
    'HOST': '127.0.0.1',
    'PORT': '5432'
}

DATABASES = {
    'default': POSTGRESQL_SETTINGS
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:32769/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

RECAPTCHA_PUBLIC_KEY = "public_key"
RECAPTCHA_PRIVATE_KEY = "secret_key"
