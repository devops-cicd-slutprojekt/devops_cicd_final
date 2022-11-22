#!/bin/sh

docker run \
    --name mysql \
    --network my-network \
    -p 3306:3306 \
    -d \
    --rm \
    -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=example \
    -e MYSQL_USER=username \
    -e MYSQL_PASSWORD=password \
    -v "$(pwd)"/sql:/docker-entrypoint-initdb.d \
    mysql:8
