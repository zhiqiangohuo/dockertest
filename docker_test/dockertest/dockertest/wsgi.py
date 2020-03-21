"""
WSGI config for dockertest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
print(os.path)
from django.core.wsgi import get_wsgi_application
print(os.path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dockertest.settings')

application = get_wsgi_application()
