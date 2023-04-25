from concurrent import futures

import grpc

from mail_service_pb2 import ScheduleResponse

import mail_service_pb2_grpc

class MailingService(
    mail_service_pb2_grpc.MailingServiceServicer
):

    def ScheduleNotification(self, request, context):
        

        return ScheduleResponse(send_status = 228)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mail_service_pb2_grpc.add_MailingServiceServicer_to_server(
        MailingService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()