from pathlib import Path
import logging


BASE_DIR = Path(__file__).resolve().parent.parent


SECONDS_FOR_SINGLE_POINT = 1

SYMBOLS_IN_TEAM_CODE = 5

logging.basicConfig(level=logging.DEBUG, filename='log.log', filemode='w',
                    format='%(asctime)s - logger:%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('DL')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler(filename='log.log'))

SESSION_COOKIE_SAMESITE = None
CRSF_COOKIE_SAMESITE = None

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080'
]

CORS_ALLOW_CREDENTIALS = True

# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [('localhost', 8000), ('127.0.0.1', 8000)],
#         },
#     },
# }

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

SECRET_KEY = 'django-secret-token'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'channels',
    'rest_framework',
    'corsheaders',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'game.apps.GameConfig',
    'team.apps.TeamConfig',
    'quichannels.apps.QuichannelsConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'quiz.urls'

TEMPLATES_ROOT = '/templates/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / TEMPLATES_ROOT],
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

WSGI_APPLICATION = 'quiz.wsgi.application'
ASGI_APPLICATION = 'quiz.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/collectedstatic/'
STATIC_ROOT = BASE_DIR / STATIC_URL
STATICFILES_DIRS = [BASE_DIR / '/static/']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
