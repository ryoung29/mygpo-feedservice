# -*- coding: utf-8 -*-

import os, os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Stefan Kögl', 'stefan@skoegl.net'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.abspath('%s/../htdocs/media/' % os.path.dirname(__file__))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'm6jkg5lzard@k^p(wui4gtx_zu4s=26c+c0bk+k1xsik6+derf'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'feedservice.urls'

TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'couchdbkit.ext.django',
    'feedservice.parse',
    'feedservice.pubsubhubbub',
    'feedservice.urlstore',
    'feedservice.webservice',
)

BASE_URL='http://localhost:8080/'

COUCHDB_DATABASES = (
    ('feedservice.urlstore',     'http://127.0.0.1:5984/feedservice'),
    ('feedservice.pubsubhubbub', 'http://127.0.0.1:5984/feedservice'),
)

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}

SOUNDCLOUD_CONSUMER_KEY = ''

FLATTR_THING = ''

try:
    from settings_prod import *
except ImportError, e:
    import sys
    print >> sys.stderr, 'create settings_prod.py with your customized settings'
