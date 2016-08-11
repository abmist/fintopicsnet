from base import *
import dj_database_url
import settings

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

DATABASES['default'] = dj_database_url.parse("mysql://b06f66936c080d:ee16062b@eu-cdbr-west-01.cleardb.com/heroku_646040fe3c68f89?reconnect=true")

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_1spV5wHeYbxQohJ5oOF1mjn4')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_4lB7Gs6AEqjCwTdMN12WFgs6')

# Paypal environment variables
SITE_URL = 'http://fintopicsnet.herokuapp.com'
PAYPAL_NOTIFY_URL = '.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'test_cib@aaaa.com'