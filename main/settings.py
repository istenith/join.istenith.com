import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a)*#0p#x9s4_g!p5mrh*4bars7z^ub(^8t@e7mn9cao24r(e#+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    'https://join.istenith.com',
    'http://join.istenith.com',
    'http://127.0.0.1:8000/',
    'https://interview-iste.azurewebsites.net',
    'http://interview-iste.azurewebsites.net'
]

INSTALLED_APPS = [
    'forms',
    'solo',
    'results',
    'phonenumber_field',
    'adminactions',
    'jazzmin',
    'widget_tweaks',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND':
        'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "templates", "jazzmin")
        ],
        'APP_DIRS':
        True,
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

WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "navbar": "navbar-dark",
    "dark_mode_theme": "darkly",
}
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title)
    "site_title": "ISTE-NITH",
    # Title on the login screen (19 chars max) (will default to current_admin_site.site_header)
    "site_header": "join.istenith.com",
    # Title on the brand (19 chars max) (will default to current_admin_site.site_header)
    "site_brand": "ISTE-NITH'22",
    "welcome_sign": "Welcome to the admin dashboard. Login to take incharge.",
    # Copyright on the footer
    "copyright": "ISTE-NITH",
    "changeform_format": "horizontal_tabs",
    "site_logo": "images/iste.png",
    "site_logo_classes": "img-circle",
    "topmenu_links": [
        {
            "name": "Home",
            "url": "/",
            "new_window": True
        },
    ],
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# SMTP setup
# EMAIL_HOST= 'smtp.gmail.com'
# EMAIL_PORT= 587
# EMAIL_HOST_USER= ''  #email id to be filled
# EMAIL_HOST_PASSWORD= '' # password for same email id!
# EMAIL_USE_TLS= True
