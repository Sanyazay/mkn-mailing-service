FROM python:latest

RUN apt-get update && apt-get install python3-pip -y && pip install --upgrade pip && pip install pipenv

ADD requirements.txt /back_endfolder/
ADD grpc-server-back.py /back_endfolder/
ADD mail_service_pb2_grpc.py /back_endfolder/
ADD mail_service_pb2.py /back_endfolder/
ADD test.py /back_endfolder/

WORKDIR /back_endfolder/
RUN pip install --no-cache-dir -r requirements.txt
# RUN python grpc-server-back.py