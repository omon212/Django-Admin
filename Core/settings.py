"""
Django settings for Core project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r@qi(^1#zd(!k8za!!gs(mxkf@ed3hf8bq@lh)igg0!g4+%hrj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
import logging
logging.basicConfig(level=logging.DEBUG)

ALLOWED_HOSTS = ['marsgame.uz',"*"]

ALLOWED_IP = '84.54.78.19'

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'UserApp',
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



# settings.py

JAZZMIN_SETTINGS = {
    "site_title": "omonullo",
    "site_header": "omonullo",
    "welcome_sign": "Welcome to the omonullo Admin",
    'site_logo': 'jazzmin/img/icon.jpg',
    'search_model': 'auth.User',
    'navigation_expanded': True,

    # Customizing the menu
    'menu': [
        # Adding a dashboard link
        {'name': 'Dashboard', 'url': 'admin:index', 'icon': 'fas fa-tachometer-alt', 'permissions': ['auth.view_user']},

        # Customizing the "Authentication and Authorization" section
        {'app': 'auth', 'name': 'Auth', 'icon': 'fas fa-users-cog', 'models': [
            {'name': 'Groups', 'icon': 'fas fa-user-friends'},
            {'name': 'Users', 'icon': 'fas fa-user'},
        ]},

        # Adding your custom app section
        {'app': 'your_app_label', 'name': 'Your App', 'icon': 'fas fa-folder-open', 'models': [
            {'name': 'Your Model', 'icon': 'fas fa-database'},
        ]},

        # Adding other links or sections as needed
        {'name': 'Custom Link', 'url': '/custom-url', 'icon': 'fas fa-link'},
    ],

    # Customizing the colors and other UI elements (optional)
    'colors': {
        'primary': '#3498db',
        'secondary': '#2c3e50',
        'accent': '#e74c3c',
        'info': '#3498db',
        'success': '#2ecc71',
        'warning': '#f39c12',
        'danger': '#e74c3c',
        'light': '#ecf0f1',
        'dark': '#34495e',
    },
    "use_google_fonts_cdn": True,
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "collapsible"
    },
    # Other settings as needed


}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Core.middleware.IPRestrictionMiddleware',
]

ROOT_URLCONF = 'Core.urls'

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

WSGI_APPLICATION = 'Core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
