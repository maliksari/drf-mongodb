import os
import datetime

# from common.log_middleware import DatabaseLoggingHandler


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'p-=s1r)tiz$i5cdx!9sq*7p)9jar^ul1zxpqe+8-=9v9xyd%5l'
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djongo',
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'corsheaders',
    'app.apps.AppConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'common.log_middleware.DatabaseLoggingHandler',
]

ROOT_URLCONF = 'common.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'common.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'django_db',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}


REST_FRAMEWORK = {
    'DATE_FORMAT': '%d.%m.%Y',
    'EXCEPTION_HANDLER': 'common.exception_handler.handle_exception',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTTokenUserAuthentication'
    ]
}


LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_L10N = True
USE_TZ = False
STATIC_URL = '/static/'

TODAY = str(datetime.date.today()).replace("-", "_")


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'filters': {
#         'filter_info_level': {
#             '()': 'common.log_middleware.FilterLevels',
#             'filter_levels': [
#                 "INFO"
#             ]
#         },
#         'filter_error_level': {
#             '()': 'common.log_middleware.FilterLevels',
#             'filter_levels': [
#                 "ERROR"
#             ]
#         },
#         'filter_warning_level': {
#             '()': 'common.log_middleware.FilterLevels',
#             'filter_levels': [
#                 "WARNING"
#             ]
#         }
#     },
#     'formatters': {
#         'info-formatter': {
#             'format': '%(levelname)s : %(message)s - [in %(pathname)s:%(lineno)d]'
#         },
#         'error-formatter': {
#             'format': '%(levelname)s : %(asctime)s {%(module)s} [%(funcName)s] %(message)s- [in %(pathname)s:%(lineno)d]',
#             'datefmt': '%Y-%m-%d %H:%M'
#         },
#         'short': {
#             'format': '%(levelname)s : %(message)s'
#         }
#     },
#     'handlers': {
#         'customHandler_1': {
#             'formatter': 'info-formatter',
#             'class': 'common.log_middleware.DatabaseLoggingHandler',
#             'database': 'log_db',
#             'collection': 'logs',
#             'filters': ['filter_info_level'],
#         },
#         'customHandler_2': {
#             'formatter': 'error-formatter',
#             'class': 'common.log_middleware.DatabaseLoggingHandler',
#             'database': "log_db",
#             'collection': 'logs',
#             'filters': ['filter_error_level'],

#         },
#         'customHandler_3': {
#             'formatter': 'short',
#             'class': 'logging.StreamHandler',
#             'filters': ['filter_warning_level'],
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': [
#                 'customHandler_1',
#                 'customHandler_2',
#                 'customHandler_3'
#             ],
#             'level': 'DEBUG',
#         },
#     },
# }


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '{levelname} {asctime} {module}: {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname} {message}',
#             'style': '{',
#         },
#     },
#     'handlers': {
#         'my_log_handler': {
#             'level': 'DEBUG',
#             'class': 'common.log_middleware.DatabaseLoggingHandler',
#             'database': "log_db",
#             'collection': 'logs',
#             'formatter': 'verbose',
           
#         },
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'level': 'ERROR',
#             'propagate': True
#         },
#         'app': {
#             'handlers': ['my_log_handler', 'console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(hours=3),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': True
}

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True


try:
    from common.local_conf import *
except ImportError:
    pass
except Exception as e:
    print(e)
