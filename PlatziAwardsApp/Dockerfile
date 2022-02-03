FROM ubuntu

RUN mkdir app
RUN apt update
RUN apt upgrade
RUN apt install python3 -y
RUN apt install python3-pip -y
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/