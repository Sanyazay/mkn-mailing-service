if [ $1 = flush ]; then
    docker system prune -a
fi
docker-compose -f docker-compose.yml up -d --force-recreate --build
docker-compose -f docker-compose.yml up -d
docker-compose restart test
docker ps