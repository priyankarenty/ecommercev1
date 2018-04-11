import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ')rs78(*7t3_!q8x^ug8!kf!s%a2#z-z1c)%hoa^)7k(z-mm8*a'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    #installed apps
    'import_export',
    'report_builder',
    'chartit',
    'controlcenter',
    'bootstrap3',
    'chartjs',
    'bokeh',
    'djangobower',
    'django_nvd3',

    #our apps
    'pricevariance',
    'catdownload',
    'chartmis',
    'chartprice',
    'compare',
    'depreciated',
    'duplicates',
    'homepage',
    'leadtime',
    'missinginfo',
    'newproducts',
    'products',
    'price_approved',
    'ProductAccessory',
    'ProductAVEng',
    'reports',
    'search',
    'tutorial',
    'chartstock',
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

ROOT_URLCONF = 'ecproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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


STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATICFILES_DIRS = [
os.path.join(BASE_DIR, "static_ecommerce"),]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn","static_root")
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn","media_root")

CONTROLCENTER_DASHBOARDS = (
    ('mydash', 'ecproject.dashboard.MyDashboard'),
)
