from os import environ

ENV = environ.get('DJANGO_ENV') or 'dev'

from .common import *

if ENV == 'dev':
    from .dev import *
elif ENV == 'prod':
    from .prod import *
