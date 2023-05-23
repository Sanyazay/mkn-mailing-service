FROM golang:latest

WORKDIR /chtohocezh
RUN git clone -b developing https://github.com/vvjke314/mkn-backend.git
WORKDIR mkn-backend
RUN go version 
ENV GOPATH=/


RUN go mod download


RUN go build -o ./bin/main ./cmd/mkn/main.go
RUN make migrate
CMD ["./bin/main"]