from .common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&ts&x7xb-mu(dw=*vpx$+22n)!4v35z+y&*n71#b4&3rq&f#0y"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "storefront2",
        "HOST": "localhost",
        "USER": "root",
        "PASSWORD": "password",
    }
}
