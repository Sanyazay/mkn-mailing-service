from kafka import KafkaConsumer

from json import loads
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

consumer = KafkaConsumer(
    'MailTopic',
     bootstrap_servers=['broker:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id=None,
     value_deserializer=lambda x: x.decode('utf-8'))
    



for message in consumer:
    #send message
    print(message.value)