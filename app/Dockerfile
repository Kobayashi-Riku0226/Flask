FROM python:3.13.7

WORKDIR /app
ADD . /app

RUN python3 -m pip install -r requirements.txt
CMD ["uwsgi", "uwsgi.ini"]