#!/bin/bash
set -e

POSTGRESQL_USER=${POSTGRESQL_USER:-"postgres"}
POSTGRESQL_PASSWORD=${POSTGRESQL_PASSWORD:-"abcd1234"}
POSTGRESQL_DB=${POSTGRESQL_DB:-"boiler"}
POSTGRESQL_TEMPLATE=${POSTGRESQL_TEMPLATE:-"DEFAULT"}

POSTGRESQL_BIN=/usr/lib/postgresql/9.3/bin/postgres
POSTGRESQL_CONFIG_FILE=/etc/postgresql/9.3/main/postgresql.conf
POSTGRESQL_DATA=/var/lib/postgresql/9.3/main

POSTGRESQL_SINGLE="sudo -u postgres $POSTGRESQL_BIN --single --config-file=$POSTGRESQL_CONFIG_FILE"

if [ ! -d $POSTGRESQL_DATA ]; then
    mkdir -p $POSTGRESQL_DATA
    chown -R postgres:postgres $POSTGRESQL_DATA
    sudo -u postgres /usr/lib/postgresql/9.3/bin/initdb -D $POSTGRESQL_DATA -E 'UTF-8'
    ln -s /etc/ssl/certs/ssl-cert-snakeoil.pem $POSTGRESQL_DATA/server.crt
    ln -s /etc/ssl/private/ssl-cert-snakeoil.key $POSTGRESQL_DATA/server.key
fi

$POSTGRESQL_SINGLE <<< "CREATE USER $POSTGRESQL_USER WITH SUPERUSER;" > /dev/null
$POSTGRESQL_SINGLE <<< "ALTER USER $POSTGRESQL_USER WITH PASSWORD '$POSTGRESQL_PASSWORD';" > /dev/null
$POSTGRESQL_SINGLE <<< "CREATE DATABASE $POSTGRESQL_DB OWNER $POSTGRESQL_USER TEMPLATE $POSTGRESQL_TEMPLATE;" > /dev/null

exec sudo -u postgres $POSTGRESQL_BIN --config-file=$POSTGRESQL_CONFIG_FILE
