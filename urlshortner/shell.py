import os
import sys
import django

sys.path.append(sys.argv[0])  # добавляем текущую диру
os.environ['DJANGO_SETTINGS_MODULE'] = 'urlshortner.settings'
django.setup()

from core.logic_layer import Logic

Logic.create_url(url='https://docs.djangoproject.com/en/2.0/topics/http/urls/')