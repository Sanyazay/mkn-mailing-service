import grpc
from mail_service_pb2_grpc import BackendServiceStub
from mail_service_pb2 import NotificationInfoRequest
from mail_service_pb2 import UpdateNotificationStatusRequest

channel = grpc.insecure_channel("backend:50051")
clientmail_service = BackendServiceStub(channel)

note_info = clientmail_service.GetFullNotificationInfo(
    NotificationInfoRequest(notification_id="7086a830-0983-4fa5-a5ae-89541d3a63eb")
)
print(note_info)
