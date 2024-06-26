# Django settings for knesset project.
import os
import logging

# dummy gettext, to get django-admin makemessages to find i18n texts in this file
gettext = lambda x: x

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'NAME': 'dev.db',
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Jerusalem'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'he'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DATA_ROOT = os.path.join(PROJECT_ROOT, os.path.pardir,os.path.pardir,'data','')
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, os.path.pardir,os.path.pardir,'static', ''))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/django_admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '1_ovxxkf(c*z_dwv!(-=dezf#%l(po5%#zzi*su-$d*_j*1sr+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",    
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',    
    'pagination.middleware.PaginationMiddleware',
    # make sure to keep the DebugToolbarMiddleware last
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'knesset.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',          # django apps
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.comments',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'piston',                       # friends apps
    'debug_toolbar',
    'tagging',
    'south',
    'planet',
    'pagination',
    'django_extensions',
    'actstream',
    'avatar',
    'hitcount',
    'annotatetext',
    'mailer',
    'backlinks',
    'backlinks.pingback',
    'backlinks.trackback',
    'django_nose',
    'gunicorn',
    'djangoratings',
    'voting',
    'knesset',
    'knesset.auxiliary',                  # knesset apps
    'knesset.mks',
    'knesset.laws',
    'knesset.committees',
    'knesset.simple',
    'knesset.tagvotes',
    'knesset.accounts',
    'knesset.links',
    'knesset.user',
    'knesset.agendas',
    'knesset.badges',
    'knesset.notify',
    'knesset.persons',
    'knesset.events',
    'knesset.video',
    'knesset.okhelptexts',
)

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.request",
"knesset.context.processor",
)
INTERNAL_IPS = ('127.0.0.1',)
# Add the following line to your local_settings.py files to disable django-debug-toolar:
INTERNAL_IPS = ()
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

LOCAL_DEV = True

LOGIN_URL = '/users/login/'

SITE_NAME = 'Open-Knesset'

MAX_TAG_LENGTH = 128

AUTH_PROFILE_MODULE = 'user.UserProfile'

LOGIN_REDIRECT_URL = '/'

USER_AGENT = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"

LOG_FILENAME = os.path.join(PROJECT_ROOT, 'open-knesset.log')
logger = logging.getLogger("open-knesset")
logger.setLevel(logging.DEBUG)  # override this in prod server to logging.ERROR
h = logging.FileHandler(LOG_FILENAME)
h.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s")
h.setFormatter(formatter)
logger.addHandler(h)

GOOGLE_CUSTOM_SEARCH = "011858809565220576533:pyrgq6kc_cy"
GOOGLE_MAPS_API_KEYS = {'dev': 'ABQIAAAAWCfW8hHVwzZc12qTG0qLEhQCULP4XOMyhPd8d_NrQQEO8sT8XBQdS2fOURLgU1OkrUWJE1ji1lJ-3w',
                        'prod': 'ABQIAAAAWCfW8hHVwzZc12qTG0qLEhR8lgcBs8YFes75W3FA_wpyzLVCpRTF-eaJoRuCHAJ2qzVu-Arahwp8QA'}
GOOGLE_MAPS_API_KEY = GOOGLE_MAPS_API_KEYS['dev'] # override this in prod server

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

LONG_CACHE_TIME = 18000 # 5 hours

ANNOTATETEXT_FLAGS = (gettext('Statement'),
                    gettext('Funny :-)'),
                    gettext('False fact'),
                    gettext('Source?'),
                    gettext('Found source'),
                    gettext('Cross reference'),
                    gettext('Important'),
                    gettext('Formatting/Error!'),
                    gettext('Comment'),)

AUTO_GENERATE_AVATAR_SIZES = (75, 48)

HITCOUNT_KEEP_HIT_ACTIVE = { 'hours': 1 }
HITCOUNT_HITS_PER_IP_LIMIT = 0
HITCOUNT_EXCLUDE_USER_GROUP = ( )

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--with-xunit']


SERIALIZATION_MODULES = {
    'oknesset' : 'auxiliary.serializers'
}

# if you add a local_settings.py file, it will override settings here
# but please, don't commit it to git.
try: 
    from local_settings import *
except ImportError:
    pass
