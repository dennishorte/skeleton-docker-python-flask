CONTAINER_NAME='dev_server_flask'

# Build new version
docker build -t skeleton-dock-python-flask:latest .

# Kill old versions
if [[ $(docker ps -a -q --filter ancestor=$CONTAINER_NAME --format="{{.ID}}") ]]; then
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

# Run new version
docker run -d -p 5000:5000 skeleton-dock-python-flask
