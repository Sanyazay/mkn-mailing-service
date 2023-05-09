import datetime
import grpc
import time
from mail_service_pb2_grpc import MailingServiceStub
from mail_service_pb2 import ScheduleRequest
# from producer import producer
# from consumer import consumer
channel = grpc.insecure_channel("localhost:50051")
client = MailingServiceStub(channel)
curTime = int(datetime.datetime.now().timestamp())
request1 = ScheduleRequest(notification_id=10, deadline=str(curTime))
request11 = ScheduleRequest(notification_id=111, deadline=str(curTime))
request111 = ScheduleRequest(notification_id=1111, deadline=str(curTime))
request2 = ScheduleRequest(notification_id=11, deadline=str(curTime + 60))
request3 = ScheduleRequest(notification_id=12, deadline=str(curTime + 120))

client.ScheduleNotification(request1)
client.ScheduleNotification(request11)
client.ScheduleNotification(request111)
client.ScheduleNotification(request1)
client.ScheduleNotification(request1)
client.ScheduleNotification(request1)
client.ScheduleNotification(request2)
client.ScheduleNotification(request2)
client.ScheduleNotification(request2)
client.ScheduleNotification(request3)
client.ScheduleNotification(request3)
client.ScheduleNotification(request3)