# Django settings for xsendfile_example project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'xsendfile_example.urls'

WSGI_APPLICATION = 'xsendfile_example.wsgi.application'

SENDFILE_BACKEND = 'sendfile.backends.development'
SENDFILE_ROOT_DIR = '/home/vagrant/media'