#! /bin/bash

gunicorn "dfweb.wsgi" --bind=0.0.0.0:8080