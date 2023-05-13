from concurrent import futures

import grpc
import redis
from mail_service_pb2 import ScheduleResponse
from mail_service_pb2 import CancelNotificationResponse

# from producer import producer
import mail_service_pb2_grpc


class MailingService(mail_service_pb2_grpc.MailingServiceServicer):
    def ScheduleNotification(self, request, context):
        try:
            r = redis.Redis(host="redis", port=6379)
            r.set(request.notification_id, request.deadline)
            print(request.notification_id, request.deadline)
            status = 0
        except Exception as e:
            print(e)
            status = 1

        return ScheduleResponse(add_status=status)

    def CancelNotification(self, request, context):
        try:
            r = redis.Redis(host="redis", port=6379)
            r.delete(request.notification_id)
            print(str(request.notification_id) + "has been deleted")
            status = 0
        except Exception as e:
            print(e)
            status = 1
        return CancelNotificationResponse(send_status=status)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mail_service_pb2_grpc.add_MailingServiceServicer_to_server(MailingService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
