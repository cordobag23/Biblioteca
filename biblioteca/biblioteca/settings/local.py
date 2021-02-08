#************INICIO***ESTO LO iomprtamos***********#
from .base import *
DEBUG = True

ALLOWED_HOSTS = []

#************FIN***ESTO LO importamos***********#


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbbiblioteca',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':3306
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
