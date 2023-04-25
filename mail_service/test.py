import grpc

from mail_service_pb2_grpc import MailingServiceStub
from mail_service_pb2 import ScheduleRequest
channel = grpc.insecure_channel("localhost:50051")
client = MailingServiceStub(channel)

request = ScheduleRequest(notification_id=1, project_title="", section_title="321", notification_title="dsadsa", description="dsa", deadline="dsadsa", email="dsadas")
print(client.ScheduleNotification(request).send_status)