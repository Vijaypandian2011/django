import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')

# Apply the 'get_wsgi_application' function to your application
application = get_wsgi_application()
