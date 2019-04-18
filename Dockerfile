FROM alpine

RUN apk update && apk add py2-pip py2-gevent py2-yaml && pip install telnetsrv requests

COPY honeypot /honeypot
CMD ["python", "/honeypot/honeypot.py"]
