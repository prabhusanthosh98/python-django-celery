#! /bin/bash

celery worker -A dfweb.celery -Ofair -E --broker='amqp://'$RABBITMQ_DEFAULT_USER':'$RABBITMQ_DEFAULT_PASS'@'$RABBITMQ_HOST':5672//' -Q demo_queue -c 2 -n celery-worker1@%h

