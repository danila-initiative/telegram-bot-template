FROM python:3.9.6-slim

# creating workdir
RUN mkdir app
WORKDIR /app
COPY . /app

# install system requirements
RUN apt update && apt upgrade -y
RUN apt install -y systemctl nano
RUN apt install -y supervisor

# install python requirements
RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
