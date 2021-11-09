FROM python:3.9.1

ADD . /api

WORKDIR /api

RUN pip install -r requirements.txt

CMD flask run --host=0.0.0.0
