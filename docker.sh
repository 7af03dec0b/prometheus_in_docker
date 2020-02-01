#!/bin/bash
export PGUSER=$UID
docker-compose build
docker-compose up
