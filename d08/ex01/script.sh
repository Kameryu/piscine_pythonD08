#!/bin/sh

gunicorn

nginx -c ~/d08/d08/nginx.conf
nginx -s reload

# Placer le nginx.conf dans /Users/sle-guil/.brew/etc/nginx

openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
