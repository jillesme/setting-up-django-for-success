from .base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = []

DJANGO_VITE = {"default": {"dev_mode": False}}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
