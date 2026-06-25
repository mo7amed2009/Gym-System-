
import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-beet@)-j=q1-=bs7%n%7(t0jto8&(mbxx7vb5e&a*mnc+^18%4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps 
    'users.apps.UsersConfig',
    'workouts.apps.WorkoutsConfig',
    'nutrition.apps.NutritionConfig',
    # Api
    'rest_framework',
    'rest_framework_simplejwt',
    
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    # عمر الـ Access Token (يفضل يكون قصير لحماية البيانات - مثلاً 5 دقائق أو ساعة)
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),
    
    # عمر الـ Refresh Token (بيستخدم عشان يطلب Access Token جديد بدون ما المستخدم يسجل دخول تاني)
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    
    # السماح بتدوير الـ Refresh Tokens (أمان أعلى)
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    
    # نوع الـ Header اللي بيبعته الـ Frontend في الـ Request
    # بيبقى كدة: Authorization: Bearer <your_token>
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    
    # الحقل اللي بيتعرف بيه على المستخدم في الـ Token
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    
    # مفتاح التشفير (بيستخدم الـ SECRET_KEY الخاص بمشروع Django)
    'SIGNING_KEY': SECRET_KEY,
    'ALGORITHM': 'HS256',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gym_db',
        'USER': 'postgres',
        'PASSWORD': 'Mohamed1234',
        'HOST' : 'localhost',
        'PORT': '5432'
            
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS=[
    
    os.path.join(BASE_DIR , 'users.static'),
    os.path.join(BASE_DIR , 'workouts.static'),
    os.path.join(BASE_DIR , 'nutrition.static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'


LOGOUT_REDIRECT_URL = 'sign_up'