#!/bin/bash
cd /vagrant/algoritmo_parelelo_distribuido || exit 1
docker-compose down || exit 1
docker rmi server || exit 1
docker build -t server . || exit 1
#docker container prune -f || exit 1
#docker image prune -f || exit 1
docker-compose up -d server2 || exit 1
sleep 3
docker-compose up -d server1 || exit 1
sleep 2
docker-compose logs

