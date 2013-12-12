from base import *
import os

# Set up redis
from redisify import redisify
CACHES = redisify(default='redis://localhost')
# Add the static files cache. Set a higher timeout.
CACHES.update({
	'staticfiles': {
    	'BACKEND': CACHES['default']['BACKEND'],
    	'LOCATION': CACHES['default']['LOCATION'],
    	'OPTIONS': {
    		'DB': CACHES['default']['OPTIONS']['DB'],
    		'PASSWORD': CACHES['default']['OPTIONS']['PASSWORD'],
    	},
    	'KEY_PREFIX': 'staticfiles_',
    	'TIMEOUT': 2592000,
    }
})

# Parse database configuration from $DATABASE_URL
from postgresify import postgresify
DATABASES = postgresify()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'staging.labelstate'
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
MEDIA_URL = "https://{0}.s3.amazonaws.com/media/".format(AWS_STORAGE_BUCKET_NAME)

#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storagescache.boto.CachedStaticS3BotoStorage'
STATIC_URL = "https://{0}.s3.amazonaws.com/static/".format(AWS_STORAGE_BUCKET_NAME)

########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django_ses.SESBackend'
########## END EMAIL CONFIGURATION




