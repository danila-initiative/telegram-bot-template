FROM python:3.9.6-slim

# creating workdir
RUN mkdir app
RUN mkdir -p /app/data
WORKDIR /app
COPY . /app

# install system requirements
RUN apt update && apt upgrade -y
RUN apt install -y systemctl nano
RUN apt install -y supervisor make cron

# copy supervisor config
ADD supervisor.conf /etc/supervisor/conf.d

# install python requirements
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

RUN touch /var/log/cron.log
