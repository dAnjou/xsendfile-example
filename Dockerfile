FROM httpd:2.4

# install setup and build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    python3-dev \
    python3 \
    && rm -rf /var/lib/apt/lists/*

# install mod_wsgi
RUN wget -O /tmp/mod_wsgi.tar.gz https://github.com/GrahamDumpleton/mod_wsgi/archive/4.6.5.tar.gz \
    && mkdir /tmp/mod_wsgi \
    && tar -xf /tmp/mod_wsgi.tar.gz -C /tmp/mod_wsgi --strip-components=1 \
    && cd /tmp/mod_wsgi \
    && ./configure --with-python=/usr/bin/python3 \
    && make \
    && make install \
    && rm -r /tmp/*

# install mod_xsendfile
RUN wget -O /tmp/mod_xsendfile.tar.gz https://tn123.org/mod_xsendfile/mod_xsendfile-0.12.tar.gz \
    && mkdir /tmp/mod_xsendfile \
    && tar -xf /tmp/mod_xsendfile.tar.gz -C /tmp/mod_xsendfile --strip-components=1 \
    && cd /tmp/mod_xsendfile \
    && apxs -cia mod_xsendfile.c \
    && rm -r /tmp/*

# install pip
RUN wget -O /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py \
    && python3 /tmp/get-pip.py \
    && rm -r /tmp/*

COPY ./provisioning/docker/httpd.conf /usr/local/apache2/conf/httpd.conf

COPY ./requirements.txt /tmp
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

RUN mkdir -p /xsendfile-example/xsendfile_example
WORKDIR /xsendfile-example
COPY ./xsendfile_example xsendfile_example
RUN mv xsendfile_example/settings.py xsendfile_example/docker_settings.py
COPY ./provisioning/docker/settings.py xsendfile_example/settings.py

RUN mkdir /data
VOLUME /data
