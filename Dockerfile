FROM ubuntu:latest

RUN apt update 
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY fibonacci.py ./

FROM python:3.8

RUN pip install psutil

WORKDIR /app
COPY . /app

CMD [ "python3", "./linearSearch.py" ]