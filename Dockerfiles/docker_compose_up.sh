#!/bin/sh

docker rm `docker ps -a -q`
rsync -av app Dockerfiles/
docker-compose -f Dockerfiles/docker-compose.yml up --build