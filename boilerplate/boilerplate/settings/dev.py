from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass


INSTALLED_APPS += [
    'debug_toolbar',
]



INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")
def show_toolbar(request):
    return True
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_currentuser.middleware.ThreadLocalUserMiddleware', # current user
    'debug_toolbar.middleware.DebugToolbarMiddleware',        
]
