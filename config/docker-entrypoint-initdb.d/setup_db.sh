#!/bin/bash
set -e

function encript_pass() {
  echo -n "md5$(echo -n "$1$2" | md5sum | tr -d ' -')"
}

psql -v ON_ERROR_STOP=1 <<EOF
CREATE ROLE $DJANGO_DB_USER;
ALTER ROLE django ENCRYPTED PASSWORD '$(encript_pass "$DJANGO_DB_USER" "$DJANGO_DB_PASSWORD")' LOGIN CREATEDB;
\c postgres $DJANGO_DB_USER;
CREATE DATABASE $DJANGO_DB_NAME;
EOF
