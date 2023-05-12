import datetime
import grpc
import time
from mail_service_pb2_grpc import MailingServiceStub
from mail_service_pb2_grpc import BackendServiceStub
from mail_service_pb2 import ScheduleRequest
from mail_service_pb2 import GetFullNotificationInfo
from mail_service_pb2 import UpdateNotificationStatus

channel = grpc.insecure_channel("localhost:50051")
clientbackend = MailingServiceStub(channel)
channel = grpc.insecure_channel("backend_mock:50052")
clientmail_service = BackendServiceStub(channel)


curTime = int(datetime.datetime.now().timestamp())


request1 = ScheduleRequest(notification_id=1, deadline=str(curTime))
request2 = ScheduleRequest(notification_id=2, deadline=str(curTime))
request3 = ScheduleRequest(notification_id=3, deadline=str(curTime))
request4 = ScheduleRequest(notification_id=4, deadline=str(curTime + 60))
request5 = ScheduleRequest(notification_id=5, deadline=str(curTime + 120))
request6 = ScheduleRequest(notification_id=6, deadline=str(curTime + 180))
request7 = ScheduleRequest(notification_id=7, deadline=str(curTime + 180))
request8 = ScheduleRequest(notification_id=8, deadline=str(curTime + 180))
request9 = ScheduleRequest(notification_id=9, deadline=str(curTime + 240))
request10 = ScheduleRequest(notification_id=10, deadline=str(curTime + 300))


# back-end планирует 10 отправок писем с уведомлениями
clientbackend.ScheduleNotification(request1)
clientbackend.ScheduleNotification(request2)
clientbackend.ScheduleNotification(request3)
clientbackend.ScheduleNotification(request4)
clientbackend.ScheduleNotification(request5)
clientbackend.ScheduleNotification(request6)
clientbackend.ScheduleNotification(request7)
clientbackend.ScheduleNotification(request8)
clientbackend.ScheduleNotification(request9)
clientbackend.ScheduleNotification(request10)


# back-end изменяет время отправки для 4 уведомления
request4 = ScheduleRequest(notification_id=4, deadline=str(curTime + 120))
clientbackend.ScheduleNotification(request4)

# mail_service
