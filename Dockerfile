FROM ubuntu:16.04
MAINTAINER Eohyung Lee (liquidnuker@gmail.com)

RUN sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -yqq install \
    build-essential python-pip software-properties-common \
    python-dev git

RUN echo "krb5-config krb5-config/default_realm string MYDOMAIN.COM" | debconf-set-selections && \
    echo "krb5-config krb5-config/kerberos_servers string krbserver.mydomain.com" | debconf-set-selections && \
    echo "krb5-config krb5-config/admin_server string krbserver.mydomain.com" | debconf-set-selections && \
    apt-get -yqq install libmysqlclient-dev libxml2-dev \
    libxslt1-dev mysql-client libpq-dev libvirt-dev \
    libnspr4-dev pkg-config libsqlite3-dev libzmq-dev \
    libffi-dev libldap2-dev libsasl2-dev ccache \
    krb5-config libkrb5-dev libssl-dev liberasurecode-dev \
    libjpeg8-dev curl

RUN pip install tox

ARG OLDBRANCH=stable/mitaka
ARG NEWBRANCH=stable/newton
ARG PROJECT

RUN git clone -b $OLDBRANCH https://github.com/openstack/$PROJECT.git /oldapp/ && cd /oldapp/ && tox -egenconfig --notest
RUN git clone -b $NEWBRANCH https://github.com/openstack/$PROJECT.git /newapp/ && cd /newapp/ && tox -egenconfig --notest

ADD diff.py .

CMD ["bash", "-l"]
