FROM alpine:3.10

RUN apk add gcc

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

ENV PORT 8080

CMD ["python3","app.py"]