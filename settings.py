# Django settings for popgalaxy project.
import os.path
import socket
PROJECT_DIR = os.path.dirname(__file__)

DEBUG = False


GRAVATAR_DEFAULT_IMG = "http://localhost:8000/media/images/popgalaxy_default_avatar.png"
GRAVATAR_SIZE = 80


ADMINS = (
    ('Lawrence Leach', 'lleach@wowio.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'popgalaxy'             # Or path to database file if using sqlite3.
DATABASE_USER = 'popgalaxy'             # Not used with sqlite3.
DATABASE_PASSWORD = '@llstar$'         # Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.
if socket.gethostname() == 'Zeus.local':
    DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
    DEBUG = True
    MEDIA_ROOT = '/Users/zeus/Desktop/Dropbox/Sites/django/popgalaxy/media/'
elif socket.gethostname() == 'mark-desktop':
    DATABASE_ENGINE = 'sqlite3'
    DATABASE_NAME = 'dev2.db'
    DEBUG = True
    MEDIA_ROOT = '/home/mark/py-env/pop_root/popgalaxy/media/'
else:
    DATABASE_HOST = '173.203.196.9'
    MEDIA_ROOT = '/home/pop/public_html/popgalaxy/media/'

TEMPLATE_DEBUG = DEBUG

# Caching Setup
CACHE_BACKEND = 'db://pg_cache_table'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '(%7bylm*s56^^9=fs(c37tuv*m5rx%rm9%v+%-ou@s#49c9&88'

# Twitter 
CONSUMER_KEY = 'z8o36ZRk6KBJTsrPRiLA'
CONSUMER_SECRET = 'LXksObjMcwz9HlF0fCAgEwlnK2rn15hIGs2bh5hmTIA'
ACCESS_TOKEN ='207726284-uFI8u4nTqBOW4wCsP9Ns3w64JGZwjosab2pdZ3P4'
ACCESS_SECRET = 'w7xe5xUqkV6qhlgmyUffrO0jaOKyxnj30BS9bwOWRQ'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

if socket.gethostname() == 'Zeus.local':
    ROOT_URLCONF = 'popgalaxy.urls'
else:
    ROOT_URLCONF = 'urls'	
	
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

TAGGING_AUTOCOMPLETE_JS_BASE_URL = '/media/js'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.markup',
    'pagination',
    'registration',
    'tagging',
    'tagging_autocomplete',
    'threadedcomments'
)

if socket.gethostname() == 'Zeus.local':
    INSTALLED_APPS += (
        'popgalaxy.blog',
        'popgalaxy.video',
        'popgalaxy.headlines',
        'popgalaxy.search',
        'popgalaxy.corp',
    )
else:
    INSTALLED_APPS += (
        'blog',
        'video',
        'headlines',
        'search',
        'corp',
    )

