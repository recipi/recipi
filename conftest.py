import os

import pytest
from django.conf import settings as django_settings


def pytest_configure(config):
    if not django_settings.configured:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipi.conf.test')

    # override a few things with our test specifics
    django_settings.INSTALLED_APPS = tuple(django_settings.INSTALLED_APPS) + (
        'recipi.tests',
    )
