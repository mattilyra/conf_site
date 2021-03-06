# Passwords, API keys, and other sensitive information.

DATABASES_DEFAULT = {
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    "NAME": "{{ django_database }}",
    "USER": "{{ database_user }}",
    "PASSWORD": "{{ database_password }}",
    "HOST": "{{ database_host }}",
    "PORT": "",
}


SECRET_KEY = "{{ django_secret_key }}"
SESSION_COOKIE_PATH = "{{ subdirectory }}" or "/"
TIME_FORMAT = "{{ time_format }}"
TIME_ZONE = "{{ timezone }}"

DEFAULT_FROM_EMAIL = "{{ default_email }}"
SERVER_EMAIL = "{{ default_email }}"
EMAIL_USE_TLS = True
EMAIL_HOST = '{{ email_host_name }}'
EMAIL_HOST_USER = '{{ email_host_user }}'
EMAIL_HOST_PASSWORD = '{{ email_host_password }}'
EMAIL_PORT = '587'
# Determine which email backend to use. Note that previous variables
# are only relevant to the SMTP backend.
{% if sendgrid_api_key and environment_type == "production" %}
EMAIL_BACKEND = "sgbackend.SendGridBackend"
SENDGRID_API_KEY = "{{ sendgrid_api_key }}"
{% elif environment_type == "production" %}
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
{% else %}
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
{% endif %}

ALLOWED_HOSTS = ['*']
USE_X_FORWARDED_HOST = {% if subdirectory %}True{% else %}False{% endif %}


FORCE_SCRIPT_NAME = "{{ subdirectory }}" or None
LOGIN_URL = "{{ website_url }}/account/login/"
MEDIA_URL = "{{ website_url }}/media/"
STATIC_URL = "{{ website_url }}/static/"

GOOGLE_ANALYTICS_PROPERTY_ID = "{{ google_analytics_id }}"
SETTINGS_EXPORT = ["GOOGLE_ANALYTICS_PROPERTY_ID", ]
WAGTAIL_SITE_NAME = "{{ conference_name }}"
