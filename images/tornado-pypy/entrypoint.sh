#!/usr/bin/env bash


NUM_PROCESSORS=`nproc --all`
WORKERS=$NUM_PROCESSORS

case $1 in

    tornado-pypy)
    exec pypy3 -m web_framework_test.apps.tornado.server $NUM_PROCESSORS
    ;;

    *)
    exit 1
    ;;

esac
