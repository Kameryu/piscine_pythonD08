#!/bin/sh

gunicorn

nginx -c ~/d08/d08/nginx.conf
nginx -s reload

# Placer le nginx.conf dans /Users/sle-guil/.brew/etc/nginx
