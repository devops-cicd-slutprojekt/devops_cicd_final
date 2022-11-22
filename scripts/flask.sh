#!/bin/sh

docker build -t my_flask .
docker run -it --rm -p5000:5000 --network=my-network -e MYSQL_HOST=mysql -e MYSQL_PASSWORD=password my_flask
