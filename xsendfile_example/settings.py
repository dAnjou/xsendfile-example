# Django settings for xsendfile_example project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'xsendfile_example.urls'

WSGI_APPLICATION = 'xsendfile_example.wsgi.application'

SECRET_KEY = 'Do you like animals?'

SENDFILE_BACKEND = 'sendfile.backends.xsendfile'
SENDFILE_ROOT_DIR = '/home/vagrant/media'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': False,
        'OPTIONS': {
            # ... some options here ...
        },
    },
]
