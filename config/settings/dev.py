import environ

from .base import *

env = environ.Env()
env.read_env('.env')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.get_value('DEBUG')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get_value('SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
