DOCKER=ustcoj_api
docker rmi $DOCKER
docker build -t $DOCKER .
