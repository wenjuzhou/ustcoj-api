NAME=ustcoj_api
DOCKER=ustcoj_api
APP=$(cd `dirname $0`; pwd)/app
docker stop $NAME && docker rm $NAME
docker run -d \
  -p 8000:8000 \
  -e MODULE=$NAME \
  -v $APP:/code \
  --name $NAME \
  $DOCKER
