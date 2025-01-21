from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DJANGO_VITE = {"default": {"dev_mode": True}}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
