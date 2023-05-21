import grpc
from mail_service_pb2_grpc import BackendServiceStub
from mail_service_pb2 import NotificationInfoRequest
from mail_service_pb2 import UpdateNotificationStatusRequest
import redis

channel = grpc.insecure_channel("localhost:50051")
clientmail_service = BackendServiceStub(channel)

note_info = clientmail_service.GetFullNotificationInfo(
    NotificationInfoRequest(notification_id=1)
)
print(note_info)
print(note_info.email[0])
print(note_info.project_title)
# print(note_info["email"][1])
r = redis.Redis(host="backendredis", port=6377)
r.set(1, 2)
print(r.get(1))
