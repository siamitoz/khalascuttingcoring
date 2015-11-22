"""
Django settings for kakaravaara project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from shoop.addons import add_enabled_addons

######## PATHS ########
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, "var", "media")
STATIC_ROOT = os.path.join(BASE_DIR, "var", "static")
LOCALE_PATHS = (
    os.path.join(BASE_DIR, "..", "locale"),
)
MEDIA_URL = "/media/"
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'

######## Shoop ########
SHOOP_BASKET_CLASS_SPEC = ("reservations.basket:ReservableBasket")
SHOOP_BASKET_ORDER_CREATOR_SPEC = ("reservations.basket:ReservableOrderCreator")
SHOOP_ENABLED_ADDONS_FILE = os.path.join(BASE_DIR, "var", "enabled_addons")
SHOOP_PRICING_MODULE = "discount_pricing"
SHOOP_ADDRESS_HOME_COUNTRY = "FI"

######## Installed apps ########
PREREQ_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_extensions",
]

PROJECT_APPS = [
    "reservations",
]

SHOOP_APPS = [
    "bootstrap3",
    "django_jinja",
    "easy_thumbnails",
    "filer",
    "registration",
    "rest_framework",
    "shoop.addons",
    "shoop.admin",
    "shoop.api",
    "shoop.core",
    "shoop.default_tax",
    "shoop.discount_pricing",
    "shoop.front",
    "shoop.front.apps.auth",
    "shoop.front.apps.customer_information",
    "shoop.front.apps.personal_order_history",
    "shoop.front.apps.registration",
    "shoop.front.apps.simple_order_notification",
    "shoop.front.apps.simple_search",
    "shoop.notify",
    "shoop.simple_cms",
    "shoop.simple_pricing",
    "shoop.simple_supplier",
    "shoop.themes.classic_gray",
    "shoop.themes.default_theme",
    "shoop.xtheme",
]

INSTALLED_APPS = PROJECT_APPS + PREREQ_APPS + add_enabled_addons(SHOOP_ENABLED_ADDONS_FILE, SHOOP_APPS)

######## Middleware ########
BASE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

SHOOP_MIDDLEWARE = [
    'shoop.front.middleware.ProblemMiddleware',
    'shoop.front.middleware.ShoopFrontMiddleware',
]

MIDDLEWARE_CLASSES = BASE_CLASSES + SHOOP_MIDDLEWARE

######## Urls ########
ROOT_URLCONF = 'kakaravaara.urls'

######## Templates ########
TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
]

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja",
            'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
            "newstyle_gettext": True,
            "environment": "shoop.xtheme.engine.XthemeEnvironment"
        },
        "NAME": "jinja2",
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
        },
    },
]

######## WSGI ########
WSGI_APPLICATION = 'kakaravaara.wsgi.application'

######## Database ########
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

######## Internatialization ########
LANGUAGE_CODE = 'fi'
LANGUAGES = [
    ('en', 'English'),
    ('fi', 'Finnish'),
]

TIME_ZONE = 'Europe/Helsinki'
USE_I18N = True
USE_L10N = True
USE_TZ = True

PARLER_DEFAULT_LANGUAGE_CODE = "fi"

PARLER_LANGUAGES = {
    None: [{"code": c, "name": n} for (c, n) in LANGUAGES],
    'default': {
        'hide_untranslated': False,
    }
}

######## Loggers ########
LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {'format': '[%(asctime)s] (%(name)s:%(levelname)s): %(message)s'},
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'shoop': {'handlers': ['console'], 'level': 'DEBUG', 'propagate': True},
    }
}

######## Mailers ########
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

######## Sessions ########
SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"

######## REST API ########
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    )
}

######## Reservations ########
RESERVABLE_SEARCH_VISIBLE_ATTRIBUTES = [
    "maxpersons",
    "wifi",
    "equipment",
    "pets",
    "sauna",
]
