"""
WSGI config for JSONPlaceholderDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/tutores/JSONPlaceholderDjango')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JSONPlaceholderDjango.settings')

os.environ.setdefault('LANG', 'en_US.UTF-8')
os.environ.setdefault('LC_ALL', 'en_US.UTF-8')

activate_this = '/home/tutores/entorno/bin/activate'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
