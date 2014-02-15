"""
WSGI config for this project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

for path in settings.PATHS:
    sys.path.insert(0, path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
