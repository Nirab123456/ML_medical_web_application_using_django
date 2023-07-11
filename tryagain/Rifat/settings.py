from pathlib import Path
import os

MEDIA_URL = '/media/'
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Specify the URL prefix for static files.
STATIC_URL = '/static/'

BLOG_STATIC_URL = '/blog_static/'

# Specify the directory for the blog static files.
BLOG_STATIC_ROOT = os.path.join(BASE_DIR, 'blog')

ABOUT_ME_URL = '/about_me/'
ABOUT_ME_ROOT = os.path.join(BASE_DIR, 'about_me')


# Add the following lines at the end of the file.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]


ENG_HANDWRITTEN_URL = '/eng_handwritten/'
ENG_HANDWRITTEN_ROOT = os.path.join(BASE_DIR, 'eng_handwritten')

BAN_HANDWRITTEN_URL = '/ban_handwritten/'
BAN_HANDWRITTEN_ROOT = os.path.join(BASE_DIR, 'ban_handwritten')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r5y(k((!k$s&xmm#kgo(%zahkfv5v-mmhi12&e4fy7g=&i0mn&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['rifatulislammajumder.me']
CSRF_TRUSTED_ORIGINS = ['http://rifatulislammajumder.me', 'https://rifatulislammajumder.me']
CORS_ALLOWED_ORIGINS = ['rifatulislammajumder.me', 'https://rifatulislammajumder.me']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nirab'

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

ROOT_URLCONF = 'Rifat.urls'

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

WSGI_APPLICATION = 'Rifat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'nirab',
        'USER':'root',
        'PASSWORD':'Nahida@123',
        'HOST':'localhost',
        'PORT':'3306',
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

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
