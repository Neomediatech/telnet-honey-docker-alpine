FROM alpine:3.9

LABEL maintainer="docker-dario@neomediatech.it"

RUN apk update; apk upgrade ; apk add --no-cache tzdata; cp /usr/share/zoneinfo/Europe/Rome /etc/localtime
RUN apk update && apk add py2-pip py2-gevent py2-yaml && pip install telnetsrv requests

COPY honeypot /honeypot

EXPOSE 2323

CMD ["python", "/honeypot/honeypot.py"]
