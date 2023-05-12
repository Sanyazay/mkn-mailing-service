from time import sleep
from json import dumps
from kafka import KafkaProducer
import redis
import datetime

producer = KafkaProducer(
    bootstrap_servers=["broker:9092"],
    value_serializer=lambda x: dumps(x).encode("utf-8"),
)


while True:
    print("start")
    curTime = int(datetime.datetime.now().timestamp())
    client = redis.StrictRedis(host="redis", port=6379, decode_responses=True)
    data = {}
    cursor = "0"
    while cursor != 0:
        cursor, keys = client.scan(cursor=cursor)

        values = client.mget(*keys) if len(keys) else []
        values = [value for value in values if not value == None]
        data.update(dict(zip(keys, values)))
    for key, value in data.items():
        if int(value) < curTime:
            print("producer sent")
            # vvjkee call
            client.delete(key)
            producer.send(
                "MailTopic",
                value={
                    "notification_id": key,
                    "time": str(datetime.datetime.now()),
                    "time_int": str(datetime.datetime.fromtimestamp(int(value))),
                },
            )
    print("end")
    sleep(60 - (int(datetime.datetime.now().timestamp()) - curTime))
