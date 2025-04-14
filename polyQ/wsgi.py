"""
WSGI config for picaponto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
import os
import time
import traceback
import signal
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/polyq/polyq')
# adjust the Python version in the line below as needed
sys.path.append('/var/www/polyq/polyq/venv/lib/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polyQ.settings')

# Get the WSGI application
application = get_wsgi_application()
