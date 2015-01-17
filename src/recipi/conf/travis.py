import os
from recipi.conf.test import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['RECIPI_TEST_DB_NAME'],
        'USER': os.environ['RECIPI_TEST_DB_USER']
    }
}
