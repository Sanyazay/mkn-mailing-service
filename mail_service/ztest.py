import grpc
from mail_service_pb2_grpc import BackendServiceStub
from mail_service_pb2 import NotificationInfoRequest
from mail_service_pb2 import UpdateNotificationStatusRequest

channel = grpc.insecure_channel("backend_mock:50051")
clientmail_service = BackendServiceStub(channel)

note_info = clientmail_service.GetFullNotificationInfo(
    NotificationInfoRequest(notification_id=1)
)
print(note_info)
print(note_info["email"][0])
print(note_info["email"][1])
