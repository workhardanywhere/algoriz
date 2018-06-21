FROM python:3

ENV TERM=xterm

add requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt