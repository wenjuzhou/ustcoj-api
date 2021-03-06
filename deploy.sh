#!/usr/bin/env bash
NAME=ustcoj_api
MIGRATE_NAME=ustcoj_api_migrate
IMAGE_NAME=ustcoj_api
APP_DIR=$(cd `dirname $0`; pwd)/app

# migrate
docker stop ${MIGRATE_NAME} && docker rm ${MIGRATE_NAME}
docker run -d \
  -e MODULE=${NAME} \
  -v ${APP_DIR}:/code \
  --name ${MIGRATE_NAME} \
  ${IMAGE_NAME} \
  python3 manage.py migrate

# api server
docker stop ${NAME} && docker rm ${NAME}
docker run -d \
  -p 8000:8000 \
  -e MODULE=${NAME} \
  -v ${APP_DIR}:/code \
  --name ${NAME} \
  ${IMAGE_NAME}
