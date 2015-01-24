import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
from django.core.urlresolvers import reverse_lazy


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, '..', '..')

SECRET_KEY = 'na2p&yexkp-g83$2m^&b!r+a%nv2ci1!d9vh^a_7h!hv*7&h79'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

INSTALLED_APPS = (
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Asyncronous worker support
    'celery',

    # i18n/l10n
    'django_babel',
    'statici18n',

    # For our REST Api
    'rest_framework',

    # Form helpers
    'floppyforms',

    # user (social-) account management
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

    # Recipi apps
    'recipi.core',
    'recipi.accounts',
    'recipi.food',
    'recipi.recipes'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'recipi.core.middlewares.server_header.ServerHeaderMiddleware'
)

ROOT_URLCONF = 'recipi.urls'

WSGI_APPLICATION = 'recipi.wsgi.application'

AUTH_USER_MODEL = 'accounts.User'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'recipi_dev',
    }
}

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',

    # Overwrite the allauth context processor because... it actively
    # verifies that the allauth processor exists.
    'recipi.accounts.context_processors.social.socialaccount'
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'bower_components'),
    os.path.join(PROJECT_DIR, 'src', 'recipi', 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'src', 'recipi', 'templates'),
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'web', 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'web', 'media')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Celery / Queue configuration
from kombu import Queue

BROKER_URL = 'redis://localhost:6379'

# Just so that this won't be forgotten, see
# http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html#caveats
# for details.
BROKER_TRANSPORT_OPTIONS = {
    'fanout_prefix': True,
    'fanout_patterns': True
}

# Force always eager to be False (it's by default but here for documentation)
CELERY_ALWAYS_EAGER = False
CELERY_EAGER_PROPAGATES_EXCEPTIONS = False

# Only accept JSON. This will be the default in Celery 3.2
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Track started tasks. This adds a new STARTED state once a task
# is started by the celery worker.
CELERY_TRACK_STARTED = True

CELERY_IMPORTS = (
    'recipi.core.tasks.mail',
)

CELERY_QUEUES = (
    Queue('default', routing_key='default'),
    Queue('celery', routing_key='celery'),
)

# Make our `LOGGING` configuration the only truth and don't let celery
# overwrite it.
CELERYD_HIJACK_ROOT_LOGGER = False

# Don't log celery log-redirection as warning (default).
# We manage our logging through `django.conf.settings.LOGGING` and
# want that to be our first-citizen config.
CELERY_REDIRECT_STDOUTS_LEVEL = 'INFO'

SESSION_SERIALIZER = 'recipi.utils.helpers.UUIDCapableJSONSerializer'

# Django REST Framework related settings.
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'recipi.api.auth.AnonymousAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'recipi.api.parsers.JSONParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}

# (social-) auth related settings
LOGIN_URL = reverse_lazy('account_login')
LOGIN_REDIRECT_URL = reverse_lazy('recipi-index')

ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = 'optional'

ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Recipi - '

ACCOUNT_SIGNUP_FORM_CLASS = 'recipi.accounts.forms.RegisterForm'

ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_USER_DISPLAY = 'recipi.accounts.utils.get_user_name'

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'

ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False

ACCOUNT_SESSION_REMEMBER = False

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'

# Directly logout once the user visits /account/logout/
ACCOUNT_LOGOUT_ON_GET = True

SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED

SOCIALACCOUNT_AUTO_SIGNUP = True
