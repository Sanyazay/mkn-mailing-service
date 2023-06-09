from concurrent import futures

import grpc
import redis
from mail_service_pb2 import ScheduleResponse
from mail_service_pb2 import NotificationInfoResponse
from mail_service_pb2 import UpdateNotificationStatusResponse
import mail_service_pb2_grpc

mock_data = {
    1: {
        "project_title": "1project_title(название проекта)",
        "section_title": "section_title(название секции)",
        "notification_title": "notification_title(название напоминания)",
        "description": "description(описание)",
        "email": ["ScaredSnael3@mail.ru", "h34th3n777@gmail.com"],
        "send_status": 0,
    },
    2: {
        "project_title": "2project_title(название проекта)",
        "section_title": "section_title(название секции)",
        "notification_title": "notification_title(название напоминания)",
        "description": "description(описание)",
        "email": ["ScaredSnael3@mail.ru", "h34th3n777@gmail.com"],
        "send_status": 0,
    },
    3: {
        "project_title": "3project_title(название проекта)",
        "section_title": "section_title(название секции)",
        "notification_title": "notification_title(название напоминания)",
        "description": "description(описание)",
        "email": ["ScaredSnael3@mail.ru", "h34th3n777@gmail.com"],
        "send_status": 0,
    },
    4: {
        "project_title": "4project_title(название проекта)",
        "section_title": "section_title(название секции)",
        "notification_title": "notification_title(название напоминания)",
        "description": "description(описание)",
        "email": ["ScaredSnael3@mail.ru", "h34th3n777@gmail.com"],
        "send_status": 0,
    },
    5: {
        "project_title": "5project_title(название проекта)",
        "section_title": "section_title(название секции)",
        "notification_title": "notification_title(название напоминания)",
        "description": "description(описание)",
        "email": ["ScaredSnael3@mail.ru", "h34th3n777@gmail.com"],
        "send_status": 0,
    },
    6: {
        "project_title": "6project_title(название проекта)",
        "section_title": "section_title(название секции)",
        "notification_title": "notification_title(название напоминания)",
        "description": "description(описание)",
        "email": ["ScaredSnael3@mail.ru", "h34th3n777@gmail.com"],
        "send_status": 0,
    },
    7: {
        "project_title": "7project_title(название проекта)",
        "section_title": "section_title(название секции)",
        "notification_title": "notification_title(название напоминания)",
        "description": "description(описание)",
        "email": ["ScaredSnael3@mail.ru", "h34th3n777@gmail.com"],
        "send_status": 0,
    },
    8: {
        "project_title": "8project_title(название проекта)",
        "section_title": "section_title(название секции)",
        "notification_title": "notification_title(название напоминания)",
        "description": "description(описание)",
        "email": ["ScaredSnael3@mail.ru", "h34th3n777@gmail.com"],
        "send_status": 0,
    },
    9: {
        "project_title": "9project_title(название проекта)",
        "section_title": "section_title(название секции)",
        "notification_title": "notification_title(название напоминания)",
        "description": "description(описание)",
        "email": ["ScaredSnael3@mail.ru", "h34th3n777@gmail.com"],
        "send_status": 0,
    },
    10: {
        "project_title": "10project_title(название проекта)",
        "section_title": "section_title(название секции)",
        "notification_title": "notification_title(название напоминания)",
        "description": "description(описание)",
        "email": ["ScaredSnael3@mail.ru", "h34th3n777@gmail.com"],
        "send_status": 0,
    },
}


class BackendService(mail_service_pb2_grpc.BackendServiceServicer):
    def GetFullNotificationInfo(self, request, context):
        return NotificationInfoResponse(
            notification_id=request.notification_id,
            project_title=mock_data[request.notification_id]["project_title"],
            section_title=mock_data[request.notification_id]["section_title"],
            notification_title=mock_data[request.notification_id]["notification_title"],
            description=mock_data[request.notification_id]["description"],
            email=mock_data[request.notification_id]["email"],
        )

    def UpdateNotificationStatus(self, request, context):
        mock_data[request.notification_id]["send_status"] = request.send_status
        return UpdateNotificationStatusResponse(send_status=1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mail_service_pb2_grpc.add_BackendServiceServicer_to_server(BackendService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
