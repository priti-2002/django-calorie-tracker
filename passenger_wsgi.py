import os
import sys

# Add your project directory to the path so Passenger can find your files
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(1, os.path.join(os.path.dirname(__file__), 'mysite'))

# Replace 'myproject' with the name of the folder containing your settings.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# Import the WSGI application object from your project's wsgi.py
from mysite.wsgi import application
