IMAGE_NAME=ustcoj_api
docker rmi $IMAGE_NAME
docker build -t $IMAGE_NAME .