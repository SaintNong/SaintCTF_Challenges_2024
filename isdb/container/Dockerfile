FROM python:3.8-alpine

STOPSIGNAL SIGINT
EXPOSE 3003

RUN apk update

WORKDIR /isdb

COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt

COPY ./src /isdb

CMD ["python3", "app.py"]
