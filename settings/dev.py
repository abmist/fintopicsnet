from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DISQUS_API_KEY = 'ZruTajAt8E3Ao1F2fzL2Dx9VUra9u0XABGKdSLXtAIHN3gL0qoUwJYywaqMEKkB8'
DISQUS_WEBSITE_SHORTNAME = 'codeinstitutesocialstaging'

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_1spV5wHeYbxQohJ5oOF1mjn4')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_4lB7Gs6AEqjCwTdMN12WFgs6')

# Paypal environment variables
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'https://291e2d8f.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'test_cib@aaaa.com'