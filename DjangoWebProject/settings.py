from os import path
PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = (
    'localhost',
)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cource6db',
        'USER': 'b3261d3c82adde',
        'PASSWORD': 'afde9d04',
        'HOST': 'eu-cdbr-azure-north-e.cloudapp.net',
        'PORT': '3306',
    }
}

LOGIN_URL = '/login'

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

USE_L10N = False

USE_TZ = False

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = path.join(PROJECT_ROOT, 'static').replace('\\', '/')

STATIC_URL = '/static/'

STATICFILES_DIRS = (

)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'n(bd1f1c%e8=_xad02x5qtfn%wgwpi492e$8_erx+d)!tpeoim'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'DjangoWebProject.urls'

WSGI_APPLICATION = 'DjangoWebProject.wsgi.application'

TEMPLATE_DIRS = (

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'movies',
    'seances',
    'tickets',
    'reports',
    'rest_framework',
    'crispy_forms',
)


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
