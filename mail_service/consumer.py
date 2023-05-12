from kafka import KafkaConsumer
import grpc
from json import loads
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mail_service_pb2_grpc import BackendServiceStub
from mail_service_pb2 import GetFullNotificationInfo
from mail_service_pb2 import UpdateNotificationStatus
from mail import send_email

consumer = KafkaConsumer(
    "MailTopic",
    bootstrap_servers=["broker:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id=None,
    value_deserializer=lambda x: x.decode("utf-8"),
)


channel = grpc.insecure_channel("backend_mock:50052")
clientmail_service = BackendServiceStub(channel)

for message in consumer:
    message = message.value
    # vvjkee call
    note_info = clientmail_service.GetFullNotificationInfo(
        notification_id=message["notification_id"]
    )
    # send message
    for i in note_info["email"]:
        send_email(
            project_title=note_info["project_title"],
            section_title=note_info["section_title"],
            notification_title=note_info["notification_title"],
            description=note_info["description"],
            email=i,
        )

    print(message.value)
