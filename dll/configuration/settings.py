"""
Django settings for dll project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import logging
import os
from environs import Env


env = Env()
logger = logging.getLogger("dll.settings")


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "SET_ME")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", ["*"])

# DJANGO_ADMINS=John:john@admin.com,Jane:jane@admin.com
ADMINS = [x.split(":") for x in env.list("DJANGO_ADMINS", [])]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "django.contrib.postgres",
    "constance",
    "constance.backends.database",
    "webpack_loader",
    "easy_thumbnails",
    "easy_thumbnails.optimize",
    "filer",
    "mptt",
    "meta",
    "taggit",
    "polymorphic",
    "django_extensions",
    "crispy_forms",
    "ckeditor",
    "import_export",
    "dll.content",
    "dll.user",
    "dll.general",
    "dll.communication",
    "rest_framework",
    "django_filters",
    "rules.apps.AutodiscoverRulesConfig",
    "haystack",
    "django_better_admin_arrayfield.apps.DjangoBetterAdminArrayfieldConfig",
    "django_select2",
    "simple_history",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = "dll.configuration.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dll.configuration.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DATABASE_NAME"),
        "USER": env.str("DATABASE_USER"),
        "HOST": env.str("DATABASE_HOST"),
        "PORT": env.int("DATABASE_PORT", 5432),
    }
}
if env.str("DATABASE_PASSWORD", None):
    DATABASES["default"]["PASSWORD"] = env.str("DATABASE_PASSWORD")


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "de-de"

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_L10N = True

USE_TZ = True


if env.bool("DJANGO_USE_S3", False):
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv("DJANGO_AWS_S3_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("DJANGO_AWS_S3_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("DJANGO_AWS_S3_BUCKET_NAME")
    AWS_REGION = os.getenv("DJANGO_AWS_REGION", "eu-central-1")
    AWS_DEFAULT_ACL = None
    AWS_IS_GZIPPED = True
    AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")
    AWS_S3_CUSTOM_DOMAIN = os.getenv("AWS_S3_CUSTOM_DOMAIN")
    # s3 static settings
    STATIC_LOCATION = "static"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
    STATICFILES_STORAGE = "dll.general.storage_backends.StaticStorage"
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = "media"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
    DEFAULT_FILE_STORAGE = "dll.general.storage_backends.PublicMediaStorage"
else:
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.2/howto/static-files/

    STATIC_URL = os.getenv("STATIC_URL") or "/static/"
    STATIC_ROOT = os.getenv("STATIC_ROOT") or os.path.join(BASE_DIR, "..", "static")

    MEDIA_URL = os.getenv("MEDIA_URL") or "/media/"
    MEDIA_ROOT = os.getenv("MEDIA_ROOT") or os.path.join(BASE_DIR, "media")

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": "dist/",  # must end with slash
        "STATS_FILE": os.path.join(BASE_DIR, "./static/dist/webpack-stats.json"),
        "POLL_INTERVAL": 0.1,
        "TIMEOUT": None,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    }
}

AUTH_USER_MODEL = "user.DllUser"
AUTHENTICATION_BACKENDS = (
    "rules.permissions.ObjectPermissionBackend",
    "django.contrib.auth.backends.ModelBackend",  # this is default
)

DEFAULT_USER_USERNAME = "TUHH"
DEFAULT_USER_EMAIL = os.getenv("DEFAULT_USER_EMAIL")
DEFAULT_USER_PASSWORD = os.getenv("DEFAULT_USER_PASSWORD")
SHELL_PLUS = "bpython"  # bpython does not work on pycharm terminal. use plain

TAGGIT_CASE_INSENSITIVE = True

SITE_ID = 1  # this is for django-flatpages

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "ERROR"),
        },
        "dll": {
            "handlers": ["console", "mail_admins"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "WARNING"),
        },
    },
}
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


LOGIN_URL = "user:login"
LOGIN_REDIRECT_URL = "user-content-overview"
LOGOUT_REDIRECT_URL = "home"

CRISPY_TEMPLATE_PACK = "bootstrap4"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "SEARCH_PARAM": "q",
    "DEFAULT_PERMISSION_CLASSES": [],
}

CONTACT_EMAIL_BSB = env.str("CONTACT_EMAIL_BSB")
CONTACT_EMAIL_DLL = env.str("CONTACT_EMAIL_DLL")

# ---------------------- ReCaptcha --------------------

VALIDATE_RECAPTCHA = True
GOOGLE_RECAPTCHA_VERIFICATION_URL = "https://www.google.com/recaptcha/api/siteverify"
GOOGLE_RECAPTCHA_SECRET_KEY = env.str("GOOGLE_RECAPTCHA_SECRET_KEY", "")
GOOGLE_RECAPTCHA_WEBSITE_KEY = env.str("GOOGLE_RECAPTCHA_WEBSITE_KEY", "")

# ---------------------- Celery --------------------

CELERY_BROKER_URL = env(
    "CELERY_BROKER_URL",
    default="redis://{hostname}:6379/0".format(
        hostname=env.str("REDIS_HOSTNAME"),
    ),
)
CELERY_TASK_ALWAYS_EAGER = env.bool("CELERY_TASK_ALWAYS_EAGER")

# ---------------------- Haystack --------------------

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "solr.backend.CustomSolrEngine",
        "URL": "http://{}:8983/solr/dll-default".format(env.str("SOLR_HOSTNAME")),
        "ADMIN_URL": "http://{}:8983/solr/admin/cores".format(env.str("SOLR_HOSTNAME")),
    },
}
HAYSTACK_SIGNAL_PROCESSOR = "dll.content.signals.ContentSignalProcessor"


# ---------------------- Django Meta --------------------

META_SITE_PROTOCOL = env.str("META_SITE_PROTOCOL")
META_SITE_DOMAIN = env.str("META_SITE_DOMAIN")
META_USE_OG_PROPERTIES = True

BSB_REVIEW_MAIL = os.getenv("EMAIL_RECEIVER_DLL", "dll@blueshoe.de")
TUHH_REVIEW_MAIL = os.getenv("EMAIL_RECEIVER_BSB", "dll@blueshoe.de")

LOCALE_PATHS = [os.path.join(BASE_DIR, "locales")]

DEFAULT_FROM_EMAIL = env.str("EMAIL_SENDER")

SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Host for sending e-mail.
EMAIL_HOST = os.getenv("EMAIL_HOST", None)

# Port for sending e-mail.
EMAIL_PORT = env.int("EMAIL_PORT")

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", None)


EMAIL_SENDER = os.getenv("EMAIL_SENDER", None)

# ---------------------- djangor-cors-headers --------------------
CORS_ORIGIN_WHITELIST = env.list("CORS_ORIGIN_WHITELIST", [])
CORS_ORIGIN_ALLOW_ALL = env.bool("CORS_ORIGIN_ALLOW_ALL", False)
CORS_ADD_ALLOW_HEADERS = env.list("CORS_Add_ALLOW_HEADERS", [])
if CORS_ADD_ALLOW_HEADERS:
    CORS_ALLOW_HEADERS = list(default_headers) + CORS_ADD_ALLOW_HEADERS

FILE_UPLOAD_PERMISSIONS = 0o644

THUMBNAIL_OPTIMIZE_COMMAND = {
    "png": "/usr/bin/optipng {filename}",
    "gif": "/usr/bin/optipng {filename}",
    "jpeg": "/usr/bin/jpegoptim {filename}",
}
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar_Full": [
            [
                "Styles",
                "Format",
                "Bold",
                "Italic",
                "Underline",
                "Strike",
                "SpellChecker",
                "Undo",
                "Redo",
            ],
            ["Link", "Unlink", "Anchor"],
            ["Image", "Flash", "Table", "HorizontalRule"],
            ["TextColor", "BGColor"],
            ["SpecialChar"],
            ["Iframe", "Source"],
        ],
        "extra_plugins": ["iframe,iframedialog"],
    }
}

# ---------------------- Constance --------------------
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"
CONSTANCE_CONFIG = {
    # Content Teaser
    "MORE_LIKE_THIS_USE_TEXT": (
        True,
        """\
        Verwendung von den im Solr Dokument enthaltenen Informationen als Suchkriterium.
        Die im Solr Dokument enthaltenen Informationen sind eine Kombination aus Inhalten von mehreren \
        Datenbankfeldern. Da das Solr Dokument oft die Grundlage für die Suchfunktion einer Homepage ist, \
        enthält es i.d.R. allgemeine Informationen.
        """,
        bool,
    ),
    "MORE_LIKE_THIS_USE_NAME": (
        True,
        """\
        Verwendung von 'Titel des Tools/Trends/Unterrichtsbausteins' als Suchkriterium.
        Inhalte (wie Unterrichtsbausteine, Tools, Trends, ...) haben verschiedene Datenbankfelder \
        (z.B.: 'Teaser', 'Hinweise/Anmerkungen/Hintergrund', ...), welche als Grundlage für die \
        Übereinstimmungsberechnung verwendet werden. \
        Über die Auswahl von Suchkriterien ist es möglich die für die Berechnung der Gesamtpunktzahl verwendeten \
        Daten einzustellen. Basierend auf der Gesamtpunktzahl, welche die Übereinstimmung zu anderen Inhalten \
        widerspiegelt, werden vorgeschlagenen Inhalte angezeigt.
        """,
        bool,
    ),
    "MORE_LIKE_THIS_USE_TEASER": (
        True,
        "Verwendung von 'Teaser' als Suchkriterium.",
        bool,
    ),
    "MORE_LIKE_THIS_USE_ADDITIONAL_INFO": (
        True,
        "Verwendung von 'Hinweise/Anmerkungen/Hintergrund' als Suchkriterium.",
        bool,
    ),
    "MORE_LIKE_THIS_USE_TAGS": (
        True,
        "Verwendung von 'Tags' als Suchkriterium.",
        bool,
    ),
    "MORE_LIKE_THIS_USE_AUTHORS": (
        True,
        "Verwendung von 'Ersteller' als Suchkriterium.",
        bool,
    ),
    "MORE_LIKE_THIS_USE_SUBJECTS": (
        True,
        "Verwendung von 'Unterrichtsfach' als Suchkriterium.",
        bool,
    ),
    "MORE_LIKE_THIS_BOOST_TEXT": (
        1.0,
        """\
        Relative Gewichtung der aus dem Solr Dokument ermittelten Punktzahl.
        Dieser Wert beeinflusst die Gesamtpunktzahl nur, wenn das entsprechende Suchkriterium ausgewählt ist.
        """,
        float,
    ),
    "MORE_LIKE_THIS_BOOST_NAME": (
        5.0,
        "Relative Gewichtung der aus 'Titel des Tools/Trends/Unterrichtsbausteins' ermittelten Punktzahl.",
        float,
    ),
    "MORE_LIKE_THIS_BOOST_TEASER": (
        0.1,
        "Relative Gewichtung der aus 'Teaser' ermittelten Punktzahl.",
        float,
    ),
    "MORE_LIKE_THIS_BOOST_ADDITIONAL_INFO": (
        0.01,
        "Relative Gewichtung der aus 'Hinweise/Anmerkungen/Hintergrund' ermittelten Punktzahl.",
        float,
    ),
    "MORE_LIKE_THIS_BOOST_TAGS": (
        10.0,
        "Relative Gewichtung der aus 'Tags' ermittelten Punktzahl.",
        float,
    ),
    "MORE_LIKE_THIS_BOOST_AUTHORS": (
        0.1,
        "Relative Gewichtung der aus 'Ersteller' ermittelten Punktzahl.",
        float,
    ),
    "MORE_LIKE_THIS_BOOST_SUBJECTS": (
        2.0,
        "Relative Gewichtung der aus 'Unterrichtsfach' ermittelten Punktzahl.",
        float,
    ),
    "MORE_LIKE_THIS_COUNT": (
        12,
        """\
        Anzahl der maximal angezeigten vorgeschlagenen Inhalte. Falls mehr Vorschläge ermittelt werden, werden die \
        Vorschläge mit der höchsten Gesamtpunktzahl angezeigt. Wenn jedoch weniger Vorschläge ermittelt werden, \
        z.B. bedingt durch den gesetzten 'MORE_LIKE_THIS_SCORE_CUTOFF', können auch weniger Vorschläge wie hier \
        definiert angezeigt werden.
        """,
        int,
    ),
    "MORE_LIKE_THIS_SCORE_CUTOFF": (
        150.0,
        """\
        Minimale Gesamtpunktzahl die erreicht werden muss, damit Vorschläge in den vorgeschlagenen Inhalten \
        auftauchen. Dieser Wert sollte an die verwendete Gewichtung der einzelnen Vorschlagkriterien angepasst \
        werden.
        """,
        float,
    ),
}
CONSTANCE_CONFIG_FIELDSETS = {
    """
    Vorgeschlagene Inhalte (Content Teaser) - Einstellungen für die 'More Like This (MLT)' Funktionalität von Solr, \
    auf der vorgeschlagene Inhalte ermittelt werden
    """: {
        "fields": (
            "MORE_LIKE_THIS_USE_TEXT",
            "MORE_LIKE_THIS_USE_NAME",
            "MORE_LIKE_THIS_USE_TEASER",
            "MORE_LIKE_THIS_USE_ADDITIONAL_INFO",
            "MORE_LIKE_THIS_USE_TAGS",
            "MORE_LIKE_THIS_USE_AUTHORS",
            "MORE_LIKE_THIS_USE_SUBJECTS",
            "MORE_LIKE_THIS_BOOST_TEXT",
            "MORE_LIKE_THIS_BOOST_NAME",
            "MORE_LIKE_THIS_BOOST_TEASER",
            "MORE_LIKE_THIS_BOOST_ADDITIONAL_INFO",
            "MORE_LIKE_THIS_BOOST_TAGS",
            "MORE_LIKE_THIS_BOOST_AUTHORS",
            "MORE_LIKE_THIS_BOOST_SUBJECTS",
            "MORE_LIKE_THIS_COUNT",
            "MORE_LIKE_THIS_SCORE_CUTOFF",
        ),
        "collapse": True,
    },
}
