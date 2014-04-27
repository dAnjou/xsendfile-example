apt-get update
apt-get install -y \
    apache2 libapache2-mod-wsgi libapache2-mod-xsendfile python-pip \
    python-virtualenv
a2enmod wsgi
a2enmod xsendfile
a2dissite 000-default
cp /home/vagrant/xsendfile_example/xsendfile_example.vhost /etc/apache2/sites-available/xsendfile_example
a2ensite xsendfile_example
