"""
WSGI config for boilerplate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if (os.environ['DJANGO_ENV'] == "prod"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boilerplate.settings.prod")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boilerplate.settings.dev")

application = get_wsgi_application()