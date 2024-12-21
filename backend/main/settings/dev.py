# backend/settings/dev.py
from .common_settings import *
from dotenv import load_dotenv
import os
import ast
load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY', default='your_default_secret_key')
DEBUG = ast.literal_eval(os.environ.get('DEBUG', default=True))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}