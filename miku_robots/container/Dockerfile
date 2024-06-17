FROM python:3.8-alpine

STOPSIGNAL SIGINT
EXPOSE 3002

RUN apk update

WORKDIR /miku_robots

COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt

COPY ./src /miku_robots

CMD ["python3", "app.py"]
