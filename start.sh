if [ -n "$1" ]; then
if [ $1 = "flush" ]; then
    docker-compose kill
    docker volume rm redis-data
    docker volume rm backendredis-data
    docker system prune -a
    
    if [ -n "$2" ]; then
      if [ $2 = "live" ]; then
        docker-compose -f docker-compose.yml up --force-recreate --build
      else
        echo "bad parameter"
      fi
    else
    docker-compose -f docker-compose.yml up -d --force-recreate --build
    fi
    docker exec broker kafka-topics --bootstrap-server broker:9092 --create --topic Mailtopic
elif [ $1 = "live" ]; then
    docker-compose -f docker-compose.yml up
elif [ $1 = "restart" ]; then
    docker-compose restart
else
    echo "bad parameter"
fi
else 
    docker-compose -f docker-compose.yml up -d
fi


docker exec mail_service sh start.sh
docker ps
