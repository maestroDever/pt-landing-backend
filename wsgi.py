import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTING_MODULE', 'server.settings')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
