"""
WSGI config for django_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings.production')

application = get_wsgi_application()
application = WhiteNoise(application, root=BASE_DIR / "static")

# from dj_static import Cling

# application = Cling(get_wsgi_application())
