import environ, os
from pathlib import Path

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS')

AUTH_USER_MODEL = 'users.User'

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'rest_framework',
    'corsheaders',
    "django_htmx",
    
    'users',
    'auth_check',
    'main',
    'tasks',
]
# django cleanup should be last
INSTALLED_APPS.append('django_cleanup.apps.CleanupConfig')

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = "switch.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR/'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "switch.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': os.getenv("DB_ENGINE"),
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
        # uncomment below for mysql
        # "OPTIONS": {
        #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
        #     'charset': 'utf8mb4',
        #     "autocommit": True,
        # }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Kampala"
USE_I18N = True
USE_TZ = True


# Static and Media files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
MEDIA_URL = 'media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/public'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static/staticfiles/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# email
EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
# end email

# azure blob setup
if not DEBUG:
    DEFAULT_FILE_STORAGE = 'backend.storage.AzureMediaStorage'
    STATICFILES_STORAGE = 'backend.storage.AzureStaticStorage'
    SECRET_KEY = env("SECRET_KEY")
    AZURE_ACCOUNT_NAME = env("AZURE_ACCOUNT_NAME")
    AZURE_CONNECTION_STRING = env("AZURE_CONNECTION_STRING")
    AZURE_ACCOUNT_KEY = env("AZURE_ACCOUNT_KEY")
    AZURE_URL_EXPIRATION_SECS = int(env("AZURE_URL_EXPIRATION_SECS"))
    # custom
    AZURE_MEDIA_CONTAINER = env("AZURE_MEDIA_CONTAINER")
    AZURE_STATIC_CONTAINER = env("AZURE_STATIC_CONTAINER")

# auth config
LOGIN_URL = 'auth_check/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'auth_check:login'
AUTH_USER_MODEL = 'users.User'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True
