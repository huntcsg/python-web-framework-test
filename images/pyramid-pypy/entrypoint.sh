#!/usr/bin/env bash


NUM_PROCESSORS=`nproc --all`
WORKERS=$(( ( $NUM_PROCESSORS * 2) + 1))

case $1 in

    pyramid-pypy)
    exec gunicorn -b 0.0.0.0:6543 -w $WORKERS web_framework_test.apps.pyramid.app:app
    ;;

    *)
    exit 1
    ;;

esac
