"""
WSGI config for labcodes_wiki project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "labcodes_wiki.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
