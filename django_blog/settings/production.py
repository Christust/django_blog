from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['djangoblogdevchris.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd3macalic5tdnq',
        'USER': 'gvxyjwivqdcxho',
        'PASSWORD': '5702c6f9ea1cf93a8f20af349e3d58245e287df949d12bd8c04e95307476451b',
        'HOST': 'ec2-44-199-22-207.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
STATIC_ROOT = BASE_DIR / "static"
