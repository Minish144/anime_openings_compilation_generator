FROM python:3.8.3-slim as build

WORKDIR /app

RUN apt update
RUN apt install gcc -y

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3", "main.py"]
