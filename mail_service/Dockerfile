FROM python:latest

RUN apt-get update && apt-get install python3-pip -y && pip install --upgrade pip && pip install pipenv

ADD requirements.txt /mailfolder/
ADD grpc-server.py /mailfolder/
ADD mail.py /mailfolder/
ADD mail_service_pb2_grpc.py /mailfolder/
ADD mail_service_pb2.py /mailfolder/
ADD test.py /mailfolder/
ADD ztest.py /mailfolder/
ADD consumer.py /mailfolder/
ADD producer.py /mailfolder/
WORKDIR /mailfolder/
RUN pip install --no-cache-dir -r requirements.txt
# RUN python grpc-server.py
# RUN python redistest.py


