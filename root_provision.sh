apt-get update
apt-get install -y \
    apache2 libapache2-mod-wsgi libapache2-mod-xsendfile python-pip \
    python-virtualenv
a2enmod wsgi
a2enmod xsendfile
service apache2 restart
