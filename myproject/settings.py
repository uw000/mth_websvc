# myproject/settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 데이터베이스 설정
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vacant_home_db',
        'USER': 'dbuser2',
        'PASSWORD': 'user1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# SECRET_KEY = 'your_secret_key_here'

DEBUG = True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vacant_homes',  # 앱 등록
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

"""
# 비밀번호 검증
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
"""


# 언어 및 시간대 설정
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static 및 Media 파일 설정
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

WSGI_APPLICATION = 'myproject.wsgi.application'

ROOT_URLCONF = 'myproject.urls'

#  # Static files (CSS, JavaScript, Images)
#  STATIC_URL = '/static/'
#  STATIC_ROOT = BASE_DIR / 'static'

#  # Media files (User-uploaded content)
#  MEDIA_URL = '/media/'
#  MEDIA_ROOT = BASE_DIR / 'media'
