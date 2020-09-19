# Build new version
docker build -t skeleton-dock-python-flask:latest .

# Kill old versions
OLD_IDS=$(docker ps -a -q --filter ancestor=skeleton-dock-python-flask --format="{{.ID}}")
for OLD_ID in $OLD_IDS; do
    docker stop $OLD_ID
    docker rm $OLD_ID
done

# Run new version
docker run -d -p 5000:5000 -e FLASK_SECRET_KEY="$FLASK_SECRET_KEY" skeleton-dock-python-flask
