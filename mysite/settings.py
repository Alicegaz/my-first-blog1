"""
Django settings for mysite project.
Generated by 'django-admin startproject' using Django 1.9.6.
For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8z(yk84j0#4r2f^ip)5r47kan-0!-m_%wqvk87i(xwffs08cxc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'sortedm2m',
    'authentication',
    'rest_framework',
    'compressor',
    'djangobower',
    'crispy_forms',
    'common',
    'django_extensions',
    'betterforms'
    # 'django.contrib.sites',

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
            'loaders': [
                'admin_tools.template_loaders.Loader',
                'django.template.loaders.app_directories.Loader',

                'django.template.loaders.filesystem.Loader',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# STATICFILE_DIRS = (
#   os.path.join(BASE_DIR, 'static'),
# )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    'djangobower.finders.BowerFinder',
)

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'smartfoods',
        'USER': 'postgres',
        'PASSWORD': '123qwe',
        'HOST': '',
        'PORT': '',
    }
}

BOWER_COMPONENTS_ROOT = '/PROJECT_ROOT/components/'

BOWER_PATH = '/usr/bin/bower'

AUTH_PROFILE_MODULE = "authentication.UserProfile"
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
CACHE_BACKEND = 'dummy:///'
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

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = 'media/'

# STATIC_ROOT = '/home/SmartFoods/mysite/blog_templates/static/'
STATIC_URL = '/staticfiles/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
ADMIN_MEDIA_PREFIX = '/static/admin/'

ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
TIME_ZONE = 'Europe/Moscow'

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.SessionAuthentication',
#     )
# }

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO", 'https')

# LOGIN_URL = r"/auth/login/"

USE_I18N = True

USE_L10N = True

USE_TZ = False

COMPRESS_ENABLED = True
COMPRESS_ROOT = 'staticfiles'
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)
# AUTH_USER_MODEL = 'authentication.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
