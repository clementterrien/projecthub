from django import setup
from os import environ as os_env

os_env.setdefault("DJANGO_SETTINGS_MODULE", "projecthub.settings")
setup()
