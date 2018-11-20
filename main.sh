#!/bin/sh

while ! mysqladmin ping -h 172.19.0.3 -u root -ptesting --silent ; do
    sleep 1
    set = $(mysqladmin ping -h databasee -u root -ptesting --silent)
    echo "$set"
    if [ "$set"=="mysqld is alive" ]
    then
    sh ./start.sh
    exit 1
    fi
done