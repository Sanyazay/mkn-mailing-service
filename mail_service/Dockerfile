FROM python:latest

RUN apt-get update && apt-get install python3-pip -y && pip install --upgrade pip && pip install pipenv

ADD redistest.py /test/
ADD requirements.txt /test/
ADD grpc-server.py /test/
ADD mail_service_pb2_grpc.py /test/
ADD mail_service_pb2.py /test/
ADD test.py /test/
ADD consumer.py /test/
ADD producer.py /test/
WORKDIR /test/
RUN pip install --no-cache-dir -r requirements.txt
# RUN python grpc-server.py
# RUN python redistest.py


