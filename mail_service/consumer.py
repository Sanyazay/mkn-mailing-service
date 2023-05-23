from kafka import KafkaConsumer
import grpc
from json import loads
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mail_service_pb2_grpc import BackendServiceStub
from mail_service_pb2 import NotificationInfoRequest
from mail_service_pb2 import UpdateNotificationStatusRequest
import mail

consumer = KafkaConsumer(
    "MailTopic",
    bootstrap_servers=["broker:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id=None,
    value_deserializer=lambda x: loads(x.decode("utf-8")),
)
# value_deserializer = lambda x : loads(x.decode('utf-8'))


for message in consumer:
    print("icancatch")
    channel = grpc.insecure_channel("backend:50051")
    clientmail_service = BackendServiceStub(channel)
    message = message.value
    print(message)
    # vvjkee call
    note_info = clientmail_service.GetFullNotificationInfo(
        NotificationInfoRequest(notification_id=message["notification_id"])
    )
    print(note_info)
    print("sent message with id" + str(message["notification_id"]))
    # send message
    try:
        for i in note_info.email:
            mail.send_email(
                project_title=note_info.project_title,
                section_title=note_info.section_title,
                notification_title=note_info.notification_title,
                description=note_info.description,
                email=i,
            )
        clientmail_service.UpdateNotificationInfo(
            UpdateNotificationStatusRequest(
                notification_id=message["notification_id"], send_status=0
            )
        )
        f = open("mail_logs.txt", "w")
        f.write("sent message with id" + str(message["notification_id"]))

    except Exception as e:
        clientmail_service.UpdateNotificationStatus(
            UpdateNotificationStatusRequest(
                notification_id=message["notification_id"], send_status=1
            )
        )
