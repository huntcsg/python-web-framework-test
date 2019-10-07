#!/usr/bin/env bash

case $1 in

    locust)
    shift
    exec /opt/venvs/locust/bin/locust "$@"
    ;;

    *)
    exit 1
    ;;

esac
