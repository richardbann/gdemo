# import os
import re
import logging.config

import sec
from django.utils.translation import ugettext_lazy as _


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = sec.load("django_secret_key")

DEBUG = True

HOST_NAMES = [x.strip() for x in sec.load("HOST_NAMES").split(",")]
ALLOWED_HOSTS = HOST_NAMES

# name <email>
email_re = r"^\s*(.*)\s+<(.*)>\s*$"
ADMINS = [re.match(email_re, x).groups() for x in sec.load("ADMINS").split(",")]

# # Email related settings
# EMAIL_HOST = os.environ.get('EMAIL_HOST')
# EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 0)) or None
# EMAIL_HOST_USER = read_secret_from_file('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = read_secret_from_file('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', '').lower() == 'true'
# EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', '').lower() == 'true'
# EMAIL_TIMEOUT = 10

SERVER_EMAIL = sec.load("SERVER_EMAIL")
# DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_SUBJECT_PREFIX = '[%s] ' % HOST_NAMES[0]

# EMAIL_BACKEND = 'mailer.backend.DbBackend'
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = sec.load("sendgrid_api_key")
# SENDGRID_SANDBOX_MODE_IN_DEBUG = False

# MAILER_EMAIL_BACKEND = 'core.rewrite_email_backend.EmailBackend'
# MAILER_LOCK_PATH = '/tmp/mailer_lock'


STATIC_URL = '/static/'
STATIC_ROOT = '/src/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)
STATICFILES_DIRS = [
    "/usr/src/frontend/build",
]

MEDIA_ROOT = '/files/'
MEDIA_URL = '/media/'
# File Upload max 50MB
# DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800
# FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o750
FILE_UPLOAD_PERMISSIONS = 0o640


ROOT_URLCONF = 'core.urls'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "demo.apps.DemoConfig",
    "user.apps.UserConfig",
    "blog.apps.BlogConfig",
    # 'django_extensions',
    # 'mailer',
    # 'channels',
    # 'rest_framework.apps.RestFrameworkConfig',
    # 'django_filters',
    # 'rest_framework.authtoken',
    # 'rest_auth',
    # 'explorer.apps.ExplorerAppConfig',
    # 'core.apps.Config',
    # 'rosetta.apps.RosettaAppConfig',
    # 'improveduser.apps.Config',
]

# # explorer has an issue, when it is fixed, we can remove this.
# MIGRATION_MODULES = {
#     'explorer': 'core.explorer_migrations',
# }
#
# # debug toolbar installs a log handler (ThreadTrackingHandler) on the root
# # logger which conflicts with mailer's management command
# if DEBUG and not os.environ.get('NO_DEBUG_TOOLBAR', ''):
#     INSTALLED_APPS.append('debug_toolbar')
#     MIDDLEWARE.append(
#         'debug_toolbar.middleware.DebugToolbarMiddleware'
#     )
#     DEBUG_TOOLBAR_CONFIG = {
#         'SHOW_TOOLBAR_CALLBACK': lambda x: DEBUG
#     }

AUTH_PREFIX = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': f"{AUTH_PREFIX}.UserAttributeSimilarityValidator",
        'OPTIONS': {
            'user_attributes': ('email', 'full_name', 'short_name')
        },
    },
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
# # ASGI_APPLICATION = "core.routing.application"
#
# # CHANNEL_LAYERS = {
# #     'default': {
# #         'BACKEND': 'channels_redis.core.RedisChannelLayer',
# #         'CONFIG': {
# #             "hosts": [('redis', 6379)],
# #         },
# #     },
# # }

# Set up custom user model
AUTH_USER_MODEL = 'user.User'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': sec.load("DJANGO_DB_HOST"),
        'PORT': int(sec.load("DJANGO_DB_PORT")),
        'NAME': sec.load("DJANGO_DB_NAME"),
        'USER': sec.load("DJANGO_DB_USER"),
        'PASSWORD': sec.load('django_db_password'),
        # 'OPTIONS': {
        #     'sslmode': 'verify-ca',
        #     'sslrootcert': '/run/secrets/PG_SERVER_SSL_CACERT',
        #     'sslcert': '/run/secrets/PG_CLIENT_SSL_CERT',
        #     'sslkey': '/run/secrets/PG_CLIENT_SSL_KEY',
        # },
    },
    # 'explorer': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'HOST': 'postgres',
    #     'PORT': '5432',
    #     'NAME': 'django',
    #     'USER': 'explorer',
    #     'PASSWORD': read_secret_from_file('DB_PASSWORD_EXPLORER'),
    #     'TEST': {
    #         'MIRROR': 'default',
    #     },
    #     'OPTIONS': {
    #         'sslmode': 'verify-ca',
    #         'sslrootcert': '/run/secrets/PG_SERVER_SSL_CACERT',
    #         'sslcert': '/run/secrets/PG_CLIENT_SSL_CERT',
    #         'sslkey': '/run/secrets/PG_CLIENT_SSL_KEY',
    #     },
    # },
}

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#     # Use this if you want to disable the form on the BrowsableAPIRenderer
#     # 'DEFAULT_RENDERER_CLASSES': (
#     #     'rest_framework.renderers.JSONRenderer',
#     #     'core.renderers.BrowsableAPIRendererWithoutForm',
#     # ),
#     'DEFAULT_FILTER_BACKENDS': (
#         'django_filters.rest_framework.DjangoFilterBackend',
#     ),
#     'DEFAULT_PAGINATION_CLASS': (
#         'core.pagination.FlexiblePagination'
#     ),
# }
#
# EXPLORER_DEFAULT_CONNECTION = 'explorer'
# EXPLORER_CONNECTIONS = {'Default': 'explorer'}
# EXPLORER_SQL_BLACKLIST = ()
# EXPLORER_DATA_EXPORTERS = [
#     ('csv', 'core.exporters.CSVExporterBOM'),
#     ('excel', 'explorer.exporters.ExcelExporter'),
#     ('json', 'explorer.exporters.JSONExporter')
# ]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('hu', _('Hungarian')),
)

MARTOR_ENABLE_CONFIGS = {
    'imgur': 'false',     # to enable/disable imgur/custom uploader.
    'mention': 'false',  # to enable/disable mention
    'jquery': 'true',    # to include/revoke jquery (require for admin default django)
    'living': 'false',   # to enable/disable live updates in preview
}

# LOCALE_PATHS = ('/data/files/locale/',)
# MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
#
# # # ROSETTA
# # ROSETTA_MESSAGES_PER_PAGE = 50
# # CACHES = {
# #     'default': {
# #         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
# #         'LOCATION': 'cache_table',
# #     }
# # }
#
# # DATE_FORMAT = ('Y-m-d')
# # DATETIME_FORMAT = ('Y-m-d H:i:s')
# # TIME_FORMAT = ('H:i:s')

# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

LOGGING_CONFIG = None
log_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'django': {
            'format': '|{asctime}|{name}|{levelname}|{message}',
            'datefmt': '%Y-%m-%d %H:%M:%S%z',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'django',
            'class': 'logging.StreamHandler',
        },
        # "file": {
        #     'level': "DEBUG",
        #     "formatter": "django",
        #     "class": "logging.handlers.RotatingFileHandler",
        #     "filename": "/host/log/django/django.log",
        #     "maxBytes": 10485760,
        #     "backupCount": 10,
        # },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

# if (
#     not DEBUG or
#     os.environ.get('MAIL_ADMINS_ON_ERROR_IN_DEBUG', '').lower() == 'true'
# ):
#     log_config['loggers']['django.request'] = {'handlers': ['mail_admins']}

logging.config.dictConfig(log_config)
