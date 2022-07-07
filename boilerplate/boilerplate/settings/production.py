from .base import *


DEBUG = False

try:
    from .local import *
except ImportError:
    pass

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    '*.boilerplate.dev',
    '127.0.0.1',
    'localhost',
    '0.0.0.0',    
    ]

# allow CIDR
ALLOWED_CIDR_NETS = ['10.0.0.0/8']

MIDDLEWARE = [
    'allow_cidr.middleware.AllowCIDRMiddleware', # django allow CIDR middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_currentuser.middleware.ThreadLocalUserMiddleware', # current user
]




DATABASE_NAME = os.environ['DATABASE_NAME']
DATABASE_USER = os.environ['DATABASE_USER']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_PORT = os.environ['DATABASE_PORT']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

BASE_URL = 'https://boilerplate.dev'

# ses 
EMAIL_BACKEND = os.environ['EMAIL_BACKEND']
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']


# templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request', # for django allauth
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],            
        },
    },
]


# When the automatic setup is used, the Debug Toolbar is not compatible with GZipMiddleware. Please disable that middleware during development or use the explicit setup to allow the toolbar to function properly.
MIDDLEWARE += [
    'django.middleware.gzip.GZipMiddleware',
]

# cache
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_CACHE_ALIAS = "default"
KEY_PREFIX = "boilerplate_"

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800 			
CACHE_MIDDLEWARE_KEY_PREFIX = ''

CACHES = {
    "default": { 
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://" + os.environ['REDIS_HOST'] + ":" + os.environ['REDIS_PORT'] + "/" + os.environ['REDIS_DB'],
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PICKLE_VERSION": -1,  # Use the latest protocol version
            # "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            # "SOCKET_TIMEOUT": 5,  # in seconds
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            "CONNECTION_POOL_KWARGS": {"max_connections": 10000, "retry_on_timeout": True},
        },
    },
    "select2": { 
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://" + os.environ['REDIS_HOST'] + ":" + os.environ['REDIS_PORT'] + "/" + os.environ['REDIS_DB_SELECT2'],
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PICKLE_VERSION": -1,  # Use the latest protocol version
            # "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            # "SOCKET_TIMEOUT": 5,  # in seconds
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            "CONNECTION_POOL_KWARGS": {"max_connections": 10000, "retry_on_timeout": True},
        },
    },    
    # "collectfast": { 
    #     "BACKEND": "django_redis.cache.RedisCache",
    #     "LOCATION": "redis://" + os.environ['REDIS_HOST'] + ":" + os.environ['REDIS_PORT'] + "/" + os.environ['REDIS_DB_COLLECTFAST'],
    #     "OPTIONS": {
    #         "CLIENT_CLASS": "django_redis.client.DefaultClient",
    #         "PICKLE_VERSION": -1,  # Use the latest protocol version
    #         # "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
    #         # "SOCKET_TIMEOUT": 5,  # in seconds
    #         "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
    #         "CONNECTION_POOL_KWARGS": {"max_connections": 10000, "retry_on_timeout": True},
    #     },
    # },   
    "disk": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(BASE_DIR, 'cache'),
        "KEY_PREFIX": "boilerplate_",
        "TIMEOUT": 3600*24*7, # one hour * 24 hours * 7 days (in seconds)
        "LOCATION": "/var/tmp/django_cache",
    }    
}





# file storage
DEFAULT_FILE_STORAGE = 'boilerplate.custom_storages.MediaStorage'
STATICFILES_STORAGE = 'boilerplate.custom_storages.StaticStorage'
AWS_S3_CUSTOM_DOMAIN = os.environ['AWS_S3_CUSTOM_DOMAIN']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_DEFAULT_ACL = 'public-read'
AWS_AUTO_CREATE_BUCKET = True
AWS_BUCKET_ACL = None
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_FILE_OVERWRITE = False
AWS_IS_GZIPPED = True
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
# AWS_HEADERS = {
#     'Expires': 'Thu, 15 Apr 2040 20:00:00 GMT',
#     'Cache-Control': 'max-age=86400',
#     'Access-Control-Allow-Origin': '*'
# }
AWS_DISTRIBUTION_ID = os.environ['AWS_DISTRIBUTION_ID']


PUBLIC_MEDIA_LOCATION = 'media/public'
MEDIA_URL = "https://{}/{}/{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, STORAGE_FOLDER, DJANGO_ENV, PUBLIC_MEDIA_LOCATION)
# COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"
# COLLECTFAST_CACHE = "collectfast"
# COLLECTFAST_THREADS = 4
# COLLECTFAST_DEBUG = False