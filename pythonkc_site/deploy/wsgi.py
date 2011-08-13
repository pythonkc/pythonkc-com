import os, sys

from django.core.handlers.wsgi import WSGIHandler
os.environ["DJANGO_SETTINGS_MODULE"] = "myproject.settings"
application = WSGIHandler()