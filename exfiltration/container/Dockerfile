FROM python:3.8-alpine

STOPSIGNAL SIGINT
EXPOSE 3008

RUN apk update

WORKDIR /exfiltration

COPY requirements.txt ./src/
RUN python3 -m pip install -r src/requirements.txt

# use default guest user in Alpine
# https://stackoverflow.com/questions/49955097/how-do-i-add-a-user-when-im-using-alpine-as-a-base-image#comment91993331_49955098
USER guest
COPY ./src ./src
COPY ./flag.txt .

CMD ["python3", "src/main.py"]
