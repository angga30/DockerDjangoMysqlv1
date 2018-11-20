#!/bin/bash
sudo docker-compose build
sudo docker-compose up -d
sleep 100
sudo docker exec -it djangolatse ./start.sh