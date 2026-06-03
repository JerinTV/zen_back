# zentodo_backend/zentodo_project/settings.py

import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

def env_bool(name, default=False):
    return os.environ.get(name, str(default)).lower() in {"1", "true", "yes", "on"}


def env_list(name, default=None):
    value = os.environ.get(name)
    if not value:
        return default or []
    return [item.strip() for item in value.split(",") if item.strip()]


# SECURITY WARNING: keep the secret key used in production secret.
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-@e^a4m-p0m5=w=k1h-@*!3-^a$s+0*d(t*t^m=f^%p+e7r=f2",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_bool("DEBUG", default=True)

ALLOWED_HOSTS = env_list(
    "ALLOWED_HOSTS",
    default=["127.0.0.1", "localhost", ".vercel.app"],
)

CSRF_TRUSTED_ORIGINS = env_list(
    "CSRF_TRUSTED_ORIGINS",
    default=[
        "https://*.vercel.app",
        "https://todo-6y48iydln-jerintvs-projects.vercel.app",
        "https://todo-ostnr7iit-jerintvs-projects.vercel.app",
        "https://todo-blond-psi.vercel.app",
        "https://todo-jerintvs-projects.vercel.app",
        "https://todo-jerintv-jerintvs-projects.vercel.app",
    ],
)

CORS_ALLOWED_ORIGINS = env_list(
    "CORS_ALLOWED_ORIGINS",
    default=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://todo-6y48iydln-jerintvs-projects.vercel.app",
        "https://todo-ostnr7iit-jerintvs-projects.vercel.app",
        "https://todo-blond-psi.vercel.app",
        "https://todo-jerintvs-projects.vercel.app",
        "https://todo-jerintv-jerintvs-projects.vercel.app",
    ],
)

CORS_ALLOW_ALL_ORIGINS = env_bool("CORS_ALLOW_ALL_ORIGINS", default=False)

# Ensure 'rest_framework' and 'corsheaders' and 'tasks' are in INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt', # Ensure this is present for JWT

    # My apps
    'tasks',
    'users', # This should already be here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Ensure this is placed correctly
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# TEMPLATES configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Added project-level templates directory
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

WSGI_APPLICATION = 'zentodo_backend.wsgi.application'

# Add this line to fix the ROOT_URLCONF error
ROOT_URLCONF = 'zentodo_backend.urls' # This tells Django where your main URL configuration is located

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASE_URL = (
    os.environ.get("DATABASE_URL")
    or os.environ.get("POSTGRES_URL")
    or os.environ.get("MYSQL_URL")
)
if DATABASE_URL:
    import dj_database_url

    is_sqlite = DATABASE_URL.startswith("sqlite")
    DATABASES["default"] = dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        ssl_require=not is_sqlite,
    )

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST Framework settings for JWT authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # You might also want 'rest_framework.authentication.SessionAuthentication'
        # for the Django admin or browsable API during development
        'rest_framework.authentication.SessionAuthentication', # Added for browsable API/admin
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny', # <--- THIS LINE IS CHANGED TO AllowAny
    ),
    'EXCEPTION_HANDLER': 'zentodo_backend.exceptions.api_exception_handler',
}

# Simple JWT specific settings
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60), # How long access token is valid
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),    # How long refresh token is valid
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": os.environ.get("SIMPLE_JWT_SIGNING_KEY", SECRET_KEY),
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}
